#!/bin/sh
# Pushes scripts/chile-law/ (no .cache, corpus.json only if under 50 MB) to the `wip` branch of lexifina/chile-law,
# under wip/, without touching the clone's main checkout (git plumbing on a temporary index).
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
CLONE="${CLONE:-C:/Users/alany/Documents/chile-law}"
TMP="$(mktemp -d)"
mkdir -p "$TMP/wip"
for f in fetch.py parse.py PROGRESS.md ISSUES.md push_wip.sh parse.log verification.json; do
  [ -f "$SRC/$f" ] && cp "$SRC/$f" "$TMP/wip/"
done
[ -d "$SRC/repo" ] && cp -r "$SRC/repo" "$TMP/wip/repo"
if [ -f "$SRC/corpus.json" ] && [ "$(wc -c < "$SRC/corpus.json")" -lt 50000000 ]; then cp "$SRC/corpus.json" "$TMP/wip/"; fi
export GIT_INDEX_FILE="$TMP/index"
export GIT_WORK_TREE="$TMP"
git -C "$CLONE" --work-tree="$TMP" add -A -f wip
TREE=$(git -C "$CLONE" write-tree)
COMMIT=$(echo "wip: chile-law scripts and corpus $(date -u +%Y-%m-%dT%H:%M:%SZ)" | \
  GIT_AUTHOR_NAME=Lexifina GIT_AUTHOR_EMAIL=chile-law@lexifina.com GIT_COMMITTER_NAME=Lexifina \
  GIT_COMMITTER_EMAIL=chile-law@lexifina.com git -C "$CLONE" commit-tree "$TREE")
git -C "$CLONE" push -f origin "$COMMIT:refs/heads/wip"
rm -rf "$TMP"
