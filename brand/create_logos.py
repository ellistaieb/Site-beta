from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
ROOT=Path(__file__).resolve().parent

def text_paths(text,font_file,size,x,y,spacing=0):
 font=TTFont(font_file);glyphs=font.getGlyphSet();cmap=font.getBestCmap();scale=size/font['head'].unitsPerEm
 paths=[]
 for c in text:
  glyph_name=cmap[ord(c)];pen=SVGPathPen(glyphs);glyphs[glyph_name].draw(TransformPen(pen,(scale,0,0,-scale,x,y)));paths.append(pen.getCommands());x+=font['hmtx'][glyph_name][0]*scale+spacing
 return ''.join(f'<path d="{p}"/>' for p in paths)

for color,name in [('#29483E','vert'),('#F7F4EE','ivoire'),('#26352F','encre')]:
 mono=text_paths('VM',ROOT/'assets/serif-source.woff',146,13,153,-10)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 200" role="img" aria-label="Monogramme VM — Valérie Migueres"><g fill="{color}">{mono}</g></svg>'
 (ROOT/f'logos/monogramme-{name}.svg').write_text(svg)
 word=text_paths('Valérie Migueres',ROOT/'assets/serif-source.woff',105,255,115,-1.4)
 tag=text_paths('ACCOMPAGNEMENT PERSONNEL & PROFESSIONNEL · NICE',ROOT/'assets/sans-source.woff',14,258,153,.6)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 205" role="img" aria-label="Valérie Migueres — Accompagnement personnel et professionnel à Nice"><g fill="{color}">{mono}{word}{tag}</g></svg>'
 (ROOT/f'logos/signature-{name}.svg').write_text(svg)
print('6 SVG vectorisés, sans dépendance de police pour les logos.')
