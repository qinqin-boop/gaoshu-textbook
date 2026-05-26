"""把 latex_inject.py 误造的空 \\sqrt{} 修回去."""
import io, sys, re, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC_DIR = 'D:/github/wechat-decrypt/notes/textbook'

for fn in sorted(os.listdir(SRC_DIR)):
    if not (fn.startswith('chapter') and fn.endswith('.md')):
        continue
    path = os.path.join(SRC_DIR, fn)
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    # $\sqrt{}$digit  -> $\sqrt{digit}$
    new = re.sub(r'\$\\sqrt\{\}\$(\d+)', r'$\\sqrt{\1}$', s)
    # any remaining $\sqrt{}$ -> plain √ (keep hack)
    new = new.replace(r'$\sqrt{}$', '√')
    if new != s:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'fixed {fn}')
    else:
        print(f'--- {fn}')
