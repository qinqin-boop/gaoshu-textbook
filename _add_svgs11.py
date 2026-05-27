"""第十一批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.4 三点决定平面
    ('chapter08-vectors.md', '### 8.4.2 三点式与截距式', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="trp" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <polygon points="80,160 250,140 200,40" fill="#fef6e4" fill-opacity="0.7" stroke="#c9a227" stroke-width="1.8"/>
  <circle cx="80" cy="160" r="4" fill="#1a365d"/>
  <text x="56" y="178" font-size="11" fill="#1a365d">A</text>
  <circle cx="250" cy="140" r="4" fill="#1a365d"/>
  <text x="258" y="143" font-size="11" fill="#1a365d">B</text>
  <circle cx="200" cy="40" r="4" fill="#1a365d"/>
  <text x="207" y="38" font-size="11" fill="#1a365d">C</text>
  <line x1="80" y1="160" x2="250" y2="140" stroke="#c2410c" stroke-width="1.5" marker-end="url(#trp)"/>
  <text x="160" y="158" font-size="11" fill="#c2410c">AB→</text>
  <line x1="80" y1="160" x2="200" y2="40" stroke="#c2410c" stroke-width="1.5" marker-end="url(#trp)"/>
  <text x="125" y="100" font-size="11" fill="#c2410c">AC→</text>
  <line x1="160" y1="110" x2="190" y2="60" stroke="#2d6e2d" stroke-width="2" marker-end="url(#trp)"/>
  <text x="195" y="70" font-size="11" fill="#2d6e2d">n⃗=AB×AC</text>
  <text x="35" y="195" font-size="11" fill="#666">三向量 AP⃗,AB⃗,AC⃗ 混合积 = 0 ⇒ 共面 ⇒ 平面方程</text>
</svg>
<figcaption>图 8.4.2 三点决定平面:法向 $\vec{n}=\vec{AB}\times\vec{AC}$,$P$ 在平面上 $\iff[\vec{AP},\vec{AB},\vec{AC}]=0$。</figcaption>
::endsvg

'''),

    # ch9 9.7 等量面族正交
    ('chapter09-multivariate.md', '### 9.7.5 等量面族的正交性', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="og1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="og2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="120" ry="60" fill="none" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="180" cy="100" rx="80" ry="40" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <text x="60" y="65" font-size="11" fill="#1a365d">F=c₁ 族</text>
  <line x1="180" y1="100" x2="280" y2="60" stroke="#888" stroke-width="1.5"/>
  <line x1="180" y1="100" x2="80" y2="140" stroke="#888" stroke-width="1.5"/>
  <line x1="180" y1="100" x2="180" y2="180" stroke="#888" stroke-width="1.5"/>
  <line x1="180" y1="100" x2="180" y2="20" stroke="#888" stroke-width="1.5"/>
  <text x="280" y="60" font-size="11" fill="#888">G=c₂ 族 (射线)</text>
  <circle cx="240" cy="80" r="3" fill="#c2410c"/>
  <line x1="240" y1="80" x2="276" y2="65" stroke="#c2410c" stroke-width="1.6" marker-end="url(#og1)"/>
  <line x1="240" y1="80" x2="245" y2="60" stroke="#2d6e2d" stroke-width="1.6" marker-end="url(#og2)"/>
  <text x="280" y="60" font-size="11" fill="#c2410c">∇F</text>
  <text x="250" y="50" font-size="11" fill="#2d6e2d">∇G</text>
  <text x="35" y="195" font-size="11" fill="#666">∇F·∇G=0 ⇒ 两族曲面正交相交 (椭圆+射线 正交)</text>
</svg>
<figcaption>图 9.7.2 等量面族正交:同心椭圆($F=c_1$)与穿过中心的射线($G=c_2$)在每个交点处 $\nabla F\perp\nabla G$ — GIS 等高线 vs 水流方向。</figcaption>
::endsvg

'''),

    # ch10 10.3 三重积分 先二后一(切片求体积)
    ('chapter10-multiple-integrals.md', '### 10.3.1 直角坐标:累次积分思想', r'''
::svg
<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="160" cy="110" rx="100" ry="40" fill="none" stroke="#1a365d" stroke-width="0.8" stroke-dasharray="3 2"/>
  <ellipse cx="160" cy="60" rx="60" ry="22" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <ellipse cx="160" cy="90" rx="80" ry="32" fill="#fef6e4" fill-opacity="0.7" stroke="#c9a227" stroke-width="1.2"/>
  <ellipse cx="160" cy="120" rx="92" ry="38" fill="#fef6e4" fill-opacity="0.5" stroke="#c9a227" stroke-width="1.2"/>
  <ellipse cx="160" cy="150" rx="80" ry="32" fill="#fef6e4" fill-opacity="0.7" stroke="#c9a227" stroke-width="1.2"/>
  <ellipse cx="160" cy="180" rx="50" ry="20" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <line x1="270" y1="40" x2="270" y2="200" stroke="#1a365d" stroke-width="1"/>
  <line x1="270" y1="40" x2="265" y2="46" stroke="#1a365d"/>
  <line x1="270" y1="40" x2="275" y2="46" stroke="#1a365d"/>
  <text x="280" y="44" font-size="11" fill="#1a365d">z</text>
  <line x1="265" y1="120" x2="275" y2="120" stroke="#c2410c" stroke-width="2"/>
  <text x="285" y="125" font-size="11" fill="#c2410c">z=c 切面 D_z</text>
  <text x="35" y="30" font-size="11" fill="#444">∭ f dV = ∫_c^d (∬_{D_z} f dxdy) dz (先二后一)</text>
</svg>
<figcaption>图 10.3.3 三重积分先二后一:把立体沿 $z$ 切片,每个 $z$ 截面 $D_z$ 上二重积分,再对 $z$ 一重积分。适合球/椭球/旋转体。</figcaption>
::endsvg

'''),

    # ch11 11.2 保守场 (路径无关 + 势能函数)
    ('chapter11-line-surface-integrals.md', '### 11.2.4 与 Green / Stokes 的衔接', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="cs1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="cs2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="80" cy="100" r="4" fill="#1a365d"/>
  <text x="65" y="120" font-size="12" font-weight="bold" fill="#1a365d">A</text>
  <circle cx="280" cy="100" r="4" fill="#1a365d"/>
  <text x="285" y="105" font-size="12" font-weight="bold" fill="#1a365d">B</text>
  <path d="M 80 100 Q 130 30 200 50 Q 250 60 280 100" fill="none" stroke="#c2410c" stroke-width="2" marker-end="url(#cs2)"/>
  <text x="155" y="50" font-size="11" fill="#c2410c">路径 1</text>
  <path d="M 80 100 Q 130 180 200 170 Q 250 160 280 100" fill="none" stroke="#2d6e2d" stroke-width="2" marker-end="url(#cs2)"/>
  <text x="155" y="190" font-size="11" fill="#2d6e2d">路径 2</text>
  <line x1="80" y1="100" x2="280" y2="100" stroke="#1a365d" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="#444">∫_path1 F⃗·dr⃗ = ∫_path2 F⃗·dr⃗ = φ(B)−φ(A)</text>
  <text x="65" y="170" font-size="11" fill="#666">保守场: ∇×F⃗=0 单连通 ⇒ 路径无关</text>
</svg>
<figcaption>图 11.2.2 保守场路径无关:$\vec{F}=\nabla\phi$ 时任何 $A\to B$ 路径积分相同 = $\phi(B)-\phi(A)$;闭路积分 = 0。物理:保守力做功 = 势能差。</figcaption>
::endsvg

'''),

    # ch12 12.3 Leibniz 子列收敛
    ('chapter12-infinite-series.md', '### 12.3.1 交错级数与 Leibniz 判别法', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="100" x2="340" y2="100" stroke="#888" stroke-width="1"/>
  <text x="20" y="22" font-size="11" fill="#888">S_n</text>
  <circle cx="50" cy="60" r="4" fill="#c2410c"/>
  <text x="42" y="55" font-size="10" fill="#c2410c">S₁</text>
  <circle cx="80" cy="140" r="4" fill="#2d6e2d"/>
  <text x="72" y="158" font-size="10" fill="#2d6e2d">S₂</text>
  <circle cx="120" cy="75" r="4" fill="#c2410c"/>
  <text x="113" y="70" font-size="10" fill="#c2410c">S₃</text>
  <circle cx="160" cy="125" r="4" fill="#2d6e2d"/>
  <text x="153" y="142" font-size="10" fill="#2d6e2d">S₄</text>
  <circle cx="200" cy="85" r="4" fill="#c2410c"/>
  <circle cx="240" cy="115" r="4" fill="#2d6e2d"/>
  <circle cx="280" cy="92" r="4" fill="#c2410c"/>
  <circle cx="310" cy="108" r="4" fill="#2d6e2d"/>
  <path d="M 50 60 L 120 75 L 200 85 L 280 92" stroke="#c2410c" stroke-width="1" stroke-dasharray="2 2" fill="none"/>
  <path d="M 80 140 L 160 125 L 240 115 L 310 108" stroke="#2d6e2d" stroke-width="1" stroke-dasharray="2 2" fill="none"/>
  <line x1="20" y1="100" x2="340" y2="100" stroke="#1a365d" stroke-width="2"/>
  <text x="285" y="95" font-size="11" font-weight="bold" fill="#1a365d">极限 S</text>
  <text x="20" y="180" font-size="11" fill="#666">奇子列 S_{2k-1} 单调↓, 偶子列 S_{2k} 单调↑, 同极限 S</text>
</svg>
<figcaption>图 12.3.2 Leibniz 判别证明思路:奇子列 $S_1>S_3>S_5>\dots$ 单调减;偶子列 $S_2<S_4<S_6<\dots$ 单调增;两子列收敛到同一极限 $S$。</figcaption>
::endsvg

'''),

    # ch10 10.4 形心 / 质心 (杠杆平衡)
    ('chapter10-multiple-integrals.md', '### 10.4.2 质量与质心', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <polygon points="50,100 320,100 290,80 75,110" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="55" y="135" font-size="12" fill="#1a365d">板 D</text>
  <circle cx="80" cy="100" r="3" fill="#c2410c"/>
  <circle cx="130" cy="103" r="3" fill="#c2410c"/>
  <circle cx="170" cy="98" r="3" fill="#c2410c"/>
  <circle cx="220" cy="100" r="3" fill="#c2410c"/>
  <circle cx="270" cy="98" r="3" fill="#c2410c"/>
  <text x="160" y="80" font-size="11" fill="#c2410c">每微元 ρ dσ</text>
  <polygon points="195,150 175,130 215,130" fill="#2d6e2d"/>
  <text x="180" y="170" font-size="13" font-weight="bold" fill="#2d6e2d">质心 (x̄, ȳ)</text>
  <line x1="195" y1="100" x2="195" y2="130" stroke="#2d6e2d" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="35" y="30" font-size="12" font-weight="bold" fill="#444">x̄ = (1/M) ∬ x ρ dσ — 质量加权平均位置</text>
</svg>
<figcaption>图 10.4.4 质心 = 跷跷板平衡点:把板看作很多小重锤,质心是单点重锤能产生相同合力矩的位置(质量加权平均)。</figcaption>
::endsvg

'''),

    # ch9 9.9 二元 Taylor 二阶逼近 (碗形拟合)
    ('chapter09-multivariate.md', '### 9.9.2 一阶 / 二阶展开:专门写出', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 30 170 Q 100 60 200 80 Q 280 110 340 50" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="35" y="35" font-size="12" fill="#1a365d">原函数 f</text>
  <line x1="120" y1="118" x2="270" y2="76" stroke="#888" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="135" y="115" font-size="11" fill="#888">1 阶: 切平面</text>
  <path d="M 110 130 Q 200 50 290 100" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="195" y="60" font-size="11" fill="#c2410c">2 阶: 二次型贴合</text>
  <circle cx="200" cy="80" r="4" fill="#2d6e2d"/>
  <text x="208" y="78" font-size="11" fill="#2d6e2d">P₀</text>
  <text x="30" y="190" font-size="11" fill="#666">f ≈ f₀ + ∇f·h + ½h^T H h + o(|h|²)</text>
</svg>
<figcaption>图 9.9.1 多元 Taylor 二阶逼近:一阶切平面只贴在 $P_0$ 附近;二阶用 Hessian 二次型补凹凸信息,逼近半径更大。</figcaption>
::endsvg

'''),
]

count_added = 0
for fname, anchor, svg_block in INJECTIONS:
    path = f'D:/github/wechat-decrypt/notes/textbook/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if anchor not in content:
        print(f'SKIP {fname}: "{anchor[:40]}"')
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
        print(f'OK  {fname}: "{anchor[:40]}"')

print(f'\n{count_added}/{len(INJECTIONS)} injected')
