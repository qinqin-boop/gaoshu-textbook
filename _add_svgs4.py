"""第四批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.4 点到平面距离投影
    ('chapter08-vectors.md', '### 8.4.3 点到平面的距离', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="dp1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <polygon points="60,150 280,170 320,130 100,110" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5" opacity="0.7"/>
  <text x="280" y="155" font-size="11" fill="#1a365d">π: Ax+By+Cz+D=0</text>
  <circle cx="170" cy="50" r="4" fill="#c2410c"/>
  <text x="178" y="48" font-size="12" fill="#c2410c">P₁</text>
  <line x1="170" y1="50" x2="180" y2="130" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="180" cy="130" r="3" fill="#888"/>
  <text x="186" y="135" font-size="11" fill="#888">投影点</text>
  <line x1="180" y1="130" x2="200" y2="70" stroke="#c2410c" stroke-width="2" marker-end="url(#dp1)"/>
  <text x="205" y="70" font-size="12" fill="#c2410c">n⃗ 法向</text>
  <text x="115" y="90" font-size="11" fill="#c2410c">d = |Ax₁+By₁+Cz₁+D|/√(A²+B²+C²)</text>
</svg>
<figcaption>图 8.4.1 点 $P_1$ 到平面 $\pi$ 的距离 = $\overrightarrow{P_0 P_1}$ 沿法向 $\vec{n}$ 的有向投影绝对值。</figcaption>
::endsvg

'''),

    # ch10 10.3 柱坐标 (r, θ, z)
    ('chapter10-multiple-integrals.md', '### 10.3.2 柱坐标', r'''
::svg
<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="cy1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <line x1="160" y1="220" x2="160" y2="20" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="220" x2="60" y2="190" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="220" x2="300" y2="200" stroke="#888" stroke-width="1"/>
  <text x="152" y="15" font-size="12" fill="#888">z</text>
  <text x="50" y="200" font-size="12" fill="#888">x</text>
  <text x="305" y="210" font-size="12" fill="#888">y</text>
  <ellipse cx="160" cy="220" rx="80" ry="22" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <ellipse cx="160" cy="120" rx="80" ry="22" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <line x1="80" y1="120" x2="80" y2="220" stroke="#1a365d" stroke-width="1"/>
  <line x1="240" y1="120" x2="240" y2="220" stroke="#1a365d" stroke-width="1"/>
  <line x1="160" y1="220" x2="225" y2="232" stroke="#c2410c" stroke-width="1.5"/>
  <text x="190" y="240" font-size="11" fill="#c2410c">r</text>
  <line x1="225" y1="232" x2="225" y2="135" stroke="#c2410c" stroke-width="1" stroke-dasharray="2 2"/>
  <circle cx="225" cy="135" r="3" fill="#1a365d"/>
  <text x="232" y="135" font-size="11" fill="#1a365d">P</text>
  <text x="172" y="195" font-size="11" fill="#c2410c">θ</text>
  <text x="235" y="180" font-size="11" fill="#c2410c">z</text>
  <text x="35" y="35" font-size="11" fill="#444">dV = r dr dθ dz</text>
</svg>
<figcaption>图 10.3.2 柱坐标 $(r,\theta,z)$:$z$ 不变,$xy$ 平面用极坐标,适合圆柱/圆锥/旋转体。$dV=r\,dr\,d\theta\,dz$。</figcaption>
::endsvg

'''),

    # ch10 10.5 Gamma 函数
    ('chapter10-multiple-integrals.md', '### 10.5.4 Gamma 函数与 Beta 函数', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="160" x2="330" y2="160" stroke="#888" stroke-width="1"/>
  <line x1="60" y1="20" x2="60" y2="190" stroke="#888" stroke-width="1"/>
  <text x="335" y="165" font-size="11" fill="#888">s</text>
  <text x="65" y="20" font-size="11" fill="#888">Γ(s)</text>
  <path d="M 75 30 Q 90 100 110 140 L 130 110 L 170 70 L 220 30" fill="none" stroke="#1a365d" stroke-width="2"/>
  <circle cx="110" cy="140" r="3" fill="#c2410c"/>
  <text x="115" y="155" font-size="11" fill="#c2410c">Γ(1)=1</text>
  <circle cx="130" cy="110" r="3" fill="#c2410c"/>
  <text x="135" y="115" font-size="11" fill="#c2410c">Γ(2)=1!</text>
  <circle cx="170" cy="70" r="3" fill="#c2410c"/>
  <text x="175" y="75" font-size="11" fill="#c2410c">Γ(3)=2!</text>
  <circle cx="220" cy="30" r="3" fill="#c2410c"/>
  <text x="225" y="35" font-size="11" fill="#c2410c">Γ(4)=3!=6</text>
  <line x1="60" y1="20" x2="60" y2="160" stroke="#b91c1c" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="38" y="40" font-size="11" fill="#b91c1c">极点</text>
  <text x="78" y="190" font-size="11" fill="#666">阶乘的连续推广: Γ(n)=(n−1)!, 在 s=0,-1,-2,... 处极点</text>
</svg>
<figcaption>图 10.5.1 Gamma 函数:整数点取阶乘 $\Gamma(n)=(n-1)!$;$s\to 0^+$ 时发散,在 $s=0,-1,-2,\dots$ 处单极点。</figcaption>
::endsvg

'''),

    # ch11 11.1 弧长元素 ds (参数化切向)
    ('chapter11-line-surface-integrals.md', '### 11.1.2 计算公式', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ls1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <path d="M 30 130 Q 100 30 200 60 T 340 110" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="40" y="155" font-size="12" fill="#1a365d">L: r⃗(t)</text>
  <circle cx="170" cy="55" r="3" fill="#c2410c"/>
  <line x1="170" y1="55" x2="230" y2="48" stroke="#c2410c" stroke-width="2" marker-end="url(#ls1)"/>
  <text x="235" y="48" font-size="12" fill="#c2410c">r⃗'(t)</text>
  <path d="M 170 55 L 200 50" stroke="#2d6e2d" stroke-width="4"/>
  <text x="172" y="78" font-size="11" fill="#2d6e2d">ds</text>
  <text x="30" y="170" font-size="11" fill="#666">ds = |r⃗'(t)| dt — 切向量长度 × 参数增量</text>
</svg>
<figcaption>图 11.1.1 弧长元素 $ds=|\vec{r}'(t)|\,dt$:沿曲线切向走 $dt$ 长的小段,长度为切向量模 $\times dt$。</figcaption>
::endsvg

'''),

    # ch11 11.6 微分形式 ∫_∂M ω = ∫_M dω 5 维度统一
    ('chapter11-line-surface-integrals.md', '### 11.6.6 三大公式与微分形式视角', r'''
::svg
<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="30" y="30" font-size="13" font-weight="bold" fill="#1a365d">∫_∂M ω = ∫_M dω</text>
  <line x1="40" y1="60" x2="100" y2="60" stroke="#1a365d" stroke-width="2"/>
  <circle cx="40" cy="60" r="3" fill="#c2410c"/>
  <circle cx="100" cy="60" r="3" fill="#c2410c"/>
  <text x="110" y="65" font-size="11" fill="#1a365d">Newton-Leibniz (1d: 区间 ↔ 端点)</text>
  <rect x="40" y="80" width="50" height="30" fill="#eef4fb" stroke="#1a365d" stroke-width="2"/>
  <text x="110" y="100" font-size="11" fill="#1a365d">Green (2d: 区域 ↔ 闭曲线)</text>
  <path d="M 40 130 Q 65 115 90 130 Q 65 145 40 130 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="2"/>
  <text x="110" y="135" font-size="11" fill="#8b6f1c">Stokes (3d: 曲面 ↔ 边界曲线)</text>
  <ellipse cx="65" cy="170" rx="30" ry="15" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="2"/>
  <text x="110" y="172" font-size="11" fill="#2d6e2d">Gauss (3d: 立体 ↔ 闭曲面)</text>
  <text x="40" y="205" font-size="11" font-style="italic" fill="#666">边界 ↔ 内部 一切归一</text>
</svg>
<figcaption>图 11.6.2 广义 Stokes $\int_{\partial M}\omega=\int_M d\omega$ 一公式统一 NL / Green / Stokes / Gauss,$M$ 维度从 1 到 3。</figcaption>
::endsvg

'''),

    # ch12 12.6 Fourier 频谱条
    ('chapter12-infinite-series.md', '### 12.6.4 Bessel 不等式与 Parseval 恒等式', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="160" x2="340" y2="160" stroke="#888" stroke-width="1"/>
  <line x1="40" y1="20" x2="40" y2="180" stroke="#888" stroke-width="1"/>
  <text x="345" y="165" font-size="11" fill="#888">n (频率)</text>
  <text x="45" y="20" font-size="11" fill="#888">|cₙ|² 能量</text>
  <rect x="55" y="40" width="20" height="120" fill="#1a365d" opacity="0.85"/>
  <text x="58" y="180" font-size="11" fill="#1a365d">1</text>
  <rect x="90" y="100" width="20" height="60" fill="#1a365d" opacity="0.7"/>
  <text x="95" y="180" font-size="11" fill="#1a365d">3</text>
  <rect x="125" y="125" width="20" height="35" fill="#1a365d" opacity="0.6"/>
  <text x="130" y="180" font-size="11" fill="#1a365d">5</text>
  <rect x="160" y="138" width="20" height="22" fill="#1a365d" opacity="0.55"/>
  <text x="165" y="180" font-size="11" fill="#1a365d">7</text>
  <rect x="195" y="148" width="20" height="12" fill="#1a365d" opacity="0.5"/>
  <text x="200" y="180" font-size="11" fill="#1a365d">9</text>
  <rect x="230" y="153" width="20" height="7" fill="#1a365d" opacity="0.4"/>
  <text x="235" y="180" font-size="11" fill="#1a365d">11</text>
  <rect x="265" y="156" width="20" height="4" fill="#1a365d" opacity="0.3"/>
  <text x="270" y="180" font-size="11" fill="#1a365d">13</text>
  <text x="100" y="40" font-size="11" fill="#666">Parseval: ‖f‖² = Σ|cₙ|² (能量在频域守恒)</text>
</svg>
<figcaption>图 12.6.2 方波 Fourier 频谱:奇次谐波幅度 $\propto 1/n$,能量按 $1/n^2$ 衰减;Parseval 保证总能量 $\sum|c_n|^2=\|f\|^2$。</figcaption>
::endsvg

'''),

    # ch9 9.7 切平面 3D
    ('chapter09-multivariate.md', '### 9.7.3 显式曲面 $z=f(x,y)$ 的切平面', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="tp1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <path d="M 50 180 Q 130 80 220 100 Q 290 110 320 60" fill="none" stroke="#1a365d" stroke-width="2"/>
  <path d="M 50 180 Q 100 130 130 80" fill="none" stroke="#1a365d" stroke-width="1" opacity="0.5" stroke-dasharray="3 3"/>
  <text x="40" y="55" font-size="12" fill="#1a365d">曲面 z=f(x,y)</text>
  <polygon points="160,130 240,118 250,160 170,172" fill="#fef6e4" fill-opacity="0.85" stroke="#c9a227" stroke-width="1.5"/>
  <text x="180" y="195" font-size="11" fill="#8b6f1c">切平面</text>
  <circle cx="205" cy="135" r="3.5" fill="#c2410c"/>
  <text x="212" y="138" font-size="11" fill="#c2410c">P₀</text>
  <line x1="205" y1="135" x2="225" y2="80" stroke="#c2410c" stroke-width="2" marker-end="url(#tp1)"/>
  <text x="228" y="80" font-size="11" fill="#c2410c">n⃗=(f_x,f_y,−1)</text>
</svg>
<figcaption>图 9.7.1 显式曲面 $z=f(x,y)$ 的切平面在 $P_0$ 处:法向 $(f_x,f_y,-1)$,切平面方程就是全微分 $z-z_0=f_x\Delta x+f_y\Delta y$。</figcaption>
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
