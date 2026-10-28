# Chile: law history in git

The law of Chile as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `cl/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución Política de la República (1980) | 78 | From its entry into force (11 March 1981) to today, through the texto refundido of 2005 (Decreto 100) |
| `codigo-civil/` | Código Civil | 29 | From the texto refundido of DFL 1 of 2000 (30 May 2000) to today |
| `ley-19628/` | Ley 19.628 sobre protección de la vida privada (1999) | 8, and 1 on `futuro` | As enacted (28 August 1999) to today; Ley 21.719, which rewrites it from 1 December 2026, is on the branch `futuro` |

Every version is LeyChile's own dated version of the act. The per-act `README.md` in each folder lists every provision, how often it changed and when.

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
- Against the official text today: `tools/verify.py` reads LeyChile's current text of each act (the page as served on the retrieval day) and compares it with the repository's version in force that day, provision by provision. On 2026-10-28 all three acts matched exactly, and every version carries the sha256 of the LeyChile response it was parsed from.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`ley-21400@leychile.invalid`), so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **Credits come only from the source.** A changed provision is credited to a law only when that law took effect on the version's day and one of LeyChile's amendment notes on the provision names it ("LEY 21400 Art. 8 D.O. 10.12.2021"), by link, by type and number, or (for a Rectificación) by its Diario Oficial date. Where exactly one law took effect that day, a provision removed outright is credited to it too.
- **Unexplained changes** are committed by the publisher, BCN, and labelled "unexplained": 22 corrections of typography on 6 January 2003 in the Constitution (º/°, accents), and four changes in the Código Civil that no note explains on their day (art. 1993 on 14 September 2000, a Rectificación of 14 July 2000 applied late; art. 141 on 30 August 2004; art. 188 on 5 July 2005; art. 144 on 30 August 2005). Each version note quotes the new notes LeyChile shows.
- Rectificaciones (corrections published in the Diario Oficial) are commits of kind "decree".
- Blame credits whole lines (one paragraph per line). In a provision written by several laws, use `git log -p --word-diff` to see exactly which words each law changed.

## What it does not show

- **The Código Civil before 2000.** LeyChile keeps the code of 1855 (idNorma 1973) with only three versions (1857, 1965, 1996) and no amending norms, and DFL 2 of 1996 with nine; neither gives the dated, credited history that the rest of this record has, so the code starts at DFL 1 of 2000.
- **DFL 1 of 2000 also fixes five other laws** (Registro Civil, cambio de nombres, Menores, Abandono de familia y pensiones alimenticias, Impuesto a las herencias) in its arts. 3 to 8. Only its art. 2, the Código Civil, is in `codigo-civil/`.
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

Historia del derecho chileno en git: un archivo por disposición y un commit por norma, fechado el día de su entrada en vigencia y firmado por la norma que hizo el cambio (`git blame` nombra la ley de cada párrafo). Contiene la Constitución Política de la República desde su entrada en vigencia el 11 de marzo de 1981, el Código Civil desde el texto refundido del DFL 1 de 2000, y la Ley 19.628 sobre protección de la vida privada desde 1999; la Ley 21.719, que la reemplaza desde el 1 de diciembre de 2026, está en la rama `futuro`.

- Texto vigente en una fecha: `python tools/en_vigor_el.py 2010-01-01 codigo-civil 102`
- Fechas: las de LeyChile (vigente desde). Regla supletoria: art. 7 del Código Civil (obligatoria desde la fecha de su publicación en el Diario Oficial, salvo que la ley disponga otra cosa).
- Autoría: cada cambio se atribuye a una norma solo si una nota de modificación de LeyChile la nombra; lo que ninguna nota explica queda como "unexplained", a nombre de la BCN.
- Fuente: Biblioteca del Congreso Nacional de Chile, LeyChile (www.bcn.cl/leychile). Ningún modelo de IA escribió texto legal.
