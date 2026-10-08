import json, html, pathlib, shutil, os
from urllib.parse import urlparse
ROOT=pathlib.Path(__file__).resolve().parent
S=json.loads((ROOT/'content/settings.json').read_text())
S['domain']=os.environ.get('SITE_DOMAIN',S['domain'])
OUT=ROOT/'dist'; OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
paths={'fr':['','accompagnements','mon-approche','a-propos','seances-tarifs','contact','mentions-legales','confidentialite','accompagnements/confiance-stress','accompagnements/transitions','accompagnements/jeunes','accompagnements/professionnel','accompagnements/entreprises'],'en':['','how-i-can-help','my-approach','about','sessions-fees','contact','legal','privacy','how-i-can-help/confidence-stress','how-i-can-help/life-transitions','how-i-can-help/young-people','how-i-can-help/career','how-i-can-help/organisations']}
support_ids=[8,9,11,10,12]
def esc(v): return html.escape(str(v),quote=True)
def url(l,i): return '/'+l+'/'+(paths[l][i]+'/' if paths[l][i] else '')
def safe_link(v): return v if urlparse(v).scheme in ('https','http') else ''
def link(l,i,text,cls='text-link'): return f'<a class="{cls}" href="{url(l,i)}">{text}<span aria-hidden="true"> ↗</span></a>'
def write(l,i,t):
 other='en' if l=='fr' else 'fr'
 def section(content,cls=''):return f'<section class="section {cls}">{content}</section>'
 def cta():return section(f'<div class="invite"><span class="eyebrow">{t["location"]}</span><h2>{t["invite"]}</h2><p>{t["invite_intro"]}</p>{link(l,5,t["contact"],"button light")}</div>','invite-wrap').replace(url(l,5),url(l,5)+('?support='+str(support_ids.index(i)) if i>=8 else ''))
 def faq(indexes=None):return section(f'<div class="split"><h2>{t["faq_title"]}</h2><div>'+''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in (t['faq'] if indexes is None else [t['faq'][n] for n in indexes]))+'</div></div>')
 def steps():return section(f'<h2>{t["steps_title"]}</h2><div class="three">'+''.join(f'<article><span class="number">0{n+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for n,(a,b) in enumerate(t['steps']))+'</div>')
 def heading(title,intro):return section(f'<span class="eyebrow">{t["label"]}</span><h1>{title}</h1><p class="lead">{intro}</p>','page-intro')
 def fees():return '<div class="fees">'+''.join(f'<article><div><h3>{esc(t["fees_names"][n])}</h3><p>{esc(t["fees_counts"][n])}</p></div><strong>{esc(p)} €</strong></article>' for n,p in enumerate(S['prices']))+'</div>'+('' if S['prices_confirmed'] else f'<p class="small">{t["provisional"]}</p>')+f'<p>{t["enquire"]}</p>'
 def tiles(indices):return '<div class="needs-list">'+''.join(f'<a class="need" href="{url(l,support_ids[n])}"><span class="number">0{n+1}</span><div><h3>{t["support_titles"][n]}</h3><p>{t["support_intros"][n]}</p></div><span class="arrow" aria-hidden="true">↗</span></a>' for n in indices)+'</div>'
 def portrait():return f'<img class="portrait" src="{esc(S["portrait"])}" width="700" height="800" loading="lazy" alt="{esc(S["name"])}">' if S['portrait'] else '<div class="still-life" aria-hidden="true"><span>◌</span><div></div></div>'
 def details_fields(keys):return ''.join(f'<div class="info-row"><h3>{t["details_labels"][n]}</h3><p>{esc(S[key])}</p></div>' for n,key in enumerate(keys) if S[key])
 body=''
 if i==0:
  body=f'<section class="hero"><div class="hero-copy"><span class="eyebrow">{t["label"]}</span><h1>{t["title"]}</h1><p class="lead">{t["intro"]}</p><div class="actions">{link(l,5,t["cta"],"button")}{link(l,2,t["explore"])}</div><div class="hero-note"><span></span>{t["location"]}</div></div><figure><img src="/assets/ambiance.webp" width="1100" height="1400" fetchpriority="high" alt="{t["ambience"]}"><figcaption>{t["caption"]}</figcaption></figure></section>'
  body+=section(f'<div class="section-heading"><span class="eyebrow">01 / {t["nav"][1]}</span><h2>{t["needs"]}</h2><p>{t["needs_intro"]}</p></div>'+tiles(range(3))+f'<div class="secondary-links">{link(l,10,t["support_titles"][3])}{link(l,12,t["support_titles"][4])}</div>')
  body+=section(f'<div class="split"><div class="quote-mark" aria-hidden="true">“</div><div><span class="eyebrow">02 / {t["nav"][2]}</span><h2>{t["approach_title"]}</h2><p>{t["approach_intro"]}</p>{link(l,2,t["explore"])}</div></div>','sage')
  body+=section(f'<div class="split about">{portrait()}<div><span class="eyebrow">03 / {t["nav"][3]}</span><h2>{t["about_title"]}</h2><p>{esc(S["name"])}</p><h3>{t["professional"]}</h3><p>{t["about_intro"]}</p>{link(l,3,t["nav"][3])}</div></div>')
  body+=steps()+section(f'<div class="split"><div><span class="eyebrow">04 / {t["nav"][4]}</span><h2>{t["fees_title"]}</h2><p>{t["fees_intro"]}</p>{link(l,4,t["nav"][4])}</div><div>{fees()}</div></div>')+faq([0,1,2])+cta()
 elif i==1: body=heading(t['needs'],t['needs_intro'])+section(tiles(range(5)))+cta()
 elif i==2: body=heading(t['approach_title'],t['approach_intro'])+section(f'<h2>{t["tools_title"]}</h2><p>{t["tools_intro"]}</p><div class="tools">'+''.join(f'<article><span class="number">0{n+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for n,(a,b) in enumerate(t['tools']))+'</div>'+f'<p class="medical">{t["medical"]}</p>')+steps()+cta()
 elif i==3:
  body=heading(t['about_title'],t['professional'])+section(f'<div class="split about">{portrait()}<div><h2>{esc(S["name"]) if S["name"] else t["nav"][3]}</h2><p class="lead">{t["subtitle"]}</p><p>{esc(S["biography"][l]) or t["about_intro"]}</p><p>{esc(S["qualifications"][l])}</p></div></div>')
  if S['gallery']:body+=section('<div class="three">'+''.join(f'<img src="{esc(x["src"])}" width="600" height="500" loading="lazy" alt="{esc(x["alt"][l])}">' for x in S['gallery'])+'</div>')
  body+=cta()
 elif i==4:body=heading(t['fees_title'],t['fees_intro'])+section(fees()+details_fields(['address','hours','consultation_languages','duration','modalities','payment','cancellation']))+faq()+cta()
 elif i==5:
  contact=f'<h2>{t["location"]}</h2>'
  if S['email']:contact+=f'<p><a href="mailto:{esc(S["email"])}">{esc(S["email"])}</a></p>'
  if S['phone']:contact+=f'<p><a href="tel:{esc(S["phone"].replace(" ",""))}">{esc(S["phone"])}</a></p>'
  contact+=details_fields(['address','hours','consultation_languages'])
  if safe_link(S['booking_url']):contact+=f'<a class="button" href="{esc(S["booking_url"])}">{t["booking"]}</a>'
  form=f'<form data-endpoint="{esc(safe_link(S["contact_endpoint"]))}" data-lang="{l}" novalidate><input type="hidden" name="language" value="{l}"><div class="form-grid">'
  for n,(name,typ,req) in enumerate([('first_name','text',True),('email','email',True),('phone','tel',False)]):form+=f'<label>{t["form"][n]}{" *" if req else ""}<input name="{name}" type="{typ}" {"required" if req else ""} maxlength="150" autocomplete="{["given-name","email","tel"][n]}"></label>'
  form+=f'<label>{t["form"][5]}<input name="company" maxlength="150" autocomplete="organization"></label></div><label>{t["form"][3]} *<select name="support" required><option value="">{t["choose"]}</option>'+''.join(f'<option value="{n}">{x}</option>' for n,x in enumerate(t['support_titles']))+'</select></label>'
  form+=f'<label>{t["form"][4]} *<textarea name="message" required maxlength="3000" rows="5"></textarea></label><p class="small">{t["privacy_note"]} <a href="{url(l,7)}">{t["privacy_link"]}</a></p><p class="form-status" role="status" aria-live="polite"></p><button class="button" type="submit" {"disabled" if not safe_link(S["contact_endpoint"]) else ""}>{t["form"][6]}</button>'
  if not safe_link(S['contact_endpoint']):form+=f'<p class="small">{t["unavailable"]}</p>'
  form+=f'<noscript><p>{t["unavailable"]}</p></noscript></form>'
  body=heading(t['contact_title'],t['contact_intro'])+section(f'<div class="split contact-layout"><aside>{contact}</aside>{form}</div>')
 elif i in (6,7):body=heading(t['legal'] if i==6 else t['privacy_link'],t['legal_pending'])+section(f'<div class="reading"><p>{t["legal_text"] if i==6 else t["privacy_text"]}</p><p>{esc(S["legal_identity"])}</p><p>{esc(S["hosting"] if i==6 else S["privacy_contact"])}</p></div>')
 else:
  n=support_ids.index(i)
  body=heading(t['support_titles'][n],t['support_intros'][n])+section(f'{link(l,1,t["back"])}<div class="split support-detail"><h2>{t["recognise"]}</h2><ul>'+''.join(f'<li>{esc(x)}</li>' for x in t['situations'][n])+'</ul></div>')+section(f'<div class="reading"><h2>{t["work_title"]}</h2><p>{t["work"][n]}</p><h3>{t["tools_title"]}</h3><p>{t["tools_intro"]}</p>{link(l,2,t["explore"])}</div>','sage')+steps()+faq([0,1,2])+cta()
 title=(t['nav'][i] if i<6 else t['legal'] if i==6 else t['privacy_link'] if i==7 else t['support_titles'][support_ids.index(i)])+' · '+(S['name'] or t['brand'])+' · Nice'
 description=t['intro'] if i==0 else t['support_intros'][support_ids.index(i)] if i>=8 else t['approach_intro'] if i==2 else t['fees_intro'] if i==4 else t['contact_intro'] if i==5 else t['about_intro'] if i==3 else t['needs_intro'] if i==1 else (t['legal_text'] if i==6 else t['privacy_text'])
 domain=S['domain'].rstrip('/')
 seo=''.join(f'<link rel="alternate" hreflang="{lang}" href="{esc(domain+url(lang,i))}">' for lang in ('fr','en'))+f'<link rel="alternate" hreflang="x-default" href="{esc(domain)}/">'
 if domain:seo+=f'<link rel="canonical" href="{esc(domain+url(l,i))}"><meta property="og:url" content="{esc(domain+url(l,i))}"><meta property="og:image" content="{esc(domain)}/assets/ambiance.webp">'
 navigation=''.join(f'<a href="{url(l,j)}" {"aria-current=page" if i==j else ""}>{esc(x)}</a>' for j,x in enumerate(t['nav']))
 translations={k:t[k] for k in ('sending','success','error','invalid','menu','close')}
 markup=f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:locale" content="{'fr_FR' if l=='fr' else 'en_GB'}">{seo}<link rel="stylesheet" href="/assets/style.css"><script src="/assets/site.js" defer></script><noscript><style>@media(max-width:950px){{header{{position:relative}}#navigation{{display:flex;position:static;flex-basis:100%;order:4}}.menu-toggle{{display:none}}}}</style></noscript></head><body><a class="skip" href="#main">{t['skip']}</a><header><a class="brand" href="{url(l,0)}"><span class="brand-mark" aria-hidden="true">a.</span><span>{esc(S['name']) or t['brand']}<small>NICE</small></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation">{t['menu']}</button><nav id="navigation" aria-label="{t['menu']}">{navigation}</nav><div class="languages"><a href="{url('fr',i)}" lang="fr" {'aria-current=page' if l=='fr' else ''}>FR</a><span>/</span><a href="{url('en',i)}" lang="en" {'aria-current=page' if l=='en' else ''}>EN</a></div></header><main id="main">{body}</main><footer><div><a class="brand" href="{url(l,0)}">{esc(S['name']) or t['brand']}</a><p>{t['copyright']}</p></div><div>{link(l,6,t['legal'])}{link(l,7,t['privacy_link'])}<p>© 2026</p></div></footer><script type="application/json" id="ui-text">{json.dumps(translations,ensure_ascii=False).replace('<','&lt;')}</script></body></html>'''
 target=OUT/url(l,i).lstrip('/');target.mkdir(parents=True,exist_ok=True);(target/'index.html').write_text(markup)
for l in paths:
 t=json.loads((ROOT/f'content/{l}.json').read_text())
 for i in range(len(paths[l])):write(l,i,t)
(OUT/'index.html').write_text('''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Bienvenue · Welcome — Nice</title><meta name="description" content="Accompagnement personnel et professionnel à Nice. Personal and professional development in Nice."><link rel="stylesheet" href="/assets/style.css"></head><body><main class="language-choice"><span class="brand-mark">a.</span><span class="eyebrow">NICE · CÔTE D’AZUR</span><h1>Un espace pour avancer.<br><em lang="en">Space to move forward.</em></h1><div class="actions"><a class="button" href="/fr/" lang="fr">Découvrir en français ↗</a><a class="button outline" href="/en/" lang="en">Explore in English ↗</a></div></main></body></html>''')
if S['domain']:
 root=OUT/'index.html'
 root.write_text(root.read_text().replace('</head>', '<link rel="canonical" href="'+esc(S['domain'].rstrip('/')+'/')+'">'+''.join('<link rel="alternate" hreflang="'+l+'" href="'+esc(S['domain'].rstrip('/')+url(l,0))+'">' for l in ('fr','en'))+'<link rel="alternate" hreflang="x-default" href="'+esc(S['domain'].rstrip('/')+'/')+'"></head>'))
 entries='<url><loc>'+esc(S['domain'].rstrip('/')+'/')+'</loc></url>'+''.join('<url><loc>'+esc(S['domain'].rstrip('/')+url(l,i))+'</loc>'+''.join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{esc(S["domain"].rstrip("/")+url(a,i))}"/>' for a in ('fr','en'))+'</url>' for l in paths for i in range(len(paths[l])))
 (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+entries+'</urlset>')
 (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+S['domain'].rstrip('/')+'/sitemap.xml\n')
else:
 (OUT/'sitemap.xml').unlink(missing_ok=True)
 (OUT/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Built 27 bilingual pages. '+('Production SEO enabled.' if S['domain'] else 'Preview indexing blocked until domain is configured.'))

# GitHub project Pages serves the site beneath /Site-beta, rather than /.
base=os.environ.get('SITE_BASE_PATH','').rstrip('/')
if base:
 import re
 if not base.startswith('/') or '..' in base or any(c in base for c in '<>"\'\\?#'):
  raise ValueError('SITE_BASE_PATH must be a safe absolute URL path')
 for page in OUT.rglob('*.html'):
  page.write_text(re.sub(r'(href|src)="/(?!/)',lambda m:m.group(1)+'="'+base+'/',page.read_text()))
 print('Base path:',base)
