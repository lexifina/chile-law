"""Runs the main agent's verify.py on the codes part (corpus.d/50-codes.json, or --corpus PATH): the text of each
code in force on --date must equal LeyChile's current text unit by unit, and every version must carry the sha256 of
a cached LeyChile response.

    python -X utf8 scripts/chile-law/codes/verify_codes.py [--corpus PATH] [--date YYYY-MM-DD] [--offline]
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
    corpus = Path(sys.argv[sys.argv.index('--corpus') + 1])
    slugs = [a['slug'] for a in json.loads(corpus.read_text(encoding='utf-8'))['acts']]
    parse_codes.setup(slugs)
    sys.exit(verify.main())
