with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace(
    '.nav-inner{max-width:var(--max);margin:0 auto;width:100%;display:flex;align-items:center;justify-content:space-between}',
    '.nav-inner{max-width:1400px;margin:0 auto;width:100%;display:flex;align-items:center;justify-content:space-between}'
)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Nav width ajustado')
