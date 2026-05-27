"""第八批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.4 链式法则 树状图
    ('chapter09-multivariate.md', '### 9.4.2 多中间变量(核心情形)', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ch1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <circle cx="180" cy="40" r="20" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="174" y="45" font-size="14" font-weight="bold">z</text>
  <line x1="170" y1="55" x2="120" y2="92" stroke="#1a365d" stroke-width="1.5" marker-end="url(#ch1)"/>
  <text x="125" y="80" font-size="11" fill="#1a365d">∂z/∂u</text>
  <line x1="190" y1="55" x2="240" y2="92" stroke="#1a365d" stroke-width="1.5" marker-end="url(#ch1)"/>
  <text x="207" y="80" font-size="11" fill="#1a365d">∂z/∂v</text>
  <circle cx="110" cy="105" r="18" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="105" y="110" font-size="13">u</text>
  <circle cx="250" cy="105" r="18" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="245" y="110" font-size="13">v</text>
  <line x1="100" y1="120" x2="60" y2="155" stroke="#1a365d" stroke-width="1.5" marker-end="url(#ch1)"/>
  <line x1="115" y1="123" x2="170" y2="155" stroke="#1a365d" stroke-width="1.5" marker-end="url(#ch1)"/>
  <line x1="245" y1="123" x2="195" y2="155" stroke="#1a365d" stroke-width="1.5" marker-end="url(#ch1)"/>
  <line x1="260" y1="120" x2="310" y2="155" stroke="#1a365d" stroke-width="1.5" marker-end="url(#ch1)"/>
  <circle cx="50" cy="170" r="16" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="46" y="175" font-size="13">x</text>
  <circle cx="180" cy="170" r="16" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="176" y="175" font-size="13">y</text>
  <circle cx="320" cy="170" r="16" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="316" y="175" font-size="13">y</text>
  <text x="35" y="20" font-size="11" fill="#444">∂z/∂x = (∂z/∂u)(∂u/∂x) + (∂z/∂v)(∂v/∂x) 所有路径相加</text>
</svg>
<figcaption>图 9.4.2 链式法则树状图:$z\to u,v\to x$ 有 2 条路径,每条路径"上游导数 $\times$ 下游导数" → 全部相加得到 $\partial z/\partial x$。</figcaption>
::endsvg

'''),

    # ch9 9.3 切平面贴近曲面 (局部线性近似)
    ('chapter09-multivariate.md', '### 9.3.3 全微分的近似计算应用', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 30 170 Q 100 50 200 100 Q 280 130 340 80" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="35" y="35" font-size="12" fill="#1a365d">原函数 z=f(x,y)</text>
  <line x1="130" y1="118" x2="270" y2="80" stroke="#c2410c" stroke-width="2" stroke-dasharray="5 3"/>
  <text x="170" y="78" font-size="11" fill="#c2410c">切平面 (线性近似)</text>
  <circle cx="200" cy="100" r="4" fill="#2d6e2d"/>
  <text x="208" y="98" font-size="11" fill="#2d6e2d">P₀</text>
  <path d="M 130 118 L 130 130 M 270 80 L 270 92" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <text x="170" y="180" font-size="11" fill="#444">局部 |x-x₀|,|y-y₀| 小时, 切平面 ≈ 曲面 (误差 o(ρ))</text>
</svg>
<figcaption>图 9.3.1 全微分 = 切平面贴近曲面:在 $P_0$ 附近 $f$ 与切平面的差是 $o(\rho)$ 高阶小量,所以「可微」相当于「能用切平面近似」。</figcaption>
::endsvg

'''),

    # ch10 10.2 X-型 Y-型 区域 + Fubini 切片
    ('chapter10-multiple-integrals.md', '### 10.2.1 Fubini 定理与区域类型', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 30 170 L 30 30 L 170 30 L 170 170 Z" fill="none"/>
  <path d="M 40 160 Q 80 50 110 60 Q 140 70 160 160 Z" fill="#eef4fb" stroke="#1a365d" stroke-width="1.6"/>
  <line x1="90" y1="32" x2="90" y2="160" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="92" y="50" font-size="11" fill="#c2410c">x=x₀ 截一段</text>
  <text x="50" y="190" font-size="11" fill="#1a365d">X-型 (竖切)</text>
  <text x="50" y="120" font-size="12" font-style="italic" fill="#1a365d">D</text>
  <path d="M 200 170 L 200 30 L 340 30 L 340 170 Z" fill="none"/>
  <path d="M 210 50 Q 270 70 330 55 Q 340 100 320 140 Q 270 155 210 140 Z" fill="#fef6e4" stroke="#8b6f1c" stroke-width="1.6"/>
  <line x1="205" y1="100" x2="338" y2="100" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="312" y="96" font-size="11" fill="#c2410c">y=y₀</text>
  <text x="220" y="190" font-size="11" fill="#8b6f1c">Y-型 (横切)</text>
  <text x="265" y="120" font-size="12" font-style="italic" fill="#8b6f1c">D</text>
</svg>
<figcaption>图 10.2.4 X-型 vs Y-型区域:X-型每条竖线截 $D$ 一段(Fubini 先 $y$ 后 $x$);Y-型每条水平线截一段(先 $x$ 后 $y$)。</figcaption>
::endsvg

'''),

    # ch11 11.3 Green 面积公式 (椭圆例子)
    ('chapter11-line-surface-integrals.md', '### 11.3.3 直接推论', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="gr1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="100" ry="55" fill="#fef6e4" fill-opacity="0.6" stroke="#1a365d" stroke-width="2"/>
  <path d="M 280 100 A 100 55 0 0 1 220 153" fill="none" stroke="#1a365d" stroke-width="2.5" marker-end="url(#gr1)"/>
  <line x1="80" y1="100" x2="280" y2="100" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="180" y1="45" x2="180" y2="155" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="280" y="95" font-size="11" fill="#888">a</text>
  <text x="184" y="50" font-size="11" fill="#888">b</text>
  <text x="195" y="105" font-size="11" fill="#1a365d">πab</text>
  <text x="30" y="190" font-size="11" fill="#444">S = (1/2)∮ x dy − y dx (∂D 逆时针), 椭圆得 πab</text>
</svg>
<figcaption>图 11.3.3 用 Green 面积公式 $S=\frac{1}{2}\oint(x\,dy-y\,dx)$ 算椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 的面积 = $\pi ab$。</figcaption>
::endsvg

'''),

    # ch12 12.1 几何级数 r=1/2 几何累加
    ('chapter12-infinite-series.md', '### 12.1.3 两个关键的"参考级数"', r'''
::svg
<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="40" width="280" height="60" fill="none" stroke="#888" stroke-width="1.5"/>
  <rect x="20" y="40" width="140" height="60" fill="#eef4fb" stroke="#1a365d" stroke-width="1"/>
  <text x="78" y="75" font-size="13" fill="#1a365d">1/2</text>
  <rect x="160" y="40" width="70" height="60" fill="#fef6e4" stroke="#8b6f1c" stroke-width="1"/>
  <text x="183" y="75" font-size="12" fill="#8b6f1c">1/4</text>
  <rect x="230" y="40" width="35" height="60" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1"/>
  <text x="237" y="75" font-size="11" fill="#2d6e2d">1/8</text>
  <rect x="265" y="40" width="17" height="60" fill="#fde2e2" stroke="#b91c1c" stroke-width="1"/>
  <rect x="282" y="40" width="9" height="60" fill="#888" opacity="0.5"/>
  <text x="50" y="130" font-size="12" fill="#444">1/2 + 1/4 + 1/8 + ... = 1 (Zeno 悖论解决)</text>
  <text x="50" y="30" font-size="11" fill="#888">总宽 1</text>
</svg>
<figcaption>图 12.1.2 几何级数 $\sum_{n=1}^\infty 1/2^n=1$ 可视化:每次取剩余的一半,无穷次后填满单位长度 — 这就是阿喀琉斯追上乌龟的几何。</figcaption>
::endsvg

'''),

    # ch11 11.0 三大公式总图 (大蓝图)
    ('chapter11-line-surface-integrals.md', '### 11.0.1 全章地图:四类积分 + 三大公式', r'''
::svg
<svg viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ar3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <line x1="20" y1="100" x2="100" y2="100" stroke="#1a365d" stroke-width="2.5"/>
  <circle cx="20" cy="100" r="3" fill="#c2410c"/>
  <circle cx="100" cy="100" r="3" fill="#c2410c"/>
  <text x="22" y="135" font-size="11" fill="#1a365d">NL: 区间↔端点</text>
  <rect x="135" y="75" width="55" height="50" fill="#eef4fb" stroke="#1a365d" stroke-width="2"/>
  <text x="140" y="135" font-size="11" fill="#1a365d">Green: 区域↔闭曲线</text>
  <path d="M 230 80 Q 270 60 310 90 Q 280 130 230 110 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="2"/>
  <text x="235" y="135" font-size="11" fill="#8b6f1c">Stokes: 曲面↔边界</text>
  <ellipse cx="380" cy="100" rx="40" ry="22" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="2"/>
  <text x="345" y="135" font-size="11" fill="#2d6e2d">Gauss: 立体↔闭曲面</text>
  <line x1="100" y1="100" x2="135" y2="100" stroke="#444" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#ar3)"/>
  <line x1="195" y1="100" x2="225" y2="100" stroke="#444" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#ar3)"/>
  <line x1="310" y1="100" x2="340" y2="100" stroke="#444" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#ar3)"/>
  <text x="100" y="30" font-size="13" font-weight="bold" fill="#1a365d">∫_∂M ω = ∫_M dω (统一)</text>
  <text x="100" y="180" font-size="11" fill="#666">维度递增: 1d → 2d → 2d 嵌 3d → 3d</text>
</svg>
<figcaption>图 11.0.1 四大边界 $\to$ 内部公式同源:Newton-Leibniz / Green / Stokes / Gauss 都是 $\int_{\partial M}\omega=\int_M d\omega$ 在维度 1,2,2,3 下的具体化。</figcaption>
::endsvg

'''),

    # ch8 8.2 数量积投影 (功 W=F·d)
    ('chapter08-vectors.md', '### 8.2.1 数量积(点乘 / 内积)', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="dt1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="dt2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <line x1="40" y1="130" x2="260" y2="130" stroke="#1a365d" stroke-width="2.5" marker-end="url(#dt1)"/>
  <text x="265" y="135" font-size="13" font-style="italic" fill="#1a365d">位移 d⃗</text>
  <line x1="40" y1="130" x2="170" y2="50" stroke="#c2410c" stroke-width="2.5" marker-end="url(#dt2)"/>
  <text x="175" y="50" font-size="13" font-style="italic" fill="#c2410c">力 F⃗</text>
  <line x1="170" y1="50" x2="170" y2="130" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <line x1="40" y1="130" x2="170" y2="130" stroke="#2d6e2d" stroke-width="4"/>
  <text x="80" y="150" font-size="12" fill="#2d6e2d">|F⃗|cosθ (有效分量)</text>
  <path d="M 70 130 A 30 30 0 0 0 60 110" fill="none" stroke="#444" stroke-width="0.8"/>
  <text x="65" y="118" font-size="11" fill="#444">θ</text>
  <text x="30" y="170" font-size="11" fill="#444">W = F⃗·d⃗ = |F⃗||d⃗|cosθ (做功)</text>
</svg>
<figcaption>图 8.2.3 数量积物理意义:力沿位移做的功 $W=\vec{F}\cdot\vec{d}=|\vec{F}|\,|\vec{d}|\cos\theta$。垂直力($\theta=90°$)做功为零。</figcaption>
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
