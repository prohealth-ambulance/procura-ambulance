with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('.hero-photo{height:180px;order:-1;}', '.hero-photo{height:130px;order:-1;}')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Foto reducida mas')
