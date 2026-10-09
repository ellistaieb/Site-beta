from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
R=Path(__file__).resolve().parent

def paths(text,font_file,size,x,y,spacing=0):
 font=TTFont(font_file);glyphs=font.getGlyphSet();cmap=font.getBestCmap();scale=size/font['head'].unitsPerEm;out=[]
 for c in text:
  name=cmap[ord(c)];pen=SVGPathPen(glyphs);glyphs[name].draw(TransformPen(pen,(scale,0,0,-scale,x,y)));out.append('<path d="'+pen.getCommands()+'"/>');x+=font['hmtx'][name][0]*scale+spacing
 return ''.join(out)
for color,name in [('#29483E','vert'),('#F7F4EE','ivoire'),('#26352F','encre')]:
 serif=R/'shared/serif-source.woff';sans=R/'shared/sans-source.woff'
 value=paths('VM',serif,146,13,153,-10)+paths('Valérie Migueres',serif,105,255,115,-1.4)+paths('PERSONAL & PROFESSIONAL DEVELOPMENT · NICE',sans,14,258,153,.6)
 (R/f'logos/signature-en-{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 205" role="img" aria-label="Valérie Migueres — Personal and professional development in Nice"><g fill="{color}">{value}</g></svg>')
print('3 signatures anglaises vectorisées ajoutées.')
