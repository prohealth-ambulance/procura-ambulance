with open('index.html','r',encoding='utf-8') as f: html=f.read()

css_add = '''
    @media(max-width:900px){
      .hero-photo{background:#f0f0f0;}
      .hero-photo img{object-fit:contain!important;}
    }
'''
html = html.replace('</style>', css_add + '</style>', 1)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Foto completa en movil - contain')
