"""第五批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.5 异面直线公垂线 (3D)
    ('chapter08-vectors.md', '### 8.5.4 距离公式', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ll1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <line x1="40" y1="160" x2="280" y2="80" stroke="#1a365d" stroke-width="2.5" marker-end="url(#ll1)"/>
  <text x="285" y="80" font-size="12" font-style="italic" fill="#1a365d">l₁</text>
  <line x1="80" y1="40" x2="320" y2="130" stroke="#c2410c" stroke-width="2.5" marker-end="url(#ll1)"/>
  <text x="325" y="135" font-size="12" font-style="italic" fill="#c2410c">l₂</text>
  <line x1="160" y1="120" x2="180" y2="85" stroke="#2d6e2d" stroke-width="2.5" stroke-dasharray="4 3"/>
  <text x="184" y="100" font-size="11" fill="#2d6e2d">公垂线 d</text>
  <circle cx="160" cy="120" r="3" fill="#2d6e2d"/>
  <circle cx="180" cy="85" r="3" fill="#2d6e2d"/>
  <text x="35" y="190" font-size="11" fill="#666">d = |[M₁M₂, s⃗₁, s⃗₂]| / |s⃗₁×s⃗₂| (体积/底面积=高)</text>
</svg>
<figcaption>图 8.5.1 异面直线 $\ell_1,\ell_2$ 公垂线段长度 = 平行六面体体积/底面积。混合积 $/$ 向量积模。</figcaption>
::endsvg

'''),

    # ch9 9.5 隐函数曲线 + 切线
    ('chapter09-multivariate.md', '### 9.5.1 一元隐函数', r'''
::svg
<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="120" x2="300" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="20" x2="160" y2="220" stroke="#888" stroke-width="1"/>
  <text x="305" y="125" font-size="11" fill="#888">x</text>
  <text x="165" y="20" font-size="11" fill="#888">y</text>
  <circle cx="160" cy="120" r="80" fill="none" stroke="#1a365d" stroke-width="2"/>
  <text x="60" y="55" font-size="12" fill="#1a365d">F(x,y)=x²+y²−1=0</text>
  <circle cx="217" cy="64" r="4" fill="#c2410c"/>
  <text x="225" y="60" font-size="11" fill="#c2410c">(x₀,y₀)</text>
  <line x1="155" y1="40" x2="285" y2="125" stroke="#c2410c" stroke-width="1.6" stroke-dasharray="4 3"/>
  <text x="232" y="118" font-size="11" fill="#c2410c">切线 dy/dx=-x/y</text>
  <circle cx="80" cy="120" r="4" fill="#b91c1c"/>
  <circle cx="240" cy="120" r="4" fill="#b91c1c"/>
  <text x="60" y="148" font-size="11" fill="#b91c1c">F_y=0 失效</text>
</svg>
<figcaption>图 9.5.1 隐函数 $x^2+y^2=1$ 圆:除 $(\pm 1,0)$($F_y=0$ 失效)外处处可解为 $y=\pm\sqrt{1-x^2}$,$dy/dx=-x/y$。</figcaption>
::endsvg

'''),

    # ch10 10.4 转动惯量 (绕轴 + r²)
    ('chapter10-multiple-integrals.md', '### 10.4.3 转动惯量', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="180" y1="20" x2="180" y2="180" stroke="#1a365d" stroke-width="2"/>
  <text x="185" y="22" font-size="12" fill="#1a365d">z 轴</text>
  <ellipse cx="180" cy="100" rx="100" ry="60" fill="#eef4fb" fill-opacity="0.6" stroke="#1a365d" stroke-width="1.5"/>
  <text x="105" y="105" font-size="11" fill="#1a365d">板 D (面密度 ρ)</text>
  <circle cx="245" cy="100" r="4" fill="#c2410c"/>
  <line x1="180" y1="100" x2="245" y2="100" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="200" y="93" font-size="12" fill="#c2410c">r</text>
  <text x="248" y="118" font-size="11" fill="#c2410c">dm</text>
  <text x="30" y="180" font-size="11" fill="#666">I_z = ∬ r² ρ dσ — 距轴远的微元贡献按 r² 放大</text>
</svg>
<figcaption>图 10.4.2 转动惯量 $I_z=\iint(x^2+y^2)\rho\,d\sigma$:距旋转轴远的微元 $r^2$ 倍放大,反映"旋转质量"。</figcaption>
::endsvg

'''),

    # ch11 11.3 Green 正向边界 + 微元方块
    ('chapter11-line-surface-integrals.md', '### 11.3.2 Green 公式', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="grn" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <path d="M 60 160 Q 90 60 200 60 Q 320 80 290 180 Q 200 200 60 160 Z" fill="#eef4fb" stroke="#1a365d" stroke-width="2"/>
  <path d="M 100 130 L 100 110 M 100 110 L 120 110 M 120 110 L 120 130 M 120 130 L 100 130 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="103" y="124" font-size="9" fill="#8b6f1c">微元</text>
  <line x1="100" y1="110" x2="130" y2="110" stroke="#c2410c" stroke-width="1.5" marker-end="url(#grn)"/>
  <line x1="120" y1="110" x2="120" y2="140" stroke="#c2410c" stroke-width="1.5" marker-end="url(#grn)"/>
  <text x="170" y="130" font-size="13" fill="#1a365d">D</text>
  <path d="M 250 65 L 280 70" stroke="#c2410c" stroke-width="1.5" marker-end="url(#grn)"/>
  <path d="M 290 100 L 295 130" stroke="#c2410c" stroke-width="1.5" marker-end="url(#grn)"/>
  <text x="100" y="200" font-size="11" fill="#1a365d">∂D 逆时针 (区域在左)</text>
  <text x="35" y="40" font-size="11" fill="#666">∮ Pdx+Qdy = ∬ (∂Q/∂x - ∂P/∂y) dxdy</text>
</svg>
<figcaption>图 11.3.2 Green 公式微元解释:每个小方块边界环流的总和 = 内部旋度密度积分;内部公共边相互抵消,只剩外边界。</figcaption>
::endsvg

'''),

    # ch11 11.4 曲面参数化 grid (u,v 网格映射到 3D)
    ('chapter11-line-surface-integrals.md', '### 11.4.3 一般参数化', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ar1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <rect x="20" y="60" width="120" height="100" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <g stroke="#1a365d" stroke-width="0.7" opacity="0.6">
    <line x1="50" y1="60" x2="50" y2="160"/>
    <line x1="80" y1="60" x2="80" y2="160"/>
    <line x1="110" y1="60" x2="110" y2="160"/>
    <line x1="20" y1="90" x2="140" y2="90"/>
    <line x1="20" y1="120" x2="140" y2="120"/>
  </g>
  <text x="55" y="180" font-size="11" fill="#1a365d">(u,v) 参数域</text>
  <text x="2" y="115" font-size="12" fill="#1a365d">v</text>
  <text x="65" y="55" font-size="12" fill="#1a365d">u</text>
  <line x1="160" y1="100" x2="220" y2="100" stroke="#c2410c" stroke-width="2.5" marker-end="url(#ar1)"/>
  <text x="170" y="92" font-size="13" font-style="italic" fill="#c2410c">r⃗(u,v)</text>
  <path d="M 240 60 Q 290 50 340 80 Q 350 120 320 160 Q 270 170 240 130 Q 230 100 240 60 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <g stroke="#c9a227" stroke-width="0.7" opacity="0.6">
    <path d="M 270 58 Q 280 100 270 165" fill="none"/>
    <path d="M 300 55 Q 320 100 310 168" fill="none"/>
    <path d="M 240 80 Q 290 70 340 90" fill="none"/>
    <path d="M 235 120 Q 290 115 335 135" fill="none"/>
  </g>
  <text x="260" y="190" font-size="11" fill="#8b6f1c">Σ ⊂ ℝ³ 参数化曲面</text>
  <text x="265" y="42" font-size="11" fill="#666">dS = |r⃗_u × r⃗_v| dudv</text>
</svg>
<figcaption>图 11.4.3 曲面参数化 $\vec{r}(u,v)$:$(u,v)$ 平面网格映射到 3D 曲面 grid;面积元 $dS=|\vec{r}_u\times\vec{r}_v|du\,dv$。</figcaption>
::endsvg

'''),

    # ch12 12.3 Riemann 重排 (条件收敛和值变化)
    ('chapter12-infinite-series.md', '### 12.3.3 Riemann 重排定理(条件收敛的危险)', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="100" x2="340" y2="100" stroke="#888" stroke-width="1"/>
  <text x="345" y="105" font-size="11" fill="#888">n</text>
  <text x="22" y="22" font-size="11" fill="#888">S_n</text>
  <path d="M 30 60 L 60 110 L 90 80 L 120 105 L 150 90 L 180 100 L 210 95 L 240 100 L 270 96 L 300 100" fill="none" stroke="#1a365d" stroke-width="2"/>
  <text x="40" y="55" font-size="11" fill="#1a365d">原次序 → ln2 ≈ 0.69</text>
  <path d="M 30 60 L 50 50 L 80 75 L 100 70 L 130 50 L 160 60 L 190 50 L 220 55 L 250 53 L 280 55 L 310 54" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="180" y="35" font-size="11" fill="#c2410c">重排次序 → (3/2)ln2 ≈ 1.04</text>
  <line x1="20" y1="55" x2="340" y2="55" stroke="#c2410c" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="20" y1="100" x2="340" y2="100" stroke="#1a365d" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="20" y="180" font-size="11" fill="#666">条件收敛: 同样项, 次序不同 → 和不同; 极端可重排到任意值</text>
</svg>
<figcaption>图 12.3.1 Riemann 重排:交错调和 $1-1/2+1/3-\dots=\ln 2$ 重排为 $1+1/3-1/2+\dots=\frac{3}{2}\ln 2$ — 同项同次数,次序变 → 和变 50%。</figcaption>
::endsvg

'''),

    # ch12 12.2 Cauchy 序列 (Cauchy 准则)
    ('chapter12-infinite-series.md', '### 12.1.5 Cauchy 准则', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="100" x2="340" y2="100" stroke="#888" stroke-width="1"/>
  <text x="345" y="105" font-size="11" fill="#888">n</text>
  <text x="20" y="22" font-size="11" fill="#888">S_n</text>
  <path d="M 30 50 L 50 110 L 75 75 L 100 95 L 130 85 L 160 92 L 195 88 L 230 90 L 265 89 L 300 90 L 335 89.5" fill="none" stroke="#1a365d" stroke-width="2"/>
  <line x1="160" y1="85" x2="335" y2="85" stroke="#c2410c" stroke-width="0.8" stroke-dasharray="3 2"/>
  <line x1="160" y1="95" x2="335" y2="95" stroke="#c2410c" stroke-width="0.8" stroke-dasharray="3 2"/>
  <rect x="160" y="85" width="175" height="10" fill="#c2410c" fill-opacity="0.18"/>
  <text x="200" y="79" font-size="11" fill="#c2410c">N 之后所有 |S_m-S_n| < ε</text>
  <line x1="160" y1="98" x2="160" y2="108" stroke="#1a365d"/>
  <text x="155" y="125" font-size="11" fill="#1a365d">N</text>
  <text x="20" y="155" font-size="11" fill="#666">Cauchy: 不必预知极限, 远处项任意小即收敛</text>
</svg>
<figcaption>图 12.1.1 Cauchy 收敛准则:$N$ 之后所有部分和落在宽 $\varepsilon$ 的窄带内,无需预知极限值即可断收敛。</figcaption>
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
        print(f'OK  {fname}: "{anchor[:40]}"')

print(f'\n{count_added}/{len(INJECTIONS)} injected')
