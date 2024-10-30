# ETFS.py

# Definición de la lista de instrumentos financieros
instrumentos_financieros = [
    {
        "nombre": "AZ China",
        "descripcion": "Índice que se enfoca en empresas chinas incluidas en el índice MSCI China, permitiendo a los inversores obtener exposición a empresas de diversos sectores económicos dentro de China.",
        "simbolo": "MCHI"
    },
    {
        "nombre": "AZ MSCI TAIWAN INDEX FD",
        "descripcion": "Fondo que sigue el índice MSCI de Taiwán, proporcionando acceso a las principales empresas cotizadas en la Bolsa de Valores de Taiwán.",
        "simbolo": "EWT"
    },
    {
        "nombre": "AZ RUSSELL 2000",
        "descripcion": "Fondo que sigue el índice Russell 2000, representando acciones de pequeña capitalización en los Estados Unidos.",
        "simbolo": "IWM"
    },
    {
        "nombre": "AZ Brasil",
        "descripcion": "Fondo relacionado con el mercado brasileño, que invierte en acciones de empresas brasileñas.",
        "simbolo": "EWZ"
    },
    {
        "nombre": "AZ MSCI UNITED KINGDOM",
        "descripcion": "Fondo que sigue el índice MSCI del Reino Unido, ofreciendo exposición a empresas británicas de gran y mediana capitalización.",
        "simbolo": "EWU"
    },
    {
        "nombre": "AZ DJ US FINANCIAL SECT",
        "descripcion": "Fondo relacionado con el sector financiero de EE.UU., que incluye bancos, seguros y otras instituciones financieras.",
        "simbolo": "IYF"
    },
    {
        "nombre": "AZ BRIC",
        "descripcion": "Fondo que sigue a los países BRIC (Brasil, Rusia, India, China), representando mercados emergentes.",
        "simbolo": "BKF"
    },
    {
        "nombre": "AZ MSCI SOUTH KOREA IND",
        "descripcion": "Fondo que sigue el índice MSCI de Corea del Sur, invirtiendo en acciones de empresas surcoreanas.",
        "simbolo": "EWY"
    },
    {
        "nombre": "AZ BARCLAYS AGGREGATE",
        "descripcion": "Fondo que sigue el índice Barclays Aggregate, que incluye una variedad de bonos de deuda en EE.UU.",
        "simbolo": "AGG"
    },
    {
        "nombre": "AZ Mercados Emergentes",
        "descripcion": "Fondo que sigue mercados emergentes, invirtiendo en una amplia gama de activos en países en desarrollo.",
        "simbolo": "EEM"
    },
    {
        "nombre": "AZ MSCI EMU",
        "descripcion": "Fondo que sigue el índice MSCI Eurozone, proporcionando acceso a acciones de países de la Eurozona.",
        "simbolo": "EZU"
    },
    {
        "nombre": "AZ FTSE/XINHUA CHINA 25",
        "descripcion": "Fondo que sigue el índice FTSE/Xinhua China 25, que incluye las 25 principales acciones en China.",
        "simbolo": "FXI"
    },
    {
        "nombre": "AZ Oro",
        "descripcion": "Fondo relacionado con el precio del oro, ofreciendo exposición a este activo precioso.",
        "simbolo": "GLD"
    },
    {
        "nombre": "AZ LATIXX MEX CETETRAC",
        "descripcion": "Índice mexicano de CETES, que permite a los inversores acceder a bonos emitidos por el gobierno mexicano.",
        "simbolo": "CETETRC.MX"
    },
    {
        "nombre": "AZ QQQ NASDAQ 100",
        "descripcion": "Fondo que sigue el índice Nasdaq 100, que incluye las 100 principales acciones no financieras de la Bolsa Nasdaq.",
        "simbolo": "QQQ"
    },
    {
        "nombre": "AZ MSCI ASIA EX-JAPAN",
        "descripcion": "Fondo que sigue el índice MSCI Asia sin Japón, representando acciones de diversos países asiáticos.",
        "simbolo": "AAXJ"
    },
    {
        "nombre": "AZ LATIXX MEX M10TRAC",
        "descripcion": "Fondo mexicano basado en bonos M10, que invierte en deuda gubernamental a mediano plazo.",
        "simbolo": "M10TRAC.MX"
    },
    {
        "nombre": "AZ BARCLAYS 1-3 YEAR TR",
        "descripcion": "Fondo que sigue el índice Barclays 1-3 Year Treasury, invirtiendo en bonos del Tesoro a corto plazo.",
        "simbolo": "SHY"
    },
    {
        "nombre": "AZ MSCI ACWI INDEX FUND",
        "descripcion": "Fondo que sigue el índice MSCI All Country World Index, ofreciendo exposición a acciones globales.",
        "simbolo": "ACWI"
    },
    {
        "nombre": "AZ LATIXX MEXICO M5TRAC",
        "descripcion": "Fondo mexicano basado en bonos M5, invirtiendo en deuda gubernamental a largo plazo.",
        "simbolo": "M5TRAC.MX"
    },
    {
        "nombre": "AZ SILVER TRUST",
        "descripcion": "Fondo relacionado con el precio de la plata, proporcionando exposición a este metal precioso.",
        "simbolo": "SLV"
    },
    {
        "nombre": "AZ MSCI HONG KONG INDEX",
        "descripcion": "Fondo que sigue el índice MSCI Hong Kong, ofreciendo acceso a empresas de Hong Kong.",
        "simbolo": "EWH"
    },
    {
        "nombre": "AZ LATIXX MEX UDITRAC",
        "descripcion": "Fondo mexicano relacionado con UDIS, un tipo de unidad de inversión en pesos.",
        "simbolo": "UDITRAC.MX"
    },
    {
        "nombre": "AZ SPDR S&P 500 ETF TRUST",
        "descripcion": "Fondo que sigue el índice S&P 500, que incluye las 500 principales acciones en EE.UU.",
        "simbolo": "SPY"
    },
    {
        "nombre": "AZ MSCI JAPAN INDEX FD",
        "descripcion": "Fondo que sigue el índice MSCI Japón, proporcionando acceso a las principales empresas cotizadas en Japón.",
        "simbolo": "EWJ"
    },
    {
        "nombre": "AZ BG EUR GOVT BOND 1-3",
        "descripcion": "Fondo relacionado con bonos gubernamentales europeos a corto plazo, invirtiendo en deuda de la Eurozona.",
        "simbolo": "IBGS.AS"
    },
    {
        "nombre": "AZ SPDR DJIA TRUST",
        "descripcion": "Fondo que sigue el índice Dow Jones Industrial Average, invirtiendo en 30 de las principales empresas de EE.UU.",
        "simbolo": "DIA"
    },
    {
        "nombre": "AZ MSCI FRANCE INDEX FD",
        "descripcion": "Fondo que sigue el índice MSCI Francia, ofreciendo acceso a acciones de empresas francesas.",
        "simbolo": "EWQ"
    },
    {
        "nombre": "AZ DJ US OIL & GAS EXPL",
        "descripcion": "Fondo relacionado con la exploración de petróleo y gas en EE.UU., invirtiendo en empresas del sector energético.",
        "simbolo": "IEO"
    },
    {
        "nombre": "AZ VANGUARD EMERGING MARKET ETF",
        "descripcion": "Fondo que sigue mercados emergentes de Vanguard, proporcionando exposición a países en desarrollo.",
        "simbolo": "VWO"
    },
    {
        "nombre": "AZ MSCI AUSTRALIA INDEX",
        "descripcion": "Fondo que sigue el índice MSCI Australia, invirtiendo en empresas australianas de gran y mediana capitalización.",
        "simbolo": "EWA"
    },
    {
        "nombre": "AZ IPC LARGE CAP TR TRAC",
        "descripcion": "Índice de capitalización grande del mercado mexicano, que incluye las principales acciones de la Bolsa Mexicana de Valores.",
        "simbolo": "ILCTRAC.MX"
    },
    {
        "nombre": "AZ FINANCIAL SELECT SECTOR SPDR",
        "descripcion": "Fondo que sigue el sector financiero del S&P 500, invirtiendo en instituciones financieras en EE.UU.",
        "simbolo": "XLF"
    },
    {
        "nombre": "AZ MSCI CANADA",
        "descripcion": "Fondo que sigue el índice MSCI Canadá, proporcionando acceso a las principales empresas en Canadá.",
        "simbolo": "EWC"
    },
    {
        "nombre": "AZ S&P LATIN AMERICA 40",
        "descripcion": "Fondo que sigue el índice S&P Latin America 40, invirtiendo en las principales empresas de América Latina.",
        "simbolo": "ILF"
    },
    {
        "nombre": "AZ HEALTH CARE SELECT SECTOR",
        "descripcion": "Fondo que sigue el sector salud del S&P 500, invirtiendo en empresas del sector salud en EE.UU.",
        "simbolo": "XLV"
    },
    {
        "nombre": "AZ MSCI GERMANY INDEX",
        "descripcion": "Fondo que sigue el índice MSCI Alemania, ofreciendo acceso a empresas alemanas de gran y mediana capitalización.",
        "simbolo": "EWG"
    },
    {
        "nombre": "AZ INDUSTRIAL SELECT SECTOR SPDR",
        "descripcion": "Fondo que sigue el sector industrial del S&P 500, invirtiendo en empresas del sector industrial en EE.UU.",
        "simbolo": "XLI"
    }
]
