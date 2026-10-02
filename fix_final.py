with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. ALS
html = html.replace(
    'Ambulancia privada para citas m\u00e9dicas, di\u00e1lisis, quimioterapia y altas hospitalarias en Puerto Rico',
    'Ambulancia privada ALS para citas m\u00e9dicas, di\u00e1lisis, quimioterapia y altas hospitalarias en Puerto Rico'
)

# 2. Color azul mas limpio (menos violeta)
html = html.replace('--blue:#2563EB;--blue-dk:#1E3A8A;', '--blue:#2563EB;--blue-dk:#1D4ED8;')

# 3. Quitar placeholder de telefono de ejemplo
html = html.replace('placeholder="787-000-0000"', 'placeholder=""')

# 4. Quitar borde raro del pago-wrap (si quedo alguno)
html = html.replace('.pago-wrap{margin-top:2.5rem;padding-top:2rem;}', '.pago-wrap{margin-top:2.5rem;}')

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Cambios finales aplicados')
