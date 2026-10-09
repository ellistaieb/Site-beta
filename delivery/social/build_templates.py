"""Regenerate editable SVG templates from content.json; never posts to a platform."""
import base64,json,pathlib,html,math,shutil
from fontTools.ttLib import TTFont
from PIL import ImageFont
R=pathlib.Path(__file__).resolve().parent
C={'ivory':'#F7F4EE','ink':'#26352F','green':'#29483E','sage':'#DEE5DB','sand':'#E8DDCB','bronze':'#947448'}
FORMATS={'post':(1080,1350),'portrait':(1080,1920),'square':(1080,1080),'banner':(2560,1440),'thumbnail':(1280,720),'video':(1920,1080)}
font_defs=[]
for file,family,style,weight in [('serif.woff2','VM Serif','normal',500),('serif-italic.woff2','VM Serif','italic',500),('sans.woff2','VM Sans','normal',400),('sans-semibold.woff2','VM Sans','normal',600)]:
 data=base64.b64encode((R/'shared'/file).read_bytes()).decode();font_defs.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
# WOFF sources use zlib, avoiding a Brotli dependency for SVG layout measurement.
fonts={}
for name,source in [('serif','serif-source.woff'),('sans','sans-source.woff')]:
 f=TTFont(R/'shared'/source);f.flavor=None;target=pathlib.Path('/tmp')/('vm-'+name+'.ttf');f.save(target);fonts[name]=target

def escape(v):return html.escape(str(v),quote=True)
def wrap(value,size,family,width):
 f=ImageFont.truetype(str(fonts[family]),int(size));lines=[]
 for paragraph in str(value).split('\n'):
  line=''
  for word in paragraph.split():
   candidate=(line+' '+word).strip()
   if f.getlength(candidate)>width and line:lines.append(line);line=word
   else:line=candidate
  if line:lines.append(line)
 return lines

def text(field,value,x,y,size,width,color,family='sans',weight=400,line_height=None,max_lines=6,align='start'):
 if not value:return ''
 lh=line_height or round(size*1.25);lines=wrap(value,size,family,width)
 if len(lines)>max_lines:raise ValueError(f'{field}: too many lines: {value}')
 anchor='middle' if align=='center' else 'start'
 spans=''.join(f'<tspan x="{x}" y="{y+n*lh}">{escape(line)}</tspan>' for n,line in enumerate(lines))
 return f'<text data-field="{field}" data-width="{width}" data-size="{size}" data-lh="{lh}" data-lines="{max_lines}" x="{x}" y="{y}" text-anchor="{anchor}" font-family="VM {"Serif" if family=="serif" else "Sans"}" font-weight="{weight}" font-size="{size}" fill="{color}">{spans}</text>'

def svg_for(m):
 w,h=FORMATS[m['format']];bg=C[m['theme']];fg=C['ivory'] if m['theme']=='green' else C['ink'];accent=C['sage'] if m['theme']=='green' else C['green'];kind=m['kind']
 defs=f'<defs><style>{"".join(font_defs)}</style></defs>'
 content=[]
 if kind!='title':content.append(f'<rect width="{w}" height="{h}" fill="{bg}"/>')
 if kind=='banner':
  content.append(f'<ellipse cx="2160" cy="680" rx="730" ry="700" fill="none" stroke="{fg}" stroke-opacity=".2" stroke-width="2"/><path d="M150 1250V700a320 320 0 0 1 640 0v550" fill="{accent}" opacity=".12"/>')
  content.append(text('brand','VM',565,750,150,230,fg,'serif',500,max_lines=1))
  content.append(text('kicker',m['kicker'],820,588,30,1160,fg,max_lines=1))
  content.append(text('title',m['title'],810,714,111,1215,fg,'serif',500,max_lines=1))
  content.append(text('body',m['body'],820,809,45,1150,fg,max_lines=1))
  safe={'x':507,'y':508.5,'width':1546,'height':423}
 elif kind=='highlight':
  content.append(f'<circle cx="540" cy="540" r="415" fill="none" stroke="{fg}" stroke-opacity=".3" stroke-width="2"/>')
  content.append(text('brand','VM',540,488,206,580,fg,'serif',500,max_lines=1,align='center'))
  content.append(text('title',m['title'],540,670,60,780,fg,max_lines=1,align='center'))
  safe={'x':180,'y':180,'width':720,'height':720,'crop':'circle'}
 elif kind=='intro':
  content.append(f'<circle cx="1530" cy="570" r="560" fill="none" stroke="{fg}" stroke-opacity=".18" stroke-width="2"/>')
  content.append('<g id="intro-mark">'+text('brand','VM',960,389,156,500,fg,'serif',500,max_lines=1,align='center')+'</g>')
  content.append('<g id="intro-name">'+text('title',m['title'],960,589,125,1560,fg,'serif',500,max_lines=1,align='center')+'</g>')
  content.append('<g id="intro-signature">'+text('body',m['body'],960,696,43,1500,fg,max_lines=1,align='center')+'</g>')
  safe={'x':192,'y':108,'width':1536,'height':864}
 elif kind=='title':
  content.append(f'<rect x="100" y="765" width="1720" height="235" fill="{C["green"]}" rx="2"/><rect x="100" y="765" width="5" height="235" fill="{C["bronze"]}"/>')
  content.append(text('kicker',m['kicker'],145,820,24,1620,C['ivory'],max_lines=1))
  content.append(text('title',m['title'],145,900,66,1620,C['ivory'],'serif',500,max_lines=1))
  content.append(text('body',m['body'],145,956,30,1620,C['ivory'],max_lines=1))
  safe={'x':96,'y':54,'width':1728,'height':972}
 elif kind=='end':
  content.append(text('kicker',m['kicker'],150,140,28,1620,fg,max_lines=1))
  content.append(text('title',m['title'],150,290,95,1600,fg,'serif',500,max_lines=1))
  content.append(text('body',m['body'],150,370,40,1550,fg,max_lines=2))
  content.append(f'<g id="video-slot"><rect x="160" y="505" width="665" height="374" fill="{C["sage"]}"/><path d="M400 620l90 70-90 70z" fill="{C["green"]}"/></g><g id="subscribe-slot"><circle cx="1330" cy="690" r="133" fill="{C["green"]}"/>'+text('brand','VM',1330,737,128,220,C['ivory'],'serif',500,max_lines=1,align='center')+'</g>')
  content.append(text('cta',m['cta'],150,992,31,1600,fg,max_lines=1))
  safe={'x':96,'y':54,'width':1728,'height':972,'video':{'x':160,'y':505,'width':665,'height':374},'subscribe':{'cx':1330,'cy':690,'radius':133}}
 elif kind=='thumbnail':
  content.append(text('brand',m['brand'],80,100,28,1100,fg,max_lines=1))
  content.append(text('kicker',m['kicker'],80,199,22,800,fg,max_lines=1))
  content.append(text('title',m['title'],80,349,95,795,fg,'serif',500,line_height=108,max_lines=3))
  content.append(text('signature',m['signature'],80,638,25,800,fg,max_lines=1))
  content.append(f'<g data-photo="true" transform="translate(935 182)"><path d="M0 385V120a130 130 0 0 1 260 0v265" fill="{accent}" opacity=".18"/>'+text('brand','VM',130,286,103,230,fg,'serif',500,max_lines=1,align='center')+'</g>')
  safe={'x':64,'y':36,'width':1152,'height':648,'avoid':'bottom-right duration badge'}
 else:
  portrait=m['format']=='portrait'
  content.append(f'<path d="M{w-240} 150a490 490 0 0 1 0 980" fill="none" stroke="{fg}" stroke-opacity=".16" stroke-width="2"/>')
  content.append(text('brand',m['brand'],90,310 if portrait else 115,34,900,fg,'serif',500,max_lines=1))
  content.append(f'<path d="M90 {380 if portrait else 175}H{w-90}" stroke="{fg}" stroke-opacity=".3" stroke-width="1.5"/>')
  content.append(text('kicker',m['kicker'],90,475 if portrait else 260,27,900,fg,weight=600,max_lines=2))
  title_size=110 if portrait else 96
  content.append(text('title',m['title'],90,650 if portrait else 409,title_size,900,fg,'serif',500,line_height=118 if portrait else 103,max_lines=3))
  body_width=650 if m.get('photo') else 900
  content.append(text('body',m['body'],90,1080 if portrait else 830,42,body_width,fg,line_height=60,max_lines=5))
  if m.get('photo'):
   x,y,pw,ph=(790,990,200,355) if portrait else (790,855,200,295)
   content.append(f'<g data-photo="true" transform="translate({x} {y})"><path d="M0 {ph}V100a100 100 0 0 1 200 0v{ph-100}" fill="{accent}" opacity=".15"/><circle cx="100" cy="{ph/2}" r="75" fill="none" stroke="{fg}" stroke-opacity=".3" stroke-width="2"/></g>')
  cta_y=1470 if portrait else 1210
  if m['cta']:
   buttonfill=C['ivory'] if m['theme']=='green' else C['green'];buttontext=C['green'] if m['theme']=='green' else C['ivory']
   content.append(f'<rect x="90" y="{cta_y-59}" width="900" height="96" fill="{buttonfill}"/>')
   content.append(text('cta',m['cta'],124,cta_y,31,832,buttontext,weight=600,max_lines=1))
  content.append(text('signature',m['signature'],90,1622 if portrait else 1310,26,900,fg,max_lines=1))
  safe={'x':90,'y':260 if portrait else 90,'width':900,'height':1390 if portrait else 1230,'crop':'For Reel cover: keep main title in centre square y=420–1500' if kind=='reel' else ''}
 return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(m["title"])}">{defs}{"".join(content)}</svg>',safe

models=json.loads((R/'content.json').read_text());manifest=[]
for m in models:
 folder=R/'templates'/m['platform']/m['lang'];folder.mkdir(parents=True,exist_ok=True)
 svg,safe=svg_for(m);file=folder/(m['id']+'.svg');file.write_text(svg)
 w,h=FORMATS[m['format']];manifest.append({**m,'width':w,'height':h,'safe':safe,'svg':str(file.relative_to(R)),'png':f'exports/{m["platform"]}/{m["lang"]}/{m["id"]}.png'})
for platform in ('whatsapp','youtube'):
 m=dict(id='profil',platform=platform,lang='commun',format='square',theme='green',kind='highlight',title='',brand='VM',body='',cta='',signature='',kicker='')
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080"><rect width="1080" height="1080" fill="{C["green"]}"/><circle cx="540" cy="540" r="390" fill="none" stroke="{C["ivory"]}" stroke-opacity=".28" stroke-width="2"/><g transform="translate(170 230) scale(3.1)">'+(R/'logos/monogramme-ivoire.svg').read_text().split('>',1)[1].rsplit('</svg>',1)[0]+'</g></svg>'
 folder=R/'templates'/platform/'commun';folder.mkdir(parents=True,exist_ok=True);file=folder/'profil.svg';file.write_text(svg)
 manifest.append({**m,'width':1080,'height':1080,'safe':{'x':180,'y':180,'width':720,'height':720,'crop':'circle'},'svg':str(file.relative_to(R)),'png':f'exports/{platform}/commun/profil.png'})
(R/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('54 SVG éditables générés, avec zones de sécurité documentées.')
