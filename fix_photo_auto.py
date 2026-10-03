with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('.hero-photo{height:160px;order:-1;}', '.hero-photo{height:auto;order:-1;}')
html = html.replace(
    '''    @media(max-width:900px){
      .hero-photo{background:#f0f0f0;}
      .hero-photo img{object-fit:contain!important;}
    }
''',
    '''    @media(max-width:900px){
      .hero-photo img{width:100%;height:auto;object-fit:unset;}
      .hero-content{padding:2rem 1.25rem 2rem;}
    }
'''
)
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Foto ancho completo, altura auto')
