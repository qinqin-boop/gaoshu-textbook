"""删除 ch11 旧的 11.6 斯托克斯公式 (旧版), 保留新插入的 11.6 Stokes 公式."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

p = 'D:/github/wechat-decrypt/notes/textbook/chapter11-line-surface-integrals.md'
with open(p, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

old_start = old_end = None
for i, l in enumerate(lines):
    if l.startswith('## 11.6 斯托克斯公式'):
        old_start = i
    elif old_start is not None and l.startswith('## 11.6 Stokes') and old_end is None:
        old_end = i
        break
assert old_start is not None and old_end is not None, f'boundary: {old_start} {old_end}'
print(f'removing old section lines {old_start+1}..{old_end}')
new_lines = lines[:old_start] + lines[old_end:]
with open(p, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print(f'written: {len(new_lines)} lines')
