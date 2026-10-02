with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('procura-hero-final.jpg?v=2', 'procura-hero-v4.jpg')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Foto actualizada a v4')
