"""For each cached version of a code, the latest Diario Oficial date its amendment notes cite, against the version's
own in-force day. A version whose notes cite norms published after its own day holds text from later years: LeyChile
did not reconstruct that version faithfully, so it cannot be dated as history.

    python -X utf8 scripts/chile-law/codes/anachronism.py slug [slug...]
"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE))
import fetch, parse  # noqa: E401,E402
from fetch_codes import CHAINS  # noqa: E402


def late_notes(raw: bytes, day: str, part=None) -> list[tuple[str, str, str]]:
    r = parse.read_version(raw, 4, part)
    out = []
    for k, u in r['units'].items():
        for n in u['notes']:
            _, dates = parse.note_refs([n])
            late = [d for d in dates if d > day]
            if late:
                out.append((max(late), k, n))
    return sorted(out)


def report(slug: str) -> None:
    for idn in CHAINS[slug]:
        for v in fetch.versions(idn, offline=True):
            day = v['@vigenteDesde']
            p = fetch.cache_path(fetch.version_url(idn, day))
            if not p.exists():
                print(slug, idn, day, 'not cached'); continue
            late = late_notes(p.read_bytes(), day)
            print(slug, idn, day, len(late), late[-1][0] if late else '', (late[-1][1] + ' ' + late[-1][2][:90]) if late else '')


if __name__ == '__main__':
    for s in sys.argv[1:]:
        report(s)
