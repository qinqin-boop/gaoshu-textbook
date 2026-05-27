"""一次性给 5 个 chapter html 加文末 footer-nav."""
from pathlib import Path

ROOT = Path(__file__).parent

CHAPTERS = [
    ('chapter08-vectors.html', '第八章 向量', None, 'chapter09-multivariate.html', '第九章 多元函数'),
    ('chapter09-multivariate.html', '第九章 多元函数', 'chapter08-vectors.html', 'chapter10-multiple-integrals.html', '第十章 重积分'),
    ('chapter10-multiple-integrals.html', '第十章 重积分', 'chapter09-multivariate.html', 'chapter11-line-surface-integrals.html', '第十一章 曲线曲面积分'),
    ('chapter11-line-surface-integrals.html', '第十一章 曲线曲面积分', 'chapter10-multiple-integrals.html', 'chapter12-infinite-series.html', '第十二章 无穷级数'),
    ('chapter12-infinite-series.html', '第十二章 无穷级数', 'chapter11-line-surface-integrals.html', None, None),
]


def make_nav(prev_file, prev_label, next_file, next_label):
    prev_html = (
        f'<a href="./{prev_file}" style="flex:1;text-align:center;padding:10px;color:#1e40af;text-decoration:none;background:white;border-radius:6px;border:1px solid #cbd5e1;">← {prev_label}</a>'
        if prev_file else '<span style="flex:1;text-align:center;padding:10px;color:#cbd5e1;background:#f8fafc;border-radius:6px;">← 已是第一章</span>'
    )
    next_html = (
        f'<a href="./{next_file}" style="flex:1;text-align:center;padding:10px;color:#1e40af;text-decoration:none;background:white;border-radius:6px;border:1px solid #cbd5e1;">{next_label} →</a>'
        if next_file else '<span style="flex:1;text-align:center;padding:10px;color:#cbd5e1;background:#f8fafc;border-radius:6px;">已是最后一章 →</span>'
    )
    return f'''
<div class="chapter-footer-nav" style="display:flex;gap:10px;margin:30px 0 10px;padding:14px;background:#dbeafe;border-radius:10px;flex-wrap:wrap;">
  {prev_html}
  <a href="./index.html" style="flex:1;text-align:center;padding:10px;color:#1e40af;text-decoration:none;background:white;border-radius:6px;border:1px solid #cbd5e1;font-weight:600;">🏠 返回目录</a>
  <a href="./formula-cheatsheet.html" style="flex:1;text-align:center;padding:10px;color:#7c3aed;text-decoration:none;background:white;border-radius:6px;border:1px solid #c4b5fd;font-weight:600;">📐 公式速查</a>
  {next_html}
</div>
'''


for fname, _label, prev_file, next_file, next_label in CHAPTERS:
    fpath = ROOT / fname
    if not fpath.exists():
        print(f'  SKIP {fname} (not found)')
        continue
    prev_label = next((c[1] for c in CHAPTERS if c[0] == prev_file), None)
    html = fpath.read_text(encoding='utf-8')
    if 'chapter-footer-nav' in html:
        print(f'  SKIP {fname} (already has nav)')
        continue
    nav = make_nav(prev_file, prev_label, next_file, next_label)
    # insert before </main>
    new = html.replace('</main>', nav + '</main>', 1)
    if new == html:
        print(f'  WARN {fname}: no </main> found, appending before </body>')
        new = html.replace('</body>', nav + '</body>', 1)
    fpath.write_text(new, encoding='utf-8')
    print(f'  + {fname} nav added')

print('\nDONE')
