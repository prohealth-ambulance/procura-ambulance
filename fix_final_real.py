with open('index.html','r',encoding='utf-8') as f: html=f.read()
old = '.hero-bg-mini{position:absolute;left:-10px;bottom:-10px;font-size:3.2rem;font-weight:900;letter-spacing:-.04em;line-height:.9;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.14);pointer-events:none;user-select:none;z-index:0;animation:float 6s ease-in-out infinite;white-space:nowrap;}'
new = '.hero-bg-mini{position:absolute;right:30px;bottom:30px;font-size:2rem;font-weight:900;letter-spacing:-.04em;line-height:.9;color:transparent;-webkit-text-stroke:1px rgba(37,99,235,.18);pointer-events:none;user-select:none;z-index:0;animation:float 6s ease-in-out infinite;white-space:nowrap;}'
print('found' if old in html else 'NOT FOUND')
html = html.replace(old, new)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('done')
