with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Quitar el bg-mini del hero (ya no va ahi)
html = html.replace(
    '<span class="hero-bg-mini" aria-hidden="true">Te llevamos.</span>\n    ',
    ''
)

# 2. Agregar CSS para el texto flotante en la columna izquierda de servicios (debajo del titulo)
css_add = '''
    .two-col{position:relative;}
    .svc-left-bg{position:absolute;left:0;bottom:-40px;font-size:3.2rem;font-weight:900;letter-spacing:-.04em;line-height:.9;color:transparent;-webkit-text-stroke:1.2px rgba(37,99,235,.16);pointer-events:none;user-select:none;z-index:0;animation:float 6s ease-in-out infinite;}
'''
html = html.replace('</style>', css_add + '</style>', 1)

# 3. Agregar el span bilingue dentro de la primera columna de two-col (despues del h2 sec-h)
old = '<h2 class="sec-h rv en">What we do <i>well.</i></h2>\n      </div>'
new = '<h2 class="sec-h rv en">What we do <i>well.</i></h2>\n        <span class="svc-left-bg es" aria-hidden="true">Te<br>llevamos.</span>\n        <span class="svc-left-bg en" aria-hidden="true" style="display:none">We take<br>you there.</span>\n      </div>'
print('found' if old in html else 'NOT found')
html = html.replace(old, new)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Texto movido a espacio vacio de servicios')
