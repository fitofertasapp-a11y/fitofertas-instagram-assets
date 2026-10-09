from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT=Path("today"); OUT.mkdir(exist_ok=True)
BG=(6,10,8); GREEN=(155,255,40); WHITE=(245,248,245); MUTED=(190,205,195)
B="/usr/share/fonts/truetype/lato/Lato-Heavy.ttf"
SB="/usr/share/fonts/truetype/lato/Lato-Semibold.ttf"
R="/usr/share/fonts/truetype/lato/Lato-Regular.ttf"

def F(path,size): return ImageFont.truetype(path,size)

def glow(im):
    g=Image.new("RGBA",im.size,(0,0,0,0)); d=ImageDraw.Draw(g); w,h=im.size
    d.ellipse((w*.55,h*.03,w*1.15,h*.62),fill=(60,255,60,28))
    d.ellipse((-w*.2,h*.6,w*.5,h*1.15),fill=(40,220,80,18))
    g=g.filter(ImageFilter.GaussianBlur(55))
    return Image.alpha_composite(im.convert("RGBA"),g).convert("RGB")

def brand(d,w):
    d.text((70,55),"Fit",font=F(B,54),fill=WHITE)
    x=70+d.textlength("Fit",font=F(B,54))
    d.text((x,55),"Ofertas",font=F(B,54),fill=GREEN)
    d.text((70,115),"ANTES DE COMPRAR, COMPARE.",font=F(SB,20),fill=MUTED)
    d.line((70,150,w-70,150),fill=(40,65,48),width=2)

def circle(d,cx,cy,label):
    d.ellipse((cx-34,cy-34,cx+34,cy+34),outline=GREEN,width=4)
    d.text((cx,cy-2),label,font=F(B,26),fill=GREEN,anchor="mm")

# Feed: pre-workout
w,h=1080,1350
im=glow(Image.new("RGB",(w,h),BG)); d=ImageDraw.Draw(im); brand(d,w)
d.text((70,215),"PRÉ-TREINO",font=F(B,104),fill=WHITE)
d.text((70,315),"O QUE COMPARAR ANTES",font=F(B,48),fill=GREEN)
d.text((70,372),"DE ESCOLHER?",font=F(B,48),fill=GREEN)
x0,y0=640,430
d.rounded_rectangle((x0,y0,x0+320,y0+470),36,fill=(18,20,19),outline=GREEN,width=6)
d.rectangle((x0+45,y0-55,x0+275,y0+30),fill=(20,22,21),outline=GREEN,width=5)
d.text((x0+160,y0+145),"PRÉ",font=F(B,74),fill=WHITE,anchor="mm")
d.text((x0+160,y0+225),"TREINO",font=F(B,74),fill=GREEN,anchor="mm")
d.text((x0+160,y0+315),"COMPARE",font=F(SB,30),fill=MUTED,anchor="mm")
d.text((x0+160,y0+355),"ANTES",font=F(SB,30),fill=MUTED,anchor="mm")
items=[("1","CAFEÍNA POR DOSE","Veja a quantidade informada no rótulo."),("2","LISTA DE INGREDIENTES","Compare fórmulas e composição."),("3","NÚMERO DE PORÇÕES","Confira quanto rende a embalagem."),("4","AVALIAÇÕES + PREÇO","Compare custo por porção e opiniões.")]
y=500
for n,t,s in items:
    circle(d,105,y+10,n); d.text((165,y-20),t,font=F(SB,31),fill=WHITE); d.text((165,y+25),s,font=F(R,24),fill=MUTED); y+=135
d.rounded_rectangle((70,1110,1010,1240),38,fill=(12,18,14),outline=GREEN,width=4)
d.text((540,1155),"VOCÊ USA PRÉ-TREINO?",font=F(B,42),fill=WHITE,anchor="mm")
d.text((540,1200),"Comenta no post",font=F(SB,28),fill=GREEN,anchor="mm")
d.text((70,1290),"FitOfertas  •  Antes de comprar, compare.",font=F(SB,24),fill=MUTED)
im.save(OUT/"feed_pre_treino_1080x1350.jpg","JPEG",quality=95,optimize=True,subsampling=0)

# Story: shoes
w,h=1080,1920
im=glow(Image.new("RGB",(w,h),BG)); d=ImageDraw.Draw(im); brand(d,w)
d.text((70,230),"TÊNIS DE TREINO",font=F(B,82),fill=WHITE)
d.text((70,330),"ANTES DE ESCOLHER,",font=F(B,45),fill=GREEN); d.text((70,385),"COMPARE.",font=F(B,45),fill=GREEN)
sx,sy=180,570
d.polygon([(sx,sy+210),(sx+80,sy+80),(sx+245,sy+40),(sx+440,sy+160),(sx+650,sy+200),(sx+690,sy+290),(sx+80,sy+300)],fill=(20,25,22),outline=GREEN)
d.line((sx+90,sy+220,sx+600,sy+235),fill=WHITE,width=8)
d.line((sx+240,sy+90,sx+330,sy+175),fill=GREEN,width=12); d.line((sx+310,sy+90,sx+395,sy+185),fill=GREEN,width=12)
items=[("1","TIPO DE TREINO","Musculação, corrida ou uso geral?"),("2","NUMERAÇÃO E AJUSTE","Confira medidas e tabela da loja."),("3","AMORTECIMENTO / ESTABILIDADE","Observe a proposta do modelo."),("4","AVALIAÇÕES E PREÇO","Compare experiências e custo.")]
y=1030
for n,t,s in items:
    circle(d,105,y+5,n); d.text((165,y-25),t,font=F(SB,32),fill=WHITE); d.text((165,y+20),s,font=F(R,25),fill=MUTED); y+=150
d.rounded_rectangle((70,1650,1010,1795),38,fill=(14,22,17),outline=GREEN,width=4)
d.text((540,1700),"QUAL TIPO DE TÊNIS VOCÊ USA?",font=F(B,35),fill=WHITE,anchor="mm")
d.text((540,1750),"Responde no story",font=F(SB,28),fill=GREEN,anchor="mm")
d.text((70,1850),"FitOfertas  •  Antes de comprar, compare.",font=F(SB,24),fill=MUTED)
im.save(OUT/"story_tenis_1080x1920.jpg","JPEG",quality=95,optimize=True,subsampling=0)

# Story: supplement comparison
im=glow(Image.new("RGB",(w,h),BG)); d=ImageDraw.Draw(im); brand(d,w)
d.text((70,230),"SUPLEMENTOS",font=F(B,88),fill=WHITE)
d.text((70,335),"4 COISAS PARA COMPARAR",font=F(B,44),fill=GREEN); d.text((70,390),"ANTES DE COMPRAR",font=F(B,44),fill=GREEN)
for x,yy in [(120,430),(405,500),(690,450)]:
    d.rounded_rectangle((x,yy,x+230,yy+360),28,fill=(20,22,21),outline=GREEN,width=5)
    d.rectangle((x+30,yy-45,x+200,yy+25),fill=(25,26,25),outline=GREEN,width=4)
    d.text((x+115,yy+135),"FIT",font=F(B,45),fill=WHITE,anchor="mm"); d.text((x+115,yy+195),"OFERTAS",font=F(B,34),fill=GREEN,anchor="mm")
items=[("1","QUANTIDADE","Compare peso/volume da embalagem."),("2","PORÇÃO","Veja quanto cada dose realmente entrega."),("3","INGREDIENTES","Leia a composição antes de decidir."),("4","AVALIAÇÕES + PREÇO","Compare opiniões e custo por porção.")]
y=1030
for n,t,s in items:
    circle(d,105,y+5,n); d.text((165,y-25),t,font=F(SB,32),fill=WHITE); d.text((165,y+20),s,font=F(R,25),fill=MUTED); y+=150
d.rounded_rectangle((70,1650,1010,1795),38,fill=(14,22,17),outline=GREEN,width=4)
d.text((540,1700),"ANTES DE COMPRAR, COMPARE.",font=F(B,38),fill=WHITE,anchor="mm")
d.text((540,1750),"FitOfertas",font=F(SB,30),fill=GREEN,anchor="mm")
d.text((70,1850),"Preço, quantidade, composição e avaliações.",font=F(SB,24),fill=MUTED)
im.save(OUT/"story_suplementos_1080x1920.jpg","JPEG",quality=95,optimize=True,subsampling=0)
print("generated")
