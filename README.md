# Chile: law history in git


The national law of Chile as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Chile's national law, which global-law reads at `chile/national/acts/`.

**What is in it now:** the Constitution, 14 codes and 367 other laws, decree-laws and decrees with force of law, among them the Código Civil, the Código Penal and the Código del Trabajo, with 4,590 versions in force from 1875 to 2026; 8 of the acts have since been repealed, and their history ends with a version that has no provisions. 32 more versions, due to take effect from 1 December 2026 to 2 April 2029, are on the `futuro` branch. [`data/versions.json`](data/versions.json) lists every act with the day each version took effect; [`data/laws.csv`](data/laws.csv) lists every norm the record names, with its dates.

Each act is a folder named after it (`codigo-trabajo/`, `ley-19628/`, `dl-3500/`), with one file per article, transitory provision and heading: `codigo-trabajo/art-067.md` is art. 67 of the Código del Trabajo, on the feriado anual. Each folder's `README.md` lists its provisions and when each changed.

The text is in Spanish, as LeyChile publishes it, one paragraph per line, with LeyChile's amendment notes and BCN's editorial notes left out.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to art. 67 of the Código del Trabajo | `git log -p --word-diff -- codigo-trabajo/art-067.md` |
| Which law wrote each paragraph of art. 67? | `git blame codigo-trabajo/art-067.md` |
| Every version of the Código del Trabajo, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- codigo-trabajo ":^codigo-trabajo/README.md"` |
| Art. 67 as in force on 1 January 2010 | `python tools/en_vigor_el.py 2010-01-01 codigo-trabajo 67` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Chilean law](https://global-law.lexifina.com/v1/try_claude?country=chile)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=chile)**: the same question in ChatGPT.
- **[Search Chilean law on our site](https://lexifina.com/law?country=chile&q=feriado+anual)**: a search for "feriado anual", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=feriado+anual&jurisdiction=chile)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Spanish or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add chile/national/acts
python3 tools/law.py show 2026-01-01 chile/national/acts/codigo-trabajo/art-067.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Santiago, on the day the change took effect, and carries it in its `In-force:` trailer, beside `Published:`, the day of the Diario Oficial:

- the day is LeyChile's own for each version (`vigenteDesde`), which already applies a law's own vigencia clause; without one, Código Civil art. 7 makes a law binding from its publication in the Diario Oficial. An act whose own text defers its entry into force to a fixed day starts on that day (the Constitution of 1980 on 11 March 1981, six months after the plebiscite);
- where LeyChile's day departs from the amending law's own transitory articles (phase-ins by region or by stage, terms counted short of Código Civil art. 48, wordings in force only until a stated day), the law's own text decides; each such decision is listed in `REPRODUCE.md`;
- git cannot store dates before 1970, so the 95 earlier commits (the Código Penal from 1875 and ten acts from 1923 to 1968) are dated from 1970-01-01, one second apart, with the real day in `In-force:`. Ask for a date with `tools/en_vigor_el.py`, not `git log --before`.

Each change is credited to the law that made it, with an address that cannot exist (`Ley 21.645 <ley-21645@leychile.invalid>`), only when one of LeyChile's amendment notes on the provision names that law. A first version that is not the act as enacted ("oldest version available", 24 acts) and the 559 changes no note explains are credited to the publisher, `Biblioteca del Congreso Nacional (LeyChile)`; the committer is Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before; both must match the corpus, whose sha256 is in `data/corpus.sha256`: 4,622 versions of 382 acts, 0 mismatches ([`REPRODUCE.md`](REPRODUCE.md)).
- Every version in `data/versions.json` carries the sha256 of the source bytes it was parsed from.
- The same corpus gives the same commit hashes (`tools/build.py`); `REPRODUCE.md` records that no second build has been compared yet.
- History is append-only (`tools/append.py`): no merge commits on `main`, no commit dates that go backwards, nothing dated in the future, and every commit's trailers parse.

## What it does not show

- **All national law.** These are 382 acts, not the whole statute book; reglamentos and other decrees, municipal ordinances and case law are not here.
- **Changes before an act's first version**, which are inside that first commit: the Código Civil starts at its texto refundido of 2000 (LeyChile keeps the code of 1855 with only three versions and no amending norms), the Código de Comercio at 1988 and the Código del Trabajo at 1994; acts whose older LeyChile versions are not included start at their first version from 1970 on (DFL 340 of 1960 from 1975).
- **Notes and images.** LeyChile's notes are used only to credit laws, and text published only as an image (such as a phase table) is not read.
- **Provisions waiting on an undated event**, such as the parts of Ley 21.770 that wait on decrees and reglamentos not yet published, and rules that apply a provision only to cases begun after a day: neither is in the dates.
- **Which law made some changes.** 559 changes no amendment note explains are credited to BCN.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [LeyChile](https://www.bcn.cl/leychile) (Biblioteca del Congreso Nacional de Chile) | Official legislation | yes, every version by date | The text of each version, the norms that ended it and the day each took effect; its notes name the law behind each change |
| [Diario Oficial](https://www.diariooficial.interior.gob.cl) | Official gazette | n/a | Ley 21.057 as published on 20 January 2018 (edition 41.962), for its versions before 3 October 2022, the day from which LeyChile gives it |

## Licence

See [`LICENSE`](LICENSE). The legal texts are official texts of the Republic of Chile, reproduced with the attribution "Fuente: Biblioteca del Congreso Nacional de Chile, LeyChile (www.bcn.cl/leychile)"; BCN publishes no licence for LeyChile, and Chile's copyright law (Ley 17.336) has no express exclusion for legal texts, so their copyright status is not confirmed here. Lexifina's own contributions (the arrangement, commit messages, tables and tools) are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs at build time; the scripts were written by Claude Code running Claude Opus 5.5 (see [`REPRODUCE.md`](REPRODUCE.md)).

## En español

Historia del derecho nacional chileno en git: un archivo por disposición y un commit por norma, fechado el día de su entrada en vigencia y firmado por la norma que hizo el cambio. Contiene la Constitución Política de la República, 14 códigos y 367 otras leyes, decretos leyes y decretos con fuerza de ley, con 4.590 versiones; las 32 que aún no rigen están en la rama `futuro`. Texto vigente en una fecha: `python tools/en_vigor_el.py 2010-01-01 codigo-trabajo 67`. Fuente: Biblioteca del Congreso Nacional de Chile, LeyChile (www.bcn.cl/leychile).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
