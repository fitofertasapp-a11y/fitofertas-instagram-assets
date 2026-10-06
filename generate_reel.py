from PIL import Image, ImageDraw, ImageFont
import os, subprocess, textwrap
W,H=1080,1920
GREEN=(54,255,105); WHITE=(248,250,248); MUTED=(180,194,184); BG=(4,9,7)
os.makedirs("reels",exist_ok=True)
def font(n,b=True):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,n)
def frame(kicker,head,sub,items):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.ellipse((720,-100,1200,380),fill=(8,70,30)); d.text((70,80),kicker,font=font(34),fill=GREEN)
    y=160
    for line in textwrap.wrap(head,22):
        d.text((70,y),line,font=font(76),fill=WHITE); y+=90
    y+=20
    for line in textwrap.wrap(sub,43):
        d.text((70,y),line,font=font(34,False),fill=MUTED); y+=48
    y=max(y+90,720)
    for item in items:
        d.rounded_rectangle((70,y,1010,y+130),radius=35,fill=(12,30,19),outline=GREEN,width=3)
        d.text((110,y+39),item,font=font(38),fill=WHITE); y+=165
    d.text((70,1790),"Antes de comprar, compare.",font=font(32),fill=GREEN)
    return im
data=[
("MITO OU VERDADE?","O mais barato sempre é a melhor compra?","MITO. Preço é só uma parte da comparação.",["Quantidade","Frete e condições","Avaliação e oferta"]),
("CHECKLIST 01","Compare a quantidade","Produtos parecidos podem ter tamanhos diferentes.",["Compare produtos equivalentes","Confira peso ou volume"]),
("CHECKLIST 02","Olhe além da etiqueta","A oferta final pode mudar conforme as condições.",["Preço","Frete","Estoque","Condições"]),
("RADAR FITOFERTAS","Menos impulso. Mais comparação.","Pesquise categorias fitness em um só lugar.",["Suplementos","Roupas fitness","Calçados","Equipamentos"]),
("FITOFERTAS","Antes de comprar, compare.","Disponível na Google Play.",["Procure","Compare","Escolha com mais informação"])
]
files=[]
for i,x in enumerate(data,1):
    p=f"reels/reel_mito_verdade_{i}.png"; frame(*x).save(p); files.append(p)
concat="reels/frames.txt"
with open(concat,"w") as f:
    for p in files:
        f.write(f"file '{os.path.basename(p)}'\nduration 1.85\n")
    f.write(f"file '{os.path.basename(files[-1])}'\n")
subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i","frames.txt","-vf","scale=1080:1920,format=yuv420p","-r","30","-c:v","libx264","-movflags","+faststart","reel_mito_verdade_fitofertas.mp4"],cwd="reels",check=True)
