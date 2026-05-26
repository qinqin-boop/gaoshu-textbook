"""把 _new_96.md 切片插入 ch9.md, 替换原 9.6 节."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

src = 'D:/github/wechat-decrypt/notes/textbook/chapter09-multivariate.md'
new_path = 'D:/github/gaoshu-textbook/_new_96.md'

with open(src, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

start = end = None
for i, l in enumerate(lines):
    if l.startswith('## 9.6'):
        start = i
    elif start is not None and l.startswith('## 9.7') and end is None:
        end = i
        break

assert start is not None and end is not None, f'9.6 boundary: start={start} end={end}'
print(f'replacing lines {start+1}..{end} (9.6 section)')

with open(new_path, 'r', encoding='utf-8') as f:
    new = f.read().rstrip('\n')

new_lines = lines[:start] + new.split('\n') + [''] + lines[end:]
with open(src, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print(f'written {src}: {len(new_lines)} lines')
