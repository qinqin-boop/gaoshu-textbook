"""第九批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.10 Ridge 几何 (椭圆 + L2 球)
    ('chapter09-multivariate.md', '### 9.10.5 与机器学习的关系', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="120" x2="320" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="180" y1="20" x2="180" y2="200" stroke="#888" stroke-width="1"/>
  <text x="325" y="125" font-size="11" fill="#888">β₁</text>
  <text x="185" y="20" font-size="11" fill="#888">β₂</text>
  <ellipse cx="230" cy="70" rx="60" ry="35" fill="none" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="230" cy="70" rx="40" ry="22" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <ellipse cx="230" cy="70" rx="20" ry="11" fill="none" stroke="#1a365d" stroke-width="1"/>
  <circle cx="230" cy="70" r="3" fill="#1a365d"/>
  <text x="237" y="68" font-size="11" fill="#1a365d">OLS 最优</text>
  <circle cx="180" cy="120" r="55" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="115" y="120" font-size="11" fill="#c2410c">L² 球 ‖β‖≤t</text>
  <circle cx="218" cy="79" r="4" fill="#2d6e2d"/>
  <text x="225" y="92" font-size="11" fill="#2d6e2d">Ridge 解</text>
  <text x="30" y="200" font-size="11" fill="#666">Ridge: 在 L² 球内找损失等高线最近点 → 解被拉向原点</text>
</svg>
<figcaption>图 9.10.2 Ridge 回归几何:损失等高线(椭圆)+ L² 约束(圆球)的相切点 = Ridge 解,$\lambda$ 越大 → 球越小 → 解越偏 0。</figcaption>
::endsvg

'''),

    # ch9 9.5 方程组隐函数 (两条曲面交曲线)
    ('chapter09-multivariate.md', '### 9.5.3 方程组 / 隐函数组', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="im1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="140" cy="100" rx="90" ry="60" fill="#eef4fb" fill-opacity="0.5" stroke="#1a365d" stroke-width="1.5"/>
  <text x="60" y="50" font-size="11" fill="#1a365d">F(x,y,u,v)=0</text>
  <ellipse cx="220" cy="100" rx="90" ry="60" fill="#fef6e4" fill-opacity="0.5" stroke="#8b6f1c" stroke-width="1.5"/>
  <text x="240" y="50" font-size="11" fill="#8b6f1c">G(x,y,u,v)=0</text>
  <path d="M 180 50 Q 180 100 180 150" fill="none" stroke="#c2410c" stroke-width="2.5" marker-end="url(#im1)"/>
  <text x="190" y="90" font-size="11" fill="#c2410c">交集: 隐曲面 u=u(x,y), v=v(x,y)</text>
  <text x="40" y="190" font-size="11" fill="#666">∂(F,G)/∂(u,v) ≠ 0 时, 雅可比满秩 → 局部能解出</text>
</svg>
<figcaption>图 9.5.2 方程组隐函数定理:两个曲面 $F=0,G=0$ 相交得曲线/曲面;雅可比 $\partial(F,G)/\partial(u,v)\neq 0$ 时 $u,v$ 局部能解为 $x,y$ 的函数。</figcaption>
::endsvg

'''),

    # ch10 10.5 Feynman 积分号下微分 (经典神技)
    ('chapter10-multiple-integrals.md', '### 10.5.2 含参变量极限的进入积分号', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="40" y="60" width="280" height="80" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="48" y="90" font-size="13" font-family="serif">I(y) = ∫</text>
  <text x="105" y="83" font-size="9">b</text>
  <text x="103" y="98" font-size="9">a</text>
  <text x="115" y="90" font-size="13" font-family="serif">f(x,y) dx</text>
  <line x1="200" y1="70" x2="200" y2="130" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="205" y="88" font-size="13" fill="#c2410c">→ d/dy</text>
  <text x="208" y="120" font-size="13" fill="#c2410c">→ ∫ ∂f/∂y dx</text>
  <text x="40" y="170" font-size="11" fill="#444">Leibniz: 对参数求导可移到积分号下 (f_y 连续时)</text>
  <text x="40" y="190" font-size="11" fill="#666">应用: ∫₀¹(x−1)/lnx dx = ∫₀¹∫₀¹ xᵗ dt dx → ∫₀¹ 1/(t+1) dt = ln 2</text>
</svg>
<figcaption>图 10.5.2 Leibniz 神技:对含参积分按参数求导可"穿进"积分号 — Feynman 用这招把不会算的 $\int e^{-x^2}\cos(2xy)dx$ 化为 ODE 求解。</figcaption>
::endsvg

'''),

    # ch11 11.4 球面分割 ρ²sinφ
    ('chapter11-line-surface-integrals.md', '### 11.4.3 一般参数化 $\vec{r}=\vec{r}(u,v)$ 的面积元素', r'''
::svg
<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="160" cy="110" r="80" fill="#eef4fb" fill-opacity="0.5" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="160" cy="110" rx="80" ry="14" fill="none" stroke="#1a365d" stroke-width="0.8" stroke-dasharray="3 2"/>
  <ellipse cx="160" cy="78" rx="76" ry="13" fill="none" stroke="#888" stroke-width="0.7"/>
  <ellipse cx="160" cy="50" rx="60" ry="10" fill="none" stroke="#888" stroke-width="0.7"/>
  <ellipse cx="160" cy="140" rx="76" ry="13" fill="none" stroke="#888" stroke-width="0.7"/>
  <line x1="160" y1="30" x2="240" y2="120" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <line x1="160" y1="30" x2="80" y2="120" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <path d="M 197 65 L 218 73 L 217 95 L 196 87 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="195" y="55" font-size="11" fill="#8b6f1c">R²sinφ dφ dθ</text>
  <text x="30" y="200" font-size="11" fill="#666">球面参数化 r⃗(φ,θ) = R(sinφcosθ, sinφsinθ, cosφ), dS = R²sinφ</text>
</svg>
<figcaption>图 11.4.4 球面参数化网格 $\vec{r}(\varphi,\theta)$:经纬线划出小四边形,面积 $dS=R^2\sin\varphi\,d\varphi\,d\theta$。两极 $\sin\varphi\to 0$ 网格退化。</figcaption>
::endsvg

'''),

    # ch12 12.2 比值判别图 (ρ < 1 收敛)
    ('chapter12-infinite-series.md', '### 12.2.2 比值判别法(d''Alembert)', r'''
::svg
<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="80" x2="340" y2="80" stroke="#1a365d" stroke-width="1.5"/>
  <line x1="340" y1="80" x2="332" y2="76" stroke="#1a365d"/>
  <line x1="340" y1="80" x2="332" y2="84" stroke="#1a365d"/>
  <line x1="180" y1="68" x2="180" y2="92" stroke="#1a365d" stroke-width="2"/>
  <text x="172" y="105" font-size="13" font-weight="bold" fill="#1a365d">ρ=1</text>
  <rect x="20" y="74" width="160" height="12" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="50" y="65" font-size="11" fill="#2d6e2d">ρ<1 收敛</text>
  <rect x="180" y="74" width="160" height="12" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="220" y="65" font-size="11" fill="#b91c1c">ρ>1 发散</text>
  <text x="138" y="125" font-size="11" fill="#888">ρ=1 失效 (用 Raabe / 积分判别)</text>
  <text x="30" y="145" font-size="11" fill="#444">ρ = lim |a_{n+1}/a_n| 比值判别 (d'Alembert)</text>
</svg>
<figcaption>图 12.2.2 比值判别 $\rho=\lim|a_{n+1}/a_n|$:$\rho<1$ 收敛,$>1$ 发散,$=1$ 临界失效需要更精细的 Raabe / 积分判别。</figcaption>
::endsvg

'''),

    # ch12 12.4 系数唯一性 (f^(n)(0) = n! a_n)
    ('chapter12-infinite-series.md', '### 12.4.4 内部的一致收敛与解析性', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="40" y="35" font-size="13" font-family="serif" fill="#1a365d">f(x) = a₀ + a₁x + a₂x² + a₃x³ + ...</text>
  <line x1="55" y1="50" x2="55" y2="60" stroke="#c2410c"/>
  <text x="40" y="78" font-size="11" fill="#c2410c">f(0)</text>
  <text x="55" y="78" font-size="11" fill="#c2410c">=a₀</text>
  <line x1="95" y1="50" x2="95" y2="60" stroke="#c2410c"/>
  <text x="73" y="100" font-size="11" fill="#c2410c">f'(0)</text>
  <text x="95" y="100" font-size="11" fill="#c2410c">=1!·a₁</text>
  <line x1="143" y1="50" x2="143" y2="60" stroke="#c2410c"/>
  <text x="120" y="122" font-size="11" fill="#c2410c">f''(0)</text>
  <text x="148" y="122" font-size="11" fill="#c2410c">=2!·a₂</text>
  <line x1="200" y1="50" x2="200" y2="60" stroke="#c2410c"/>
  <text x="175" y="144" font-size="11" fill="#c2410c">f⁽ⁿ⁾(0)=n!·aₙ</text>
  <text x="40" y="170" font-size="11" fill="#666">系数 aₙ 由 f 的导数唯一决定 → 两个幂级数和函数同 ⇒ 系数同</text>
</svg>
<figcaption>图 12.4.4 幂级数系数唯一性:对和函数求 $n$ 阶导代 $x=0$,得 $f^{(n)}(0)=n!\,a_n$,逆推系数唯一确定。这是 Taylor 级数定义的根。</figcaption>
::endsvg

'''),

    # ch8 8.0 章节地图
    ('chapter08-vectors.md', '### 8.0.1 全章地图', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="m1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="80" width="80" height="40" rx="5" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="35" y="105" font-size="12" font-weight="bold" fill="#1a365d">8.1 向量</text>
  <line x1="100" y1="100" x2="125" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#m1)"/>
  <rect x="125" y="80" width="80" height="40" rx="5" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="135" y="105" font-size="12" font-weight="bold" fill="#8b6f1c">8.2 点乘叉乘</text>
  <line x1="205" y1="100" x2="230" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#m1)"/>
  <rect x="230" y="40" width="70" height="35" rx="5" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="240" y="63" font-size="11" font-weight="bold" fill="#2d6e2d">8.3 曲面</text>
  <rect x="230" y="80" width="70" height="35" rx="5" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="240" y="103" font-size="11" font-weight="bold" fill="#2d6e2d">8.4 平面</text>
  <rect x="230" y="120" width="70" height="35" rx="5" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="240" y="143" font-size="11" font-weight="bold" fill="#2d6e2d">8.5 直线</text>
  <line x1="300" y1="58" x2="350" y2="58" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="305" y="55" font-size="10" fill="#888">→ §9 切平面</text>
  <line x1="300" y1="100" x2="350" y2="100" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="305" y="98" font-size="10" fill="#888">→ §10 坐标系</text>
  <line x1="300" y1="142" x2="350" y2="142" stroke="#888" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="305" y="140" font-size="10" fill="#888">→ §11 曲面积分</text>
</svg>
<figcaption>图 8.0.1 ch8 学习路径:8.1 向量代数基础 → 8.2 数量积/向量积/混合积 → 8.3/8.4/8.5 曲面/平面/直线几何应用 → 后续章节衔接。</figcaption>
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
