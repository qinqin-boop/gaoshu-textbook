"""第六批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.2 偏导数几何 (沿坐标轴剖面斜率)
    ('chapter09-multivariate.md', '### 9.2.4 偏导数的几何意义与切平面', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="pd1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <path d="M 40 180 Q 130 60 240 90 Q 310 105 340 70" fill="none" stroke="#1a365d" stroke-width="1.5"/>
  <text x="35" y="40" font-size="12" fill="#1a365d">z=f(x,y)</text>
  <path d="M 40 180 Q 100 130 130 80" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <circle cx="190" cy="100" r="4" fill="#c2410c"/>
  <text x="198" y="98" font-size="11" fill="#c2410c">P₀</text>
  <line x1="120" y1="135" x2="260" y2="65" stroke="#c2410c" stroke-width="2" marker-end="url(#pd1)"/>
  <text x="265" y="63" font-size="11" fill="#c2410c">沿 x 切线斜率 f_x</text>
  <line x1="160" y1="130" x2="220" y2="70" stroke="#2d6e2d" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="155" y="155" font-size="11" fill="#2d6e2d">y=y₀ 切面</text>
</svg>
<figcaption>图 9.2.1 偏导数几何意义:$f_x(x_0,y_0)$ = 把曲面用 $y=y_0$ 截切得到的剖面曲线在 $P_0$ 处的斜率。</figcaption>
::endsvg

'''),

    # ch10 10.2 极坐标面积元 r dr dθ
    ('chapter10-multiple-integrals.md', '### 10.2.3 极坐标变换与雅可比因子', r'''
::svg
<svg viewBox="0 0 280 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="50" cy="180" r="40" fill="none" stroke="#1a365d" stroke-width="0.7" opacity="0.5"/>
  <circle cx="50" cy="180" r="80" fill="none" stroke="#1a365d" stroke-width="0.7" opacity="0.5"/>
  <circle cx="50" cy="180" r="120" fill="none" stroke="#1a365d" stroke-width="0.7" opacity="0.5"/>
  <line x1="50" y1="180" x2="50" y2="50" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <line x1="50" y1="180" x2="170" y2="180" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <line x1="50" y1="180" x2="155" y2="120" stroke="#1a365d" stroke-width="0.7" opacity="0.5"/>
  <line x1="50" y1="180" x2="135" y2="100" stroke="#1a365d" stroke-width="0.7" opacity="0.5"/>
  <path d="M 88 138 A 60 60 0 0 1 108 154 L 96 174 A 40 40 0 0 0 84 162 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="1.6"/>
  <text x="92" y="155" font-size="11" fill="#8b6f1c">r dr dθ</text>
  <text x="155" y="172" font-size="12" fill="#1a365d">r</text>
  <text x="115" y="155" font-size="12" fill="#1a365d">θ</text>
  <text x="180" y="50" font-size="12" fill="#444">∬f dxdy</text>
  <text x="180" y="70" font-size="12" fill="#444">= ∬f(rcosθ,</text>
  <text x="180" y="90" font-size="12" fill="#444">    rsinθ)·r drdθ</text>
  <text x="180" y="125" font-size="11" fill="#c2410c">r 来自扇环</text>
  <text x="180" y="140" font-size="11" fill="#c2410c">面积公式</text>
</svg>
<figcaption>图 10.2.3 极坐标面积元 $dA=r\,dr\,d\theta$:$r,r+dr$ 圆环与 $\theta,\theta+d\theta$ 射线围成扇环,长 $\approx r\,d\theta$、宽 $dr$。</figcaption>
::endsvg

'''),

    # ch11 11.2 第二类曲线积分 (力沿曲线做功)
    ('chapter11-line-surface-integrals.md', '### 11.2.1 定义', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ll2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="ll3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <path d="M 30 150 Q 100 50 200 80 T 340 120" fill="none" stroke="#1a365d" stroke-width="2.5" marker-end="url(#ll2)"/>
  <text x="30" y="170" font-size="11" fill="#1a365d">L (A→B 有向)</text>
  <line x1="100" y1="115" x2="135" y2="85" stroke="#c2410c" stroke-width="2" marker-end="url(#ll3)"/>
  <text x="138" y="83" font-size="11" fill="#c2410c">F⃗</text>
  <line x1="180" y1="80" x2="215" y2="78" stroke="#c2410c" stroke-width="2" marker-end="url(#ll3)"/>
  <line x1="260" y1="90" x2="290" y2="105" stroke="#c2410c" stroke-width="2" marker-end="url(#ll3)"/>
  <text x="50" y="30" font-size="12" fill="#444">W = ∫_L F⃗·dr⃗ (力 · 微小位移 累加)</text>
  <text x="50" y="190" font-size="11" fill="#666">反向走: ∫_{-L} = -∫_L</text>
</svg>
<figcaption>图 11.2.1 第二类曲线积分:沿有向曲线 $L$ 累加 $\vec{F}\cdot d\vec{r}$ = 力沿路径做的功。反向走积分变号。</figcaption>
::endsvg

'''),

    # ch12 12.5 e^{-1/x²} 反例
    ('chapter12-infinite-series.md', '### 12.5.3 光滑但非解析:经典反例', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="140" x2="340" y2="140" stroke="#888" stroke-width="1"/>
  <line x1="180" y1="20" x2="180" y2="180" stroke="#888" stroke-width="1"/>
  <text x="345" y="145" font-size="11" fill="#888">x</text>
  <text x="185" y="20" font-size="11" fill="#888">y</text>
  <line x1="40" y1="140" x2="180" y2="140" stroke="#1a365d" stroke-width="2.5"/>
  <text x="100" y="160" font-size="12" fill="#1a365d">f≡0 (x≤0)</text>
  <path d="M 180 140 Q 210 138 225 110 Q 245 60 280 40 L 340 35" fill="none" stroke="#c2410c" stroke-width="2.5"/>
  <text x="240" y="65" font-size="12" fill="#c2410c">f=e^{-1/x²} (x>0)</text>
  <circle cx="180" cy="140" r="4" fill="#2d6e2d"/>
  <text x="186" y="158" font-size="11" fill="#2d6e2d">x=0: 所有阶导数 = 0</text>
  <text x="30" y="190" font-size="11" fill="#666">但 f≠0 (x>0) → Taylor 级数 = 0 不收敛到 f</text>
</svg>
<figcaption>图 12.5.1 $e^{-1/x^2}$ 反例:$f$ 在 $x=0$ 处无穷次可导且**所有阶导数 = 0**,但 $f$ 不恒为零。Taylor 级数 $\equiv 0$ 但不收敛到原函数 — 实分析 vs 复分析分水岭。</figcaption>
::endsvg

'''),

    # ch12 12.4 Abel 第一定理 (收敛沿用)
    ('chapter12-infinite-series.md', '### 12.4.1 收敛半径与收敛区间', r'''
::svg
<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="20" y1="80" x2="340" y2="80" stroke="#1a365d" stroke-width="1.5"/>
  <line x1="340" y1="80" x2="332" y2="76" stroke="#1a365d"/>
  <line x1="340" y1="80" x2="332" y2="84" stroke="#1a365d"/>
  <line x1="180" y1="68" x2="180" y2="92" stroke="#1a365d" stroke-width="2"/>
  <text x="174" y="105" font-size="11" fill="#1a365d">0</text>
  <circle cx="240" cy="80" r="4" fill="#c2410c"/>
  <text x="225" y="105" font-size="11" fill="#c2410c">x₁ (收敛)</text>
  <rect x="120" y="74" width="120" height="12" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="125" y="65" font-size="11" fill="#2d6e2d">|x|<|x₁| 全部绝对收敛</text>
  <text x="20" y="135" font-size="11" fill="#666">Abel I: 在 x₁ 收敛 ⇒ 整个 (−|x₁|,|x₁|) 绝对收敛</text>
</svg>
<figcaption>图 12.4.3 Abel 第一定理:若幂级数在 $x_1$ 收敛,则对所有 $|x|<|x_1|$ 处绝对收敛 — 收敛性可"沿用"到中心更近的所有点。</figcaption>
::endsvg

'''),

    # ch8 8.1 向量加法 平行四边形 + 三角形
    ('chapter08-vectors.md', '### 8.1.3 加法、减法、数乘', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="vt1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="vt2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#8b3a0a"/></marker>
    <marker id="vt3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <line x1="30" y1="150" x2="120" y2="150" stroke="#1a365d" stroke-width="2.5" marker-end="url(#vt1)"/>
  <text x="65" y="165" font-size="13" font-style="italic" fill="#1a365d">a</text>
  <line x1="30" y1="150" x2="80" y2="80" stroke="#8b3a0a" stroke-width="2.5" marker-end="url(#vt2)"/>
  <text x="45" y="115" font-size="13" font-style="italic" fill="#8b3a0a">b</text>
  <line x1="120" y1="150" x2="170" y2="80" stroke="#8b3a0a" stroke-width="1.5" stroke-dasharray="3 2"/>
  <line x1="80" y1="80" x2="170" y2="80" stroke="#1a365d" stroke-width="1.5" stroke-dasharray="3 2"/>
  <line x1="30" y1="150" x2="170" y2="80" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#vt3)"/>
  <text x="90" y="105" font-size="13" font-style="italic" fill="#2d6e2d">a+b</text>
  <text x="80" y="185" font-size="11" fill="#666">平行四边形法则: 同起点 → 对角线</text>
  <line x1="210" y1="150" x2="290" y2="100" stroke="#1a365d" stroke-width="2.5" marker-end="url(#vt1)"/>
  <text x="240" y="135" font-size="13" font-style="italic" fill="#1a365d">a</text>
  <line x1="290" y1="100" x2="330" y2="60" stroke="#8b3a0a" stroke-width="2.5" marker-end="url(#vt2)"/>
  <text x="320" y="82" font-size="13" font-style="italic" fill="#8b3a0a">b</text>
  <line x1="210" y1="150" x2="330" y2="60" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#vt3)" stroke-dasharray="5 2"/>
  <text x="245" y="100" font-size="13" font-style="italic" fill="#2d6e2d">a+b</text>
  <text x="225" y="185" font-size="11" fill="#666">三角形法则: 首尾相接</text>
</svg>
<figcaption>图 8.1.3 向量加法两法则等价:平行四边形(同起点对角)= 三角形(首尾相接)。代数式 $\vec{a}+\vec{b}=(a_1+b_1,\,a_2+b_2)$。</figcaption>
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
