"""第十三批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.0 学习路径补完(已有,改成给"应用"展开)
    ('chapter08-vectors.md', '### 8.0.2 核心代数对象', r'''
::svg
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="20" width="80" height="40" rx="5" fill="#eef4fb" stroke="#1a365d"/>
  <text x="35" y="45" font-size="12" fill="#1a365d">向量 a⃗</text>
  <rect x="20" y="70" width="80" height="40" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="30" y="95" font-size="11" fill="#8b6f1c">数量积 a·b</text>
  <rect x="20" y="120" width="80" height="40" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="30" y="145" font-size="11" fill="#8b6f1c">向量积 a×b</text>
  <line x1="100" y1="40" x2="130" y2="40" stroke="#1a365d" stroke-width="1.5"/>
  <text x="135" y="35" font-size="10" fill="#888">→ §9.6 方向导数</text>
  <line x1="100" y1="90" x2="130" y2="90" stroke="#1a365d" stroke-width="1.5"/>
  <text x="135" y="85" font-size="10" fill="#888">→ §9.7 切平面</text>
  <line x1="100" y1="140" x2="130" y2="140" stroke="#1a365d" stroke-width="1.5"/>
  <text x="135" y="135" font-size="10" fill="#888">→ §10.3 三重雅可比</text>
  <text x="135" y="60" font-size="10" fill="#888">→ §11.4 dS=|r_u×r_v|</text>
  <text x="135" y="110" font-size="10" fill="#888">→ §11.5 通量 F·n</text>
  <text x="135" y="160" font-size="10" fill="#888">→ §11.6 旋度 ∇×F</text>
</svg>
<figcaption>图 8.0.2 ch8 核心对象在后续章节中的具体应用对照。</figcaption>
::endsvg

'''),

    # ch9 9.2 高阶混合偏导 Clairaut 反例
    ('chapter09-multivariate.md', '### 9.2.3 高阶偏导与 Clairaut 定理', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="40" width="160" height="100" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="35" y="65" font-size="13" font-weight="bold" fill="#2d6e2d">大部分工程函数 C²</text>
  <text x="45" y="95" font-size="13" font-weight="bold" fill="#2d6e2d">f_xy = f_yx ✓</text>
  <text x="35" y="125" font-size="11" fill="#444">Clairaut 定理保证</text>
  <rect x="190" y="40" width="160" height="100" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="195" y="65" font-size="13" font-weight="bold" fill="#b91c1c">反例 xy(x²-y²)/(x²+y²)</text>
  <text x="195" y="95" font-size="13" font-weight="bold" fill="#b91c1c">f_xy(0,0) = -1</text>
  <text x="195" y="115" font-size="13" font-weight="bold" fill="#b91c1c">f_yx(0,0) = +1</text>
  <text x="195" y="135" font-size="11" fill="#444">f_xy 不连续 → 失效</text>
  <text x="35" y="170" font-size="11" fill="#666">Clairaut 条件: 混合偏导至少一个连续 → 对称</text>
</svg>
<figcaption>图 9.2.2 Clairaut 定理对比:工程常见 $C^2$ 函数混合偏导对称;反例 $f_{xy}\neq f_{yx}$ 出现于偏导不连续时。</figcaption>
::endsvg

'''),

    # ch10 10.2 雅可比变换 面积放大因子
    ('chapter10-multiple-integrals.md', '### 10.2.4 一般换元公式', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="jc1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="60" width="80" height="80" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="35" y="155" font-size="11" fill="#1a365d">(u,v) 平面 du dv</text>
  <line x1="105" y1="100" x2="155" y2="100" stroke="#1a365d" stroke-width="2" marker-end="url(#jc1)"/>
  <text x="115" y="93" font-size="11" fill="#1a365d">T</text>
  <polygon points="170,60 280,80 290,150 180,140" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="190" y="170" font-size="11" fill="#8b6f1c">(x,y) 平面 |J| du dv</text>
  <text x="30" y="30" font-size="11" fill="#444">∬f dxdy = ∬f(T(u,v))·|J| dudv  (|J|=面积放大因子)</text>
</svg>
<figcaption>图 10.2.5 雅可比变换:$(u,v)$ 小方块映到 $(x,y)$ 平面成平行四边形,$|J|$ 是局部面积放大因子。</figcaption>
::endsvg

'''),

    # ch11 11.4 dS = dxdy/cos α 切平面投影
    ('chapter11-line-surface-integrals.md', '### 11.4.2 显式参数化 $z=z(x,y)$ 的面积元素', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <polygon points="40,160 140,160 160,140 60,140" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="55" y="180" font-size="11" fill="#1a365d">dx dy (xy 平面)</text>
  <polygon points="180,60 280,40 300,110 200,130" fill="#fef6e4" stroke="#c9a227" stroke-width="1.8"/>
  <text x="200" y="100" font-size="12" font-style="italic" fill="#8b6f1c">dS</text>
  <line x1="100" y1="150" x2="240" y2="80" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <path d="M 145 145 A 25 25 0 0 0 130 130" fill="none" stroke="#666" stroke-width="0.8"/>
  <text x="140" y="135" font-size="11" fill="#666">α</text>
  <text x="35" y="30" font-size="11" fill="#444">dS = dxdy / cosα, cosα = 1/√(1+z_x²+z_y²)</text>
</svg>
<figcaption>图 11.4.6 切平面投影:倾斜曲面微元 $dS$ = 投影 $dxdy$ 除以倾角余弦 = $\sqrt{1+z_x^2+z_y^2}\,dxdy$。</figcaption>
::endsvg

'''),

    # ch12 12.6 Dirichlet 核 D_N(u)
    ('chapter12-infinite-series.md', '### 12.6.3 Dirichlet 定理:逐点收敛', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="120" x2="330" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="180" y1="20" x2="180" y2="180" stroke="#888" stroke-width="1"/>
  <text x="335" y="125" font-size="11" fill="#888">u</text>
  <text x="185" y="20" font-size="11" fill="#888">D_N(u)</text>
  <path d="M 30 130 L 50 130 L 60 125 L 70 130 L 80 130 L 100 125 L 130 35 L 180 30 L 230 35 L 260 125 L 280 130 L 290 125 L 300 130 L 310 130 L 330 130" fill="none" stroke="#1a365d" stroke-width="2"/>
  <line x1="180" y1="30" x2="180" y2="120" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="185" y="40" font-size="11" fill="#c2410c">高峰 ~N</text>
  <text x="120" y="155" font-size="11" fill="#888">←宽 ~1/N→</text>
  <text x="30" y="180" font-size="11" fill="#444">D_N(u) = sin((N+½)u)/sin(u/2) — 越窄越高 (Dirac δ 极限)</text>
</svg>
<figcaption>图 12.6.5 Dirichlet 核 $D_N(u)$:零点 $u=0$ 处尖峰宽 $\sim 1/N$、高 $\sim N$。$N\to\infty$ 时趋 Dirac delta,这是 Dirichlet 定理证明的引擎。</figcaption>
::endsvg

'''),

    # ch11 11.6 d²=0 经典恒等式 (∇×∇φ=0, ∇·∇×F=0)
    ('chapter11-line-surface-integrals.md', '### 11.6.6 三大公式与微分形式视角', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="dd1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="40" width="80" height="40" rx="5" fill="#eef4fb" stroke="#1a365d"/>
  <text x="40" y="65" font-size="13">φ (0-form)</text>
  <line x1="100" y1="60" x2="135" y2="60" stroke="#1a365d" marker-end="url(#dd1)"/>
  <text x="105" y="55" font-size="10" fill="#888">∇</text>
  <rect x="135" y="40" width="80" height="40" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="145" y="65" font-size="13">∇φ (1-form)</text>
  <line x1="215" y1="60" x2="250" y2="60" stroke="#1a365d" marker-end="url(#dd1)"/>
  <text x="222" y="55" font-size="10" fill="#888">∇×</text>
  <rect x="250" y="40" width="80" height="40" rx="5" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="270" y="65" font-size="13" fill="#b91c1c">0</text>
  <text x="20" y="110" font-size="12" font-weight="bold" fill="#444">∇×(∇φ) = 0 (梯度场无旋)</text>
  <text x="20" y="140" font-size="12" font-weight="bold" fill="#444">∇·(∇×F) = 0 (旋度场无源)</text>
  <text x="20" y="160" font-size="11" fill="#666">外微分 d²=0 的经典版本</text>
</svg>
<figcaption>图 11.6.4 $d^2=0$ 推导:梯度的旋度为零 + 旋度的散度为零,是外微分代数最深的恒等式 — 通向 de Rham 上同调 / 同伦论。</figcaption>
::endsvg

'''),

    # ch9 9.6 等高线 + 梯度方向 (再一个细致版)
    ('chapter09-multivariate.md', '### 9.6.3 例题', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ee1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="180" cy="120" r="100" fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2 2"/>
  <circle cx="180" cy="120" r="70" fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2 2"/>
  <circle cx="180" cy="120" r="40" fill="none" stroke="#888" stroke-width="0.6" stroke-dasharray="2 2"/>
  <text x="280" y="125" font-size="11" fill="#888">f=3</text>
  <text x="250" y="125" font-size="11" fill="#888">f=2</text>
  <text x="220" y="125" font-size="11" fill="#888">f=1</text>
  <circle cx="245" cy="155" r="3" fill="#1a365d"/>
  <text x="252" y="158" font-size="11" fill="#1a365d">P (1,2)</text>
  <line x1="245" y1="155" x2="285" y2="115" stroke="#c2410c" stroke-width="2" marker-end="url(#ee1)"/>
  <text x="290" y="115" font-size="11" fill="#c2410c">∇f=(2,4)</text>
  <text x="35" y="205" font-size="11" fill="#666">f(x,y)=x²+y², 在 P(1,2): ∇f=(2,4), |∇f|=2√5 (最大变化率)</text>
</svg>
<figcaption>图 9.6.4 $f=x^2+y^2$ 等高线($f=c$ 的同心圆)与梯度 $\nabla f=(2x,2y)$:在每点处梯度沿圆心指向,模 $2\sqrt{x^2+y^2}$ 给最大变化率。</figcaption>
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
