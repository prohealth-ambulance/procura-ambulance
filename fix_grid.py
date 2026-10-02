with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = html.replace('.svc-row{display:grid;grid-template-columns:24px 1fr;gap:1.5rem;align-items:start;padding:1.625rem 1rem;margin:0 -1rem;border-bottom:1px solid var(--rule);border-radius:10px;transition:background .15s}', '.svc-row{display:block;padding:1.625rem 1rem;margin:0 -1rem;border-bottom:1px solid var(--rule);border-radius:10px;transition:background .15s}')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Grid corregido')
