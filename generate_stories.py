from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
Path("stories").mkdir(exist_ok=True)
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
slides=[
("VAI COMPRAR\nSUPLEMENTOS\nOU ROUPAS FITNESS?","Compare antes de decidir.","🔎  Compare opções\n✓  Confira avaliações\n✓  Analise especificações"),
("CREATINA","Compare diferentes opções.","✓ Preço e quantidade\n✓ Avaliações\n✓ Especificações"),
("WHEY PROTEIN","Escolha pensando no seu objetivo.","✓ Compare opções equivalentes\n✓ Confira avaliações\n✓ Veja quantidade"),
("ROUPAS FITNESS","Estilo também pede comparação.","✓ Modelos e tamanhos\n✓ Material\n✓ Avaliações"),
("CALÇADOS FITNESS","Conforto e desempenho.","✓ Numeração\n✓ Especificações\n✓ Avaliações"),
("EQUIPAMENTOS","Monte seu treino do seu jeito.","✓ Compare modelos\n✓ Confira medidas\n✓ Leia avaliações"),
("DICAS FIT","Compare melhor. Escolha melhor.","1  Confira especificações\n2  Veja avaliações\n3  Observe frete e prazo\n4  Compare opções"),
("FITOFERTAS","Antes de comprar, compare.","Disponível na Google Play")
]
for i,(title,sub,body) in enumerate(slides,1):
 im=Image.new("RGB",(1080,1920),(4,9,6)); d=ImageDraw.Draw(im)
 # glow blocks
 for k in range(14):
  x=760+k*10; d.rectangle((x,0,x+10,1920),fill=(0,max(20,90-k*5),30))
 d.ellipse((650,620,1180,1150),fill=(7,45,20))
 d.rounded_rectangle((70,70,1010,1850),55,outline=(28,230,110),width=5)
 d.text((85,105),f"{i}/8",font=ImageFont.truetype(B,34),fill=(40,240,125))
 fs=86 if i!=1 else 78
 font=ImageFont.truetype(B,fs)
 y=250
 for line in title.split("\n"):
  d.text((85,y),line,font=font,fill=(255,255,255) if "SUPLEMENTOS" not in line else (40,240,125)); y+=105
 d.text((85,y+35),sub,font=ImageFont.truetype(R,42),fill=(225,235,228))
 # generic visual object
 if i in (2,3):
  d.rounded_rectangle((280,730,800,1260),65,fill=(15,18,16),outline=(35,210,100),width=8)
  d.rectangle((390,650,690,760),fill=(18,20,19),outline=(35,210,100),width=6)
 elif i==4:
  d.polygon([(330,720),(540,650),(750,720),(680,1050),(400,1050)],fill=(18,20,19),outline=(35,210,100))
 elif i==5:
  d.ellipse((230,760,850,1120),fill=(18,20,19),outline=(35,210,100),width=8)
 elif i==6:
  d.rectangle((220,820,860,930),fill=(30,33,31)); d.ellipse((150,730,370,1020),fill=(18,20,19),outline=(35,210,100),width=8); d.ellipse((710,730,930,1020),fill=(18,20,19),outline=(35,210,100),width=8)
 else:
  d.rounded_rectangle((650,700,930,1300),45,fill=(245,248,246),outline=(35,210,100),width=8)
  d.rectangle((690,780,890,820),fill=(30,210,100)); d.rectangle((690,870,850,900),fill=(30,210,100)); d.rectangle((690,950,875,980),fill=(30,210,100))
 by=1390
 d.rounded_rectangle((70,by,1010,1770),45,fill=(245,248,246))
 yy=by+55
 for line in body.split("\n"):
  d.text((115,yy),line,font=ImageFont.truetype(B if i==8 else R,38),fill=(10,20,15)); yy+=70
 d.text((85,1800),"Antes de comprar, compare.",font=ImageFont.truetype(B,30),fill=(40,240,125))
 im.save(f"stories/story_{i}.jpg","JPEG",quality=90,optimize=True)
