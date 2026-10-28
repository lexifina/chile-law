"""Phase 2 of Chile (gitlaw-CL-codes): reads the LeyChile cache and writes scripts/chile-law/corpus.d/50-codes.json
(--part codes, the default), corpus.d/60-more.json (--part more) or corpus.d/70-batch3.json (--part batch3).

    python -X utf8 scripts/chile-law/codes/parse_codes.py [--part codes|more|batch3] [--acts a,b,...] [--out PATH]

It reuses the main agent's parse.py unchanged (read_version, the credit rules, the law key scheme): it only adds the
verified idNorma chains (codes/fetch_codes.py) and the act metadata of the codes, then runs parse.act_versions on
each. No network. The part is written atomically (.tmp, then rename). Law keys shared with corpus.json must name the
same LeyChile norm; the script stops if one does not.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))
import fetch  # noqa: E402
import parse  # noqa: E402
from fetch_codes import CHAINS  # noqa: E402
import anachronism  # noqa: E402

L = parse.LEYCHILE
META = {
    'codigo-penal': {'short': 'CP', 'title': 'Código Penal', 'url': L + '1984', 'first_law': True},
    'codigo-comercio': {'short': 'CCom', 'title': 'Código de Comercio', 'url': L + '1974', 'first_law': True},
    'codigo-trabajo': {'short': 'CT', 'title': 'Código del Trabajo', 'url': L + '207436', 'first_law': False},
    'codigo-procedimiento-civil': {'short': 'CPC', 'title': 'Código de Procedimiento Civil', 'url': L + '22740',
                                   'first_law': True},
    'codigo-procesal-penal': {
        'short': 'CPP', 'title': 'Código Procesal Penal', 'url': L + '176595', 'first_law': True,
        'first': ('2000-12-16', 'The Código Procesal Penal (Ley 19.696, published in the Diario Oficial on 12 October '
                  '2000) says in its own art. 484 when it takes effect: "regirá para las Regiones de Coquimbo y de la '
                  'Araucanía desde el 16 de diciembre de 2000", and for the other regions from 16 October 2001, 2002 '
                  'and 2003 (dates later changed by amendment; today\'s text has the Región Metropolitana from 16 '
                  'June 2005). Its first '
                  'version is dated 2000-12-16, the first day it was in force anywhere, not the publication day '
                  'LeyChile shows; the regional phases are in the text of art. 484, not in the dates.')},
}
META.update({
    'codigo-tributario': {'short': 'CTrib', 'title': 'Código Tributario', 'url': L + '6374', 'first_law': True},
    'codigo-sanitario': {'short': 'CSan', 'title': 'Código Sanitario', 'url': L + '5595', 'first_law': True},
    'codigo-aguas': {'short': 'CAguas', 'title': 'Código de Aguas', 'url': L + '5605', 'first_law': True},
    'ley-18046': {'short': 'Ley 18.046', 'title': 'Ley 18.046 sobre sociedades anónimas', 'url': L + '29473',
                  'first_law': True},
    'ley-19496': {'short': 'Ley 19.496', 'title': 'Ley 19.496 sobre protección de los derechos de los consumidores',
                  'url': L + '1160403', 'first_law': True},
})
META.update({
    'codigo-organico-tribunales': {'short': 'COT', 'title': 'Código Orgánico de Tribunales', 'url': L + '25563',
                                   'first_law': True},
    'codigo-mineria': {'short': 'CMin', 'title': 'Código de Minería', 'url': L + '29668', 'first_law': True},
    'codigo-aeronautico': {'short': 'CAer', 'title': 'Código Aeronáutico', 'url': L + '30287', 'first_law': True},
    'codigo-justicia-militar': {'short': 'CJM', 'title': 'Código de Justicia Militar', 'url': L + '18914',
                                'first_law': False},
    'ley-20393': {'short': 'Ley 20.393', 'title': 'Ley 20.393 sobre responsabilidad penal de las personas jurídicas',
                  'url': L + '1008668', 'first_law': True},
    'ley-19880': {'short': 'Ley 19.880', 'title': 'Ley 19.880 de bases de los procedimientos administrativos',
                  'url': L + '210676', 'first_law': True},
    'ley-18010': {'short': 'Ley 18.010', 'title': 'Ley 18.010 sobre operaciones de crédito de dinero',
                  'url': L + '29438', 'first_law': True},
})
# Each part file this script writes: its acts, its path, and the decisions that are its own.
PARTS = {
    'codes': {
        'acts': 'codigo-penal,codigo-comercio,codigo-trabajo,codigo-procedimiento-civil,codigo-procesal-penal',
        'out': ROOT / 'corpus.d' / '50-codes.json',
        'decisions': [
            'Código Penal, Código de Comercio, Código del Trabajo, Código de Procedimiento Civil and Código Procesal '
            'Penal (corpus.d/50-codes.json) are parsed by the same parse.py rules as the Constitution, from the LeyChile '
            'norms verified on 2026-10-28 with get_cadena_refundidos and get_versiones: CP 1984, CCom 1974, CT 3471 '
            '(DFL 1 of 1994) then 207436 (DFL 1 of 2003), CPC 22740 (Ley 1.552), CPP 176595 (Ley 19.696).',
            'Código del Trabajo: LeyChile keeps the Código del Trabajo of 1987 (Ley 18.620, idNorma 30011) in one '
            'undated version only, so its history from 1987 to 1994 is not available; the act starts with the texto '
            'refundido of DFL 1 of 1994 as the oldest version available, and DFL 1 of 2003 is its next text.',
        ],
    },
    'batch3': {
        'acts': 'codigo-organico-tribunales,codigo-mineria,codigo-aeronautico,codigo-justicia-militar,ley-20393,'
                'ley-19880,ley-18010',
        'out': ROOT / 'corpus.d' / '70-batch3.json',
        'decisions': [
            'Código Orgánico de Tribunales, Código de Minería, Código Aeronáutico, Código de Justicia Militar, Ley '
            '20.393, Ley 19.880 and Ley 18.010 (corpus.d/70-batch3.json) are parsed by the same parse.py rules as the '
            'Constitution, from the LeyChile norms verified on 2026-10-28 with get_cadena_refundidos and get_versiones: '
            'Ley 7.421 of 1943 (25563), Ley 18.248 (29668), Ley 18.916 (30287), Decreto 2.226 of 1944 (18914), Ley '
            '20.393 (1008668), Ley 19.880 (210676) and Ley 18.010 (29438).',
            'Código de Justicia Militar: LeyChile keeps DL 806 of 1925 (idNorma 6363), which approved the code, in one '
            'version only (1926-03-01), so the act starts with Decreto 2.226 of 1944, which fixed the text of the code, '
            'as the oldest version available.',
        ],
    },
    'more': {
        'acts': 'codigo-tributario,codigo-sanitario,codigo-aguas,ley-18046,ley-19496',
        'out': ROOT / 'corpus.d' / '60-more.json',
        'decisions': [
            'Código Tributario, Código Sanitario, Código de Aguas, Ley 18.046 and Ley 19.496 (corpus.d/60-more.json) '
            'are parsed by the same parse.py rules as the Constitution, from the LeyChile norms verified on 2026-10-28 '
            'with get_cadena_refundidos and get_versiones: DL 830 of 1974 (6374), DFL 725 of 1968 (5595), DFL 1.122 of '
            '1981 (5605), Ley 18.046 (29473), and Ley 19.496 (61438) followed by its texto refundido, DFL 3 of 2021 '
            '(1160403).',
        ],
    },
}
DEFAULT_ACTS = PARTS['codes']['acts']
OUT = PARTS['codes']['out']


STARTS: dict[str, tuple[str, list[str]]] = {}


def setup(slugs: list[str]) -> None:
    """Registers the chains and metadata, and cuts each code's history where LeyChile's versions stop being anachronistic
    (codes/anachronism.py): the versions before that day are left out, and the act's first version is then the oldest
    version available (first_law null), not the act as enacted."""
    fetch.ACTS.update(CHAINS)
    parse.ACT_META.update(META)
    if not getattr(parse.read_version, 'rekeyed', False):
        parse.read_version = rekeyed(parse.read_version)
    for s in slugs:
        day, ev = anachronism.start_day(s)
        if day:
            STARTS[s] = (day, ev)
            parse.ACT_META[s] = dict(parse.ACT_META[s], first_law=False)
            norms = [n for n in CHAINS[s] if fetch.versions(n, offline=True)[-1]['@vigenteDesde'] >= day]
            fetch.ACTS[s] = norms
    cut = {n: STARTS[s][0] for s in STARTS for n in fetch.ACTS[s]}
    original = fetch.versions

    def versions(id_norma: int, offline: bool = False) -> list[dict]:
        vs = original(id_norma, offline)
        return [v for v in vs if v['@vigenteDesde'] >= cut[id_norma]] if id_norma in cut else vs
    fetch.versions = versions


ART_LINE = re.compile(r'(?i)^(art[íi]culo\s+\d+\s*(?:' + parse.SUFFIX + r')?(?:\s+[A-Z])?)\b')


def rekeyed(read_version):
    """LeyChile's table of contents of some old texts names several leaves alike (DFL 1 of 1994 calls the leaves of
    arts. 40 bis A to 40 bis D all "Artículo 40"), so parse.py keys them art-040-2, art-040-3... Such a collision key
    is replaced by the key of the article name the leaf's own text starts with ("Artículo 40 bis A.-"), when that key
    is free, so the file of each article stays the same across versions."""
    def wrapped(raw, width, part=None):
        if part is None:
            raw = unwrap(raw)
        r = read_version(raw, width, part)
        units = r['units']
        out = {}
        for k, u in units.items():
            if re.search(r'-\d+$', k) and re.sub(r'-\d+$', '', k) in units:
                for line in u['text'].splitlines():
                    m = ART_LINE.match(line)
                    if m:
                        nk, label, kind = parse.unit_key(m.group(1), width)
                        if (nk == re.sub(r'-\d+$', '', k) or nk in units) and lettered(line, width):
                            nk, label, kind = lettered(line, width)
                        if nk != re.sub(r'-\d+$', '', k) and nk not in units and nk not in out:
                            u = dict(u, label=label, kind=kind)
                            k = nk
                        break
            out[k] = u
        r['units'] = out
        return r
    wrapped.rekeyed = True
    return wrapped


LETTERED = re.compile(r'(?i)^art[íi]culo\s+(\d+)\s*(?:(bis|ter|quater|quáter)\s+)?([a-zñ])\s*[.°º-]')


def lettered(line: str, width: int) -> tuple[str, str, str] | None:
    """(key, label, kind) for an article named with a capital letter ("Artículo 54 O.-", "Artículo 54 Ñ.-"), which
    parse.unit_key reads as a degree sign (O) or folds into another letter (Ñ to N); Ñ is keyed "nn", between n and o."""
    m = LETTERED.match(line)
    if not m:
        return None
    num, word, letter = int(m.group(1)), (m.group(2) or '').lower(), m.group(3)
    suf = word.replace('á', 'a')
    key = f'art-{num:0{width}d}' + (f'-{suf}' if suf else '') + '-' + ('nn' if letter.lower() == 'ñ' else letter.lower())
    return key, f'Art. {num}' + (f' {word}' if word else '') + f' {letter.upper()}', 'art'


DEL_ART = re.compile(r'(?i)\s*\(DEL ART(?:[ÍI]CULO)?\.?\s*(?:\d+|[ÚU]NICO)\s*\)')


def unwrap(raw: bytes) -> bytes:
    """A norm that enacts a whole text in one article ("doble articulado": DL 830's "Artículo 1°.- Apruébase el
    siguiente texto del Código Tributario", DFL 3 of 2021's "Artículo único.- Fíjase el siguiente texto refundido...
    de la ley N° 19.496") is read as the text it enacts: that article's tree takes its place among the norm's top-level
    nodes (heading and closing formula kept), and the "(DEL ART. 1)" LeyChile adds to the names inside is dropped. The
    enacting sentence itself is not part of the act's text. Other norms are returned unchanged."""
    d = json.loads(raw)
    if not (d.get('metadatos') or {}).get('doble_articulado'):
        return raw
    html = d.get('html') or []
    boxes = [i for i, x in enumerate(html) if x.get('h')]
    if len(boxes) != 1:
        return raw
    node = html[boxes[0]]
    while len(node['h']) == 1 and node['h'][0].get('h'):
        node = node['h'][0]
    d['html'] = html[:boxes[0]] + node['h'] + html[boxes[0] + 1:]

    def strip(nodes):
        for x in nodes:
            if 'n' in x:
                x['n'] = DEL_ART.sub('', x['n'])
            strip(x.get('h') or [])
    strip(d.get('estructura') or [])
    return json.dumps(d, ensure_ascii=False).encode('utf-8')


def cut_note(slug: str) -> str:
    day, ev = STARTS[slug]
    return (f'Oldest version available: LeyChile lists older versions of this code, but each of them, up to the version '
            f'before {day}, carries amendment notes naming norms published after the day it is dated (for example '
            f'{ev[-1]}), so their text is not the text in force on those days. History here starts on {day}.')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', default='codes', choices=sorted(PARTS))
    ap.add_argument('--acts', help='default: the acts of --part')
    ap.add_argument('--out', help='default: the file of --part')
    ap.add_argument('--main-corpus', default=str(ROOT / 'corpus.json'),
                    help='checked for law keys that name a different norm')
    args = ap.parse_args()
    spec = PARTS[args.part]
    args.acts = args.acts or spec['acts']
    args.out = args.out or str(spec['out'])
    slugs = args.acts.split(',')
    setup(slugs)
    laws = parse.Laws()
    log: list[str] = []
    acts = [parse.act_versions(s, laws, log) for s in slugs]
    disclosed = []
    for a in acts:
        if a['slug'] in STARTS:
            v0 = a['versions'][0]
            v0['note'] = cut_note(a['slug']) + (' ' + v0['note'] if v0.get('note') else '')
        disclosed += correct(a, laws)
    out_laws = {k: {kk: vv for kk, vv in v.items() if not kk.startswith('_')} for k, v in sorted(laws.laws.items())}
    main_laws = json.loads(Path(args.main_corpus).read_text(encoding='utf-8')).get('laws', {})
    for other in sorted((ROOT / 'corpus.d').glob('*.json')):
        if other.resolve() != Path(spec['out']).resolve():
            for k, v in json.loads(other.read_text(encoding='utf-8')).get('laws', {}).items():
                main_laws.setdefault(k, v)
    clash = [k for k, v in out_laws.items() if k in main_laws and (
        main_laws[k]['label'] != v['label'] or (main_laws[k].get('url') and v.get('url')
                                                and main_laws[k]['url'] != v['url']))]
    if clash:
        raise SystemExit('law keys naming a different norm than corpus.json: ' + ', '.join(
            f'{k} ({out_laws[k]["label"]} {out_laws[k]["url"]} vs {main_laws[k]["label"]} {main_laws[k]["url"]})'
            for k in clash))
    decisions = spec['decisions'] + [
        'A version dated D is anachronistic when its amendment notes name a norm published after D (by Diario Oficial '
        'date, or by a Ley number at least that of a Ley published after D). Where LeyChile\'s "Texto Original" of a '
        'code holds no article text (only a PDF link), its later old versions are reconstructions, and the code starts '
        'at the oldest version from which no version is anachronistic: ' + ('; '.join(f'{parse.ACT_META[s]["short"]} from {STARTS[s][0]} ({len(STARTS[s][1])} older versions '
                            'affected)' for s in STARTS) or 'none') + '. The first version is then the oldest '
        'version available, credited to the publisher. (codes/anachronism.py)',
    ] + [d for d in extra_decisions(acts)] + disclosed
    part = {
        'laws': out_laws,
        'acts': acts,
        'decisions': decisions,
        'ai_use': ['Phase 2 codes: none at data-build time; codes/*.py are deterministic code written with Claude '
                   'Code (claude-opus-5-5), reusing parse.py; no model reads, writes or summarises legal text.'],
    }
    parse.stats(part)
    for a in acts:
        to_changes(a)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(out.name + '.tmp')
    tmp.write_text(json.dumps(part, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    tmp.replace(out)
    (HERE / 'parse.log').write_text('\n'.join(log) + '\n', encoding='utf-8', newline='\n')


def to_changes(act: dict) -> None:
    """SCHEMA.md "Large acts": every version after the first gives only `changes` ({unit key: unit, or null to remove
    it}) against the version before it, instead of all its units. expand() is the inverse, as the builder reads it."""
    full = [v['units'] for v in act['versions']]
    for prev, cur, v in zip(full, full[1:], act['versions'][1:]):
        ch = {k: cur.get(k) for k in sorted(set(prev) | set(cur)) if prev.get(k) != cur.get(k)}
        items = [(k, ch if k == 'units' else x) for k, x in v.items()]
        v.clear()
        v.update((('changes' if k == 'units' else k), x) for k, x in items)


def expand(part: dict) -> dict:
    """The part with every version's full `units`, rebuilt from `changes` exactly as gitlaw_common/build.py does."""
    for act in part.get('acts', []):
        for prev, v in zip(act['versions'], act['versions'][1:]):
            if 'units' in v:
                continue
            units = dict(prev['units'])
            for k, u in (v.get('changes') or {}).items():
                if u is None:
                    units.pop(k, None)
                else:
                    units[k] = u
            v['units'] = units
    return part


PLACEHOLDER = '[La fuente no da el texto vigente en esta fecha.]\n'


def zkey(k: str) -> str:
    return re.sub(r'(?<=-)0+(?=\d)', '', k)


def note_laws(laws: parse.Laws, notes: list[str]) -> list[str]:
    """The law keys the amendment notes name (registering a law known only from a note, as parse.py does)."""
    dated = dict(anachronism.ley_dates())
    keys = set()
    for n in notes:
        refs, dates = parse.note_refs([n])
        day = max(dates) if dates else None
        for t, num in sorted(refs):
            pub = day or (dated.get(num) if t == 'ley' else None)
            if t == 'ley' or pub:
                keys.add(laws.from_note(t, num, pub, n))
        if not refs and day and re.match(r'(?i)RECTIFICA', n):
            keys.add(laws.from_note('rec', None, day, n))
    return sorted(keys)


def correct(act: dict, laws: parse.Laws) -> list[str]:
    """Coordinator rule for anachronistic versions (codes/anachronism.py): a provision whose LeyChile text, in a version
    dated D, carries an amendment note naming a norm published after D holds wording that is not yet in force. Only
    those provisions are corrected, in the run of versions in which the note is ahead of its day:
      - the provision did not exist before the run and no norm in force that day is credited with it: that norm
        inserted it, so it is left out of the run;
      - otherwise, where its text differs from the text before the run, it becomes the placeholder line (the source
        does not give the wording in force then), credited to the publisher (unexplained);
    and in the first version after the run, where LeyChile's wording arrives, the change is credited to the norm(s)
    the notes name. Returns the decision lines."""
    bad = anachronism.defects(act['slug'])
    vs = act['versions']
    keys = {zkey(k): k for v in vs for k in v['units']}
    flagged: dict[str, dict[int, list[str]]] = {}
    for i, v in enumerate(vs):
        for _why, k4, n in bad.get(v['from'], []):
            k = keys.get(zkey(k4))
            if k:
                flagged.setdefault(k, {}).setdefault(i, []).append(n)
    lines = []
    for k in sorted(flagged):
        idx = sorted(flagged[k])
        runs, start = [], idx[0]
        for a, b in zip(idx, idx[1:] + [None]):
            if b != a + 1:
                runs.append((start, a))
                start = b
        for i, j in runs:
            pre = vs[i - 1]['units'].get(k) if i else None
            # New in the run: inserted by the late norm, unless the versions list credits its arrival to a norm in
            # force that day (that norm inserted it; the late norm changed it later).
            inserted = pre is None and not vs[i]['credits'].get(k)
            pre = pre or {'text': None}
            label = next((vs[t]['units'][k]['label'] for t in range(i, j + 1) if k in vs[t]['units']), k)
            for t in range(i, j + 1):
                u = vs[t]['units'].get(k)
                if inserted:
                    vs[t]['units'].pop(k, None)
                elif u is not None and u['text'] != pre['text']:
                    vs[t]['units'][k] = dict(u, text=PLACEHOLDER)
                vs[t]['credits'].pop(k, None)
            names = sorted({n for t in range(i, j + 1) for n in flagged[k].get(t, [])})
            how = 'left out (the norm its note names inserted it)' if inserted else \
                'shown as the placeholder line where LeyChile gives a later wording'
            vs[i]['note'] = (vs[i]['note'] + ' ' if vs[i].get('note') else '') + (
                f'Corrected: LeyChile\'s text of {label} from this version to {vs[j]["from"]} carries amendment notes '
                f'naming norms published after those days ({"; ".join(names)[:300]}), so its wording there is not yet '
                f'in force: it is {how}.')
            arrive = ''
            if j + 1 < len(vs):
                nxt = vs[j + 1]
                if nxt['units'].get(k) != vs[j]['units'].get(k):
                    lk = note_laws(laws, flagged[k][j])
                    if lk:
                        nxt['credits'][k] = sorted(set(nxt['credits'].get(k, [])) | set(lk))
                        nxt['note'] = (nxt['note'] + ' ' if nxt.get('note') else '') + (
                            f'{label}: the wording LeyChile gives once '
                            + ', '.join(laws.laws[x]['label'] for x in lk)
                            + ' is in force; credited to it (see the correction noted on '
                            + vs[i]['from'] + ').')
                        arrive = f'; from {nxt["from"]} credited to ' + ', '.join(laws.laws[x]['label'] for x in lk)
            lines.append(f'{label} {vs[i]["from"]} to {vs[j]["from"]} {"left out" if inserted else "placeholder"}'
                         + arrive)
    if not lines:
        return []
    return [f'{act["short"]}: provisions whose LeyChile text in a version carries notes naming a norm published after '
            'that version (coordinator rule: correct only those provisions, never keep text in force before its law; '
            'placeholder "' + PLACEHOLDER.strip() + '" credited to the publisher): ' + '; '.join(lines) + '.']


def extra_decisions(acts: list[dict]) -> list[str]:
    out = []
    for a in acts:
        m = parse.ACT_META[a['slug']]
        if m.get('first'):
            out.append(f'{a["short"]}: ' + m['first'][1])
    return out


if __name__ == '__main__':
    main()
