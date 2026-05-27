"""删除 ch12 旧的 '## 12.5 泰勒级数' (中文), 保留新写的 '## 12.5 Taylor 级数'."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

p = 'D:/github/wechat-decrypt/notes/textbook/chapter12-infinite-series.md'
with open(p, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

old_start = old_end = None
for i, l in enumerate(lines):
    if l.startswith('## 12.5 泰勒级数'):
        old_start = i
    elif old_start is not None and l.startswith('## ') and not l.startswith('## 12.5 泰勒') and old_end is None:
        old_end = i
        break

assert old_start is not None and old_end is not None
print(f'removing old "12.5 泰勒级数" lines {old_start+1}..{old_end}')
new_lines = lines[:old_start] + lines[old_end:]
with open(p, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print(f'written: {len(new_lines)} lines')
