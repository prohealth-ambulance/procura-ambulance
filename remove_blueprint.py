with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('<span class="hero-bg-mini" aria-hidden="true">Te llevamos.</span>\n    ', '')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Texto removido')
