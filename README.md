# Chile: law history in git

The law of Chile as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `cl/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución Política de la República (1980) | 78 | From its entry into force (11 March 1981) to today, through the texto refundido of 2005 (Decreto 100) |
| `codigo-civil/` | Código Civil | 29 | From the texto refundido of DFL 1 of 2000 (30 May 2000) to today |
| `ley-19628/` | Ley 19.628 sobre protección de la vida privada (1999) | 7, and 1 on `futuro` | As enacted (28 August 1999) to today; Ley 21.719, which rewrites it from 1 December 2026, is on the branch `futuro` |
| `codigo-penal/` | Código Penal | 164 | As enacted (1 March 1875) to today |
| `codigo-comercio/` | Código de Comercio | 22 | Oldest version available (20 October 1988) to today |
| `codigo-trabajo/` | Código del Trabajo | 145, and 4 on `futuro` | Oldest version available (24 January 1994) to today |
| `codigo-procedimiento-civil/` | Código de Procedimiento Civil | 14 | Oldest version available (30 August 2004) to today |
| `codigo-procesal-penal/` | Código Procesal Penal | 55 | As enacted (16 December 2000) to today |
| `codigo-tributario/` | Código Tributario | 91, and 1 on `futuro` | As enacted (1 January 1975) to today |
| `codigo-sanitario/` | Código Sanitario | 52 | As enacted (31 January 1968) to today |
| `codigo-aguas/` | Código de Aguas | 29, and 1 on `futuro` | As enacted (29 October 1981) to today |
| `ley-18046/` | Ley 18.046 sobre sociedades anónimas | 22 | As enacted (22 October 1981) to today |
| `ley-19496/` | Ley 19.496 sobre protección de los derechos de los consumidores | 24, and 1 on `futuro` | As enacted (6 June 1997) to today |
| `codigo-organico-tribunales/` | Código Orgánico de Tribunales | 225 | As enacted (9 July 1943) to today |
| `codigo-mineria/` | Código de Minería | 12 | As enacted (14 December 1983) to today |
| `codigo-aeronautico/` | Código Aeronáutico | 11 | As enacted (9 August 1990) to today |
| `codigo-justicia-militar/` | Código de Justicia Militar | 38 | Oldest version available (19 December 1944) to today |
| `ley-20393/` | Ley 20.393 sobre responsabilidad penal de las personas jurídicas | 10 | As enacted (2 December 2009) to today |
| `ley-19880/` | Ley 19.880 de bases de los procedimientos administrativos | 8, and 1 on `futuro` | As enacted (29 May 2003) to today |
| `ley-18010/` | Ley 18.010 sobre operaciones de crédito de dinero | 12 | As enacted (27 June 1981) to today |
| `ley-18695/` | Ley 18.695 orgánica constitucional de municipalidades | 81 | As enacted (1 May 1988) to today |
| `ley-18575/` | Ley 18.575 orgánica constitucional de bases generales de la administración del Estado | 15 | As enacted (5 December 1986) to today |
| `ley-20000/` | Ley 20.000 sobre tráfico ilícito de estupefacientes y sustancias sicotrópicas | 8 | As enacted (16 February 2005) to today |
| `ley-17336/` | Ley 17.336 sobre propiedad intelectual | 12 | As enacted (2 October 1970) to today |
| `ley-19039/` | Ley 19.039 de propiedad industrial | 9 | As enacted (25 January 1991) to today |
| `ley-18045/` | Ley 18.045 de mercado de valores | 31 | As enacted (22 October 1981) to today |
| `ley-20720/` | Ley 20.720 de reorganización y liquidación de empresas y personas | 5 | As enacted (10 October 2014) to today |
| `dfl-1-2005-salud/` | DFL 1 de 2005 del Ministerio de Salud (texto refundido del DL 2.763 de 1979 y de las leyes 18.933 y 18.469) | 34, and 1 on `futuro` | Oldest version available (24 April 2006) to today |
| `ley-16744/` | Ley 16.744 sobre accidentes del trabajo y enfermedades profesionales | 24 | As enacted (1 February 1968) to today |
| `ley-19300/` | Ley 19.300 sobre bases generales del medio ambiente | 15, and 2 on `futuro` | As enacted (9 March 1994) to today |
| `ley-18834/` | Ley 18.834 sobre Estatuto Administrativo | 32 | As enacted (23 September 1989) to today |
| `dl-3500/` | DL 3.500 que establece el nuevo sistema de pensiones | 74, and 1 on `futuro` | As enacted (13 November 1980) to today |
| `ley-21595/` | Ley 21.595 de delitos económicos | 3, and 1 on `futuro` | As enacted (17 August 2023) to today |
| `ley-19913/` | Ley 19.913 que crea la Unidad de Análisis Financiero | 23 | As enacted (18 December 2003) to today |
| `ley-18290/` | Ley 18.290 de Tránsito | 87 | As enacted (1 January 1985) to today |
| `ley-19968/` | Ley 19.968 que crea los Tribunales de Familia | 23, and 1 on `futuro` | As enacted (1 October 2005) to today |
| `ley-20084/` | Ley 20.084 sobre responsabilidad penal de los adolescentes | 7 | As enacted (8 June 2007) to today |
| `ley-19947/` | Ley 19.947 de Matrimonio Civil | 9 | As enacted (18 November 2004) to today |
| `ley-14908/` | Ley 14.908 sobre abandono de familia y pago de pensiones alimenticias | 16 | As enacted (5 October 1962) to today |
| `ley-19537/` | Ley 19.537 sobre copropiedad inmobiliaria | 10 | As enacted (16 December 1997) to its repeal by Ley 21.442 (13 April 2022) |
| `ley-18101/` | Ley 18.101 sobre arrendamiento de predios urbanos | 6 | As enacted (29 January 1982) to today |
| `ley-20285/` | Ley 20.285 sobre acceso a la información pública | 4, and 1 on `futuro` | As enacted (21 April 2009) to today |
| `ley-18700/` | Ley 18.700 orgánica constitucional sobre votaciones populares y escrutinios | 40 | As enacted (6 May 1988) to today |
| `ley-20584/` | Ley 20.584 sobre derechos y deberes de las personas en relación con su atención de salud | 13 | As enacted (1 October 2012) to today |
| `ley-19733/` | Ley 19.733 sobre libertades de opinión e información y ejercicio del periodismo | 6 | As enacted (4 June 2001) to today |
| `ley-20529/` | Ley 20.529 sobre el sistema nacional de aseguramiento de la calidad de la educación | 12 | As enacted (27 August 2011) to today |
| `ley-21091/` | Ley 21.091 sobre educación superior | 4, and 1 on `futuro` | As enacted (29 May 2018) to today |
| `dl-824/` | DL 824 que aprueba la Ley sobre Impuesto a la Renta | 115, and 3 on `futuro` | As enacted (1 January 1975) to today |
| `dl-825/` | DL 825 sobre Impuesto a las Ventas y Servicios | 76 | As enacted (1 March 1975) to today |
| `ley-21325/` | Ley 21.325 de Migración y Extranjería | 7 | As enacted (12 February 2022) to today |
| `ley-19886/` | Ley 19.886 de bases sobre contratos administrativos de suministro y prestación de servicios | 15, and 1 on `futuro` | As enacted (30 August 2003) to today |
| `ley-18840/` | Ley 18.840 orgánica constitucional del Banco Central de Chile | 19 | As enacted (10 December 1989) to today |
| `ley-20066/` | Ley 20.066 de violencia intrafamiliar | 10 | As enacted (7 October 2005) to today |
| `ley-18314/` | Ley 18.314 que determina conductas terroristas y fija su penalidad | 15 | As enacted (17 May 1984) to its repeal by Ley 21.732 (12 February 2025) |
| `ley-17798/` | Ley 17.798 sobre control de armas | 24 | As enacted (21 October 1972) to today |
| `ley-20609/` | Ley 20.609 que establece medidas contra la discriminación | 5 | As enacted (24 July 2012) to today |
| `ley-19799/` | Ley 19.799 sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma | 4 | As enacted (12 April 2002) to today |
| `ley-20370/` | Ley 20.370 General de Educación | 22 | As enacted (12 September 2009) to today |
| `ley-20730/` | Ley 20.730 que regula el lobby y las gestiones que representen intereses particulares ante las autoridades y funcionarios | 7 | As enacted (8 March 2014) to today |
| `ley-21430/` | Ley 21.430 sobre garantías y protección integral de los derechos de la niñez y adolescencia | 1 | As enacted (15 March 2022) to today |
| `ley-19253/` | Ley 19.253 sobre protección, fomento y desarrollo de los indígenas | 10 | As enacted (5 October 1993) to today |
| `ley-20422/` | Ley 20.422 sobre igualdad de oportunidades e inclusión social de personas con discapacidad | 22 | As enacted (10 February 2010) to today |
| `ley-10336/` | Ley 10.336 de organización y atribuciones de la Contraloría General de la República | 19 | As enacted (29 May 1952) to today |
| `ley-17997/` | Ley 17.997 orgánica constitucional del Tribunal Constitucional | 13 | As enacted (19 May 1981) to today |
| `ley-19640/` | Ley 19.640 orgánica constitucional del Ministerio Público | 24, and 1 on `futuro` | As enacted (15 October 1999) to today |
| `ley-18918/` | Ley 18.918 orgánica constitucional del Congreso Nacional | 13 | As enacted (11 March 1990) to today |
| `ley-21442/` | Ley 21.442 que aprueba nueva ley de copropiedad inmobiliaria | 8 | As enacted (13 April 2022) to today |
| `ley-19418/` | Ley 19.418 sobre juntas de vecinos y demás organizaciones comunitarias | 13 | As enacted (9 October 1995) to today |
| `ley-3918/` | Ley 3.918 sobre sociedades de responsabilidad limitada | 4 | As enacted (14 March 1923) to today |
| `ley-19857/` | Ley 19.857 que autoriza el establecimiento de empresas individuales de responsabilidad limitada | 2 | As enacted (11 February 2003) to today |
| `ley-21521/` | Ley 21.521 que promueve la competencia e inclusión financiera a través de la innovación y tecnología en la prestación de servicios financieros (Ley Fintec) | 1 | As enacted (4 February 2023) to today |
| `ley-20500/` | Ley 20.500 sobre asociaciones y participación ciudadana en la gestión pública | 1 | As enacted (16 February 2011) to today |
| `ley-4808/` | Ley 4.808 sobre Registro Civil | 23 | As enacted (10 February 1930) to today; from 30 May 2000 as art. 3 of DFL 1 of 2000 |
| `ley-17344/` | Ley 17.344 que autoriza el cambio de nombres y apellidos | 4 | As enacted (22 September 1970) to today; from 30 May 2000 as art. 4 of DFL 1 of 2000 |
| `ley-16618/` | Ley 16.618 de Menores | 27 | As enacted (8 March 1967) to today; from 30 May 2000 as art. 6 of DFL 1 of 2000 |
| `ley-16271/` | Ley 16.271 de impuesto a las herencias, asignaciones y donaciones | 13 | As enacted (10 July 1965) to today; from 30 May 2000 as art. 8 of DFL 1 of 2000 |
| `dfl-458/` | DFL 458 que aprueba la Ley General de Urbanismo y Construcciones | 60, and 1 on `futuro` | As enacted (13 April 1976) to today |
| `ley-general-bancos/` | Ley General de Bancos | 33 | Oldest version available (13 July 1996) to today: DFL 252 of 1960, then the texto refundido of DFL 3 of 1997; its two 1960 versions are left out (git cannot date them without moving published commits) |
| `dl-211/` | DL 211 que fija normas para la defensa de la libre competencia | 18 | As enacted (22 December 1973) to today |
| `ley-18892/` | Ley 18.892 General de Pesca y Acuicultura | 65, and 1 on `futuro` | As enacted (1 April 1990) to today |
| `ley-18168/` | Ley 18.168 General de Telecomunicaciones | 45 | As enacted (2 October 1982) to today |
| `ley-19175/` | Ley 19.175 orgánica constitucional sobre gobierno y administración regional | 24 | As enacted (11 November 1992) to today |
| `ley-19070/` | Ley 19.070 que aprueba el Estatuto de los Profesionales de la Educación | 35 | As enacted (1 July 1991) to today |
| `ley-20600/` | Ley 20.600 que crea los Tribunales Ambientales | 5, and 1 on `futuro` | As enacted (28 June 2012) to today |
| `ley-18287/` | Ley 18.287 que establece el procedimiento ante los juzgados de policía local | 27 | As enacted (1 January 1985) to today |
| `ley-15231/` | Ley 15.231 sobre organización y atribuciones de los juzgados de policía local | 25 | Oldest version available (23 May 1978) to today, from the texto refundido of Decreto 307 of 1978 |
| `ley-19728/` | Ley 19.728 que establece un seguro de desempleo | 22 | As enacted (14 May 2001) to today |
| `ley-20880/` | Ley 20.880 sobre probidad en la función pública y prevención de los conflictos de intereses | 12, and 1 on `futuro` | As enacted (3 September 2016) to today |
| `ley-19983/` | Ley 19.983 que regula la transferencia y otorga mérito ejecutivo a copia de la factura | 8 | As enacted (16 April 2005) to today |
| `ley-18603/` | Ley 18.603 orgánica constitucional de los partidos políticos | 13 | As enacted (3 April 1987) to today |
| `ley-17322/` | Ley 17.322 sobre cobranza judicial de cotizaciones, aportes y multas de las instituciones de seguridad social | 19 | As enacted (19 August 1970) to today |
| `ley-18097/` | Ley 18.097 orgánica constitucional sobre concesiones mineras | 4 | As enacted (21 January 1982) to today |
| `ley-19378/` | Ley 19.378 que establece el estatuto de atención primaria de salud municipal | 10 | As enacted (13 April 1995) to today |
| `ley-21040/` | Ley 21.040 que crea el Sistema de Educación Pública | 11 | As enacted (24 November 2017) to today |
| `ley-20712/` | Ley 20.712 sobre administración de fondos de terceros y carteras individuales | 9 | As enacted (1 May 2014) to today |
| `ley-20659/` | Ley 20.659 que simplifica el régimen de constitución, modificación y disolución de las sociedades comerciales | 2 | As enacted (2 May 2013) to today |
| `ley-20830/` | Ley 20.830 que crea el Acuerdo de Unión Civil | 3 | As enacted (22 October 2015) to today |
| `ley-21120/` | Ley 21.120 que reconoce y da protección al derecho a la identidad de género | 3 | As enacted (27 December 2019) to today |
| `ley-19620/` | Ley 19.620 que dicta normas sobre adopción de menores | 7 | As enacted (5 August 1999) to today |
| `ley-18216/` | Ley 18.216 que establece penas que indica como sustitutivas a las penas privativas o restrictivas de libertad | 23 | As enacted (14 May 1983) to today |
| `ley-12927/` | Ley 12.927 sobre Seguridad del Estado | 11 | Oldest version available (26 August 1975) to today, from the texto refundido of Decreto 890 of 1975; its 1958 version is left out (git cannot date it without moving published commits) |
| `ley-21000/` | Ley 21.000 que crea la Comisión para el Mercado Financiero | 4 | As enacted (23 February 2017) to today |
| `ley-20920/` | Ley 20.920 que establece marco para la gestión de residuos, la responsabilidad extendida del productor y fomento al reciclaje | 1 | As enacted (1 June 2016) to today |
| `ley-21455/` | Ley 21.455 Marco de Cambio Climático | 2 | As enacted (13 June 2022) to today |
| `ley-17288/` | Ley 17.288 sobre Monumentos Nacionales | 13, and 1 on `futuro` | As enacted (4 February 1970) to today |
| `ley-18883/` | Ley 18.883 que aprueba el Estatuto Administrativo para Funcionarios Municipales | 23 | As enacted (29 December 1989) to today |
| `ley-18415/` | Ley 18.415 orgánica constitucional de los estados de excepción | 2 | As enacted (14 June 1985) to today |
| `ley-21459/` | Ley 21.459 que establece normas sobre delitos informáticos | 4 | As enacted (20 June 2022) to today |
| `ley-20416/` | Ley 20.416 que fija normas especiales para las empresas de menor tamaño | 4 | As enacted (3 February 2010) to today |
| `ley-19966/` | Ley 19.966 que establece un régimen de garantías en salud | 1 | As enacted (3 September 2004) to today |
| `ley-18838/` | Ley 18.838 que crea el Consejo Nacional de Televisión | 12 | As enacted (31 October 1989) to today |
| `ley-20255/` | Ley 20.255 que establece la reforma previsional | 15, and 1 on `futuro` | As enacted (17 March 2008) to today |
| `ley-19995/` | Ley 19.995 que establece las bases generales para la autorización, funcionamiento y fiscalización de casinos de juego | 5 | As enacted (7 May 2005) to today |
| `ley-20283/` | Ley 20.283 sobre recuperación del bosque nativo y fomento forestal | 5 | As enacted (30 July 2008) to today |
| `ley-19884/` | Ley 19.884 orgánica constitucional sobre transparencia, límite y control del gasto electoral | 16 | As enacted (5 August 2003) to today, through the texto refundido of DFL 3 of 2017 |
| `ley-18460/` | Ley 18.460 orgánica constitucional del Tribunal Calificador de Elecciones | 10 | As enacted (15 November 1985) to today |
| `ley-20551/` | Ley 20.551 que regula el cierre de faenas e instalaciones mineras | 3 | As enacted (12 November 2012) to today |
| `ley-18961/` | Ley 18.961 orgánica constitucional de Carabineros | 21 | As enacted (7 March 1990) to today |
| `ley-21389/` | Ley 21.389 que crea el Registro Nacional de Deudores de Pensiones de Alimentos | 1 | As enacted (18 November 2021) to today |
| `ley-21057/` | Ley 21.057 que regula entrevistas grabadas en video y otras medidas de resguardo a menores de edad víctimas de delitos sexuales | 3 | As enacted (3 October 2022) to today |
| `ley-19970/` | Ley 19.970 que crea el Sistema Nacional de Registros de ADN | 5 | As enacted (6 October 2004) to today |
| `ley-20357/` | Ley 20.357 que tipifica crímenes de lesa humanidad y genocidio y crímenes y delitos de guerra | 2 | As enacted (18 July 2009) to today |
| `ley-21600/` | Ley 21.600 que crea el Servicio de Biodiversidad y Áreas Protegidas y el Sistema Nacional de Áreas Protegidas | 4, and 1 on `futuro` | As enacted (6 September 2023) to today |
| `ley-general-servicios-electricos/` | Ley General de Servicios Eléctricos | 48 | As enacted (13 September 1982) to today: DFL 1 of 1982, then the texto refundido of DFL 4 of 2006 (published 2007) |
| `dl-1263/` | DL 1.263 orgánico de administración financiera del Estado | 23 | As enacted (28 November 1975) to today |
| `dl-2186/` | DL 2.186 que aprueba la Ley Orgánica de Procedimiento de Expropiaciones | 4 | As enacted (8 September 1978) to today |
| `ley-20169/` | Ley 20.169 que regula la competencia desleal | 4 | As enacted (16 February 2007) to today |
| `ley-19342/` | Ley 19.342 que regula derechos de obtentores de nuevas variedades vegetales | 1 | As enacted (3 November 1994) to today |
| `ley-20850/` | Ley 20.850 que crea un sistema de protección financiera para diagnósticos y tratamientos de alto costo (Ley Ricarte Soto) | 2 | As enacted (4 December 2015) to today |
| `ley-19451/` | Ley 19.451 que establece normas sobre trasplante y donación de órganos | 7 | As enacted (10 July 1996) to today |
| `ley-20418/` | Ley 20.418 que fija normas sobre información, orientación y prestaciones en materia de regulación de la fertilidad | 2 | As enacted (28 January 2010) to today |
| `ley-19419/` | Ley 19.419 que regula actividades relacionadas con el tabaco | 7 | As enacted (8 January 1996) to today |
| `ley-20606/` | Ley 20.606 sobre composición nutricional de los alimentos y su publicidad | 4 | As enacted (6 July 2012) to today |
| `ley-19925/` | Ley 19.925 sobre expendio y consumo de bebidas alcohólicas | 9 | As enacted (19 January 2004) to today |
| `ley-21094/` | Ley 21.094 sobre universidades estatales | 6 | As enacted (5 June 2018) to today |
| `ley-20129/` | Ley 20.129 que establece un sistema nacional de aseguramiento de la calidad de la educación superior | 13 | As enacted (17 November 2006) to today |
| `ley-19718/` | Ley 19.718 que crea la Defensoría Penal Pública | 6 | As enacted (10 March 2001) to today |
| `ley-19974/` | Ley 19.974 sobre el sistema de inteligencia del Estado | 2 | As enacted (2 October 2004) to today |
| `ley-20405/` | Ley 20.405 del Instituto Nacional de Derechos Humanos | 4 | As enacted (10 December 2009) to today |
| `ley-21067/` | Ley 21.067 que crea la Defensoría de los Derechos de la Niñez | 1 | As enacted (30 June 2018) to today |
| `ley-21302/` | Ley 21.302 que crea el Servicio Nacional de Protección Especializada a la Niñez y Adolescencia | 2 | As enacted (1 October 2021) to today |
| `ley-20848/` | Ley 20.848 que establece marco para la inversión extranjera directa en Chile | 1 | As enacted (21 January 2016) to today |
| `ley-21131/` | Ley 21.131 que establece pago a treinta días | 3 | As enacted (17 May 2019) to today |
| `ley-21663/` | Ley 21.663 Marco de Ciberseguridad | 2 | As enacted (1 January 2025) to today |
| `ley-20640/` | Ley 20.640 que establece el sistema de elecciones primarias | 7 | As enacted (6 December 2012) to today |
| `ley-18410/` | Ley 18.410 que crea la Superintendencia de Electricidad y Combustibles | 9 | As enacted (1 June 1985) to today |
| `ley-18902/` | Ley 18.902 que crea la Superintendencia de Servicios Sanitarios | 9 | As enacted (27 January 1990) to today |
| `ley-19542/` | Ley 19.542 que moderniza el sector portuario estatal | 4 | As enacted (19 December 1997) to today |
| `ley-18876/` | Ley 18.876 sobre entidades privadas de depósito y custodia de valores | 10 | As enacted (21 December 1989) to today |
| `ley-20009/` | Ley 20.009 sobre limitación de responsabilidad de titulares o usuarios de tarjetas de pago | 5 | As enacted (1 April 2005) to today |
| `ley-21236/` | Ley 21.236 que regula la portabilidad financiera | 2 | As enacted (8 September 2020) to today |
| `ley-20249/` | Ley 20.249 que crea el espacio costero marino de los pueblos originarios | 1 | As enacted (16 February 2008) to today |
| `ley-19473/` | Ley 19.473 sobre caza | 3 | As enacted (27 September 1996) to today |
| `ley-21020/` | Ley 21.020 sobre tenencia responsable de mascotas y animales de compañía | 1 | As enacted (2 August 2017) to today |
| `ley-19856/` | Ley 19.856 que crea un sistema de reinserción social de los condenados | 5 | As enacted (4 February 2003) to today |
| `ley-20322/` | Ley 20.322 que fortalece y perfecciona la jurisdicción tributaria y aduanera | 9 | As enacted (27 January 2009) to today |
| `ley-19518/` | Ley 19.518 que fija el Estatuto de Capacitación y Empleo | 11, and 1 on `futuro` | As enacted (1 December 1997) to today |
| `ley-21419/` | Ley 21.419 que crea la Pensión Garantizada Universal | 3, and 3 on `futuro` | As enacted (1 February 2022) to today |
| `ley-19882/` | Ley 19.882 que regula nueva política de personal a los funcionarios públicos (Alta Dirección Pública) | 23 | As enacted (23 June 2003) to today |
| `ley-20380/` | Ley 20.380 sobre protección de animales | 4 | As enacted (3 October 2009) to today |
| `ley-18755/` | Ley 18.755 que establece normas sobre el Servicio Agrícola y Ganadero | 11 | As enacted (7 January 1989) to today |
| `ley-21105/` | Ley 21.105 que crea el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación | 2 | As enacted (13 August 2018) to today |
| `ley-21045/` | Ley 21.045 que crea el Ministerio de las Culturas, las Artes y el Patrimonio | 4, and 1 on `futuro` | As enacted (3 November 2017) to today |
| `ley-20530/` | Ley 20.530 que crea el Ministerio de Desarrollo Social y Familia | 11, and 1 on `futuro` | As enacted (13 October 2011) to today |
| `ley-19862/` | Ley 19.862 que establece registros de las personas jurídicas receptoras de fondos públicos | 1 | As enacted (8 February 2003) to today |
| `ley-20248/` | Ley 20.248 que establece la Ley de Subvención Escolar Preferencial | 12 | As enacted (1 February 2008) to today |
| `ley-19123/` | Ley 19.123 que crea la Corporación Nacional de Reparación y Reconciliación y establece pensión de reparación | 4 | As enacted (8 February 1992) to today |
| `ley-19992/` | Ley 19.992 que establece pensión de reparación y otros beneficios a favor de las personas que indica | 2 | As enacted (24 December 2004) to today |
| `ley-20256/` | Ley 20.256 que establece normas sobre pesca recreativa | 5 | As enacted (12 April 2008) to today |
| `ley-19281/` | Ley 19.281 que establece normas sobre arrendamiento de viviendas con promesa de compraventa | 9 | As enacted (27 December 1993) to today |
| `ley-21369/` | Ley 21.369 que regula el acoso sexual, la violencia y la discriminación de género en el ámbito de la educación superior | 1 | As enacted (15 September 2021) to today |
| `ley-18956/` | Ley 18.956 que reestructura el Ministerio de Educación Pública | 8 | As enacted (8 March 1990) to today |
| `ley-21109/` | Ley 21.109 que establece un Estatuto de los Asistentes de la Educación Pública | 10 | As enacted (2 October 2018) to today |
| `ley-20832/` | Ley 20.832 que crea la autorización de funcionamiento de establecimientos de educación parvularia | 2 | As enacted (1 May 2016) to today |
| `ley-18833/` | Ley 18.833 que establece un nuevo estatuto general para las cajas de compensación de asignación familiar | 11 | As enacted (1 October 1989) to today |
| `ley-19296/` | Ley 19.296 que establece normas sobre asociaciones de funcionarios de la Administración del Estado | 8 | As enacted (14 March 1994) to today |
| `ley-19664/` | Ley 19.664 que establece normas especiales para profesionales funcionarios de los servicios de salud | 4 | As enacted (1 August 2000) to today |
| `ley-18948/` | Ley 18.948 orgánica constitucional de las Fuerzas Armadas | 12 | As enacted (27 February 1990) to today |
| `ley-20424/` | Ley 20.424 estatuto orgánico del Ministerio de Defensa Nacional | 4 | As enacted (4 February 2010) to today |
| `ley-18993/` | Ley 18.993 que crea el Ministerio Secretaría General de la Presidencia de la República | 5 | As enacted (21 August 1990) to today |
| `ley-20430/` | Ley 20.430 que establece disposiciones sobre protección de refugiados | 3 | As enacted (15 April 2010) to today |
| `ley-18556/` | Ley 18.556 orgánica constitucional sobre sistema de inscripciones electorales y Servicio Electoral | 17 | As enacted (1 October 1986) to today, through the texto refundido of DFL 5 of 2017 |
| `ley-18593/` | Ley 18.593 de los tribunales electorales regionales | 6 | As enacted (9 January 1987) to today |
| `ley-20179/` | Ley 20.179 que establece un marco legal para la constitución y operación de sociedades de garantía recíproca | 1 | As enacted (20 June 2007) to today |
| `ley-20027/` | Ley 20.027 que establece normas para el financiamiento de estudios de educación superior | 2 | As enacted (11 June 2005) to today |
| `ley-21015/` | Ley 21.015 que incentiva la inclusión de personas con discapacidad al mundo laboral | 2 | As enacted (1 April 2018) to today |
| `ley-20120/` | Ley 20.120 sobre la investigación científica en el ser humano, su genoma, y prohíbe la clonación humana | 1 | As enacted (22 September 2006) to today |
| `ley-21331/` | Ley 21.331 del reconocimiento y protección de los derechos de las personas en la atención de salud mental | 1 | As enacted (11 May 2021) to today |
| `ley-21375/` | Ley 21.375 que consagra los cuidados paliativos y los derechos de las personas que padecen enfermedades terminales o graves | 1 | As enacted (22 March 2022) to today |
| `ley-20261/` | Ley 20.261 que crea el Examen Único Nacional de Conocimientos de Medicina | 5 | As enacted (19 April 2008) to today |
| `ley-19132/` | Ley 19.132 que crea la empresa Televisión Nacional de Chile | 3 | As enacted (8 April 1992) to today |
| `ley-19846/` | Ley 19.846 sobre calificación de la producción cinematográfica | 7 | As enacted (4 January 2003) to today |
| `ley-19981/` | Ley 19.981 sobre fomento audiovisual | 2 | As enacted (10 November 2004) to today |
| `ley-19928/` | Ley 19.928 sobre fomento de la música chilena | 4 | As enacted (31 January 2004) to today |
| `ley-19227/` | Ley 19.227 que crea el Fondo Nacional de Fomento del Libro y la Lectura | 4 | As enacted (10 July 1993) to today |
| `ley-19638/` | Ley 19.638 que establece normas sobre la constitución jurídica de las iglesias y organizaciones religiosas | 1 | As enacted (14 October 1999) to today |
| `ley-20032/` | Ley 20.032 que regula el régimen de aportes financieros del Estado a los colaboradores acreditados | 4 | As enacted (24 September 2005) to today |
| `ley-20128/` | Ley 20.128 sobre responsabilidad fiscal | 6 | As enacted (30 September 2006) to today |
| `ley-20910/` | Ley 20.910 que crea quince centros de formación técnica estatales | 3 | As enacted (29 March 2016) to today |
| `ley-21450/` | Ley 21.450 sobre integración social en la planificación urbana, gestión de suelo y plan de emergencia habitacional | 5 | As enacted (27 May 2022) to today |
| `ley-20998/` | Ley 20.998 que regula los servicios sanitarios rurales | 5 | As enacted (20 November 2020) to today |
| `ley-19657/` | Ley 19.657 sobre concesiones de energía geotérmica | 3 | As enacted (7 January 2000) to today |
| `ley-18455/` | Ley 18.455 que fija normas sobre producción, elaboración y comercialización de alcoholes etílicos, bebidas alcohólicas y vinagres | 3 | As enacted (1 January 1986) to today |
| `ley-21154/` | Ley 21.154 que designa al Instituto Nacional de Derechos Humanos como el Mecanismo Nacional de Prevención contra la Tortura | 1 | As enacted (26 October 2019) to today |
| `ley-20835/` | Ley 20.835 que crea la Subsecretaría de Educación Parvularia y la Intendencia de Educación Parvularia | 2 | As enacted (5 May 2015) to today |
| `ley-20820/` | Ley 20.820 que crea el Ministerio de la Mujer y la Equidad de Género | 1 | As enacted (20 March 2015) to today |
| `ley-19287/` | Ley 19.287 sobre fondos solidarios de crédito universitario | 3 | As enacted (4 February 1994) to today |
| `ley-17235/` | Ley 17.235 sobre impuesto territorial | 16, and 1 on `futuro` | From the oldest version available (30 August 1996) to today, through the texto refundido of DFL 1 of 1998 |
| `ley-15076/` | Ley 15.076 estatuto para los médicos-cirujanos, farmacéuticos o químico-farmacéuticos, bioquímicos y cirujanos dentistas | 7 | From the oldest version available (20 November 2001) to today (DFL 1 of 2001, texto refundido) |
| `ley-21078/` | Ley 21.078 sobre transparencia del mercado del suelo e impuesto al aumento de valor por ampliación del límite urbano | 2 | As enacted (16 August 2018) to today |
| `ley-21305/` | Ley 21.305 sobre eficiencia energética | 1 | As enacted (13 February 2021) to today |
| `ley-17374/` | Ley 17.374 orgánica del Instituto Nacional de Estadísticas | 4 | As enacted (10 December 1970) to today |
| `ley-18778/` | Ley 18.778 que establece subsidio al pago de consumo de agua potable y servicio de alcantarillado | 4 | As enacted (2 February 1989) to today |
| `ley-21484/` | Ley 21.484 sobre responsabilidad parental y pago efectivo de deudas de pensiones de alimentos | 1 | As enacted (20 May 2023) to today |
| `ley-21730/` | Ley 21.730 que crea el Ministerio de Seguridad Pública | 1 | As enacted (1 April 2025) to today |
| `ley-19865/` | Ley 19.865 sobre financiamiento urbano compartido | 2 | As enacted (1 April 2003) to today |
| `ley-20345/` | Ley 20.345 sobre sistemas de compensación y liquidación de instrumentos financieros | 4 | As enacted (6 June 2009) to today |
| `ley-19220/` | Ley 19.220 que regula el establecimiento de bolsas de productos | 9 | As enacted (31 May 1993) to today |
| `ley-18657/` | Ley 18.657 que autoriza la creación de fondos de inversión de capital extranjero | 8 | As enacted (29 September 1987) to its repeal by Ley 20.712 (1 May 2014) |
| `ley-21364/` | Ley 21.364 que establece el Sistema Nacional de Prevención y Respuesta ante Desastres | 3 | As enacted (7 August 2021) to today |
| `ley-18450/` | Ley 18.450 que aprueba normas para el fomento de la inversión privada en obras de riego y drenaje | 9 | As enacted (1 January 1986) to today |
| `ley-20378/` | Ley 20.378 que crea un subsidio nacional para el transporte público remunerado de pasajeros | 11 | As enacted (5 September 2009) to today |
| `ley-21675/` | Ley 21.675 que estatuye medidas para prevenir, sancionar y erradicar la violencia en contra de las mujeres, en razón de su género | 2 | As enacted (14 June 2024) to today |
| `ley-21545/` | Ley 21.545 que establece la promoción de la inclusión, la atención integral y la protección de los derechos de las personas con trastorno del espectro autista | 1 | As enacted (10 March 2023) to today |
| `ley-21258/` | Ley 21.258 que crea la Ley Nacional del Cáncer | 2 | As enacted (3 October 2020) to today |
| `ley-19712/` | Ley 19.712 del Deporte | 18 | As enacted (9 February 2001) to today |
| `ley-20686/` | Ley 20.686 que crea el Ministerio del Deporte | 5 | As enacted (28 August 2013) to today |
| `ley-20019/` | Ley 20.019 que regula las sociedades anónimas deportivas profesionales | 9 | As enacted (7 May 2005) to today |
| `ley-19327/` | Ley 19.327 de derechos y deberes en los espectáculos de fútbol profesional | 5 | As enacted (31 August 1994) to today |
| `ley-20379/` | Ley 20.379 que crea el Sistema Intersectorial de Protección Social e institucionaliza el subsistema Chile Crece Contigo | 4 | As enacted (12 September 2009) to today |
| `ley-19949/` | Ley 19.949 que establece un sistema de protección social para familias en situación de extrema pobreza denominado Chile Solidario | 7 | As enacted (5 June 2004) to today |
| `ley-20595/` | Ley 20.595 que crea el Ingreso Ético Familiar | 2 | As enacted (17 May 2012) to today |
| `ley-19828/` | Ley 19.828 que crea el Servicio Nacional del Adulto Mayor | 4, and 1 on `futuro` | As enacted (27 September 2002) to today |
| `ley-20089/` | Ley 20.089 que crea el Sistema Nacional de Certificación de Productos Orgánicos Agrícolas | 2 | As enacted (17 January 2006) to today |
| `ley-21368/` | Ley 21.368 que regula la entrega de plásticos de un solo uso y las botellas plásticas | 3 | As enacted (13 August 2021) to today |
| `ley-21100/` | Ley 21.100 que prohíbe la entrega de bolsas plásticas de comercio en todo el territorio nacional | 1 | As enacted (4 February 2019) to today |
| `ley-20293/` | Ley 20.293 que protege a los cetáceos | 1 | As enacted (25 October 2008) to today |
| `ley-21069/` | Ley 21.069 que crea el Instituto Nacional de Desarrollo Sustentable de la Pesca Artesanal y de la Acuicultura de Pequeña Escala (INDESPA) | 3 | As enacted (15 February 2018) to today |
| `ley-21151/` | Ley 21.151 que otorga reconocimiento legal al pueblo tribal afrodescendiente chileno | 1 | As enacted (16 April 2019) to today |
| `dfl-251/` | DFL 251 de 1931, Ley de Seguros (compañías de seguros, sociedades anónimas y bolsas de comercio) | 38 | From the oldest version available (1 July 1970) to today |
| `dfl-382/` | DFL 382 de 1988, Ley General de Servicios Sanitarios | 13 | As enacted (21 June 1989) to today |
| `dl-1939/` | Decreto Ley 1.939 de 1977, normas sobre adquisición, administración y disposición de bienes del Estado | 16 | As enacted (10 November 1977) to today |
| `dl-3063/` | Decreto Ley 3.063 de 1979, Ley de Rentas Municipales | 27, and 2 on `futuro` | As enacted (1 January 1980) to today, through the texto refundido of Decreto 2.385 of 1996 |
| `dl-2222/` | Decreto Ley 2.222 de 1978, Ley de Navegación | 14 | As enacted (31 May 1978) to today |
| `ordenanza-aduanas/` | Ordenanza de Aduanas | 25, and 1 on `futuro` | From the oldest version available (21 July 1998) to today, through DFL 2 of 1998 and DFL 30 of 2004 (textos refundidos) |
| `ley-concesiones-obras-publicas/` | Ley de Concesiones de Obras Públicas | 15 | As enacted (3 February 1983) to today, from DFL 591 of 1982 through DFL 164 of 1991 and Decreto 900 of 1996 |
| `dfl-7-1980/` | DFL 7 de 1980, Ley Orgánica del Servicio de Impuestos Internos | 17 | As enacted (15 October 1980) to today |
| `dl-3475/` | Decreto Ley 3.475 de 1980, Ley sobre Impuesto de Timbres y Estampillas | 74 | As enacted (1 November 1980) to today |
| `dl-2695/` | Decreto Ley 2.695 de 1979, normas para regularizar la posesión de la pequeña propiedad raíz | 10 | As enacted (21 July 1979) to today |
| `dl-2460/` | Decreto Ley 2.460 de 1979, Ley Orgánica de la Policía de Investigaciones de Chile | 21 | As enacted (24 January 1979) to today |
| `ley-general-cooperativas/` | Ley General de Cooperativas | 20 | As enacted (9 November 1978) to today, from Decreto 502 of 1978 through the texto refundido of DFL 5 of 2003 |
| `dfl-850/` | DFL 850 de 1997, Ley Orgánica del Ministerio de Obras Públicas y DFL 206 de 1960 sobre caminos | 14, and 1 on `futuro` | From the oldest version available (20 May 1985) to today, through Decreto 294 of 1985 and the texto refundido of DFL 850 of 1997 |
| `ley-21680/` | Ley 21.680 que crea un registro de deuda consolidada | 1 | As enacted (1 April 2026) to today |
| `ley-20575/` | Ley 20.575 que establece el principio de finalidad en el tratamiento de datos personales | 1 | As enacted (17 February 2012) to today |
| `ley-18059/` | Ley 18.059 que asigna al Ministerio de Transportes y Telecomunicaciones el carácter de organismo rector nacional de tránsito | 2 | As enacted (7 November 1981) to today |
| `ley-19420/` | Ley 19.420 que establece incentivos para el desarrollo económico de las provincias de Arica y Parinacota | 18 | As enacted (23 October 1995) to today, through the texto refundido of DFL 1 of 2001 |
| `ley-20241/` | Ley 20.241 que establece un incentivo tributario a la inversión privada en investigación y desarrollo | 4 | As enacted (19 April 2008) to today |
| `ley-20885/` | Ley 20.885 que crea la Subsecretaría de Derechos Humanos | 1 | As enacted (5 January 2016) to today |
| `ley-19532/` | Ley 19.532 que crea el régimen de jornada escolar completa diurna | 2 | As enacted (17 November 1997) to today |
| `ley-19032/` | Ley 19.032 que reorganiza el Ministerio Secretaría General de Gobierno | 2 | As enacted (4 February 1991) to today |
| `ley-19606/` | Ley 19.606 que establece incentivos para el desarrollo económico de las regiones de Aysén y de Magallanes y de la provincia de Palena | 6 | As enacted (14 April 1999) to today |
| `ley-18392/` | Ley 18.392 que establece un régimen preferencial aduanero y tributario para el territorio de la XII Región de Magallanes y de la Antártica Chilena | 6 | As enacted (14 January 1985) to today |
| `ley-19149/` | Ley 19.149 que establece régimen aduanero y tributario para las comunas de Porvenir y Primavera de Tierra del Fuego | 4 | As enacted (6 July 1992) to today |
| `ley-20412/` | Ley 20.412 que establece un sistema de incentivos para la sustentabilidad agroambiental de los suelos agropecuarios | 1 | As enacted (9 February 2010) to today |
| `ley-19162/` | Ley 19.162 que establece sistema obligatorio de clasificación de ganado, tipificación y nomenclatura de sus carnes | 4 | As enacted (7 September 1992) to today |
| `ley-20234/` | Ley 20.234 que establece un procedimiento de saneamiento y regularización de loteos | 7 | As enacted (5 January 2008) to today |
| `ley-20962/` | Ley 20.962 que aplica la Convención sobre el Comercio Internacional de Especies Amenazadas de Flora y Fauna Silvestre | 1 | As enacted (16 November 2016) to today |
| `ley-18302/` | Ley 18.302 de Seguridad Nuclear | 7 | As enacted (2 May 1984) to today |
| `ley-20765/` | Ley 20.765 que crea mecanismo de estabilización de precios de los combustibles | 9 | As enacted (9 July 2014) to today |
| `ley-20063/` | Ley 20.063 que crea fondos de estabilización de precios de combustibles derivados del petróleo | 7 | As enacted (29 September 2005) to today |
| `ley-19779/` | Ley 19.779 que establece normas relativas al virus de inmunodeficiencia humana | 3 | As enacted (14 December 2001) to today |
| `ley-21155/` | Ley 21.155 que establece medidas de protección a la lactancia materna y su ejercicio | 1 | As enacted (2 May 2019) to today |
| `ley-21659/` | Ley 21.659 sobre seguridad privada | 3, and 1 on `futuro` | As enacted (28 November 2025) to today |
| `ley-18020/` | Ley 18.020 que establece subsidio familiar para personas de escasos recursos | 38 | As enacted (17 August 1981) to today |
| `ley-20365/` | Ley 20.365 que establece franquicia tributaria respecto de sistemas solares térmicos | 2 | As enacted (19 August 2009) to today |
| `ley-19713/` | Ley 19.713 que establece como medida de administración el límite máximo de captura por armador | 6 | As enacted (25 January 2001) to today |
| `ley-16395/` | Ley 16.395 de organización y atribuciones de la Superintendencia de Seguridad Social | 6 | From the oldest version available (4 December 1974) to today |
| `dl-2859/` | Decreto Ley 2.859 de 1979, Ley Orgánica de Gendarmería de Chile | 16 | As enacted (15 September 1979) to today |
| `dl-1350/` | Decreto Ley 1.350 de 1976, que crea la Corporación Nacional del Cobre de Chile | 4 | As enacted (1 April 1976) to today |
| `ley-19172/` | Ley 19.172 sobre arrepentimiento eficaz | 2 | As enacted (4 November 1992) to today |
| `ley-19553/` | Ley 19.553 que concede asignación de modernización y otros beneficios | 8 | As enacted (4 February 1998) to today |
| `ley-21592/` | Ley 21.592 que establece un estatuto de protección en favor del denunciante | 1 | As enacted (21 August 2023) to today |
| `ley-19853/` | Ley 19.853 que crea una bonificación a la contratación de mano de obra en las regiones extremas y las provincias de Chiloé y Palena | 4 | As enacted (11 February 2003) to today |
| `ley-20930/` | Ley 20.930 que establece el derecho real de conservación medioambiental | 1 | As enacted (25 June 2016) to today |
| `ley-20096/` | Ley 20.096 que establece mecanismos de control aplicables a las sustancias agotadoras de la capa de ozono | 1 | As enacted (23 March 2006) to today |
| `ley-19067/` | Ley 19.067 que establece normas permanentes sobre entrada de tropas extranjeras y salida de tropas nacionales | 3 | As enacted (1 July 1991) to today |
| `ley-21175/` | Ley 21.175 sobre fomento a las artes escénicas | 1 | As enacted (16 September 2019) to today |
| `ley-21527/` | Ley 21.527 que crea el Servicio Nacional de Reinserción Social Juvenil | 1 | As enacted (13 January 2026) to today |
| `ley-21565/` | Ley 21.565 que establece un régimen de protección y reparación integral en favor de las víctimas de femicidio y suicidio femicida y sus familias | 1 | As enacted (9 May 2023) to today |
| `ley-21332/` | Ley 21.332 que implementa un sistema táctico de operación policial | 1 | As enacted (11 June 2021) to today |
| `ley-20655/` | Ley 20.655 que establece incentivos especiales para las zonas extremas del país | 1 | As enacted (1 February 2013) to today |
| `ley-18196/` | Ley 18.196 sobre normas complementarias de administración financiera, personal y de incidencia presupuestaria | 4 | As enacted (29 December 1982) to today |
| `ley-21371/` | Ley 21.371 que establece medidas especiales en caso de muerte gestacional o perinatal | 1 | As enacted (29 September 2021) to today |
| `ley-21334/` | Ley 21.334 sobre determinación del orden de los apellidos por acuerdo de los padres | 1 | As enacted (11 January 2022) to today |
| `ley-21198/` | Ley 21.198 que autoriza la intermediación de medicamentos por parte de CENABAST | 1 | As enacted (8 January 2020) to today |
| `ley-18989/` | Ley 18.989 que crea el Ministerio de Planificación y Cooperación | 7 | As enacted (19 July 1990) to today |
| `ley-20254/` | Ley 20.254 que crea el Instituto Nacional de Propiedad Industrial | 2 | As enacted (14 April 2008) to today, through the texto refundido of DFL 3 of 2022 |
| `ley-18156/` | Ley 18.156 que establece exención de cotizaciones previsionales a los técnicos extranjeros | 3 | As enacted (25 August 1982) to today |
| `ley-20879/` | Ley 20.879 que sanciona el transporte de desechos hacia vertederos clandestinos | 1 | As enacted (25 November 2015) to today |
| `dfl-2-1998-educacion/` | DFL 2 de 1998 (Educación), sobre subvención del Estado a establecimientos educacionales | 29 | As enacted (28 November 1998) to today |
| `dfl-150/` | DFL 150 de 1981, Sistema Único de Prestaciones Familiares y Sistema de Subsidios de Cesantía | 10 | As enacted (25 March 1982) to today |
| `dfl-2-1967-trabajo/` | DFL 2 de 1967 (Trabajo), Ley Orgánica de la Dirección del Trabajo | 3 | From the oldest version available (3 December 1996) to today |
| `dl-3346/` | Decreto Ley 3.346 de 1980, Ley Orgánica del Ministerio de Justicia y Derechos Humanos | 11 | As enacted (22 May 1980) to today, through the texto refundido of DFL 3 of 2017 |
| `dfl-1-1997-defensa/` | DFL 1 de 1997 (Defensa), Estatuto del Personal de las Fuerzas Armadas | 21 | As enacted (27 October 1997) to today |
| `ley-19284/` | Ley 19.284 que establece normas para la plena integración social de personas con discapacidad | 5 | As enacted (14 January 1994) to today |
| `ley-20423/` | Ley 20.423 del sistema institucional para el desarrollo del turismo | 3 | As enacted (12 February 2010) to today |
| `ley-20594/` | Ley 20.594 que crea inhabilidades para condenados por delitos sexuales contra menores y establece registro de dichas inhabilidades | 1 | As enacted (19 June 2012) to today |
| `ley-19701/` | Ley 19.701 que reforma los institutos tecnológicos CORFO | 1 | As enacted (28 January 2001) to today |
| `ley-20304/` | Ley 20.304 sobre operación de embalses frente a alertas y emergencias de crecidas | 2 | As enacted (13 December 2008) to today |
| `ley-20670/` | Ley 20.670 que crea el sistema Elige Vivir Sano | 2 | As enacted (31 May 2013) to today |
| `ley-20715/` | Ley 20.715 sobre protección a deudores de créditos en dinero | 1 | As enacted (13 December 2013) to today |
| `ley-21033/` | Ley 21.033 que crea la XVI Región de Ñuble y las provincias de Diguillín, Punilla e Itata | 2 | As enacted (6 September 2018) to today |
| `ley-21163/` | Ley 21.163 que incorpora las resoluciones del Consejo de Seguridad de las Naciones Unidas referentes al financiamiento del terrorismo | 1 | As enacted (13 July 2019) to today |
| `ley-21349/` | Ley 21.349 que establece normas sobre composición, etiquetado y comercialización de los fertilizantes y bioestimulantes | 1 | As enacted (27 September 2022) to today |
| `ley-21512/` | Ley 21.512 que regula la disposición final de elementos de protección personal de carácter sanitario | 1 | As enacted (14 December 2022) to today |
| `ley-21673/` | Ley 21.673 que adopta medidas para combatir el sobreendeudamiento | 1 | As enacted (30 May 2024) to today |
| `ley-21678/` | Ley 21.678 que establece el acceso a internet como servicio público de telecomunicaciones | 1 | As enacted (3 July 2024) to today |
| `ley-19023/` | Ley 19.023 que crea el Servicio Nacional de la Mujer | 4 | As enacted (3 January 1991) to today |
| `ley-19137/` | Ley 19.137 que establece normas sobre pertenencias mineras de CODELCO-Chile que no forman parte de yacimientos en actual explotación | 3 | As enacted (12 May 1992) to today |
| `ley-18502/` | Ley 18.502 que establece impuestos a combustibles | 8 | As enacted (3 April 1986) to today |
| `ley-18525/` | Ley 18.525 sobre normas de importación de mercancías al país | 10 | As enacted (30 June 1986) to today, through the texto refundido of DFL 31 of 2005 |
| `ley-18634/` | Ley 18.634 que establece sistema de pago diferido de derechos de aduana y crédito fiscal | 36 | As enacted (5 August 1987) to today |
| `dl-2757/` | Decreto Ley 2.757 de 1979, normas sobre asociaciones gremiales | 8 | As enacted (4 July 1979) to today |
| `dl-3516/` | Decreto Ley 3.516 de 1980, normas sobre división de predios rústicos | 8 | As enacted (1 December 1980) to today |
| `dl-2079/` | Decreto Ley 2.079 de 1977, Ley Orgánica del Banco del Estado de Chile | 10 | As enacted (18 January 1978) to today |
| `dfl-323/` | DFL 323 de 1931, Ley de Servicios de Gas | 6 | From the oldest version available (4 August 1979) to today |
| `dl-3472/` | Decreto Ley 3.472 de 1980, Fondo de Garantía para Pequeños y Medianos Empresarios | 19 | As enacted (2 September 1980) to today |
| `dl-1094/` | Decreto Ley 1.094 de 1975, normas sobre extranjeros en Chile | 8 | As enacted (19 July 1975) to its repeal by Ley 21.325 (12 February 2022) |
| `dl-3607/` | Decreto Ley 3.607 de 1981, normas sobre funcionamiento de vigilantes privados | 9 | As enacted (8 January 1981) to its repeal by Ley 21.659 (28 November 2025) |
| `dl-600/` | Decreto Ley 600 de 1974, Estatuto de la Inversión Extranjera | 5 | As enacted (13 July 1974), through the texto refundido of DFL 523 of 1993 to its repeal by Ley 20.780 (1 January 2016) |
| `dl-2565/` | Decreto Ley 2.565 de 1979, que sustituye el texto del Decreto Ley 701 de 1974 sobre fomento forestal | 10 | As enacted (3 April 1979) to today |

Every version is LeyChile's own dated version of the act. "As enacted" starts with the act as published, on the day it took effect; "oldest version available" starts with the oldest text LeyChile gives that holds up (see `REPRODUCE.md`). Where an act's own text defers its entry into force to a fixed day, its first version is dated that day. Versions dated after the retrieval day are on the branch `futuro`. The per-act `README.md` in each folder lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 102 of the Código Civil say on 1 January 2010? | `python tools/en_vigor_el.py 2010-01-01 codigo-civil 102` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2010-01-01T23:59:59Z" main -- codigo-civil/art-0102.md):codigo-civil/art-0102.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2010-01-01T23:59:59Z" main -- codigo-civil/art-0102.md; git show "$($r):codigo-civil/art-0102.md"` |
| Which law wrote each paragraph of art. 19 of the Constitution? | `git blame constitucion/art-019.md` |
| Every change to art. 102, word by word | `git log -p --word-diff codigo-civil/art-0102.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/ley-21400` (tags `law/<key>` mark each law's commit) |
| The whole act on a date | `python tools/en_vigor_el.py 2000-01-01 constitucion` |
| The act as LeyChile dated a version | `git show constitucion/2005-09-22` (tags `<act>/<in-force day>`) |
| Laws passed but not yet in force | `git log main..futuro` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Santiago, on the day the change took effect** (the in-force date). Enactment and publication dates are trailers (`Enacted:`, `Published:`), and the in-force day is in `In-force:`, which the tools read.
- **The in-force day is LeyChile's.** BCN dates every version of a norm from the day it entered into force (`vigenteDesde`) and lists, for each version, the norms that ended it and the day each took effect (`inicioVigencia`). Those are the dates used.
- **Default rule.** Código Civil art. 7: "La publicación de la ley se hará mediante su inserción en el Diario Oficial, y desde la fecha de éste se entenderá conocida de todos y será obligatoria." A law's own vigencia rule overrides it (art. 7, inciso tercero), and LeyChile's dates already apply such rules.
- **The Constitution of 1980** was published on 11 August 1980 (DL 3.464) and approved by plebiscite on 11 September 1980; by its own Artículo final it took effect six months after the plebiscite, on 11 March 1981. Its first commit is dated 1981-03-11, not the publication day LeyChile shows.
- **Textos refundidos.** When a code is re-enacted as a consolidated text, LeyChile continues it as a new norm: the Constitution under Decreto 100 of 2005 (from 22 September 2005), the Código Civil under DFL 1 of 2000. The Constitution's switch is one commit credited to Decreto 100, which lists the renumbered provisions. The Código Civil starts at DFL 1 of 2000: its first commit is "oldest version available", not the code of 1855.
- **Deferred entry into force.** Where LeyChile's versions list names no norm for a day but the new amendment notes on the changed provisions name one law, published earlier, the change is credited to that law (Ley 21.120, Ley 21.334, Ley 21.484 in the Código Civil). The version note says so.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.
- Git cannot store dates before 1970. Nothing in this repository is dated before 1981.

## How it is checked

- Every version of every act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- Against the official text today: Lexifina's code reads LeyChile's current text of each act (the page as served on the retrieval day) and compares it with the repository's version in force that day, provision by provision. On 2026-10-28 every act matched exactly (the acts added on 2026-10-29 were read that day and compared with the text in force on 2026-10-28), and every version carries the sha256 of the LeyChile response it was parsed from.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`ley-21400@leychile.invalid`), so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **Credits come only from the source.** A changed provision is credited to a law only when that law took effect on the version's day and one of LeyChile's amendment notes on the provision names it ("LEY 21400 Art. 8 D.O. 10.12.2021"), by link, by type and number, or (for a Rectificación) by its Diario Oficial date. Where exactly one law took effect that day, a provision removed outright is credited to it too.
- **Unexplained changes** are committed by the publisher, BCN, and labelled "unexplained": 22 corrections of typography on 6 January 2003 in the Constitution (º/°, accents), and four changes in the Código Civil that no note explains on their day (art. 1993 on 14 September 2000, a Rectificación of 14 July 2000 applied late; art. 141 on 30 August 2004; art. 188 on 5 July 2005; art. 144 on 30 August 2005). Each version note quotes the new notes LeyChile shows.
- Rectificaciones (corrections published in the Diario Oficial) are commits of kind "decree".
- Blame credits whole lines (one paragraph per line). In a provision written by several laws, use `git log -p --word-diff` to see exactly which words each law changed.

## What it does not show

- **The Código Civil before 2000.** LeyChile keeps the code of 1855 (idNorma 1973) with only three versions (1857, 1965, 1996) and no amending norms, and DFL 2 of 1996 with nine; neither gives the dated, credited history that the rest of this record has, so the code starts at DFL 1 of 2000.
- **DFL 1 of 2000 fixes five other laws** (Registro Civil, cambio de nombres, Menores, Abandono de familia y pensiones alimenticias, Impuesto a las herencias) in its arts. 3 to 8. Its art. 2, the Código Civil, is in `codigo-civil/`; arts. 3, 4, 6, 7 and 8 continue `ley-4808/`, `ley-17344/`, `ley-16618/`, `ley-14908/` and `ley-16271/`, each reading only its own article.
- **BCN's editorial notes** ("NOTA" boxes) and the amendment notes themselves are not in the text: the notes are used only to credit laws.
- **Commencement that LeyChile does not date.** Where a law says that a provision applies only to cases begun after a day, that is in the text, not in the dates; no applicability data is recorded yet.
- **Court rulings.** Rulings of the Tribunal Constitucional that strike a provision (art. 93 N° 7) appear only where LeyChile shows them as a version of the act; none of the acts here has one so far.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code turns LeyChile's responses, each kept with the sha256 of its bytes, into `corpus.json`, and the shared builder `tools/build.py` writes the history with `git fast-import`.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [LeyChile, Biblioteca del Congreso Nacional de Chile](https://www.bcn.cl/leychile) | Official legislation | yes, every version by date | yes, a note per paragraph and a list per version | JSON services | Used. `Consulta/get_versiones` (dated versions and the norms that ended each), `Navegar/get_norma_json` (the text of one version), `Navegar/get_cadena_refundidos` (textos refundidos) |
| LeyChile XML export (`Consulta/obtxml`) | Official legislation | current text | yes | per norm | Answers, but the notes are mixed into the text columns; not used |
| [Diario Oficial](https://www.diariooficial.interior.gob.cl) | Official gazette | n/a | n/a | no | Not read; LeyChile gives the D.O. date of every norm |
| [pisanvs/ley-chile](https://github.com/pisanvs/ley-chile) | Volunteer git repo (AGPL-3.0) | yes | partly | n/a | Prior art, for reconciliation only; no text copied |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of the Republic of Chile, as published by the Biblioteca del Congreso Nacional de Chile in LeyChile. Fuente: Biblioteca del Congreso Nacional de Chile, LeyChile (www.bcn.cl/leychile). Chile's copyright law (Ley 17.336) has no express exclusion for legal texts, and BCN publishes no licence for LeyChile, so their copyright status is not confirmed here; they are reproduced with that attribution. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## En español

Historia del derecho chileno en git: un archivo por disposición y un commit por norma, fechado el día de su entrada en vigencia y firmado por la norma que hizo el cambio (`git blame` nombra la ley de cada párrafo). Contiene la Constitución Política de la República desde su entrada en vigencia el 11 de marzo de 1981, el Código Civil desde el texto refundido del DFL 1 de 2000, la Ley 19.628 sobre protección de la vida privada desde 1999 (la Ley 21.719, que la reemplaza desde el 1 de diciembre de 2026, está en la rama `futuro`) y los demás códigos y leyes de la tabla de arriba, cada uno con las versiones fechadas de LeyChile.

- Texto vigente en una fecha: `python tools/en_vigor_el.py 2010-01-01 codigo-civil 102`
- Fechas: las de LeyChile (vigente desde). Regla supletoria: art. 7 del Código Civil (obligatoria desde la fecha de su publicación en el Diario Oficial, salvo que la ley disponga otra cosa).
- Autoría: cada cambio se atribuye a una norma solo si una nota de modificación de LeyChile la nombra; lo que ninguna nota explica queda como "unexplained", a nombre de la BCN.
- Fuente: Biblioteca del Congreso Nacional de Chile, LeyChile (www.bcn.cl/leychile). Ningún modelo de IA escribió texto legal.
