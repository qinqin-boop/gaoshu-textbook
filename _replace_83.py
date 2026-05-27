"""把 ch8 446 起的所有 8.3 重号 sections 合并替换为新 _new_83.md."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

p = 'D:/github/wechat-decrypt/notes/textbook/chapter08-vectors.md'
new_path = 'D:/github/gaoshu-textbook/_new_83.md'

with open(p, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# 找第一个 ## 8.3 起头, 到下一个非 8.3 ## 之前
start = end = None
for i, l in enumerate(lines):
    if l.startswith('## 8.3'):
        if start is None:
            start = i
    elif start is not None and l.startswith('## ') and not l.startswith('## 8.3'):
        end = i
        break

assert start is not None and end is not None
print(f'replacing lines {start+1}..{end} (all 8.3 sections)')

with open(new_path, 'r', encoding='utf-8') as f:
    new = f.read().rstrip('\n')

new_lines = lines[:start] + new.split('\n') + [''] + lines[end:]
with open(p, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print(f'written: {len(new_lines)} lines')
