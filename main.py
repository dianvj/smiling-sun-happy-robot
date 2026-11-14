"""make.fun bounty "Make the AI judge happy" (ai-happy-01).

Writes one image to /output/entry.png by copying the bundled entry.png.
No network, no randomness: both runs write identical bytes.
After copying, the destination is hashed and compared to the source;
a mismatch fails loudly instead of silently writing wrong bytes.
Python 3.13, standard library only.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
src_hash = sha256(SRC)
dst_hash = sha256(DST)
if src_hash != dst_hash:
    raise SystemExit(f"copy mismatch: src {src_hash} != dst {dst_hash}")
print(f"wrote {DST} sha256={dst_hash}")
