import re
with open('index.html','r',encoding='utf-8') as f: html=f.read()
html = re.sub(r'<div class="svc-n">0[1-6]</div>', '', html)
html = html.replace('.fl-btn{display:flex;align-items:center;gap:8px;font-family:var(--font);font-size:13px;font-weight:600;text-decoration:none;padding:11px 18px;border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,.15);transition:transform .12s}', '.fl-btn{display:flex;align-items:center;justify-content:center;gap:8px;font-family:var(--font);font-size:13px;font-weight:600;text-decoration:none;padding:13px;width:48px;height:48px;border-radius:50%;box-shadow:0 4px 16px rgba(0,0,0,.18);transition:transform .12s}')
html = html.replace('.fl-btn span{display:none}' + chr(10), '')
html = html.replace('.fl-btn:hover{transform:translateY(-1px)}', '.fl-btn span{display:none}' + chr(10) + '.fl-btn:hover{transform:scale(1.08)}')
with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('Diseno ajustado')
