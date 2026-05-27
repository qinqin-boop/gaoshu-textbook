"""第十四批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.1 方向余弦 (3 个夹角)
    ('chapter08-vectors.md', '### 8.1.6 方向余弦', r'''
::svg
<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="dc1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <line x1="160" y1="200" x2="160" y2="20" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="200" x2="60" y2="170" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="200" x2="290" y2="180" stroke="#888" stroke-width="1"/>
  <text x="152" y="15" font-size="12" fill="#888">z</text>
  <text x="50" y="180" font-size="12" fill="#888">x</text>
  <text x="295" y="190" font-size="12" fill="#888">y</text>
  <line x1="160" y1="200" x2="240" y2="80" stroke="#c2410c" stroke-width="2.5" marker-end="url(#dc1)"/>
  <text x="245" y="78" font-size="13" font-style="italic" fill="#c2410c">a⃗</text>
  <path d="M 200 140 A 30 30 0 0 0 215 160" fill="none" stroke="#888" stroke-width="0.8"/>
  <text x="205" y="155" font-size="11" fill="#888">α</text>
  <path d="M 175 105 A 30 30 0 0 1 195 130" fill="none" stroke="#888" stroke-width="0.8"/>
  <text x="178" y="125" font-size="11" fill="#888">γ</text>
  <path d="M 215 175 A 30 30 0 0 0 235 165" fill="none" stroke="#888" stroke-width="0.8"/>
  <text x="220" y="175" font-size="11" fill="#888">β</text>
  <text x="30" y="210" font-size="11" fill="#444">cos²α + cos²β + cos²γ = 1 (单位向量)</text>
</svg>
<figcaption>图 8.1.4 方向余弦:向量 $\vec{a}$ 与三坐标轴夹角余弦 $(\cos\alpha,\cos\beta,\cos\gamma)$ = 单位向量分量,满足 $\sum\cos^2=1$。</figcaption>
::endsvg

'''),

    # ch9 9.4 高阶导数 (二阶混合 + 易忘项)
    ('chapter09-multivariate.md', '### 9.4.5 高阶导数', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="30" y="40" font-size="13" font-family="serif" fill="#1a365d">∂²z/∂x² =</text>
  <text x="130" y="40" font-size="13" font-family="serif" fill="#c2410c">f_uu·u_x²</text>
  <text x="220" y="40" font-size="13" fill="#c2410c">+ 2f_uv·u_x v_x</text>
  <text x="130" y="65" font-size="13" font-family="serif" fill="#c2410c">+ f_vv·v_x²</text>
  <rect x="120" y="80" width="200" height="40" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="130" y="100" font-size="13" font-family="serif" fill="#b91c1c">+ f_u·u_xx + f_v·v_xx</text>
  <text x="125" y="117" font-size="11" font-style="italic" fill="#b91c1c">⚠ 易忘高阶项</text>
  <text x="30" y="150" font-size="11" fill="#666">链式法则二次应用: 二阶 = 一阶链式套一次 + u/v 二阶项</text>
</svg>
<figcaption>图 9.4.3 二阶偏导链式公式:含 $f_u u_{xx},\,f_v v_{xx}$ 高阶项 — 这是 PDE 推导(波动 / 热)中最易遗漏的部分。</figcaption>
::endsvg

'''),

    # ch10 10.5 Beta 函数
    ('chapter10-multiple-integrals.md', '### 10.5.5 物理 / 工程应用速览', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="140" x2="330" y2="140" stroke="#888" stroke-width="1"/>
  <line x1="30" y1="20" x2="30" y2="160" stroke="#888" stroke-width="1"/>
  <text x="335" y="145" font-size="11" fill="#888">x</text>
  <text x="35" y="20" font-size="11" fill="#888">B</text>
  <text x="22" y="135" font-size="10" fill="#888">0</text>
  <text x="320" y="135" font-size="10" fill="#888">1</text>
  <path d="M 35 130 Q 175 30 320 130" fill="none" stroke="#1a365d" stroke-width="2"/>
  <text x="60" y="60" font-size="11" fill="#1a365d">B(p,q)=∫₀¹ x^{p-1}(1-x)^{q-1} dx</text>
  <text x="40" y="160" font-size="11" fill="#c2410c">Beta(2,2) (对称)</text>
  <path d="M 35 130 Q 100 85 320 50" fill="none" stroke="#c9a227" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="200" y="80" font-size="11" fill="#8b6f1c">Beta(2,5) (偏左)</text>
</svg>
<figcaption>图 10.5.3 Beta 函数 $B(p,q)$ 概率密度:不同 $(p,q)$ 控制偏态;$B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$ — Bayesian 先验 / 二项似然的共轭族。</figcaption>
::endsvg

'''),

    # ch11 11.3 复连通 反例 (-y,x)/(x²+y²) 绕原点 2π
    ('chapter11-line-surface-integrals.md', '### 11.3.4 例题', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ws1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="180" cy="110" r="80" fill="#eef4fb" fill-opacity="0.4" stroke="#1a365d" stroke-width="1.8"/>
  <circle cx="180" cy="110" r="4" fill="#b91c1c"/>
  <text x="190" y="115" font-size="11" fill="#b91c1c">奇点</text>
  <path d="M 260 110 A 80 80 0 1 1 259 109" fill="none" stroke="#c2410c" stroke-width="2.5" marker-end="url(#ws1)"/>
  <text x="120" y="40" font-size="11" fill="#c2410c">∮ (-y dx + x dy)/(x²+y²) = 2π</text>
  <line x1="180" y1="110" x2="220" y2="60" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="180" y1="110" x2="140" y2="60" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="180" y1="110" x2="240" y2="160" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="35" y="205" font-size="11" fill="#666">∂Q/∂x = ∂P/∂y 但环路积分≠0 — 区域含奇点 Green 失效</text>
</svg>
<figcaption>图 11.3.4 复连通经典反例:$P=-y/(x^2+y^2),Q=x/(x^2+y^2)$ 满足 $\partial_xQ=\partial_yP$ 但绕原点积分 $=2\pi$ — 因区域含原点奇点,Green 公式破坏。</figcaption>
::endsvg

'''),

    # ch12 12.6 Gibbs 现象细节
    ('chapter12-infinite-series.md', '### 12.6.6 物理 / 工程应用速览', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="100" x2="330" y2="100" stroke="#888" stroke-width="1"/>
  <line x1="170" y1="20" x2="170" y2="180" stroke="#888" stroke-width="1"/>
  <path d="M 30 140 L 165 140 L 165 50 L 330 50" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="35" y="155" font-size="11" fill="#1a365d">方波 f(x)</text>
  <path d="M 30 138 L 80 138 L 110 145 L 130 130 L 145 30 L 160 50 L 165 50 L 175 50 L 180 50 L 195 70 L 215 50 L 230 50 L 260 55 L 290 50 L 330 50" fill="none" stroke="#c2410c" stroke-width="1.8"/>
  <line x1="148" y1="30" x2="148" y2="50" stroke="#b91c1c" stroke-width="2"/>
  <text x="105" y="22" font-size="11" fill="#b91c1c">超出 ~9% (Gibbs)</text>
  <text x="35" y="190" font-size="11" fill="#666">N→∞ 也消不掉, 实际 8.95% (Wilbraham 1848 / Gibbs 1899)</text>
</svg>
<figcaption>图 12.6.6 Gibbs 现象:方波 Fourier 部分和在间断点附近永远过冲 $\approx 8.95\%$(即使 $N\to\infty$),只是峰更靠近间断点。Fejér 求和 (Cesàro 平均) 可消除。</figcaption>
::endsvg

'''),

    # ch8 8.0 应用对照 (后续章节衔接)
    ('chapter08-vectors.md', '### 8.0.3 学这章的意义', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="20" width="60" height="35" rx="4" fill="#eef4fb" stroke="#1a365d"/>
  <text x="34" y="42" font-size="11">向量 a⃗</text>
  <line x1="80" y1="38" x2="100" y2="38" stroke="#888" stroke-width="1"/>
  <text x="100" y="42" font-size="10" fill="#666">→ 词嵌入 (300d)</text>
  <rect x="20" y="65" width="60" height="35" rx="4" fill="#fef6e4" stroke="#c9a227"/>
  <text x="28" y="87" font-size="11">a⃗·b⃗</text>
  <line x1="80" y1="83" x2="100" y2="83" stroke="#888" stroke-width="1"/>
  <text x="100" y="87" font-size="10" fill="#666">→ 余弦相似度 / 注意力</text>
  <rect x="20" y="110" width="60" height="35" rx="4" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="28" y="132" font-size="11">a⃗×b⃗</text>
  <line x1="80" y1="128" x2="100" y2="128" stroke="#888" stroke-width="1"/>
  <text x="100" y="132" font-size="10" fill="#666">→ 力矩 / 法向 / CGI</text>
  <rect x="220" y="20" width="60" height="35" rx="4" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="232" y="42" font-size="11">平面/曲面</text>
  <line x1="220" y1="38" x2="200" y2="38" stroke="#888" stroke-width="1"/>
  <text x="135" y="42" font-size="10" fill="#666">PDE 边界 / CAD</text>
  <rect x="220" y="110" width="60" height="35" rx="4" fill="#eef4fb" stroke="#1a365d"/>
  <text x="232" y="132" font-size="11">3D 直线</text>
  <line x1="220" y1="128" x2="200" y2="128" stroke="#888" stroke-width="1"/>
  <text x="135" y="132" font-size="10" fill="#666">机器人 / GPS</text>
</svg>
<figcaption>图 8.0.3 向量代数在工程 / AI 落地:词向量(300d) / 余弦相似度(注意力) / 法向(CGI 光照) / PDE / 机器人。</figcaption>
::endsvg

'''),

    # ch11 11.6 物理:洛伦兹力 v×B
    ('chapter11-line-surface-integrals.md', '### 11.6.5 例题', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="lv1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="lv2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="lv3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <line x1="60" y1="120" x2="180" y2="120" stroke="#1a365d" stroke-width="2.5" marker-end="url(#lv1)"/>
  <text x="115" y="140" font-size="13" font-style="italic" fill="#1a365d">v⃗</text>
  <line x1="60" y1="120" x2="60" y2="40" stroke="#c2410c" stroke-width="2.5" marker-end="url(#lv2)"/>
  <text x="45" y="60" font-size="13" font-style="italic" fill="#c2410c">B⃗</text>
  <line x1="60" y1="120" x2="170" y2="220" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#lv3)"/>
  <text x="120" y="215" font-size="13" font-style="italic" fill="#2d6e2d">F⃗=qv⃗×B⃗</text>
  <text x="35" y="170" font-size="11" fill="#666">右手定则: 食指 v, 中指 B, 拇指 F</text>
</svg>
<figcaption>图 11.6.5 洛伦兹力 $\vec{F}=q\vec{v}\times\vec{B}$:正电荷沿 $\vec{v}$ 在磁场 $\vec{B}$ 中受力垂直于二者,右手定则 — 向量积在物理学中的最重要应用。</figcaption>
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
