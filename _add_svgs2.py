"""第二批 SVG: 加 ch8 球面/法平面/旋转面 + ch9 多元图像/等高线 + ch10 球坐标 3D + ch11 散度/旋度 + ch12 比较判别."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 球面 + 旋转面对照
    ('chapter08-vectors.md', '### 8.3.2 旋转曲面', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 60 120 L 100 60 L 60 60 Z" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="40" y="155" font-size="11" fill="#1a365d">原曲线 (yOz)</text>
  <line x1="120" y1="90" x2="200" y2="90" stroke="#888" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="135" y="80" font-size="11" fill="#888">绕 z 轴旋转</text>
  <ellipse cx="280" cy="90" rx="60" ry="40" fill="#fef6e4" stroke="#c9a227" stroke-width="1.8"/>
  <ellipse cx="280" cy="90" rx="60" ry="10" fill="none" stroke="#8b6f1c" stroke-width="1" stroke-dasharray="2 2" opacity="0.7"/>
  <line x1="280" y1="20" x2="280" y2="160" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="285" y="20" font-size="11" fill="#888">z</text>
  <text x="260" y="155" font-size="11" fill="#8b6f1c">圆锥旋转面</text>
</svg>
<figcaption>图 8.3.1 旋转面生成:把 $yOz$ 平面上的曲线绕 $z$ 轴旋转一周。三角形→圆锥,抛物线→碟形天线。</figcaption>
::endsvg

'''),

    # ch9 9.1 等高线
    ('chapter09-multivariate.md', '### 9.1.4 等高线与图像', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="180" cy="100" rx="140" ry="75" fill="none" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="180" cy="100" rx="100" ry="55" fill="none" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="180" cy="100" rx="60" ry="33" fill="none" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="180" cy="100" rx="25" ry="14" fill="#c9b97a" fill-opacity="0.4" stroke="#1a365d" stroke-width="1"/>
  <text x="170" y="105" font-size="11" fill="#1a365d">峰</text>
  <text x="324" y="105" font-size="11" fill="#888">f=1</text>
  <text x="284" y="105" font-size="11" fill="#888">f=2</text>
  <text x="244" y="105" font-size="11" fill="#888">f=3</text>
  <text x="195" y="105" font-size="11" fill="#888">f=4</text>
  <text x="40" y="180" font-size="11" fill="#666">等高线密 = 函数变化快 (梯度大); 稀 = 变化慢</text>
</svg>
<figcaption>图 9.1.1 二元函数等高线:同心椭圆从外到内函数值递增。等高线密集处梯度大,稀疏处梯度小。</figcaption>
::endsvg

'''),

    # ch10 10.3 球坐标 (ρ, φ, θ)
    ('chapter10-multiple-integrals.md', '### 10.3.3 球坐标(关键)', r'''
::svg
<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="sp1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <line x1="160" y1="220" x2="160" y2="20" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="220" x2="60" y2="190" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="220" x2="300" y2="200" stroke="#888" stroke-width="1"/>
  <text x="152" y="15" font-size="12" fill="#888">z</text>
  <text x="50" y="200" font-size="12" fill="#888">x</text>
  <text x="305" y="210" font-size="12" fill="#888">y</text>
  <ellipse cx="160" cy="220" rx="60" ry="20" fill="none" stroke="#666" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="160" y1="220" x2="230" y2="80" stroke="#1a365d" stroke-width="2.5" marker-end="url(#sp1)"/>
  <circle cx="230" cy="80" r="3" fill="#1a365d"/>
  <text x="237" y="78" font-size="13" fill="#1a365d" font-weight="bold">P</text>
  <text x="185" y="155" font-size="13" fill="#1a365d" font-style="italic">ρ</text>
  <path d="M 160 130 A 50 50 0 0 1 200 145" fill="none" stroke="#c2410c" stroke-width="1.4"/>
  <text x="175" y="148" font-size="13" fill="#c2410c">φ</text>
  <line x1="160" y1="220" x2="200" y2="208" stroke="#1a365d" stroke-width="1" stroke-dasharray="3 2"/>
  <line x1="200" y1="208" x2="230" y2="80" stroke="#1a365d" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 180 220 A 25 25 0 0 1 195 213" fill="none" stroke="#2d6e2d" stroke-width="1.4"/>
  <text x="183" y="215" font-size="13" fill="#2d6e2d">θ</text>
  <text x="30" y="40" font-size="11" fill="#444">dV = ρ²sinφ dρ dφ dθ</text>
</svg>
<figcaption>图 10.3.1 球坐标 $(\rho,\varphi,\theta)$:$\rho$ 到原点距离,$\varphi$ 与 $+z$ 轴夹角,$\theta$ 方位角。体积元 $\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$。</figcaption>
::endsvg

'''),

    # ch11 11.6 旋度小风车
    ('chapter11-line-surface-integrals.md', '### 11.6.1 旋度与方向匹配', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="cw1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="cw2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="180" cy="100" r="60" fill="none" stroke="#1a365d" stroke-width="1.5"/>
  <line x1="180" y1="100" x2="180" y2="20" stroke="#c2410c" stroke-width="2.5" marker-end="url(#cw2)"/>
  <text x="185" y="25" font-size="13" fill="#c2410c" font-style="italic" font-weight="bold">∇×F</text>
  <path d="M 200 65 Q 215 80 200 95" fill="none" stroke="#1a365d" stroke-width="2" marker-end="url(#cw1)"/>
  <path d="M 200 95 Q 215 110 200 125" fill="none" stroke="#1a365d" stroke-width="2" marker-end="url(#cw1)"/>
  <text x="220" y="105" font-size="11" fill="#1a365d">流场绕轴转</text>
  <text x="42" y="170" font-size="11" fill="#666">点 P 处放小风车: 旋度方向 = 轴向, 大小 = 转速</text>
</svg>
<figcaption>图 11.6.1 旋度 = 小风车几何:风车轴沿 $\nabla\times\vec{F}$,转速 $=|\nabla\times\vec{F}|$。</figcaption>
::endsvg

'''),

    # ch12 12.2 p-级数发散临界
    ('chapter12-infinite-series.md', '### 12.2.1 比较判别法', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="100" x2="320" y2="100" stroke="#888" stroke-width="1"/>
  <line x1="40" y1="100" x2="34" y2="106" stroke="#888"/>
  <line x1="320" y1="100" x2="312" y2="96" stroke="#888"/>
  <line x1="320" y1="100" x2="312" y2="104" stroke="#888"/>
  <line x1="180" y1="93" x2="180" y2="107" stroke="#1a365d" stroke-width="2"/>
  <text x="172" y="125" font-size="13" fill="#1a365d" font-weight="bold">p=1</text>
  <text x="155" y="142" font-size="11" fill="#1a365d">调和发散</text>
  <rect x="40" y="92" width="140" height="16" fill="#fde2e2" stroke="#b91c1c" stroke-width="1" opacity="0.6"/>
  <text x="80" y="80" font-size="11" fill="#b91c1c">发散区 (p ≤ 1)</text>
  <rect x="180" y="92" width="140" height="16" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1" opacity="0.6"/>
  <text x="220" y="80" font-size="11" fill="#2d6e2d">收敛区 (p > 1)</text>
  <text x="38" y="160" font-size="11" fill="#888">∑ 1/n^p:</text>
  <text x="120" y="160" font-size="11" fill="#888">p=1/2 发散</text>
  <text x="225" y="160" font-size="11" fill="#888">p=2 收敛到 π²/6</text>
</svg>
<figcaption>图 12.2.1 p-级数 $\sum 1/n^p$ 收敛性:$p=1$ 是临界点(调和级数发散),$p>1$ 收敛、$p\le 1$ 发散。</figcaption>
::endsvg

'''),
]

count_added = 0
for fname, anchor, svg_block in INJECTIONS:
    path = f'D:/github/wechat-decrypt/notes/textbook/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if anchor not in content:
        print(f'SKIP {fname}: "{anchor[:40]}" not found')
        continue
    idx = content.index(anchor)
    line_end = content.index('\n', idx) + 1
    while line_end < len(content) and content[line_end] == '\n':
        line_end += 1
    new_content = content[:line_end] + svg_block.lstrip('\n') + content[line_end:]
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count_added += 1
        print(f'OK  {fname}: injected after "{anchor[:40]}"')

print(f'\n{count_added}/{len(INJECTIONS)} SVG injected')
