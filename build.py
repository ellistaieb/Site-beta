import json, html, pathlib, shutil, os
from urllib.parse import urlparse
ROOT=pathlib.Path(__file__).resolve().parent
S=json.loads((ROOT/'content/settings.json').read_text())
S['domain']=os.environ.get('SITE_DOMAIN',S['domain'])
OUT=ROOT/'dist'; OUT.mkdir(exist_ok=True)
shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
paths={'fr':['','accompagnements','mon-approche','a-propos','seances-tarifs','contact','mentions-legales','confidentialite','accompagnements/confiance-stress','accompagnements/transitions','accompagnements/jeunes','accompagnements/professionnel','accompagnements/entreprises'],'en':['','how-i-can-help','my-approach','about','sessions-fees','contact','legal','privacy','how-i-can-help/confidence-stress','how-i-can-help/life-transitions','how-i-can-help/young-people','how-i-can-help/career','how-i-can-help/organisations']}
paths['fr'].append('conditions-utilisation')
paths['en'].append('terms-of-use')
LEGAL=json.loads((ROOT/'content/legal-content.json').read_text())
LEGAL_SETTINGS=json.loads((ROOT/'content/legal-settings.json').read_text())
for feature in ('contact_endpoint','booking_url'):
 if S.get(feature,'')!=LEGAL_SETTINGS['audited_features'].get(feature,''):
  raise ValueError('Revoir les documents juridiques et leur audit avant de modifier '+feature)
LEGAL_PAGES={6:'legal',7:'privacy',13:'terms'}
support_ids=[8,9,11,10,12]
def esc(v): return html.escape(str(v),quote=True)
def url(l,i): return '/'+l+'/'+(paths[l][i]+'/' if paths[l][i] else '')
def safe_link(v): return v if urlparse(v).scheme == 'https' and urlparse(v).netloc else ''
def link(l,i,text,cls='text-link'): return f'<a class="{cls}" href="{url(l,i)}">{text}<span aria-hidden="true"> ↗</span></a>'
def write(l,i,t):
 other='en' if l=='fr' else 'fr'
 def section(content,cls=''):return f'<section class="section {cls}">{content}</section>'
 def cta():return section(f'<div class="invite"><span class="eyebrow">{t["location"]}</span><h2>{t["invite"]}</h2><p>{t["invite_intro"]}</p>{link(l,5,t["contact"],"button light")}</div>','invite-wrap').replace(url(l,5),url(l,5)+('?support='+str(support_ids.index(i)) if i in support_ids else ''))
 def faq(indexes=None):return section(f'<div class="split"><h2>{t["faq_title"]}</h2><div>'+''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in (t['faq'] if indexes is None else [t['faq'][n] for n in indexes]))+'</div></div>')
 def steps():return section(f'<h2>{t["steps_title"]}</h2><div class="three">'+''.join(f'<article><span class="number">0{n+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for n,(a,b) in enumerate(t['steps']))+'</div>')
 def heading(title,intro):return section(f'<span class="eyebrow">{t["label"]}</span><h1>{title}</h1><p class="lead">{intro}</p>','page-intro')
 def fees():return '<div class="fees">'+''.join(f'<article><div><h3>{esc(t["fees_names"][n])}</h3><p>{esc(t["fees_counts"][n])}</p></div><strong>{esc(p)} €</strong></article>' for n,p in enumerate(S['prices']))+'</div>'+('' if S['prices_confirmed'] else f'<p class="small">{t["provisional"]}</p>')+f'<p>{t["enquire"]}</p>'
 def tiles(indices, expanded=False):
  entries=[]
  for n in indices:
   examples='<ul class="offer-examples">'+''.join(f'<li>{esc(x)}</li>' for x in t['support_examples'][n])+'</ul>' if expanded else ''
   entries.append(f'<a class="need offer-{n}" href="{url(l,support_ids[n])}"><span class="number">0{n+1}</span><div><h3>{t["support_titles"][n]}</h3><p>{t["support_intros"][n]}</p>{examples}<span class="offer-link">{t["offer_link"]}</span></div><span class="arrow" aria-hidden="true"></span></a>')
  return '<div class="needs-list">'+''.join(entries)+'</div>'
 def image(slot, cls, eager=False):
  photo=S['images'].get(slot,{})
  if not photo.get('src'):return ''
  position=photo.get('position','50% 50%')
  import re
  if not re.fullmatch(r'\d{1,3}% \d{1,3}%',position):position='50% 50%'
  return f'<img class="{cls}" src="{esc(photo["src"])}" width="800" height="1000" style="object-position:{position}" alt="{esc(photo["alt"][l])}" {"fetchpriority=high" if eager else "loading=lazy"}>'
 def portrait():
  return image('portrait','portrait') or '<div class="identity-art" aria-hidden="true"><span class="identity-initials">VM</span><span class="identity-line"></span><span class="identity-circle"></span></div>'
 def details_fields(keys):return ''.join(f'<div class="info-row"><h3>{t["details_labels"][n]}</h3><p>{esc(S[key])}</p></div>' for n,key in enumerate(keys) if S[key])
 body=''
 if i==0:
  visual=image('hero','hero-photo',True) or '<div class="sculpture" aria-hidden="true"><div class="sculpture-halo"></div><div class="stone"></div><div class="glass"></div><span class="sculpture-line"></span></div>'
  body=f'<section class="hero"><div class="hero-copy"><span class="eyebrow">{t["label"]}</span><p class="hero-name">{esc(S["name"])}</p><h1>{t["title"]}</h1><p class="lead">{t["intro"]}</p><div class="actions">{link(l,5,t["cta"],"button")}{link(l,1,t["discover"],"button outline")}</div><div class="hero-note"><span></span>{t["hero_note"]}</div></div><div class="hero-visual">{visual}</div></section>'
  body+=section(f'<div class="section-heading"><span class="eyebrow">01 / {t["nav"][1]}</span><h2>{t["needs"]}</h2><p>{t["needs_summary"]}</p></div>'+tiles(range(3))+f'<div class="secondary-links">{link(l,10,t["support_titles"][3])}{link(l,12,t["support_titles"][4])}</div>')
  body+=section(f'<div class="split about">{portrait()}<div><span class="eyebrow">02 / {t["nav"][3]}</span><h2>{esc(S["name"])}</h2><h3>{t["professional"]}</h3><p>{t["about_intro"]}</p>{link(l,3,t["nav"][3])}</div></div>')
  body+=section(f'<div class="split"><div class="quote-mark" aria-hidden="true">“</div><div><span class="eyebrow">03 / {t["nav"][2]}</span><h2>{t["approach_title"]}</h2><p>{t["approach_intro"]}</p>{link(l,2,t["explore"])}</div></div>','sage')
  body+=steps()+section(f'<div class="split"><div><span class="eyebrow">04 / {t["nav"][4]}</span><h2>{t["fees_title"]}</h2><p>{t["fees_intro"]}</p>{link(l,4,t["nav"][4])}</div><div>{fees()}</div></div>')+faq([0,1,2])+cta()
 elif i==1: body=heading(t['needs'],t['needs_summary'])+section(link(l,5,t['cta'],'button'),'intro-action')+section(tiles(range(5),True),'offers-section')+cta()
 elif i==2: body=heading(t['approach_title'],t['approach_intro'])+section(f'<h2>{t["tools_title"]}</h2><p>{t["tools_intro"]}</p><div class="tools">'+''.join(f'<article><span class="number">0{n+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for n,(a,b) in enumerate(t['tools']))+'</div>'+f'<p class="medical">{t["medical"]}</p>')+steps()+cta()
 elif i==3:
  body=heading(t['about_title'],t['professional'])+section(f'<div class="split about">{portrait()}<div><h2>{esc(S["name"]) if S["name"] else t["nav"][3]}</h2><p class="lead">{t["subtitle"]}</p><p>{esc(S["biography"][l]) or t["about_intro"]}</p><p>{esc(S["qualifications"][l])}</p></div></div>')
  if S['gallery']:body+=section('<div class="three">'+''.join(f'<img style="object-position:{esc(x.get("position","50% 50%"))}" src="{esc(x["src"])}" width="600" height="500" loading="lazy" alt="{esc(x["alt"][l])}">' for x in S['gallery'])+'</div>')
  body+=cta()
 elif i==4:body=heading(t['fees_title'],t['fees_intro'])+section(fees()+details_fields(['address','hours','consultation_languages','duration','modalities','payment','cancellation']))+faq()+cta()
 elif i==5:
  contact=f'<h2>{t["location"]}</h2>'
  if S['email']:contact+=f'<p><a href="mailto:{esc(S["email"])}">{esc(S["email"])}</a></p>'
  if S['phone']:contact+=f'<p><a href="tel:{esc(S["phone"].replace(" ",""))}">{esc(S["phone"])}</a></p>'
  contact+=details_fields(['address','hours','consultation_languages'])
  if safe_link(S['booking_url']):contact+=f'<a class="button" href="{esc(S["booking_url"])}">{t["booking"]}</a>'
  endpoint=safe_link(S['contact_endpoint'])
  form=f'<form action="{esc(endpoint) if endpoint else "#"}" method="post" data-endpoint="{esc(endpoint)}" data-provider="{esc(S["contact_provider"])}" data-lang="{l}" novalidate><input type="hidden" name="language" value="{l}"><div class="form-grid">'
  for n,(name,typ,req) in enumerate([('first_name','text',True),('email','email',True),('phone','tel',False)]):
   form+=f'<label>{t["form"][n]}{" *" if req else ""}<input name="{name}" type="{typ}" {"required" if req else ""} maxlength="150" autocomplete="{["given-name","email","tel"][n]}" aria-describedby="{name}-error"><span id="{name}-error" class="field-error"></span></label>'
  form+='</div>'
  form+=f'<label>{t["form"][3]} *<select name="support" required aria-describedby="support-error"><option value="">{t["choose"]}</option>'+''.join(f'<option value="{n}">{x}</option>' for n,x in enumerate(t['support_titles']))+'</select><span id="support-error" class="field-error"></span></label>'
  form+=f'<label class="company-field" hidden>{t["form"][5]}<input name="company" maxlength="150" autocomplete="organization"></label>'
  form+=f'<label>{t["form"][4]} *<textarea name="message" required maxlength="3000" rows="5" aria-describedby="message-error"></textarea><span id="message-error" class="field-error"></span></label>'
  form+=f'<label class="honeypot" aria-hidden="true">{t["anti_spam_label"]}<input name="_gotcha" tabindex="-1" autocomplete="off"></label>'
  form+=f'<p class="small">{t["privacy_note"] if endpoint else t["privacy_note_inactive"]} <a href="{url(l,7)}">{t["privacy_link"]}</a></p><p class="form-status" role="status" aria-live="polite"></p><button class="button" type="submit" {"disabled" if not endpoint else ""}>{t["form"][6]}</button>'
  if not endpoint:form+=f'<p class="small">{t["unavailable"]}</p>'
  form+=f'<noscript><style>form:has(select[name=support] option[value="4"]:checked) .company-field[hidden]{{display:block}}</style><p>{t["nojs_send"] if endpoint else t["unavailable"]}</p></noscript></form>'
  body=heading(t['contact_title'],t['contact_intro'])+section(f'<div class="split contact-layout"><aside>{contact}</aside>{form}</div>')
 elif i in LEGAL_PAGES:
  doc=LEGAL[l][LEGAL_PAGES[i]]
  draft=LEGAL[l]['draft']
  articles=''.join(f'<article id="article-{n+1}"><h2>{esc(part["heading"])}</h2>'+''.join(f'<p>{esc(p)}</p>' for p in part['paragraphs'])+'</article>' for n,part in enumerate(doc['sections']))
  keys=['status','registered_name','registration','business_address','professional_email','professional_phone','publication_director','vat','professional_rules','host_identity'] if i==6 else ['controller_identity','rights_contact','hosting_roles','hosting_retention','transfer_guarantees'] if i==7 else ['registered_name','professional_email']
  fields=''.join(f'<dt>{esc(LEGAL_SETTINGS["fields"][key][l])}</dt><dd>{esc(LEGAL_SETTINGS["fields"][key]["value"]) if LEGAL_SETTINGS["fields"][key]["value"] else ("[À COMPLÉTER / À CONFIRMER]" if l=="fr" else "[TO COMPLETE / CONFIRM]")}</dd>' for key in keys)
  body=heading(doc['title'],doc['description'])+section(f'<div class="reading legal-draft"><aside class="draft-notice" role="note"><strong>{esc(LEGAL[l]["version"])}</strong><p>{esc(draft)}</p></aside>{articles}<h2>{esc(LEGAL[l]["missing"])}</h2><dl>{fields}</dl></div>')

 else:
  n=support_ids.index(i)
  body=heading(t['support_titles'][n],t['support_intros'][n])+section(f'{link(l,1,t["back"])}<div class="split support-detail"><h2>{t["recognise"]}</h2><ul>'+''.join(f'<li>{esc(x)}</li>' for x in t['situations'][n])+'</ul></div>')+section(f'<div class="reading"><h2>{t["work_title"]}</h2><p>{t["work"][n]}</p><h3>{t["tools_title"]}</h3><p>{t["tools_intro"]}</p>{link(l,2,t["explore"])}</div>','sage')+steps()+faq([0,1,2])+cta()
 page_title=LEGAL[l][LEGAL_PAGES[i]]['title'] if i in LEGAL_PAGES else t['nav'][i] if i<6 else t['support_titles'][support_ids.index(i)]
 title=page_title+' · '+S['name']+' · Nice'
 if i==0:title=S['name']+' · '+t['brand_line']
 description=LEGAL[l][LEGAL_PAGES[i]]['description'] if i in LEGAL_PAGES else t['intro'] if i==0 else t['support_intros'][support_ids.index(i)] if i in support_ids else t['approach_intro'] if i==2 else t['fees_intro'] if i==4 else t['contact_intro'] if i==5 else t['about_intro'] if i==3 else t['needs_intro']
 description=description+(' — '+S['name']+' · Nice' if S['name'] not in description else '')
 domain=S['domain'].rstrip('/')
 seo=''.join(f'<link rel="alternate" hreflang="{lang}" href="{esc(domain+url(lang,i))}">' for lang in ('fr','en'))+f'<link rel="alternate" hreflang="x-default" href="{esc(domain)}/">'
 if domain:seo+=f'<link rel="canonical" href="{esc(domain+url(l,i))}"><meta property="og:url" content="{esc(domain+url(l,i))}"><meta property="og:image" content="{esc(domain+S["images"]["share"][l])}">'
 navigation=''.join(f'<a href="{url(l,j)}" {"aria-current=page" if i==j else ""}>{esc(x)}</a>' for j,x in enumerate(t['nav']))
 translations={k:t[k] for k in ('sending','success','error','invalid','menu','close')}
 structured={'@context':'https://schema.org','@type':'Person','name':S['name'],'jobTitle':t['professional'],'url':domain+url(l,3)}
 mobile_cta=link(l,5,t['cta'],'button mobile-appointment') if i not in (5,6,7,13) else ''
 markup=f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:locale" content="{'fr_FR' if l=='fr' else 'en_GB'}">{seo}<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/style.css"><script src="/assets/site.js" defer></script><noscript><style>@media(max-width:1190px){{header{{position:relative;flex-wrap:wrap}}#navigation{{display:flex;position:static;flex-basis:100%;order:4}}.menu-toggle{{display:none}}}}</style></noscript></head><body><a class="skip" href="#main">{t['skip']}</a><header><a class="brand" href="{url(l,0)}"><span class="brand-mark" aria-hidden="true">VM</span><span>{esc(S['name']) or t['brand']}<small>{t["brand_line"]}</small></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation">{t['menu']}</button><nav id="navigation" aria-label="{t['menu']}">{navigation}</nav>{link(l,5,t["cta"],"button header-appointment")}<div class="languages"><a href="{url('fr',i)}" lang="fr" {'aria-current=page' if l=='fr' else ''}>FR</a><span>/</span><a href="{url('en',i)}" lang="en" {'aria-current=page' if l=='en' else ''}>EN</a></div></header><main id="main" tabindex="-1">{body}</main>{mobile_cta}<footer><div><a class="brand" href="{url(l,0)}">{esc(S['name']) or t['brand']}</a><p>{t['copyright']}</p></div><div>{link(l,6,t['legal'])}{link(l,7,t['privacy_link'])}{link(l,13,t['terms'])}<p>© 2026</p></div></footer><script type="application/ld+json">{json.dumps(structured,ensure_ascii=False).replace("<","\\u003c")}</script><script type="application/json" id="ui-text">{json.dumps(translations,ensure_ascii=False).replace('<','&lt;')}</script></body></html>'''
 target=OUT/url(l,i).lstrip('/');target.mkdir(parents=True,exist_ok=True);(target/'index.html').write_text(markup)
for l in paths:
 t=json.loads((ROOT/f'content/{l}.json').read_text())
 for i in range(len(paths[l])):write(l,i,t)
choice={lang:json.loads((ROOT/f'content/{lang}.json').read_text()) for lang in ('fr','en')}
root_title=S['name']+' · Nice'
root_description=choice['fr']['brand_line']+' / '+choice['en']['brand_line']
(OUT/'index.html').write_text(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(root_title)}</title><meta name="description" content="{esc(root_description)}"><meta property="og:title" content="{esc(root_title)}"><meta property="og:description" content="{esc(root_description)}"><meta property="og:type" content="website"><meta property="og:image" content="{esc(S['domain'].rstrip('/')+S['images']['share']['fr'])}"><link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/style.css"></head><body><main class="language-choice"><span class="brand-mark" aria-hidden="true">VM</span><span class="eyebrow">NICE · CÔTE D’AZUR</span><p class="eyebrow">{esc(S['name'])}</p><h1>{esc(choice['fr']['welcome_signature'])}<br><em lang="en">{esc(choice['en']['welcome_signature'])}</em></h1><div class="actions"><a class="button" href="/fr/" lang="fr">{esc(choice['fr']['language_choice'])}</a><a class="button outline" href="/en/" lang="en">{esc(choice['en']['language_choice'])}</a></div></main></body></html>''')
if S['domain']:
 root=OUT/'index.html'
 root.write_text(root.read_text().replace('</head>', '<link rel="canonical" href="'+esc(S['domain'].rstrip('/')+'/')+'">'+''.join('<link rel="alternate" hreflang="'+l+'" href="'+esc(S['domain'].rstrip('/')+url(l,0))+'">' for l in ('fr','en'))+'<link rel="alternate" hreflang="x-default" href="'+esc(S['domain'].rstrip('/')+'/')+'"></head>'))
 entries='<url><loc>'+esc(S['domain'].rstrip('/')+'/')+'</loc></url>'+''.join('<url><loc>'+esc(S['domain'].rstrip('/')+url(l,i))+'</loc>'+''.join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{esc(S["domain"].rstrip("/")+url(a,i))}"/>' for a in ('fr','en'))+'<xhtml:link rel="alternate" hreflang="x-default" href="'+esc(S['domain'].rstrip('/')+'/')+'"/></url>' for l in paths for i in range(len(paths[l])))
 (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+entries+'</urlset>')
 (OUT/'robots.txt').write_text('User-agent: *\n'+('Allow: /' if S.get('indexing_enabled') else 'Disallow: /')+'\nSitemap: '+S['domain'].rstrip('/')+'/sitemap.xml\n')
else:
 (OUT/'sitemap.xml').unlink(missing_ok=True)
 (OUT/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Built 29 bilingual pages. Absolute SEO metadata enabled; indexing '+('enabled.' if S.get('indexing_enabled') else 'blocked for preview.'))

# GitHub project Pages serves the site beneath /Site-beta, rather than /.
base=os.environ.get('SITE_BASE_PATH','').rstrip('/')
if base:
 import re
 if not base.startswith('/') or '..' in base or any(c in base for c in '<>"\'\\?#'):
  raise ValueError('SITE_BASE_PATH must be a safe absolute URL path')
 for page in OUT.rglob('*.html'):
  page.write_text(re.sub(r'(href|src)="/(?!/)',lambda m:m.group(1)+'="'+base+'/',page.read_text()))
 print('Base path:',base)
