with open('index.html','r',encoding='utf-8') as f: html=f.read()
count = html.count('<option value="" disabled selected>\u2014</option>')
print(f'Guiones encontrados: {count}')
html = html.replace(
    '<option value="" disabled selected>\u2014</option>',
    '<option value="" disabled selected>Seleccionar</option>'
)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Guiones reemplazados')
