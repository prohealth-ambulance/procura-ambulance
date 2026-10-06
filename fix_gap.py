h=open('index.html',encoding='utf-8').read()
h=h.replace('      body{padding-bottom:60px}','      body{padding-bottom:0}\n      footer{padding-bottom:72px}')
open('index.html','w',encoding='utf-8').write(h)
print('ok')
