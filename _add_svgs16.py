"""第十六批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.6 梯度下降轨迹 (凸 vs 鞍点)
    ('chapter09-multivariate.md', '### 9.6.4 与 AI 优化的联系', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="gd1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="gd2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="100" cy="120" rx="60" ry="50" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <ellipse cx="100" cy="120" rx="40" ry="33" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <ellipse cx="100" cy="120" rx="20" ry="16" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <circle cx="100" cy="120" r="3" fill="#1a365d"/>
  <path d="M 35 80 L 55 100 L 75 110 L 90 118 L 98 119 L 100 120" fill="none" stroke="#1a365d" stroke-width="2" marker-end="url(#gd1)"/>
  <circle cx="35" cy="80" r="3" fill="#1a365d"/>
  <text x="20" y="195" font-size="11" fill="#1a365d">凸: 收敛快</text>
  <circle cx="270" cy="120" r="3" fill="#c2410c"/>
  <path d="M 270 120 Q 285 80 240 60 Q 200 50 280 70 Q 320 90 300 110" fill="none" stroke="#c2410c" stroke-width="2" marker-end="url(#gd2)"/>
  <text x="220" y="195" font-size="11" fill="#c2410c">非凸: SGD 噪声跳出鞍点</text>
  <text x="200" y="30" font-size="11" fill="#888">SGD 在高维非凸优化中比 Newton 更好用</text>
</svg>
<figcaption>图 9.6.5 梯度下降轨迹:凸损失下沿等高线垂直收敛快;非凸 + SGD 随机噪声反而能跳出鞍点(deep learning 实践证据)。</figcaption>
::endsvg

'''),

    # ch10 10.4 蒙特卡洛积分 (随机点估面积)
    ('chapter10-multiple-integrals.md', '### 10.4.1 几何量:面积、体积、曲面面积', r'''
::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="40" y="20" width="160" height="160" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <circle cx="120" cy="100" r="80" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <circle cx="90" cy="50" r="2.5" fill="#2d6e2d"/>
  <circle cx="130" cy="80" r="2.5" fill="#2d6e2d"/>
  <circle cx="160" cy="120" r="2.5" fill="#2d6e2d"/>
  <circle cx="80" cy="140" r="2.5" fill="#2d6e2d"/>
  <circle cx="170" cy="60" r="2.5" fill="#2d6e2d"/>
  <circle cx="50" cy="100" r="2.5" fill="#2d6e2d"/>
  <circle cx="130" cy="160" r="2.5" fill="#2d6e2d"/>
  <circle cx="60" cy="30" r="2.5" fill="#b91c1c"/>
  <circle cx="190" cy="170" r="2.5" fill="#b91c1c"/>
  <circle cx="180" cy="30" r="2.5" fill="#b91c1c"/>
  <text x="225" y="55" font-size="11" fill="#2d6e2d">圆内 7 个</text>
  <text x="225" y="75" font-size="11" fill="#b91c1c">圆外 3 个</text>
  <text x="220" y="115" font-size="12" font-weight="bold">π ≈ 4×(7/10)</text>
  <text x="220" y="135" font-size="12" font-weight="bold">= 2.8</text>
  <text x="220" y="160" font-size="11" fill="#666">N→∞ 收敛到 π</text>
</svg>
<figcaption>图 10.4.5 蒙特卡洛积分估 $\pi$:在 $[-1,1]^2$ 随机撒点,落圆内比例 $\to\pi/4$ — 高维积分跑不动时的实用方法(Bayesian 推断 / 路径积分)。</figcaption>
::endsvg

'''),

    # ch11 11.2 路径无关 (势场 + 等势线)
    ('chapter11-line-surface-integrals.md', '### 11.2.3 一般参数化与定向', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ps1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="130" ry="70" fill="none" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="180" cy="100" rx="90" ry="48" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <ellipse cx="180" cy="100" rx="50" ry="27" fill="none" stroke="#1a365d" stroke-width="1.4"/>
  <text x="35" y="40" font-size="11" fill="#1a365d">等势线 φ=c</text>
  <line x1="180" y1="100" x2="240" y2="65" stroke="#c2410c" stroke-width="1.5" marker-end="url(#ps1)"/>
  <line x1="240" y1="65" x2="180" y2="40" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="180" y1="40" x2="120" y2="60" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="120" y1="60" x2="100" y2="100" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="100" y1="100" x2="120" y2="130" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="120" y1="130" x2="180" y2="100" stroke="#c2410c" stroke-width="1.5"/>
  <text x="35" y="190" font-size="11" fill="#444">∮F·dr=0 (保守场闭路无功); F=∇φ ⇒ 任意路径=Δφ</text>
</svg>
<figcaption>图 11.2.3 保守力场环路 = 0:沿任意闭路径回到起点 = 势能不变 → 重力 / 弹簧力 / 库仑力都满足。摩擦力非保守(消耗能量)。</figcaption>
::endsvg

'''),

    # ch11 11.4 旋转曲面参数化 (圆锥)
    ('chapter11-line-surface-integrals.md', '### 11.4.4 一般参数化 $\vec{r}=\vec{r}(u,v)$ 的面积元素', r'''
::svg
<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="160" y1="200" x2="160" y2="40" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="165" y="40" font-size="11" fill="#888">z</text>
  <path d="M 160 40 L 100 200 L 220 200 Z" fill="#fef6e4" fill-opacity="0.6" stroke="#c9a227" stroke-width="1.8"/>
  <ellipse cx="160" cy="200" rx="60" ry="14" fill="#fef6e4" stroke="#c9a227" stroke-width="1.2" stroke-dasharray="3 2"/>
  <text x="40" y="195" font-size="11" fill="#8b6f1c">圆锥 z=√(x²+y²)</text>
  <text x="35" y="40" font-size="11" fill="#444">侧面积 = √2·π·R² (z_x²+z_y²=1)</text>
</svg>
<figcaption>图 11.4.7 圆锥 $z=\sqrt{x^2+y^2}$ 侧面:$\sqrt{1+z_x^2+z_y^2}=\sqrt{2}$,$0\le z\le 1$ 部分侧面积 $=\sqrt{2}\,\pi$。</figcaption>
::endsvg

'''),

    # ch12 12.2 积分判别 (面积比较)
    ('chapter12-infinite-series.md', '### 12.2.4 积分判别法(Cauchy-MacLaurin)', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="160" x2="330" y2="160" stroke="#888" stroke-width="1"/>
  <line x1="30" y1="20" x2="30" y2="180" stroke="#888" stroke-width="1"/>
  <text x="335" y="165" font-size="11" fill="#888">x</text>
  <text x="20" y="20" font-size="11" fill="#888">f</text>
  <path d="M 30 30 Q 80 90 150 130 Q 220 150 330 158" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="220" y="55" font-size="12" font-weight="bold" fill="#c2410c">∫_1^∞ f(x) dx</text>
  <rect x="40" y="40" width="40" height="120" fill="#1a365d" fill-opacity="0.25" stroke="#1a365d" stroke-width="0.8"/>
  <rect x="80" y="65" width="40" height="95" fill="#1a365d" fill-opacity="0.25" stroke="#1a365d" stroke-width="0.8"/>
  <rect x="120" y="95" width="40" height="65" fill="#1a365d" fill-opacity="0.25" stroke="#1a365d" stroke-width="0.8"/>
  <rect x="160" y="120" width="40" height="40" fill="#1a365d" fill-opacity="0.25" stroke="#1a365d" stroke-width="0.8"/>
  <rect x="200" y="135" width="40" height="25" fill="#1a365d" fill-opacity="0.25" stroke="#1a365d" stroke-width="0.8"/>
  <text x="160" y="35" font-size="12" font-weight="bold" fill="#1a365d">∑ f(n)</text>
  <text x="40" y="190" font-size="11" fill="#666">单调递减 f: ∑ 与 ∫ 同敛散 (上下夹挤)</text>
</svg>
<figcaption>图 12.2.4 积分判别:单调减 $f$ 时,$\sum f(n)$ 与 $\int_1^\infty f$ 上下夹挤 → 同收敛或同发散。$p$-级数 $\sum 1/n^p$ 由此严格证。</figcaption>
::endsvg

'''),

    # ch9 9.0 微分算子三件套 (梯度/散度/旋度)
    ('chapter09-multivariate.md', '### 9.0.2 核心定理速查', r'''
::svg
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="40" width="100" height="60" rx="6" fill="#eef4fb" stroke="#1a365d" stroke-width="1.8"/>
  <text x="35" y="65" font-size="13" font-weight="bold" fill="#1a365d">∇f 梯度</text>
  <text x="25" y="85" font-size="11" fill="#1a365d">标量 → 向量</text>
  <rect x="140" y="40" width="100" height="60" rx="6" fill="#fef6e4" stroke="#c9a227" stroke-width="1.8"/>
  <text x="155" y="65" font-size="13" font-weight="bold" fill="#8b6f1c">∇·F 散度</text>
  <text x="145" y="85" font-size="11" fill="#8b6f1c">向量 → 标量</text>
  <rect x="260" y="40" width="100" height="60" rx="6" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.8"/>
  <text x="275" y="65" font-size="13" font-weight="bold" fill="#b91c1c">∇×F 旋度</text>
  <text x="265" y="85" font-size="11" fill="#b91c1c">向量 → 向量</text>
  <text x="30" y="130" font-size="11" fill="#444">同一算子 ∇ = (∂/∂x, ∂/∂y, ∂/∂z) 不同搭配:</text>
  <text x="30" y="150" font-size="11" fill="#666">∇·∇=∇²(拉普拉斯) / ∇·(∇×F)=0 / ∇×(∇f)=0</text>
</svg>
<figcaption>图 9.0.3 ∇ 算子三件套:梯度(标量→向量)/ 散度(向量→标量)/ 旋度(向量→向量),组合得 Laplacian 与两条 $d^2=0$ 恒等式。</figcaption>
::endsvg

'''),

    # ch10 10.4 联合 vs 边缘分布
    ('chapter10-multiple-integrals.md', '### 10.4.5 概率应用:边缘分布、期望、协方差', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="80" y="40" width="120" height="120" fill="#eef4fb" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="140" cy="100" rx="40" ry="35" fill="#1a365d" fill-opacity="0.3"/>
  <ellipse cx="140" cy="100" rx="25" ry="20" fill="#1a365d" fill-opacity="0.5"/>
  <text x="115" y="180" font-size="11" fill="#1a365d">联合 f(x,y)</text>
  <path d="M 80 170 Q 140 145 200 170" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="100" y="195" font-size="11" fill="#c2410c">边缘 f_X(x) (∫ f dy)</text>
  <path d="M 60 160 Q 35 100 60 40" fill="none" stroke="#2d6e2d" stroke-width="2"/>
  <text x="20" y="35" font-size="11" fill="#2d6e2d">边缘 f_Y(y)</text>
  <text x="240" y="60" font-size="11" fill="#444">f_X(x) = ∫f(x,y) dy</text>
  <text x="240" y="85" font-size="11" fill="#444">f_Y(y) = ∫f(x,y) dx</text>
  <text x="240" y="125" font-size="11" fill="#666">"压扁": 联合密度沿一个方向积分掉</text>
</svg>
<figcaption>图 10.4.6 联合密度 → 边缘密度:把 2D 联合分布沿 $y$ 积分得 $f_X$,沿 $x$ 积分得 $f_Y$ — 几何上"压扁"到一维。Bayesian 边缘化的基本动作。</figcaption>
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
