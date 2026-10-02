with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('placeholder="\u2014"', 'placeholder=""')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Guiones removidos')
