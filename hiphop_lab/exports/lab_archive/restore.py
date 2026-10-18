"""Restore the lab from the bundles: python3 restore.py <bundle> [<bundle>...]  (splits on '=== FILE: path ===')."""
import sys, os, re
for b in sys.argv[1:]:
    parts = re.split(r'^=== FILE: (.+?) ===\n', open(b, encoding='utf-8').read(), flags=re.M)
    for path, body in zip(parts[1::2], parts[2::2]):
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        open(path, 'w', encoding='utf-8').write(body[:-1] if body.endswith('\n') else body); print('restored', path)
