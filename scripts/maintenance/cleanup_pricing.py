from pathlib import Path
import re

files = [
    'ativa-x.html','ativa-h.html','ativa-av.html',
    'aruz-av.html','aruz-x.html',
    'axia-av.html','axia-g.html','axia-se.html',
    'bezza-av.html','bezza-g.html','bezza-x.html',
    'myvi-av.html','myvi-g.html','myvi-h.html','myvi-x.html',
    'traz-h.html','traz-x.html'
]

pattern = re.compile(r'<!-- Pricing Section -->.*?</section>\s*</main>', re.S)

for fname in files:
    path = Path(fname)
    if not path.exists():
        print(f'MISSING {fname}')
        continue
    text = path.read_text(encoding='utf-8')
    new_text, count = pattern.subn('</main>', text)
    if count > 0:
        path.write_text(new_text, encoding='utf-8')
        print(f'CLEARED {fname}')
    else:
        print(f'NO MATCH {fname}')
