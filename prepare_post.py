from pathlib import Path
from urllib.request import Request, urlopen
from io import BytesIO
from PIL import Image

URL = "https://d2jqrm6oza8nb6.cloudfront.net/datasets/ff1991ff-2980-42ec-8220-eaf26335629d.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiYTc2ZTZkYmFjOGM3YjczYiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MTQxMjkyMn0.lGQ-HuPciKj7_iueu0WinHjOEIcCqJsf2z00ujtRH2U"
OUT = Path("posts/fitofertas_post_atual.jpg")
OUT.parent.mkdir(exist_ok=True)

req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urlopen(req, timeout=60) as resp:
    raw = resp.read()

im = Image.open(BytesIO(raw)).convert("RGB")
im = im.resize((1080, 1080), Image.Resampling.LANCZOS)
im.save(OUT, "JPEG", quality=94, optimize=True, progressive=True)
print(f"saved {OUT} {OUT.stat().st_size} bytes")
