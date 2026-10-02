with open('index.html','r',encoding='utf-8') as f: html=f.read()

css_add = '''
    .hero-content{position:relative;overflow:hidden;}
    .hero-bg-mini{position:absolute;left:-10px;bottom:-10px;font-size:3.2rem;font-weight:900;letter-spacing:-.04em;line-height:.9;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.14);pointer-events:none;user-select:none;z-index:0;animation:float 6s ease-in-out infinite;white-space:nowrap;}
    .svc-bg-mini{position:absolute;right:20px;top:20px;font-size:5rem;font-weight:900;letter-spacing:-.04em;line-height:.85;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.08);pointer-events:none;user-select:none;z-index:0;white-space:nowrap;}
    #servicios .wrap{position:relative;overflow:hidden;}
'''
html = html.replace('</style>', css_add + '</style>', 1)

# Agregar mini texto flotante en hero-content, despues del div de abrir
html = html.replace(
    '<div class="hero-content">\n    <p class="h-eyebrow rv es">',
    '<div class="hero-content">\n    <span class="hero-bg-mini" aria-hidden="true">Te llevamos.</span>\n    <p class="h-eyebrow rv es">'
)

# Agregar texto decorativo en la seccion de servicios
html = html.replace(
    '<div class="wrap">\n    <div class="two-col">',
    '<div class="wrap">\n      <span class="svc-bg-mini" aria-hidden="true">Servicios</span>\n    <div class="two-col">'
)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Blueprint text agregado')
