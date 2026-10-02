with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('src="procura-hero-final.jpg"', 'src="procura-hero-final.jpg?v=2"')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Cache bust agregado')
