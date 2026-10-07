from pathlib import Path
from urllib.request import Request, urlopen
from io import BytesIO
from PIL import Image

SOURCE_URL = "https://d2ol7oe51mr4n9.cloudfront.net/user_3JatvcpwHl7WjwDT2SggZyvAcDH/a7ccb426-97d9-4227-aabc-ce17e1567911.png"
OUT = Path("posts/fitofertas-beneficios-2026-10-07.jpg")

OUT.parent.mkdir(parents=True, exist_ok=True)
req = Request(SOURCE_URL, headers={"User-Agent":"Mozilla/5.0"})
with urlopen(req, timeout=60) as response:
    data = response.read()

im = Image.open(BytesIO(data)).convert("RGB")
im = im.resize((1080, 1350), Image.Resampling.LANCZOS)
im.save(OUT, "JPEG", quality=95, optimize=True, subsampling=0)
print(f"Wrote {OUT} {im.size}")
