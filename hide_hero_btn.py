h=open('index.html',encoding='utf-8').read()
css='''
    @media(max-width:900px){ .h-btns .btn-main{display:none!important} }
'''
h=h.replace('</style>',css+'</style>',1)
open('index.html','w',encoding='utf-8').write(h)
print('ok')
