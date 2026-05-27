"""通用 splice: 在 ch{NN}.md 里找 ## START 标题, 替换到下一个 ## 标题."""
import io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

if len(sys.argv) != 4:
    print('usage: _splice_generic.py <ch_md_path> <start_heading> <new_md_path>')
    print('  start_heading: e.g. "## 11.3"  ## 12.2"  ## 9.6"')
    sys.exit(1)

ch_path = sys.argv[1]
start_h = sys.argv[2]
new_path = sys.argv[3]

with open(ch_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

start = end = None
for i, l in enumerate(lines):
    if l.startswith(start_h):
        start = i
    elif start is not None and l.startswith('## ') and not l.startswith(start_h) and end is None:
        end = i
        break
if end is None and start is not None:
    end = len(lines)

assert start is not None, f'start "{start_h}" not found'
print(f'replacing lines {start+1}..{end}')

with open(new_path, 'r', encoding='utf-8') as f:
    new = f.read().rstrip('\n')

new_lines = lines[:start] + new.split('\n') + [''] + lines[end:]
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print(f'written {ch_path}: {len(new_lines)} lines')
