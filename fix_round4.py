with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Eyebrow mas corto
html = html.replace(
    'Ambulancia privada ALS para citas m\u00e9dicas, di\u00e1lisis, quimioterapia y altas hospitalarias en Puerto Rico',
    'Ambulancia privada ALS en Puerto Rico'
)
html = html.replace(
    'Private ALS ambulance for medical appointments, dialysis, chemotherapy and hospital discharges in Puerto Rico',
    'Private ALS ambulance in Puerto Rico'
)

# 2. Dialisis ->
cd ~/Downloads/procura-ambulance
cat > fix_select_dash.py << 'PYEOF'
with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('<option value="" disabled selected>\u2014</option>', '<option value="" disabled selected>Selecciona una opci\u00f3n</option>')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Select dash removido')
