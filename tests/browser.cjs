const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('node:fs');const path=require('node:path');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',args:['--no-sandbox']});
 const origin=process.env.PREVIEW_ORIGIN||'http://127.0.0.1:8001';const base=process.env.SITE_BASE_PATH||'/Site-beta';
 const output=path.resolve(__dirname,'../review');fs.mkdirSync(output,{recursive:true});
 const page=await browser.newPage();let checks=0;function check(value,label){checks++;if(!value)throw Error(label);}
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const visited=new Set(),pending=[base+'/'];
 while(pending.length){const href=pending.shift();const route=href.split('?')[0];if(visited.has(route))continue;visited.add(route);const response=await page.goto(origin+route);check(response.status()===200,'HTTP '+route);
  for(const href of await page.locator('a[href]').evaluateAll(a=>a.map(x=>x.getAttribute('href')))){if(href.startsWith(base+'/'))pending.push(href);}
  check((await page.title()).includes('Valérie Migueres'),'identity '+route);
  if(route!==base+'/'){
   const lang=route.slice(base.length+1).split('/')[0];check(await page.locator('html').getAttribute('lang')===lang,'language '+route);
   const other=lang==='fr'?'en':'fr';const opposite=await page.locator('.languages a[lang='+other+']').getAttribute('href');
   const alternate=await page.locator('link[hreflang='+other+']').getAttribute('href');check(alternate==='https://ellistaieb.github.io'+opposite,'absolute hreflang '+route);
   check((await page.locator('link[rel=canonical]').getAttribute('href'))==='https://ellistaieb.github.io'+route,'canonical '+route);
   await page.goto(origin+opposite);check(await page.locator('.languages a[lang='+lang+']').getAttribute('href')===route,'reciprocal language '+route);
  }
 }
 check(visited.size===27,'27 pages found, actual '+visited.size);
 for(const width of [320,390,768,1024,1440]){
  await page.setViewportSize({width,height:950});
  for(const route of visited){await page.goto(origin+route);check(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'overflow '+width+' '+route);check(await page.locator('h1').count()===1,'single H1 '+route);
   check(await page.evaluate(()=>[...document.querySelectorAll('header > *')].filter(e=>e.getClientRects().length&&getComputedStyle(e).display!=='none').every((e,i,a)=>{if(i===0||e.tagName==='NAV')return true;let r=e.getBoundingClientRect(),p=a[i-1].getBoundingClientRect();return a[i-1].tagName==='NAV'||r.left>=p.right-1;})),'header collision '+width+' '+route);
  }
  for(const [slug,name] of [['/fr/','home'],['/fr/accompagnements/','offers'],['/en/contact/','contact']]){await page.goto(origin+base+slug);await page.waitForTimeout(450);await page.screenshot({path:output+'/'+name+'-'+width+'.png',fullPage:true});}
 }
 await page.setViewportSize({width:390,height:844});await page.goto(origin+base+'/fr/');await page.locator('.menu-toggle').click();check(await page.locator('.menu-toggle').getAttribute('aria-expanded')==='true','menu state');check(await page.locator('#navigation').evaluate(el=>!el.inert),'menu interactive');check(await page.locator('#navigation a').first().evaluate(el=>el===document.activeElement),'menu focus');await page.keyboard.press('Escape');check(await page.locator('.menu-toggle').evaluate(el=>el===document.activeElement),'escape focus');check(await page.locator('#navigation').evaluate(el=>el.inert),'closed menu inert');
 await page.keyboard.press('Tab');check(await page.locator('.languages a[lang=fr]').evaluate(el=>el===document.activeElement),'keyboard language selector');
 await page.goto(origin+base+'/fr/accompagnements/entreprises/');await page.locator('.invite .button').click();check(await page.locator('[name=support]').inputValue()==='4','offer preselection');check(await page.locator('.company-field').isVisible(),'company for business');await page.locator('.languages a[lang=en]').click();check(await page.locator('[name=support]').inputValue()==='4','language preserves offer');await page.locator('[name=support]').selectOption('0');check(await page.locator('.company-field').isHidden(),'company hidden for individual');
 for(const lang of ['fr','en']){
  await page.goto(origin+base+'/'+lang+'/contact/');check(await page.locator('button[type=submit]').isDisabled(),'unconfigured form disabled');
  await page.evaluate(()=>{const form=document.querySelector('form');form.dataset.endpoint='https://contact.test/send';form.querySelector('button[type=submit]').disabled=false;});
  await page.locator('button[type=submit]').click();check(await page.locator('[name=first_name]').getAttribute('aria-invalid')==='true','accessible validation');check(await page.locator('[name=first_name]').evaluate(el=>el===document.activeElement),'invalid first focus');
  await page.locator('[name=first_name]').fill('Test');await page.locator('[name=email]').fill('invalid');await page.locator('[name=support]').selectOption('0');await page.locator('[name=message]').fill('Hello');await page.locator('button[type=submit]').click();check(await page.locator('[name=email]').getAttribute('aria-invalid')==='true','invalid email');await page.locator('[name=email]').fill('test@example.org');
  const fail=lang==='fr'?'n’a pas':'could not',success=lang==='fr'?'bien été':'has been';
  for(const [status,body,expected] of [[500,{ok:false},fail],[200,{ok:false},fail],[200,{success:true},fail],[200,{ok:true},success]]){
   await page.route('https://contact.test/send',async r=>{check(r.request().postDataJSON().language===lang,'submitted language');check(!('company' in r.request().postDataJSON()),'individual excludes company');await new Promise(resolve=>setTimeout(resolve,180));return r.fulfill({status,contentType:'application/json',body:JSON.stringify(body)});});
   await page.locator('button[type=submit]').click();check(await page.locator('form').getAttribute('aria-busy')==='true','sending state');await page.waitForFunction(()=>!document.querySelector('form').hasAttribute('aria-busy'));check((await page.locator('.form-status').innerText()).includes(expected),'delivery state '+lang+' '+status+' '+JSON.stringify(body));await page.unroute('https://contact.test/send');
  }
  await page.locator('[name=first_name]').fill('Bot');await page.locator('[name=email]').fill('bot@example.org');await page.locator('[name=support]').selectOption('0');await page.locator('[name=message]').fill('Spam');await page.locator('[name=_gotcha]').evaluate(el=>el.value='spam');let sent=false;await page.route('https://contact.test/send',r=>{sent=true;return r.abort();});await page.locator('button[type=submit]').click();check(!sent,'honeypot blocks submission');await page.unroute('https://contact.test/send');
 }
 const staticContext=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});const staticPage=await staticContext.newPage();await staticPage.goto(origin+base+'/fr/');check(await staticPage.locator('#navigation').isVisible(),'no JS nav');check(await staticPage.locator('h1').isVisible(),'no JS content');
 await staticPage.setViewportSize({width:1024,height:768});await staticPage.goto(origin+base+'/en/');check(await staticPage.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'no JS tablet overflow');
 const reduced=await browser.newContext({reducedMotion:'reduce',viewport:{width:1440,height:900}});const rp=await reduced.newPage();await rp.goto(origin+base+'/en/');check(await rp.locator('.stone').evaluate(el=>getComputedStyle(el).animationName==='none'),'reduced sculpture');check(await rp.evaluate(()=>document.getAnimations().length===0),'reduced animations');
 for(const viewport of [{width:768,height:1024},{width:1024,height:768}]){await page.setViewportSize(viewport);await page.goto(origin+base+'/en/');check(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'tablet orientation');}
 check(errors.length===0,'JavaScript errors: '+errors.join(', '));
 console.log(JSON.stringify({pages:visited.size,widths:[320,390,768,1024,1440],checks,failures:errors,contact:'simulated API only; no real message sent'},null,2));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
