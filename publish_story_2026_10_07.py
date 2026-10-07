from pathlib import Path
from urllib.request import Request, urlopen

SOURCE_URL = "https://d2ol7oe51mr4n9.cloudfront.net/user_3JatvcpwHl7WjwDT2SggZyvAcDH/aec757ed-1ed1-4d6b-bd23-c8d3a7adb2cc.jpg"
OUT = Path("stories/2026-10-07-fitofertas-story.jpg")

OUT.parent.mkdir(parents=True, exist_ok=True)
req = Request(SOURCE_URL, headers={"User-Agent": "Mozilla/5.0"})
with urlopen(req, timeout=60) as response:
    data = response.read()

if len(data) < 100_000:
    raise RuntimeError(f"Downloaded image looks too small: {len(data)} bytes")
if not data.startswith(b"\xff\xd8\xff"):
    raise RuntimeError("Downloaded asset is not a JPEG")

OUT.write_bytes(data)
print(f"Wrote {OUT} ({len(data)} bytes)")
