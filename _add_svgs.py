"""批量给关键章节加 SVG 图: 在指定 marker 后面注入 SVG 块."""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# SVG 注入项: (file, anchor_pattern_to_find, svg_block_to_insert_AFTER)
INJECTIONS = [
    # ch12 12.4 幂级数收敛区(数轴)
    ('chapter12-infinite-series.md', '### 12.4.1 收敛半径与收敛区间', r'''
::svg
<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="60" x2="340" y2="60" stroke="#1a365d" stroke-width="2"/>
  <line x1="340" y1="60" x2="332" y2="56" stroke="#1a365d" stroke-width="2"/>
  <line x1="340" y1="60" x2="332" y2="64" stroke="#1a365d" stroke-width="2"/>
  <line x1="100" y1="55" x2="100" y2="65" stroke="#888" stroke-width="1.5"/>
  <text x="92" y="80" font-size="12" fill="#888">−R</text>
  <line x1="180" y1="50" x2="180" y2="70" stroke="#1a365d" stroke-width="2"/>
  <text x="174" y="85" font-size="13" fill="#1a365d" font-weight="bold">x₀</text>
  <line x1="260" y1="55" x2="260" y2="65" stroke="#888" stroke-width="1.5"/>
  <text x="252" y="80" font-size="12" fill="#888">+R</text>
  <rect x="100" y="50" width="160" height="20" fill="#eef4fb" stroke="#1a365d" stroke-width="1.2" opacity="0.55"/>
  <text x="142" y="40" font-size="12" fill="#1a365d">绝对收敛区</text>
  <circle cx="100" cy="60" r="4" fill="none" stroke="#c2410c" stroke-width="2"/>
  <circle cx="260" cy="60" r="4" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="295" y="65" font-size="11" fill="#c2410c">端点单独判</text>
</svg>
<figcaption>图 12.4.1 幂级数收敛区:以 $x_0$ 为中心半径 $R$ 的对称区间,端点 $\pm R$ 需单独判别。</figcaption>
::endsvg

'''),

    # ch12 12.5 Taylor 多项式逼近 sin x
    ('chapter12-infinite-series.md', '### 12.5.2 Taylor 级数与收敛性', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="100" x2="360" y2="100" stroke="#888" stroke-width="1"/>
  <line x1="190" y1="20" x2="190" y2="180" stroke="#888" stroke-width="1"/>
  <path d="M 20 100 Q 60 30 100 30 T 180 100 T 260 170 T 360 100" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="345" y="115" font-size="12" fill="#1a365d">sin x</text>
  <path d="M 20 290 L 360 -90" fill="none" stroke="#c2410c" stroke-width="1.2" stroke-dasharray="4 3"/>
  <text x="100" y="60" font-size="11" fill="#c2410c">T₁(x) = x</text>
  <path d="M 20 220 Q 100 -40 180 100 T 360 -10" fill="none" stroke="#2d6e2d" stroke-width="1.2" stroke-dasharray="6 3"/>
  <text x="240" y="50" font-size="11" fill="#2d6e2d">T₃(x) = x − x³/6</text>
  <text x="50" y="190" font-size="11" fill="#666">Taylor 多项式阶数越高, 逼近区间越大</text>
</svg>
<figcaption>图 12.5.1 sin x 与其 1 阶/3 阶 Taylor 多项式逼近:阶数越高、与原函数贴合越久。</figcaption>
::endsvg

'''),

    # ch12 12.6 Fourier 方波逼近
    ('chapter12-infinite-series.md', '### 12.6.1 三角函数系是正交系', r'''
::svg
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="90" x2="360" y2="90" stroke="#888" stroke-width="1"/>
  <line x1="190" y1="15" x2="190" y2="165" stroke="#888" stroke-width="1"/>
  <path d="M 20 130 L 105 130 L 105 50 L 275 50 L 275 130 L 360 130" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="80" y="142" font-size="11" fill="#1a365d">方波 f(x)</text>
  <path d="M 20 90 Q 62 30 105 90 T 190 90 T 275 90 T 360 90" fill="none" stroke="#c2410c" stroke-width="1.4" opacity="0.75"/>
  <text x="20" y="30" font-size="11" fill="#c2410c">─ 1 项基波</text>
  <path d="M 20 110 L 60 55 L 105 60 L 145 90 L 190 90 L 235 90 L 275 60 L 320 55 L 360 110"
        fill="none" stroke="#2d6e2d" stroke-width="1.8" opacity="0.85"/>
  <text x="20" y="46" font-size="11" fill="#2d6e2d">─ 3 项叠加</text>
</svg>
<figcaption>图 12.6.1 Fourier 部分和逼近方波:1 项只是基础正弦,3 项已较像。间断点附近 Gibbs 现象永不消除。</figcaption>
::endsvg

'''),

    # ch9 9.8 鞍点 (z = x²-y²)
    ('chapter09-multivariate.md', '### 9.8.3 二阶判别(Hessian)', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="120" cy="100" rx="80" ry="50" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="120" cy="100" rx="50" ry="30" fill="none" stroke="#1a365d" stroke-width="1" opacity="0.6"/>
  <circle cx="120" cy="100" r="3" fill="#1a365d"/>
  <text x="125" y="115" font-size="11" fill="#1a365d">极小</text>
  <text x="105" y="170" font-size="11" fill="#444">D>0, A>0 正定</text>
  <path d="M 240 60 Q 300 100 240 140 M 350 60 Q 290 100 350 140" fill="none" stroke="#c2410c" stroke-width="1.5"/>
  <path d="M 260 70 Q 295 100 260 130 M 330 70 Q 295 100 330 130" fill="none" stroke="#c2410c" stroke-width="1" opacity="0.6"/>
  <circle cx="295" cy="100" r="3" fill="#c2410c"/>
  <text x="300" y="115" font-size="11" fill="#c2410c">鞍点</text>
  <text x="270" y="170" font-size="11" fill="#444">D<0 不定</text>
</svg>
<figcaption>图 9.8.1 极小(等高线为同心椭圆,正定 Hessian)vs 鞍点(等高线为双曲线,不定 Hessian)。</figcaption>
::endsvg

'''),

    # ch9 9.10 最小二乘 OLS 几何
    ('chapter09-multivariate.md', '### 9.10.3 矩阵形式与几何意义', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="170" x2="320" y2="170" stroke="#888" stroke-width="1"/>
  <line x1="40" y1="170" x2="40" y2="20" stroke="#888" stroke-width="1"/>
  <text x="325" y="175" font-size="12" fill="#888">x</text>
  <text x="25" y="22" font-size="12" fill="#888">y</text>
  <line x1="40" y1="150" x2="320" y2="40" stroke="#1a365d" stroke-width="2"/>
  <text x="180" y="100" font-size="11" fill="#1a365d">ŷ = ax + b</text>
  <circle cx="70" cy="140" r="4" fill="#c2410c"/>
  <circle cx="120" cy="100" r="4" fill="#c2410c"/>
  <circle cx="180" cy="120" r="4" fill="#c2410c"/>
  <circle cx="240" cy="60" r="4" fill="#c2410c"/>
  <circle cx="290" cy="55" r="4" fill="#c2410c"/>
  <line x1="70" y1="140" x2="70" y2="134" stroke="#2d6e2d" stroke-dasharray="2 2"/>
  <line x1="120" y1="100" x2="120" y2="110" stroke="#2d6e2d" stroke-dasharray="2 2"/>
  <line x1="180" y1="120" x2="180" y2="86" stroke="#2d6e2d" stroke-dasharray="2 2"/>
  <line x1="240" y1="60" x2="240" y2="63" stroke="#2d6e2d" stroke-dasharray="2 2"/>
  <line x1="290" y1="55" x2="290" y2="44" stroke="#2d6e2d" stroke-dasharray="2 2"/>
  <text x="100" y="190" font-size="11" fill="#2d6e2d">残差 yᵢ − ŷᵢ (虚线)</text>
  <text x="200" y="190" font-size="11" fill="#c2410c">数据点 (xᵢ, yᵢ)</text>
</svg>
<figcaption>图 9.10.1 最小二乘:在所有直线中选残差平方和 $\sum(y_i-\hat y_i)^2$ 最小者。</figcaption>
::endsvg

'''),

    # ch10 10.1 二重黎曼和柱体
    ('chapter10-multiple-integrals.md', '### 10.1.1 划分与黎曼和', r'''
::svg
<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <polygon points="40,180 280,160 320,190 60,210" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="20" y="200" font-size="12" fill="#1a365d">D (xy 平面)</text>
  <g stroke="#1a365d" stroke-width="0.6" opacity="0.5">
    <line x1="100" y1="175" x2="116" y2="205"/>
    <line x1="160" y1="170" x2="176" y2="200"/>
    <line x1="220" y1="165" x2="236" y2="195"/>
    <line x1="65" y1="190" x2="295" y2="170"/>
    <line x1="75" y1="200" x2="305" y2="180"/>
  </g>
  <polygon points="160,170 176,200 200,135 184,105" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="195" y="80" font-size="11" fill="#8b6f1c">f(ξᵢ,ηᵢ)·ΔSᵢ</text>
  <text x="170" y="135" font-size="11" fill="#c2410c">↑ 小柱体</text>
  <text x="40" y="30" font-size="12" fill="#444">∬ f dσ ≈ Σ f(ξᵢ,ηᵢ)·ΔSᵢ (取极限)</text>
</svg>
<figcaption>图 10.1.1 二重黎曼和:把区域 $D$ 切成小块,每小块上建一根柱体,体积累加取极限即二重积分。</figcaption>
::endsvg

'''),

    # ch11 11.5 通量 (流体穿过曲面)
    ('chapter11-line-surface-integrals.md', '### 11.5.1 双侧曲面与定向', r'''
::svg
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="flx" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <ellipse cx="190" cy="90" rx="55" ry="55" fill="#eef4fb" stroke="#1a365d" stroke-width="1.8"/>
  <ellipse cx="190" cy="90" rx="55" ry="15" fill="none" stroke="#1a365d" stroke-width="1" stroke-dasharray="3 2" opacity="0.5"/>
  <line x1="40" y1="60" x2="120" y2="60" stroke="#1a365d" stroke-width="2" marker-end="url(#flx)"/>
  <line x1="40" y1="90" x2="120" y2="90" stroke="#1a365d" stroke-width="2" marker-end="url(#flx)"/>
  <line x1="40" y1="120" x2="120" y2="120" stroke="#1a365d" stroke-width="2" marker-end="url(#flx)"/>
  <line x1="260" y1="60" x2="340" y2="60" stroke="#1a365d" stroke-width="2" marker-end="url(#flx)"/>
  <line x1="260" y1="90" x2="340" y2="90" stroke="#1a365d" stroke-width="2" marker-end="url(#flx)"/>
  <line x1="260" y1="120" x2="340" y2="120" stroke="#1a365d" stroke-width="2" marker-end="url(#flx)"/>
  <line x1="190" y1="90" x2="260" y2="90" stroke="#c2410c" stroke-width="2.5" marker-end="url(#flx)"/>
  <text x="220" y="80" font-size="13" fill="#c2410c" font-style="italic">n</text>
  <text x="180" y="95" font-size="14" font-style="italic" fill="#1a365d" font-weight="bold">Σ</text>
  <text x="48" y="160" font-size="11" fill="#666">流场 F⃗ 穿过曲面 Σ, 通量 = ∬ F·n dS</text>
</svg>
<figcaption>图 11.5.1 通量直观:流体场穿过曲面单位时间体积 = $\iint\vec{F}\cdot\vec{n}\,dS$。</figcaption>
::endsvg

'''),
]

count_added = 0
for fname, anchor, svg_block in INJECTIONS:
    path = f'D:/github/wechat-decrypt/notes/textbook/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 找 anchor 行, 在该 section 标题后插入 (在下一个空行或下一个段落开始前)
    if anchor not in content:
        print(f'SKIP {fname}: anchor "{anchor[:30]}" not found')
        continue
    # 在 anchor 行之后第一个空行后插入 svg
    idx = content.index(anchor)
    # 找该行末尾
    line_end = content.index('\n', idx) + 1
    # 跳过紧跟的空行
    while line_end < len(content) and content[line_end] == '\n':
        line_end += 1
    new_content = content[:line_end] + svg_block.lstrip('\n') + content[line_end:]
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count_added += 1
        print(f'OK  {fname}: injected after "{anchor[:40]}"')

print(f'\n{count_added}/{len(INJECTIONS)} SVG blocks injected')
