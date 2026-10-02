with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Reducir texto de fondo "Te llevamos"
html = html.replace(
    '.hero-bg-text{position:absolute;right:0;bottom:10%;font-size:clamp(80px,15vw,200px);font-weight:900;letter-spacing:-.08em;line-height:.85;color:transparent;-webkit-text-stroke:1.5px rgba(37,99,235,.45);pointer-events:none;user-select:none;text-align:right;z-index:0;padding-right:3%;white-space:nowrap;animation:float 6s ease-in-out infinite}',
    '.hero-bg-text{position:absolute;right:0;bottom:2%;font-size:clamp(50px,8vw,110px);font-weight:900;letter-spacing:-.08em;line-height:.85;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.18);pointer-events:none;user-select:none;text-align:right;z-index:0;padding-right:3%;white-space:nowrap;animation:float 6s ease-in-out infinite}'
)

# 2. Hero: eyebrow mas claro, trato consistente con tu
html = html.replace(
    '<p class="h-eyebrow rv es">Ambulancia Privada &middot; Puerto Rico</p>',
    '<p class="h-eyebrow rv es">Ambulancia privada para citas m\u00e9dicas, di\u00e1lisis, quimioterapia y altas hospitalarias en Puerto Rico</p>'
)
html = html.replace(
    '<p class="h-eyebrow rv en">Private Ambulance &middot; Puerto Rico</p>',
    '<p class="h-eyebrow rv en">Private ambulance for medical appointments, dialysis, chemotherapy and hospital discharges in Puerto Rico</p>'
)
html = html.replace(
    '<p class="h-desc rv d2 es">Coordinamos el traslado m\u00e9dico de principio a fin. Puntualidad, seguridad y param\u00e9dicos certificados \u2014 para que usted no tenga que preocuparse.</p>',
    '<p class="h-desc rv d2 es">Coordinamos tu traslado m\u00e9dico de principio a fin. Puntualidad, seguridad y param\u00e9dicos certificados, en toda Puerto Rico \u2014 para que t\u00fa y tu familia tengan tranquilidad.</p>'
)
html = html.replace(
    '<p class="h-desc rv d2 en">We coordinate medical transport from start to finish. Punctuality, safety and certified paramedics \u2014 so you don\'t have to worry.</p>',
    '<p class="h-desc rv d2 en">We coordinate your medical transport from start to finish. Punctuality, safety and certified paramedics, across Puerto Rico \u2014 so you and your family have peace of mind.</p>'
)

# 3. Solicitar un traslado
html = html.replace(
    '<span class="es">Solicitar por escrito &rarr;</span>',
    '<span class="es">Solicitar un traslado &rarr;</span>'
)
html = html.replace(
    '<span class="en">Request in writing &rarr;</span>',
    '<span class="en">Request a transport &rarr;</span>'
)

# 4. Dialisis sin data-es/en -> separar
html = html.replace(
    '<h3>Di\u00e1lisis</h3>',
    '<h3 class="es">Di\u00e1lisis</h3><h3 class="en">Dialysis</h3>'
)

# 5. Medicare Parte B
html = html.replace(
    '<div class="pl-row">Medicare Parte B<div class="pl-ck">',
    '<div class="pl-row"><span class="es">Medicare Parte B</span><span class="en">Medicare Part B</span><div class="pl-ck">'
)

# 6. Formulario: separar selects por idioma
old_select = '<select class="fi" id="svc" name="servicio" required>\n            <option value="" disabled selected>\u2014</option>\n            <option value="cita">Cita m\u00e9dica / Medical appointment</option>\n            <option value="dialisis">Di\u00e1lisis / Dialysis</option>\n            <option value="quimio">Quimioterapia / Chemotherapy</option>\n            <option value="alta">Alta hospitalaria / Hospital discharge</option>\n            <option value="traslado">Traslado entre facilidades / Facility transfer</option>\n            <option value="emergencia">Emergencia / Emergency</option>\n            <option value="otro">Otro / Other</option>\n          </select>'
new_select = '''<select class="fi svc-select-es" id="svc" name="servicio" required>
            <option value="" disabled selected>\u2014</option>
            <option value="cita">Cita m\u00e9dica</option>
            <option value="dialisis">Di\u00e1lisis</option>
            <option value="quimio">Quimioterapia</option>
            <option value="alta">Alta hospitalaria</option>
            <option value="traslado">Traslado entre facilidades</option>
            <option value="emergencia">Emergencia</option>
            <option value="otro">Otro</option>
          </select>
          <select class="fi svc-select-en" id="svc-en" name="service_en" style="display:none">
            <option value="" disabled selected>\u2014</option>
            <option value="appointment">Medical appointment</option>
            <option value="dialysis">Dialysis</option>
            <option value="chemo">Chemotherapy</option>
            <option value="discharge">Hospital discharge</option>
            <option value="transfer">Facility transfer</option>
            <option value="emergency">Emergency</option>
            <option value="other">Other</option>
          </select>'''
print('select found' if old_select in html else 'select NOT found')
html = html.replace(old_select, new_select)

# 7. reCAPTCHA bilingue
html = html.replace(
    '<p class="recaptcha-note">Protegido por reCAPTCHA &middot; <a href="https://policies.google.com/privacy" target="_blank">Privacidad</a> &middot; <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos</a></p>',
    '<p class="recaptcha-note es">Protegido por reCAPTCHA &middot; <a href="https://policies.google.com/privacy" target="_blank">Privacidad</a> &middot; <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos</a></p>\n      <p class="recaptcha-note en" style="display:none">Protected by reCAPTCHA &middot; <a href="https://policies.google.com/privacy" target="_blank">Privacy</a> &middot; <a href="https://policies.google.com/terms" target="_blank">Terms</a></p>'
)

# 8. Footer privacidad bilingue
html = html.replace(
    '\u00a9 2026 Procura Ambulance LLC \u00b7 San Juan, Puerto Rico \u00b7 <a href="/privacy.html" style="color:inherit;opacity:.5;text-decoration:none">Privacidad</a>',
    '<span class="es">\u00a9 2026 Procura Ambulance LLC \u00b7 San Juan, Puerto Rico \u00b7 <a href="/privacy.html" style="color:inherit;opacity:.5;text-decoration:none">Privacidad</a></span><span class="en">\u00a9 2026 Procura Ambulance LLC \u00b7 San Juan, Puerto Rico \u00b7 <a href="/privacy.html" style="color:inherit;opacity:.5;text-decoration:none">Privacy</a></span>'
)

# 9. Titulo de pestana dinamico + persistencia idioma
old_js_toggle = '''let en=false;
document.getElementById('langBtn').addEventListener('click',function(){
  en=!en;
  document.body.className=en?'lang-en':'lang-es';
  this.textContent=en?'ES':'EN';
  document.documentElement.lang=en?'en':'es';
});'''
new_js_toggle = '''const titles={es:'Procura Ambulance | Transporte M\\u00e9dico Privado en Puerto Rico',en:'Procura Ambulance | Private Medical Transport in Puerto Rico'};
function applyLang(lang,skipSave){
  document.body.className='lang-'+lang;
  document.getElementById('langBtn').textContent=lang==='en'?'ES':'EN';
  document.documentElement.lang=lang;
  document.title=titles[lang];
  const se=document.querySelector('.svc-select-es'),sn=document.querySelector('.svc-select-en');
  if(se&&sn){se.style.display=lang==='es'?'block':'none';sn.style.display=lang==='en'?'block':'none';se.required=(lang==='es');sn.required=false;se.name='servicio';sn.name=lang==='en'?'servicio':'service_en_unused';}
  document.querySelectorAll('.recaptcha-note').forEach(el=>{el.style.display=el.classList.contains(lang)?'block':'none';});
  if(!skipSave){try{localStorage.setItem('pc_lang',lang);}catch(e){}}
}
document.getElementById('langBtn').addEventListener('click',function(){
  const cur=document.body.classList.contains('lang-en')?'en':'es';
  applyLang(cur==='en'?'es':'en');
});
try{const saved=localStorage.getItem('pc_lang');if(saved==='en'){applyLang('en',true);}}catch(e){}'''
print('js found' if old_js_toggle in html else 'js NOT found')
html = html.replace(old_js_toggle, new_js_toggle)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('DONE')
