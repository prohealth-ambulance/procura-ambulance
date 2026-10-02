with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Servicios mas claros
html = html.replace('<h3>Di\u00e1lisis</h3><h3 class="en">Dialysis</h3>', '<h3 class="es">Transporte para di\u00e1lisis</h3><h3 class="en">Dialysis transport</h3>')
html = html.replace('<h3 class="es">Quimioterapia</h3><h3 class="en">Chemotherapy</h3>', '<h3 class="es">Transporte para quimioterapia</h3><h3 class="en">Chemotherapy transport</h3>')

# 2. Gramatica: toda -> todo
html = html.replace('en toda Puerto Rico', 'en todo Puerto Rico')
html = html.replace('across Puerto Rico', 'across Puerto Rico')

# 3. Trato consistente: tu en vez de usted/Le/servirle
html = html.replace('<h2 class="con-h rv es">Estamos para <i>servirle.</i></h2>', '<h2 class="con-h rv es">Estamos para <i>ayudarte.</i></h2>')
html = html.replace('<p class="f-sub es">Le contactamos a la brevedad.</p>', '<p class="f-sub es">Te contactamos a la brevedad.</p>')
html = html.replace('<span class="es">Mensaje enviado. Le contactaremos a la brevedad.</span>', '<span class="es">Mensaje enviado. Te contactaremos a la brevedad.</span>')
html = html.replace('<p class="pl-p es">Aceptamos la mayor\u00eda de los planes m\u00e9dicos de Puerto Rico. Llame para verificar su cobertura.</p>', '<p class="pl-p es">Aceptamos la mayor\u00eda de los planes m\u00e9dicos de Puerto Rico. Llama para verificar tu cobertura.</p>')

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Copy round 3 aplicado')
