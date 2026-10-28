"""Runs the main agent's verify.py on the codes part (corpus.d/50-codes.json, or --corpus PATH): the text of each
code in force on --date must equal LeyChile's current text unit by unit, and every version must carry the sha256 of
a cached LeyChile response.

    python -X utf8 scripts/chile-law/codes/verify_codes.py [--corpus PATH] [--date YYYY-MM-DD] [--offline]

The part stores versions as `changes` (SCHEMA.md, "Large acts"); they are expanded to full `units`, as the builder
reads them, into .tmp-build/codes/verify-expanded.json, which verify.py then checks.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
import parse_codes  # noqa: E402
import verify  # noqa: E402

if __name__ == '__main__':
    if '--corpus' not in sys.argv:
        sys.argv += ['--corpus', str(parse_codes.OUT)]
    i = sys.argv.index('--corpus') + 1
    part = parse_codes.expand(json.loads(Path(sys.argv[i]).read_text(encoding='utf-8')))
    tmp = HERE.parent / '.tmp-build' / 'codes' / 'verify-expanded.json'
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps(part, ensure_ascii=False), encoding='utf-8', newline='\n')
    sys.argv[i] = str(tmp)
    parse_codes.setup([a['slug'] for a in part['acts']])
    sys.exit(verify.main())
