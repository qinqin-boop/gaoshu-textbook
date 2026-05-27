"""清理 ch8 中重复/错位的 8.3 标号 section: 删除 misnamed '## 8.3 平面及其方程' 整段."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

p = 'D:/github/wechat-decrypt/notes/textbook/chapter08-vectors.md'
with open(p, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

old_start = old_end = None
for i, l in enumerate(lines):
    if l.startswith('## 8.3 平面及其方程'):
        old_start = i
    elif old_start is not None and l.startswith('## ') and not l.startswith('## 8.3 平面') and old_end is None:
        old_end = i
        break

if old_start is None:
    print('no misnamed section to remove')
else:
    print(f'removing misnamed 8.3 平面 section lines {old_start+1}..{old_end}')
    new_lines = lines[:old_start] + lines[old_end:]
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    print(f'written: {len(new_lines)} lines')
