h=open('index.html',encoding='utf-8').read()
h=h.replace('.svc-bg-mini{position:absolute;right:20px;top:20px;font-size:5rem;','.svc-bg-mini{position:absolute;right:20px;top:20px;font-size:4rem;')
h=h.replace('.svc-left-bg{position:absolute;left:0;bottom:-40px;font-size:3.2rem;','.svc-left-bg{position:absolute;left:0;bottom:-40px;font-size:4rem;')
css='''
    @media(max-width:900px){ .svc-bg-mini,.svc-left-bg{font-size:2.4rem} }
'''
h=h.replace('</style>',css+'</style>',1)
open('index.html','w',encoding='utf-8').write(h)
print('ok')
