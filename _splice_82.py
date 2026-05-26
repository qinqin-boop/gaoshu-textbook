"""把 _new_82.md 切片插入 ch8.md, 替换原 8.2 节(行 178-362)."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

src = 'D:/github/wechat-decrypt/notes/textbook/chapter08-vectors.md'
new82_path = 'D:/github/gaoshu-textbook/_new_82.md'

with open(src, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# 找 8.2 起止
start = end = None
for i, l in enumerate(lines):
    if l.startswith('## 8.2'):
        start = i
    elif start is not None and l.startswith('## 8.3') and end is None:
        end = i
        break

assert start is not None and end is not None, f'boundaries: start={start} end={end}'
print(f'replacing lines {start+1}..{end} (8.2 section) with new content')

with open(new82_path, 'r', encoding='utf-8') as f:
    new82 = f.read().rstrip('\n')

new_lines = lines[:start] + new82.split('\n') + [''] + lines[end:]
with open(src, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print(f'written {src}: {len(new_lines)} lines')
