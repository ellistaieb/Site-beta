const text=JSON.parse(document.querySelector('#ui-text').textContent);
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
function closeMenu(){toggle.setAttribute('aria-expanded','false');toggle.textContent=text.menu;nav.classList.remove('open');}
toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?text.close:text.menu;nav.classList.toggle('open',open);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true'){closeMenu();toggle.focus();}});
nav.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
window.addEventListener('scroll',()=>document.querySelector('header').classList.toggle('scrolled',window.scrollY>20),{passive:true});
const form=document.querySelector('form');
if(form){
 const choice=new URLSearchParams(location.search).get('support');if(choice!==null&&/^[0-4]$/.test(choice))form.elements.support.value=choice;
 form.addEventListener('submit',async e=>{
 e.preventDefault();const status=form.querySelector('.form-status');const button=form.querySelector('button');
 if(!form.reportValidity()){status.textContent=text.invalid;return;} if(!form.dataset.endpoint)return;
 button.disabled=true;status.textContent=text.sending;form.setAttribute('aria-busy','true');
 try{const response=await fetch(form.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(form))),signal:AbortSignal.timeout(15000)});if(!response.ok)throw Error('delivery');const result=await response.json();if(result.success!==true)throw Error('delivery');status.textContent=text.success;form.reset();}catch{status.textContent=text.error;}finally{button.disabled=false;form.removeAttribute('aria-busy');}
 });
}
const selected=new URLSearchParams(location.search).get('support');
if(selected!==null&&/^[0-4]$/.test(selected))document.querySelectorAll('.languages a').forEach(a=>{a.href+='?support='+selected;});
