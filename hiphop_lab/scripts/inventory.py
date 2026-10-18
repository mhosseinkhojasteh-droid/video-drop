"""Phase 2: reproducible inventory of reference audio. Usage: python3 -I scripts/inventory.py references/raw reports/01_asset_inventory.csv"""
import sys, os, csv, hashlib, json, subprocess
src, out = sys.argv[1], sys.argv[2]
rows = []
for f in sorted(os.listdir(src)):
    p = os.path.join(src, f)
    if not f.lower().endswith(('.mp3', '.wav', '.flac', '.m4a', '.aiff', '.ogg')): continue
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_format', '-show_streams', p], capture_output=True, text=True).stdout)
    st = [s for s in pr['streams'] if s['codec_type'] == 'audio'][0]
    dec = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'null', '-'], capture_output=True, text=True).stderr.strip()
    rows.append(dict(filename=f, path=p, sha256=h[:16], size_bytes=os.path.getsize(p), codec=st['codec_name'],
                     sample_rate=st['sample_rate'], channels=st['channels'], bit_rate=pr['format'].get('bit_rate'),
                     duration_s=round(float(pr['format']['duration']), 2), decode_errors=len(dec.splitlines()) if dec else 0,
                     tags=json.dumps(pr['format'].get('tags', {}), ensure_ascii=False)[:200]))
seen = {}
for r in rows:
    r['duplicate_of'] = seen.get(r['sha256'], ''); seen.setdefault(r['sha256'], r['filename'])
with open(out, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), 'files ->', out)
