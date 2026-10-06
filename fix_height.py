h=open('index.html',encoding='utf-8').read()
h=h.replace('min-height:100svh;', 'min-height:auto;')
open('index.html','w',encoding='utf-8').write(h)
print('procura ok')
