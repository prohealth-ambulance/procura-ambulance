with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace(
    '<h3 class="es">Di\u00e1lisis</h3><h3 class="en">Dialysis</h3>',
    '<h3 class="es">Transporte para di\u00e1lisis</h3><h3 class="en">Dialysis transport</h3>'
)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Dialisis corregido definitivo')
