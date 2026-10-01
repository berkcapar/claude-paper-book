"""Build data/portfolio.json from documents exported by ArtifactData (out_dir).

Usage: python3 scripts/build_data.py <export_dir>
<export_dir> must contain portfolio/state.json, trades/*.json and snapshots/*.json.
"""
import glob, json, os, sys

src = sys.argv[1]

def load(path):
    d = json.load(open(path))
    return d.get("data", d)

state = load(os.path.join(src, "portfolio", "state.json"))
trades = sorted((load(p) for p in glob.glob(os.path.join(src, "trades", "*.json"))),
                key=lambda t: (t["date"], t.get("seq", 0)))
snaps = sorted((load(p) for p in glob.glob(os.path.join(src, "snapshots", "*.json"))),
               key=lambda s: s["date"])
os.makedirs("data", exist_ok=True)
json.dump({"state": state, "trades": trades, "snapshots": snaps},
          open("data/portfolio.json", "w"), indent=2)
print(f"wrote data/portfolio.json: {len(trades)} trades, {len(snaps)} snapshots")
