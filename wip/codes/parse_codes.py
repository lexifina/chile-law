"""Phase 2 of Chile (gitlaw-CL-codes): reads the LeyChile cache and writes scripts/chile-law/corpus.d/50-codes.json.

    python -X utf8 scripts/chile-law/codes/parse_codes.py [--acts codigo-penal,...] [--out PATH]

It reuses the main agent's parse.py unchanged (read_version, the credit rules, the law key scheme): it only adds the
verified idNorma chains (codes/fetch_codes.py) and the act metadata of the codes, then runs parse.act_versions on
each. No network. The part is written atomically (.tmp, then rename). Law keys shared with corpus.json must name the
same LeyChile norm; the script stops if one does not.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
import fetch  # noqa: E402
import parse  # noqa: E402
from fetch_codes import CHAINS  # noqa: E402

L = parse.LEYCHILE
META = {
    'codigo-penal': {'short': 'CP', 'title': 'Código Penal', 'url': L + '1984', 'first_law': True},
    'codigo-comercio': {'short': 'CCom', 'title': 'Código de Comercio', 'url': L + '1974', 'first_law': True},
    'codigo-trabajo': {'short': 'CT', 'title': 'Código del Trabajo', 'url': L + '207436', 'first_law': False},
    'codigo-procedimiento-civil': {'short': 'CPC', 'title': 'Código de Procedimiento Civil', 'url': L + '22740',
                                   'first_law': True},
    'codigo-procesal-penal': {'short': 'CPP', 'title': 'Código Procesal Penal', 'url': L + '176595',
                              'first_law': True},
}
DEFAULT_ACTS = 'codigo-penal,codigo-comercio,codigo-trabajo,codigo-procedimiento-civil,codigo-procesal-penal'
OUT = ROOT / 'corpus.d' / '50-codes.json'


def setup() -> None:
    fetch.ACTS.update(CHAINS)
    parse.ACT_META.update(META)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--acts', default=DEFAULT_ACTS)
    ap.add_argument('--out', default=str(OUT))
    ap.add_argument('--main-corpus', default=str(ROOT / 'corpus.json'),
                    help='checked for law keys that name a different norm')
    args = ap.parse_args()
    setup()
    laws = parse.Laws()
    log: list[str] = []
    acts = [parse.act_versions(s, laws, log) for s in args.acts.split(',')]
    out_laws = {k: {kk: vv for kk, vv in v.items() if not kk.startswith('_')} for k, v in sorted(laws.laws.items())}
    main_laws = json.loads(Path(args.main_corpus).read_text(encoding='utf-8')).get('laws', {})
    clash = [k for k, v in out_laws.items() if k in main_laws and (
        main_laws[k]['label'] != v['label'] or (main_laws[k].get('url') and v.get('url')
                                                and main_laws[k]['url'] != v['url']))]
    if clash:
        raise SystemExit('law keys naming a different norm than corpus.json: ' + ', '.join(
            f'{k} ({out_laws[k]["label"]} {out_laws[k]["url"]} vs {main_laws[k]["label"]} {main_laws[k]["url"]})'
            for k in clash))
    decisions = [
        'Código Penal, Código de Comercio, Código del Trabajo, Código de Procedimiento Civil and Código Procesal '
        'Penal (corpus.d/50-codes.json) are parsed by the same parse.py rules as the Constitution, from the LeyChile '
        'norms verified on 2026-10-28 with get_cadena_refundidos and get_versiones: CP 1984, CCom 1974, CT 3471 '
        '(DFL 1 of 1994) then 207436 (DFL 1 of 2003), CPC 22740 (Ley 1.552), CPP 176595 (Ley 19.696).',
        'Código del Trabajo: LeyChile keeps the Código del Trabajo of 1987 (Ley 18.620, idNorma 30011) in one '
        'undated version only, so its history from 1987 to 1994 is not available; the act starts with the texto '
        'refundido of DFL 1 of 1994 as the oldest version available, and DFL 1 of 2003 is its next text.',
    ] + [d for d in extra_decisions(acts)]
    part = {
        'laws': out_laws,
        'acts': acts,
        'decisions': decisions,
        'ai_use': ['Phase 2 codes: none at data-build time; codes/*.py are deterministic code written with Claude '
                   'Code (claude-opus-5-5), reusing parse.py; no model reads, writes or summarises legal text.'],
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.name + '.tmp')
    tmp.write_text(json.dumps(part, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    tmp.replace(out)
    (HERE / 'parse.log').write_text('\n'.join(log) + '\n', encoding='utf-8', newline='\n')
    parse.stats(part)


def extra_decisions(acts: list[dict]) -> list[str]:
    out = []
    for a in acts:
        m = parse.ACT_META[a['slug']]
        if m.get('first'):
            out.append(f'{a["short"]}: ' + m['first'][1])
    return out


if __name__ == '__main__':
    main()
