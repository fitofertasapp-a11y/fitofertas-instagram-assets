from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
Path("posts").mkdir(exist_ok=True)
bold="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
reg="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
B=ImageFont.truetype(bold,76); M=ImageFont.truetype(bold,52); R=ImageFont.truetype(reg,38); S=ImageFont.truetype(reg,28)
slides=[
("ANTES DE COMPRAR,\nCOMPARE.","O mesmo tipo de produto pode aparecer\ncom condições diferentes.","Salve este carrossel para consultar depois."),
("CREATINA","Compare quantidade, preço por grama\ne avaliações — não apenas o valor do pote.","Preço e disponibilidade podem mudar."),
("WHEY PROTEIN","Confira peso da embalagem, composição\ne custo por porção antes de escolher.","Compare produtos equivalentes."),
("ROUPAS E CALÇADOS","Olhe tamanho, material, avaliações\ne condições de entrega antes da compra.","Comprar bem vai além do preço."),
("EQUIPAMENTOS","Compare especificações, medidas, avaliações\ne custo total antes de decidir.","Evite comparar itens de categorias diferentes."),
("RADAR FITOFERTAS","Quer comparar antes de comprar?\nConheça o FitOfertas na Google Play.","Antes de comprar, compare.")
]
for i,(title,body,foot) in enumerate(slides,1):
    im=Image.new("RGB",(1080,1080),"#090b0a"); d=ImageDraw.Draw(im)
    d.rounded_rectangle((70,70,1010,1010),radius=38,outline="#21d07a",width=5)
    d.text((100,110),"FITOFERTAS",font=M,fill="#21d07a")
    y=270
    for line in title.split("\n"):
        d.text((100,y),line,font=B,fill="white"); y+=92
    y+=45
    for line in body.split("\n"):
        d.text((100,y),line,font=R,fill="#e8ece9"); y+=58
    d.line((100,820,980,820),fill="#1f2b25",width=3)
    d.text((100,865),foot,font=S,fill="#b9c5be")
    d.text((100,950),f"{i}/6",font=S,fill="#21d07a")
    im.save(f"posts/carrossel_{i}.jpg","JPEG",quality=88,optimize=True)
