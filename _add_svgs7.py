"""第七批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.6 方向导数 (任意方向 + 切线斜率)
    ('chapter09-multivariate.md', '### 9.6.1 方向导数', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="dd1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="180" cy="120" rx="130" ry="75" fill="none" stroke="#888" stroke-width="0.7" stroke-dasharray="3 2"/>
  <ellipse cx="180" cy="120" rx="85" ry="48" fill="none" stroke="#888" stroke-width="0.7" stroke-dasharray="3 2"/>
  <ellipse cx="180" cy="120" rx="45" ry="25" fill="none" stroke="#888" stroke-width="0.7" stroke-dasharray="3 2"/>
  <circle cx="180" cy="120" r="3" fill="#1a365d"/>
  <text x="186" y="115" font-size="11" fill="#1a365d">P₀</text>
  <line x1="180" y1="120" x2="260" y2="65" stroke="#c2410c" stroke-width="2" marker-end="url(#dd1)"/>
  <text x="252" y="60" font-size="11" fill="#c2410c">l⃗ (任意方向)</text>
  <line x1="180" y1="120" x2="245" y2="105" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#dd1)"/>
  <text x="248" y="108" font-size="11" fill="#2d6e2d">∇f (最速)</text>
  <path d="M 230 80 A 30 30 0 0 0 215 110" fill="none" stroke="#444" stroke-width="0.8"/>
  <text x="220" y="100" font-size="11" fill="#444">θ</text>
  <text x="35" y="200" font-size="11" fill="#666">∂f/∂l⃗ = ∇f·l⃗ = |∇f| cosθ</text>
</svg>
<figcaption>图 9.6.3 方向导数:沿任意方向 $\vec{l}$ 的变化率 $=\nabla f\cdot\vec{l}=|\nabla f|\cos\theta$;沿梯度方向($\theta=0$)取最大值。</figcaption>
::endsvg

'''),

    # ch9 9.8 鞍点 3D 视图
    ('chapter09-multivariate.md', '### 9.8.4 例题与高维推广', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 40 130 Q 100 60 180 100 Q 260 140 320 90" fill="none" stroke="#1a365d" stroke-width="2"/>
  <path d="M 60 60 Q 130 100 180 100 Q 240 100 290 150" fill="none" stroke="#8b3a0a" stroke-width="2"/>
  <text x="50" y="50" font-size="11" fill="#1a365d">z=x²−y² 沿 y=0 (碗朝上)</text>
  <text x="190" y="180" font-size="11" fill="#8b3a0a">沿 x=0 (碗朝下)</text>
  <circle cx="180" cy="100" r="5" fill="#c2410c"/>
  <text x="190" y="98" font-size="12" fill="#c2410c">鞍点 ∇f=0</text>
  <text x="30" y="180" font-size="11" fill="#666">同一点: x 方向极小, y 方向极大 — Hessian D<0 不定</text>
</svg>
<figcaption>图 9.8.2 鞍点 $z=x^2-y^2$:沿 $x$ 方向是极小,沿 $y$ 方向是极大,同一点矛盾 = 不定 Hessian。深度学习高维损失景观中鞍点远多于极小。</figcaption>
::endsvg

'''),

    # ch10 10.4 联合概率密度 (二维高斯)
    ('chapter10-multiple-integrals.md', '### 10.4.5 概率应用:边缘分布、期望、协方差', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="180" cy="120" rx="120" ry="75" fill="#eef4fb" fill-opacity="0.3" stroke="#1a365d" stroke-width="0.8" stroke-dasharray="3 2"/>
  <ellipse cx="180" cy="120" rx="80" ry="50" fill="#eef4fb" fill-opacity="0.5" stroke="#1a365d" stroke-width="0.8"/>
  <ellipse cx="180" cy="120" rx="45" ry="28" fill="#1a365d" fill-opacity="0.5" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="180" cy="120" rx="20" ry="13" fill="#1a365d" stroke="#1a365d" stroke-width="1"/>
  <text x="160" y="123" font-size="11" fill="#fff">峰</text>
  <line x1="40" y1="120" x2="320" y2="120" stroke="#888" stroke-width="0.8"/>
  <line x1="180" y1="30" x2="180" y2="210" stroke="#888" stroke-width="0.8"/>
  <path d="M 40 200 Q 120 195 180 165 Q 240 195 320 200" fill="none" stroke="#c2410c" stroke-width="1.8"/>
  <text x="225" y="190" font-size="11" fill="#c2410c">f_X(x) = ∫f(x,y)dy</text>
  <text x="40" y="30" font-size="11" fill="#444">联合密度 f(x,y) 等高线 (二维 Gauss)</text>
</svg>
<figcaption>图 10.4.3 二维 Gauss 联合密度 + 边缘密度:等高线为同心椭圆;边缘密度 $f_X(x)$(下方曲线)= 对 $y$ 积分 = 1D Gauss。</figcaption>
::endsvg

'''),

    # ch11 11.5 散度 (源 + 汇 + 无源)
    ('chapter11-line-surface-integrals.md', '### 11.5.4 Gauss 公式(散度定理)', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="dv1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="dv2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <circle cx="60" cy="100" r="35" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <circle cx="60" cy="100" r="3" fill="#c2410c"/>
  <line x1="60" y1="100" x2="100" y2="100" stroke="#c2410c" marker-end="url(#dv1)"/>
  <line x1="60" y1="100" x2="60" y2="60" stroke="#c2410c" marker-end="url(#dv1)"/>
  <line x1="60" y1="100" x2="60" y2="140" stroke="#c2410c" marker-end="url(#dv1)"/>
  <line x1="60" y1="100" x2="20" y2="100" stroke="#c2410c" marker-end="url(#dv1)"/>
  <text x="35" y="170" font-size="11" fill="#c2410c">∇·F>0 源</text>
  <circle cx="180" cy="100" r="35" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <circle cx="180" cy="100" r="3" fill="#1a365d"/>
  <line x1="220" y1="100" x2="186" y2="100" stroke="#1a365d" marker-end="url(#dv2)"/>
  <line x1="180" y1="60" x2="180" y2="94" stroke="#1a365d" marker-end="url(#dv2)"/>
  <line x1="180" y1="140" x2="180" y2="106" stroke="#1a365d" marker-end="url(#dv2)"/>
  <line x1="140" y1="100" x2="174" y2="100" stroke="#1a365d" marker-end="url(#dv2)"/>
  <text x="155" y="170" font-size="11" fill="#1a365d">∇·F<0 汇</text>
  <circle cx="300" cy="100" r="35" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <line x1="270" y1="80" x2="335" y2="120" stroke="#2d6e2d" stroke-width="1.4"/>
  <line x1="270" y1="120" x2="335" y2="80" stroke="#2d6e2d" stroke-width="1.4"/>
  <text x="270" y="170" font-size="11" fill="#2d6e2d">∇·F=0 无源</text>
</svg>
<figcaption>图 11.5.3 散度物理意义:$\nabla\cdot\vec{F}>0$ 源(向外发射);$<0$ 汇(向内吸收);$=0$ 无源场(局部流入=流出,如不可压流体)。</figcaption>
::endsvg

'''),

    # ch11 11.6 法拉第电磁感应 (磁通变化 → 电动势)
    ('chapter11-line-surface-integrals.md', '### 11.6.4 物理意义:法拉第电磁感应', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="fr1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="fr2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="80" ry="55" fill="#eef4fb" stroke="#1a365d" stroke-width="2"/>
  <line x1="120" y1="60" x2="120" y2="80" stroke="#c2410c" stroke-width="2" marker-end="url(#fr1)"/>
  <line x1="180" y1="55" x2="180" y2="75" stroke="#c2410c" stroke-width="2" marker-end="url(#fr1)"/>
  <line x1="240" y1="60" x2="240" y2="80" stroke="#c2410c" stroke-width="2" marker-end="url(#fr1)"/>
  <line x1="120" y1="120" x2="120" y2="140" stroke="#c2410c" stroke-width="2" marker-end="url(#fr1)"/>
  <line x1="180" y1="125" x2="180" y2="145" stroke="#c2410c" stroke-width="2" marker-end="url(#fr1)"/>
  <line x1="240" y1="120" x2="240" y2="140" stroke="#c2410c" stroke-width="2" marker-end="url(#fr1)"/>
  <text x="140" y="45" font-size="11" fill="#c2410c">B⃗ (变化中)</text>
  <ellipse cx="180" cy="170" rx="100" ry="14" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <line x1="280" y1="170" x2="290" y2="167" stroke="#1a365d" stroke-width="2.5" marker-end="url(#fr2)"/>
  <text x="200" y="195" font-size="11" fill="#1a365d">闭合导线 ∂Σ</text>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="#444">∮ E⃗·dr⃗ = −dΦ_B/dt</text>
</svg>
<figcaption>图 11.6.3 法拉第电磁感应:磁场 $\vec{B}$ 穿过 $\Sigma$ 的磁通量 $\Phi_B$ 随时间变 → 沿闭合导线 $\partial\Sigma$ 产生电动势 emf,由 Stokes + Maxwell 第三条立得。</figcaption>
::endsvg

'''),

    # ch12 12.6 内积空间 (函数当向量, 三角基垂直)
    ('chapter12-infinite-series.md', '### 12.6.1 三角函数系是正交系', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="hl1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="hl2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
    <marker id="hl3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <line x1="180" y1="100" x2="280" y2="100" stroke="#c2410c" stroke-width="2.5" marker-end="url(#hl1)"/>
  <text x="240" y="92" font-size="13" font-style="italic" fill="#c2410c">cos x</text>
  <line x1="180" y1="100" x2="180" y2="30" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#hl2)"/>
  <text x="186" y="50" font-size="13" font-style="italic" fill="#2d6e2d">sin x</text>
  <line x1="180" y1="100" x2="120" y2="160" stroke="#1a365d" stroke-width="2.5" marker-end="url(#hl3)"/>
  <text x="100" y="170" font-size="13" font-style="italic" fill="#1a365d">cos 2x</text>
  <text x="35" y="160" font-size="11" fill="#444">∫_{-π}^{π} sin(nx)cos(mx) dx = 0  (两两正交)</text>
  <text x="35" y="180" font-size="11" fill="#444">→ Fourier 系数 = "函数到基函数的投影"</text>
</svg>
<figcaption>图 12.6.3 函数空间正交基:把 sin, cos, cos2x, ... 当作 $L^2$ 空间里两两垂直的"轴";Fourier 系数 = 函数沿每条轴的投影分量。</figcaption>
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
