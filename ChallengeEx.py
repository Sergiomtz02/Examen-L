import yfinance as yf      
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from ETFS import instrumentos_financieros

# Función para obtener el rendimiento logarítmico diario, el rendimiento acumulado y el riesgo (volatilidad anualizada)
def obtener_rendimiento_y_riesgo_logaritmico(instrumento, inicio, fin):
    try:
        datos = yf.download(instrumento["simbolo"], start=inicio, end=fin)
        if datos.empty:
            st.warning(f"No se encontraron datos para el símbolo {instrumento['simbolo']}.")
            return None, None, None, None
        precios = datos['Adj Close'].dropna()
        rendimientos_logaritmicos_diarios = np.log(precios / precios.shift(1)).dropna()
        rendimiento_acumulado = rendimientos_logaritmicos_diarios.sum()
        volatilidad_diaria = rendimientos_logaritmicos_diarios.std()
        volatilidad_anualizada = volatilidad_diaria * np.sqrt(252)
        return rendimientos_logaritmicos_diarios, rendimiento_acumulado, volatilidad_anualizada, precios
    except Exception as e:
        st.error(f"Ocurrió un error: {str(e)}")
        return None, None, None, None

# Función para calcular capital final
def calcular_capital_final(capital_inicial, rendimiento_acumulado):
    return capital_inicial * np.exp(rendimiento_acumulado)

# Función para obtener la fecha de inicio para los diferentes periodos
def obtener_fecha_periodo(meses):
    return (datetime.now() - timedelta(days=meses * 30)).strftime('%Y-%m-%d')

# Aplicación en Streamlit
st.title("Simulador OptiMaxx Patrimonial")

capital_minimo = 500000
capital = st.number_input("Ingrese el capital a invertir (mínimo $500,000 pesos):", min_value=capital_minimo, value=capital_minimo, step=100000)
capital_format = "${:,.0f}".format(float(capital))
st.write(f"**Capital ingresado**: {capital_format}")

horizonte_inversion = st.selectbox("Seleccione el horizonte de inversión (en años):", options=list(range(1, 11)))

nombres_instrumentos = [instrumento["nombre"] for instrumento in instrumentos_financieros]
seleccionados = st.multiselect("Seleccione uno o más instrumentos financieros:", options=nombres_instrumentos)

# Crear un diccionario para guardar los porcentajes de inversión
porcentajes_inversion = {}
for nombre in seleccionados:
    porcentaje = st.number_input(f"Ingrese el porcentaje de inversión para {nombre} (%):", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    porcentajes_inversion[nombre] = porcentaje

fecha_fin = datetime.now().strftime('%Y-%m-%d')
fecha_inicio_ytd = f"{datetime.now().year}-01-01"

periodos = {"1M": 1, "3M": 3, "6M": 6, "1A": 12, "3A": 36, "5A": 60, "10A": 120, "YTD": 0}

if st.button("Calcular"):
    if seleccionados:
        precios_historicos = {}
        rendimientos_acumulados = []
        volatilidades_anualizadas = []
        resultados_globales = pd.DataFrame()
        detalles_inversion = pd.DataFrame(columns=["Instrumento", "Descripción", "Símbolo"])

        st.markdown("<h3 style='color: lightblue; font-weight: bold;'>Detalles de la Inversión:</h3>", unsafe_allow_html=True)

        for instrumento in instrumentos_financieros:
            if instrumento["nombre"] in seleccionados:
                rendimientos_log, rendimiento_acumulado, volatilidad_anualizada, precios = obtener_rendimiento_y_riesgo_logaritmico(instrumento, fecha_inicio_ytd, fecha_fin)
                if rendimientos_log is not None:
                    precios_historicos[instrumento["nombre"]] = precios
                    rendimientos_acumulados.append(rendimiento_acumulado)
                    volatilidades_anualizadas.append(volatilidad_anualizada)

                    df_temp = pd.DataFrame({
                        "Instrumento": [instrumento['nombre']],
                        "Descripción": [instrumento['descripcion']],
                        "Símbolo": [instrumento['simbolo']], 
                    })

                    detalles_inversion = pd.concat([detalles_inversion, df_temp], ignore_index=True)

                for nombre_periodo, meses in periodos.items():
                    if nombre_periodo == "YTD":
                        fecha_inicio = fecha_inicio_ytd
                    else:
                        fecha_inicio = obtener_fecha_periodo(meses)

                    rendimientos_log, rendimiento_acumulado, volatilidad_anualizada, _ = obtener_rendimiento_y_riesgo_logaritmico(instrumento, fecha_inicio, fecha_fin)
                    if rendimientos_log is not None and volatilidad_anualizada is not None:
                        temp_df = pd.DataFrame({
                            "Instrumento": [instrumento['nombre']],
                            "Periodo": [nombre_periodo],
                            "Rendimiento": [f"{rendimiento_acumulado * 100:.2f}%"],
                            "Volatilidad": [f"{volatilidad_anualizada * 100:.2f}%"]
                        })
                        resultados_globales = pd.concat([resultados_globales, temp_df], ignore_index=True)

        # Mostrar los detalles de la inversión sin tabla
        for index, row in detalles_inversion.iterrows():
            st.markdown(f"**Instrumento**: {row['Instrumento']}")
            st.markdown(f"**Descripción**: {row['Descripción']}")
            st.markdown(f"**Símbolo**: {row['Símbolo']}")
            st.markdown("---")  # Línea divisoria entre instrumentos

        st.write("**Rendimiento y Volatilidad**:")
        st.dataframe(resultados_globales)

        st.write("**Gráfico de Tendencia de Rendimiento**:")
        fig, ax = plt.subplots(figsize=(15, 8))
        for nombre, precios in precios_historicos.items():
            rendimiento_relativo = (precios / precios.iloc[0]) * 100
            ax.plot(rendimiento_relativo.index, rendimiento_relativo, label=nombre)

        ax.set_xlabel("Fecha")
        ax.set_ylabel("Rendimiento")
        ax.set_title("Rendimiento de precios (Base 100)")
        ax.legend(loc="upper left")
        st.pyplot(fig)

        # Calcular rendimiento ajustado por el porcentaje de inversión
        if len(rendimientos_acumulados) == len(seleccionados):
            rendimiento_acumulado_portafolio = sum(porcentajes_inversion[nombre] * rendimientos_acumulados[i] / 100 for i, nombre in enumerate(seleccionados))

            st.write(f"**Rendimiento Acumulado del Portafolio**: {rendimiento_acumulado_portafolio * 100:.2f}%")
        else:
            st.error("Error: No se obtuvieron suficientes datos para todos los instrumentos seleccionados.")
