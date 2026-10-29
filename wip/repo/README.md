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
| `ley-19537/` | Ley 19.537 sobre copropiedad inmobiliaria | 9 | As enacted (16 December 1997) to today |
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
| `ley-18314/` | Ley 18.314 que determina conductas terroristas y fija su penalidad | 14 | As enacted (17 May 1984) to today |
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
- Against the official text today: `tools/verify.py` reads LeyChile's current text of each act (the page as served on the retrieval day) and compares it with the repository's version in force that day, provision by provision. On 2026-10-28 every act matched exactly (the acts added on 2026-10-29 were read that day and compared with the text in force on 2026-10-28), and every version carries the sha256 of the LeyChile response it was parsed from.
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

`tools/fetch.py` downloads every source response once through curl (one request per second, cached by the sha256 of the URL), `tools/parse.py` turns the cache into `corpus.json`, and the shared builder `tools/build.py` writes the history with `git fast-import`. The same corpus always gives the same hashes. `REPRODUCE.md` records every command, tool version, data hash and decision, and the result of a hash-for-hash rebuild.

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
