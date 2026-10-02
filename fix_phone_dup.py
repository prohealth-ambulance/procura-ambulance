with open('index.html','r',encoding='utf-8') as f: html=f.read()

# Ocultar el boton flotante de telefono en desktop, solo mostrar WhatsApp
css_add = '''
    @media(min-width:901px){ .fl-tel { display: none; } }
'''
html = html.replace('</style>', css_add + '</style>', 1)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Telefono flotante oculto en desktop')
