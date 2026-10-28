"""Prints the law of Chile as it stood on a given day, read from this repository's history.

    python tools/en_vigor_el.py 2022-03-09 codigo-civil art-0102 # art. 102 the day before Ley 21.400
    python tools/en_vigor_el.py 2022-03-10 codigo-civil 102      # the same article, by number, as amended
    python tools/en_vigor_el.py 2000-01-01 constitucion           # the whole Constitution on 1 January 2000
    python tools/en_vigor_el.py --law 2020-01-01 constitucion 19     # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. Standard library only.
"""
import runpy
import sys
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
