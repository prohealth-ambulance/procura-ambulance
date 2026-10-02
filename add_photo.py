with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. CSS: convertir hero a grid de 2 columnas con foto a la derecha
css_add = '''
    #hero{display:grid!important;grid-template-columns:1fr 1fr;min-height:100svh;flex-direction:unset;}
    .hero-content{padding:3rem 3rem 2rem 2.5rem;}
    .hero-photo{position:relative;overflow:hidden;z-index:1;}
    .hero-photo img{width:100%;height:100%;object-fit:cover;display:block;}
    @media(max-width:900px){
      #hero{grid-template-columns:1fr!important;}
      .hero-photo{height:280px;order:-1;}
    }
'''
html = html.replace('</style>', css_add + '</style>', 1)

# 2. Agregar la foto despues del hero-content, dentro de #hero
old_close = '''    </div>
  </div>
</section>
<section id="servicios">'''
new_close = '''    </div>
  </div>
  <div class="hero-photo">
    <img src="procura-hero-final.jpg" alt="Ambulancia Procura Ambulance en Puerto Rico" />
  </div>
</section>
<section id="servicios">'''
print('found' if old_close in html else 'NOT found')
html = html.replace(old_close, new_close, 1)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Foto integrada')
