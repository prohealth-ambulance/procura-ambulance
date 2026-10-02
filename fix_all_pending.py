with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Capitalizar Transporte para Dialisis / Quimioterapia (es)
html = html.replace(
    '<h3 class="es">Transporte para di\u00e1lisis</h3><h3 class="en">Dialysis transport</h3>',
    '<h3 class="es">Transporte para Di\u00e1lisis</h3><h3 class="en">Dialysis Transport</h3>'
)
html = html.replace(
    '<h3 class="es">Transporte para quimioterapia</h3><h3 class="en">Chemotherapy transport</h3>',
    '<h3 class="es">Transporte para Quimioterapia</h3><h3 class="en">Chemotherapy Transport</h3>'
)

# 2. Eyebrow en ingles: agregar ALS
html = html.replace(
    '<p class="h-eyebrow rv en">Private ambulance for medical appointments, dialysis, chemotherapy and hospital discharges in Puerto Rico</p>',
    '<p class="h-eyebrow rv en">Private ALS ambulance for medical appointments, dialysis, chemotherapy and hospital discharges in Puerto Rico</p>'
)

# 3. reCAPTCHA note bilingue (separar en es/en)
html = html.replace(
    '<p class="recaptcha-note">Protegido por reCAPTCHA \u00b7 <a href="https://policies.google.com/privacy" target="_blank">Privacidad</a> \u00b7 <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos</a></p>',
    '<p class="recaptcha-note es">Protegido por reCAPTCHA \u00b7 <a href="https://policies.google.com/privacy" target="_blank">Privacidad</a> \u00b7 <a href="https://policies.google.com/terms" target="_blank">T\u00e9rminos</a></p>\n        <p class="recaptcha-note en" style="display:none">Protected by reCAPTCHA \u00b7 <a href="https://policies.google.com/privacy" target="_blank">Privacy</a> \u00b7 <a href="https://policies.google.com/terms" target="_blank">Terms</a></p>'
)

# 4. WhatsApp aria-label bilingue (usar atributo dinamico simple: dejar en espanol por defecto, JS lo cambia)
html = html.replace(
    'aria-label="Contactar por WhatsApp a Procura Ambulance"',
    'aria-label="Contactar por WhatsApp a Procura Ambulance" id="wa-float-btn"'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Todos los pendientes corregidos')
