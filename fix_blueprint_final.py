with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace(
    '.hero-bg-mini{position:absolute;left:50%;bottom:-10px;transform:translateX(-50%);font-size:3.2rem;font-weight:900;letter-spacing:-.04em;line-height:.9;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.14);pointer-events:none;user-select:none;z-index:0;animation:float 6s ease-in-out infinite;white-space:nowrap;}',
    '.hero-bg-mini{position:absolute;right:-20px;bottom:40px;font-size:2.4rem;font-weight:900;letter-spacing:-.04em;line-height:.9;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.16);pointer-events:none;user-select:none;z-index:0;animation:float 6s ease-in-out infinite;white-space:nowrap;}'
)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Posicion final junto al enlace')
