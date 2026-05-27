"""第十五批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.8 Lagrange 乘子 (约束极值几何)
    ('chapter09-multivariate.md', '### 9.8.5 与凸优化、机器学习的联系', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="lg1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="lg2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <ellipse cx="200" cy="100" rx="130" ry="70" fill="none" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="200" cy="100" rx="90" ry="50" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <ellipse cx="200" cy="100" rx="50" ry="28" fill="none" stroke="#1a365d" stroke-width="1.4"/>
  <text x="35" y="50" font-size="11" fill="#1a365d">f 等高线</text>
  <path d="M 60 180 Q 200 150 340 180" fill="none" stroke="#c2410c" stroke-width="2"/>
  <text x="270" y="200" font-size="11" fill="#c2410c">约束 g(x,y)=0</text>
  <circle cx="200" cy="150" r="4" fill="#2d6e2d"/>
  <text x="208" y="155" font-size="12" font-weight="bold" fill="#2d6e2d">最优 P*</text>
  <line x1="200" y1="150" x2="200" y2="115" stroke="#c2410c" stroke-width="1.5" marker-end="url(#lg1)"/>
  <line x1="200" y1="150" x2="200" y2="185" stroke="#2d6e2d" stroke-width="1.5" marker-end="url(#lg2)"/>
  <text x="155" y="125" font-size="11" fill="#c2410c">∇f</text>
  <text x="155" y="180" font-size="11" fill="#2d6e2d">λ∇g</text>
  <text x="35" y="30" font-size="11" fill="#444">∇f = λ∇g (两族曲线相切处 = 约束极值)</text>
</svg>
<figcaption>图 9.8.3 Lagrange 乘子法几何:目标 $f$ 等高线与约束 $g=0$ 相切处即极值,梯度共线 $\nabla f=\lambda\nabla g$ — 约束优化 / SVM / 经济均衡的基础。</figcaption>
::endsvg

'''),

    # ch9 9.10 SVD 几何 (主成分)
    ('chapter09-multivariate.md', '### 9.10.4 推广:多元线性回归与非线性拟合', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="sv1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="sv2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="120" ry="40" fill="none" stroke="#1a365d" stroke-width="1.5" transform="rotate(-25 180 100)"/>
  <circle cx="100" cy="135" r="3" fill="#c2410c" opacity="0.7"/>
  <circle cx="130" cy="115" r="3" fill="#c2410c" opacity="0.7"/>
  <circle cx="180" cy="100" r="3" fill="#c2410c" opacity="0.7"/>
  <circle cx="230" cy="85" r="3" fill="#c2410c" opacity="0.7"/>
  <circle cx="260" cy="70" r="3" fill="#c2410c" opacity="0.7"/>
  <line x1="80" y1="138" x2="280" y2="62" stroke="#1a365d" stroke-width="2" marker-end="url(#sv1)"/>
  <text x="285" y="60" font-size="12" font-style="italic" fill="#1a365d">v₁ (主成分)</text>
  <line x1="180" y1="100" x2="220" y2="160" stroke="#2d6e2d" stroke-width="1.5" stroke-dasharray="3 2" marker-end="url(#sv2)"/>
  <text x="225" y="160" font-size="11" fill="#2d6e2d">v₂ (副)</text>
  <text x="30" y="190" font-size="11" fill="#666">SVD: X = UΣV^T, v₁ 解释最多方差; 协方差椭圆 = OLS 几何</text>
</svg>
<figcaption>图 9.10.4 SVD / PCA 几何:数据点云在椭圆内,主成分 $v_1$ 沿长轴(方差最大方向);PCA 投影 = 沿 $v_1$ 一维压缩。</figcaption>
::endsvg

'''),

    # ch10 10.5 Laplace 变换 (跟 Γ 关系)
    ('chapter10-multiple-integrals.md', '### 10.5.3 广义含参积分', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="lp1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="40" width="120" height="80" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="35" y="70" font-size="13" font-weight="bold" fill="#1a365d">时域 f(t)</text>
  <text x="35" y="95" font-size="11" fill="#1a365d">(ODE 难解)</text>
  <line x1="140" y1="80" x2="220" y2="80" stroke="#1a365d" stroke-width="2" marker-end="url(#lp1)"/>
  <text x="148" y="73" font-size="11" fill="#888">∫₀^∞ e^{-st}f(t) dt</text>
  <rect x="220" y="40" width="120" height="80" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="235" y="70" font-size="13" font-weight="bold" fill="#8b6f1c">s 域 F(s)</text>
  <text x="235" y="95" font-size="11" fill="#8b6f1c">(代数易解)</text>
  <text x="35" y="160" font-size="11" fill="#444">Laplace 变换: 微分方程 → 代数方程</text>
  <text x="35" y="180" font-size="11" fill="#666">L[t^n] = n!/s^{n+1}, L[1] = 1/s, L[e^at] = 1/(s-a)</text>
</svg>
<figcaption>图 10.5.4 Laplace 变换 = 含参广义积分:把时域 ODE 化为 $s$ 域代数方程;线性电路 / 控制论 / 信号处理的核心工具。</figcaption>
::endsvg

'''),

    # ch11 11.5 流体散度 不可压 vs 可压
    ('chapter11-line-surface-integrals.md', '### 11.5.5 例题', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="fl1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="fl2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <rect x="30" y="50" width="130" height="100" fill="#eef4fb" stroke="#1a365d" stroke-width="1.2"/>
  <text x="50" y="40" font-size="11" font-weight="bold" fill="#1a365d">不可压 ∇·v=0</text>
  <line x1="35" y1="80" x2="80" y2="80" stroke="#1a365d" stroke-width="1.5" marker-end="url(#fl1)"/>
  <line x1="35" y1="100" x2="80" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#fl1)"/>
  <line x1="35" y1="120" x2="80" y2="120" stroke="#1a365d" stroke-width="1.5" marker-end="url(#fl1)"/>
  <line x1="115" y1="80" x2="155" y2="80" stroke="#1a365d" stroke-width="1.5" marker-end="url(#fl1)"/>
  <line x1="115" y1="100" x2="155" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#fl1)"/>
  <line x1="115" y1="120" x2="155" y2="120" stroke="#1a365d" stroke-width="1.5" marker-end="url(#fl1)"/>
  <text x="65" y="170" font-size="11" fill="#1a365d">流入 = 流出</text>
  <rect x="200" y="50" width="130" height="100" fill="#fef6e4" stroke="#c9a227" stroke-width="1.2"/>
  <text x="215" y="40" font-size="11" font-weight="bold" fill="#c2410c">有源 ∇·v>0</text>
  <line x1="265" y1="100" x2="220" y2="80" stroke="#c2410c" stroke-width="1.5" marker-end="url(#fl2)"/>
  <line x1="265" y1="100" x2="310" y2="80" stroke="#c2410c" stroke-width="1.5" marker-end="url(#fl2)"/>
  <line x1="265" y1="100" x2="220" y2="120" stroke="#c2410c" stroke-width="1.5" marker-end="url(#fl2)"/>
  <line x1="265" y1="100" x2="310" y2="120" stroke="#c2410c" stroke-width="1.5" marker-end="url(#fl2)"/>
  <circle cx="265" cy="100" r="3" fill="#c2410c"/>
  <text x="235" y="170" font-size="11" fill="#c2410c">点源 (汽泡)</text>
</svg>
<figcaption>图 11.5.6 不可压流体($\nabla\cdot\vec{v}=0$):水流入 = 水流出 vs 有源场($>0$):每个点都"冒出"流体 — N-S 方程的根本区分。</figcaption>
::endsvg

'''),

    # ch12 12.4 比值 vs 根值 (强弱关系)
    ('chapter12-infinite-series.md', '### 12.4.2 计算 $R$ 的两种公式', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="30" y="40" width="120" height="100" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="50" y="65" font-size="13" font-weight="bold" fill="#1a365d">Cauchy-Hadamard</text>
  <text x="50" y="90" font-size="12">1/R = limsup ⁿ√|aₙ|</text>
  <text x="50" y="115" font-size="11" fill="#2d6e2d">永远成立</text>
  <text x="155" y="93" font-size="20" fill="#666">⊃</text>
  <rect x="180" y="40" width="120" height="100" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="195" y="65" font-size="13" font-weight="bold" fill="#8b6f1c">d'Alembert 比值</text>
  <text x="200" y="90" font-size="12">R = lim |aₙ/aₙ₊₁|</text>
  <text x="200" y="115" font-size="11" fill="#b91c1c">极限存在时</text>
  <text x="30" y="170" font-size="11" fill="#666">根值更强: 比值跳变时仍可用 (取 limsup 求 R)</text>
</svg>
<figcaption>图 12.4.5 Cauchy-Hadamard(根值)vs d'Alembert(比值):根值版用 $\limsup$ 永远成立,比值版要求极限存在,二者求 $R$ 相同(若都给出)。</figcaption>
::endsvg

'''),

    # ch12 补充: ζ 函数解析延拓 临界带
    ('chapter12-infinite-series.md', '### 12.0.6 怎么读这章', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="100" x2="330" y2="100" stroke="#888" stroke-width="1"/>
  <line x1="100" y1="20" x2="100" y2="180" stroke="#888" stroke-width="1"/>
  <text x="335" y="105" font-size="11" fill="#888">Re(s)</text>
  <text x="105" y="20" font-size="11" fill="#888">Im(s)</text>
  <text x="80" y="115" font-size="11" fill="#888">0</text>
  <text x="195" y="115" font-size="11" fill="#1a365d" font-weight="bold">1/2</text>
  <text x="240" y="115" font-size="11" fill="#888">1</text>
  <rect x="100" y="20" width="160" height="160" fill="#fef6e4" fill-opacity="0.4" stroke="#c9a227" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="115" y="40" font-size="11" fill="#8b6f1c">临界带 0<Re(s)<1</text>
  <line x1="200" y1="20" x2="200" y2="180" stroke="#c2410c" stroke-width="2"/>
  <text x="205" y="40" font-size="11" font-weight="bold" fill="#c2410c">临界线 Re(s)=1/2</text>
  <circle cx="200" cy="55" r="3" fill="#c2410c"/>
  <circle cx="200" cy="75" r="3" fill="#c2410c"/>
  <circle cx="200" cy="125" r="3" fill="#c2410c"/>
  <circle cx="200" cy="145" r="3" fill="#c2410c"/>
  <rect x="260" y="92" width="60" height="16" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1"/>
  <text x="265" y="103" font-size="11" fill="#2d6e2d">∑1/nˢ 收敛区</text>
  <text x="30" y="195" font-size="10" fill="#666">Riemann 猜想: 所有非平凡零点都在 Re(s)=1/2 (Clay 千年大奖)</text>
</svg>
<figcaption>图 12.0.2 Riemann ζ 函数:$\zeta(s)=\sum 1/n^s$ 仅在 $\mathrm{Re}(s)>1$ 收敛,通过解析延拓扩到整个复平面除 $s=1$ 极点;非平凡零点位置 = 千禧 7 大难题之一。</figcaption>
::endsvg

'''),

    # ch11 11.6 磁力线 (向量场流线)
    ('chapter11-line-surface-integrals.md', '### 11.6.3 旋度的不依赖坐标定义', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ml1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <line x1="180" y1="20" x2="180" y2="180" stroke="#1a365d" stroke-width="3"/>
  <text x="185" y="22" font-size="12" fill="#1a365d">导线 I</text>
  <circle cx="180" cy="100" r="30" fill="none" stroke="#c2410c" stroke-width="1.5"/>
  <circle cx="180" cy="100" r="50" fill="none" stroke="#c2410c" stroke-width="1.2"/>
  <circle cx="180" cy="100" r="80" fill="none" stroke="#c2410c" stroke-width="1" opacity="0.7"/>
  <path d="M 250 95 A 70 70 0 0 1 250 105" fill="none" stroke="#c2410c" stroke-width="2" marker-end="url(#ml1)"/>
  <path d="M 220 105 A 40 40 0 0 1 220 115" fill="none" stroke="#c2410c" stroke-width="2" marker-end="url(#ml1)"/>
  <text x="265" y="105" font-size="11" fill="#c2410c">B⃗ 磁力线</text>
  <text x="35" y="195" font-size="11" fill="#666">Biot-Savart: 导线电流产生绕轴磁场, 越远越弱 (~1/r)</text>
</svg>
<figcaption>图 11.6.6 直线电流的磁力线:同心圆围绕导线,方向由右手定则 — 旋度 $\nabla\times\vec{B}=\mu_0\vec{J}$ 在 Ampère 环路中的几何源。</figcaption>
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
