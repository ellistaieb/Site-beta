const text=JSON.parse(document.querySelector('#ui-text').textContent);
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
const header=document.querySelector('header');
const compact=matchMedia('(max-width:1190px)');
function closeMenu(restore=false){toggle.setAttribute('aria-expanded','false');toggle.textContent=text.menu;nav.classList.remove('open');nav.inert=compact.matches;if(restore)toggle.focus();}
function openMenu(){toggle.setAttribute('aria-expanded','true');toggle.textContent=text.close;nav.classList.add('open');nav.inert=false;nav.querySelector('a').focus();}
closeMenu();
toggle.addEventListener('click',()=>toggle.getAttribute('aria-expanded')==='true'?closeMenu(true):openMenu());
compact.addEventListener('change',()=>closeMenu());
document.addEventListener('keydown',e=>{
 if(toggle.getAttribute('aria-expanded')!=='true')return;
 if(e.key==='Escape'){e.preventDefault();closeMenu(true);}
 if(e.key==='Tab'){
  const focusable=[...header.querySelectorAll('a,button')].filter(el=>el.getClientRects().length&&!el.closest('[inert]'));
  const first=focusable[0],last=focusable.at(-1);
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
  else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}
 }
});
document.addEventListener('pointerdown',e=>{if(!header.contains(e.target)&&toggle.getAttribute('aria-expanded')==='true')closeMenu(true);});
nav.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
window.addEventListener('scroll',()=>header.classList.toggle('scrolled',window.scrollY>20),{passive:true});
const reduce=matchMedia('(prefers-reduced-motion:reduce)');
if('IntersectionObserver'in window&&!reduce.matches){
 const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){if(!reduce.matches)entry.target.animate([{opacity:.45,transform:'translateY(16px)'},{opacity:1,transform:'none'}],{duration:350,easing:'ease-out'});observer.unobserve(entry.target);}},{threshold:.08});
 document.querySelectorAll('.section').forEach(el=>observer.observe(el));
 reduce.addEventListener('change',()=>{if(reduce.matches)document.getAnimations().forEach(a=>a.cancel());});
}
const mobileCta=document.querySelector('.mobile-appointment');
if(mobileCta&&'IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>{for(const entry of entries)mobileCta.hidden=entry.isIntersecting;},{rootMargin:'0px 0px 90px 0px'});observer.observe(document.querySelector('footer'));}
const form=document.querySelector('form');
if(form){
 const choice=new URLSearchParams(location.search).get('support');if(choice!==null&&/^[0-4]$/.test(choice))form.elements.support.value=choice;
 const company=form.querySelector('.company-field');
 function syncCompany(){const visible=form.elements.support.value==='4';company.hidden=!visible;form.elements.company.disabled=!visible;if(!visible)form.elements.company.value='';}
 syncCompany();form.elements.support.addEventListener('change',syncCompany);
 function validate(){let first=null;for(const field of form.querySelectorAll('[required]')){const valid=field.validity.valid&&(field.tagName==='SELECT'||field.value.trim().length>0);field.setAttribute('aria-invalid',String(!valid));const error=document.getElementById(field.getAttribute('aria-describedby'));error.textContent=valid?'':text.invalid;if(!valid&&!first)first=field;}if(first)first.focus();return !first;}
 form.addEventListener('input',e=>{const field=e.target;if(field.hasAttribute('aria-invalid')&&field.validity.valid){field.removeAttribute('aria-invalid');const error=document.getElementById(field.getAttribute('aria-describedby'));if(error)error.textContent='';}});
 form.addEventListener('submit',async e=>{
  e.preventDefault();const status=form.querySelector('.form-status');const button=form.querySelector('button[type=submit]');
  if(!validate()){status.textContent=text.invalid;return;}
  if(!form.dataset.endpoint)return;
  if(form.elements._gotcha.value){status.textContent=text.error;return;}
  button.disabled=true;status.textContent=text.sending;form.setAttribute('aria-busy','true');
  try{
   const data=Object.fromEntries(new FormData(form));
   // Support values remain stable across both languages; include a readable label.
   data.support_label=form.elements.support.selectedOptions[0].textContent;
   const controller=new AbortController();const timeout=setTimeout(()=>controller.abort(),15000);
   let response;try{response=await fetch(form.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data),signal:controller.signal});}finally{clearTimeout(timeout);}
   if(!response.ok)throw Error('delivery');const result=await response.json();
   const confirmed=form.dataset.provider==='formspree'?result.ok===true:result.success===true;
   if(!confirmed)throw Error('delivery');status.textContent=text.success;form.reset();syncCompany();
  }catch{status.textContent=text.error;}finally{button.disabled=false;form.removeAttribute('aria-busy');}
 });
}
const selected=new URLSearchParams(location.search).get('support');
if(selected!==null&&/^[0-4]$/.test(selected))document.querySelectorAll('.languages a').forEach(a=>{a.href+='?support='+selected;});
