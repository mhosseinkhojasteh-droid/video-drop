#!/bin/bash
# Phase 3 batch runner: analyses every reference in references/raw (4 in parallel), skips finished ones.
cd "$(dirname "$0")/.."
ls references/raw | while read f; do
  n="${f%.*}"; n="${n// /_}"
  [ -s "analysis/data/$n.json" ] || echo "$f"
done | xargs -P 4 -I{} bash -c 'f="{}"; n="${f%.*}"; n="${n// /_}"; python3 -I scripts/analyze_track.py "references/raw/$f" "analysis/data/$n.json" "analysis/plots/$n.png" > "analysis/data/$n.log" 2>&1 && echo "OK $n" || echo "FAIL $n"'
