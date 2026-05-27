"""第三批 SVG: 向量场 / 二次曲面 / 复变圆盘 / Newton 迭代 / 链式 DAG / Maxwell."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.3 二次曲面五兄弟对照(椭球/单叶/双叶/抛物面/双曲抛物面)
    ('chapter08-vectors.md', '### 8.3.4 二次曲面五兄弟(标准型)', r'''
::svg
<svg viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="50" cy="100" rx="35" ry="50" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="50" cy="100" rx="35" ry="10" fill="none" stroke="#1a365d" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="22" y="180" font-size="11" fill="#1a365d">椭球面</text>
  <path d="M 130 60 Q 110 100 130 140 M 170 60 Q 190 100 170 140" fill="none" stroke="#c2410c" stroke-width="1.8"/>
  <ellipse cx="150" cy="100" rx="20" ry="6" fill="none" stroke="#c2410c" stroke-width="1.4"/>
  <text x="118" y="180" font-size="11" fill="#c2410c">单叶双曲</text>
  <path d="M 230 60 Q 250 80 230 90 M 270 60 Q 250 80 270 90" fill="none" stroke="#8b6f1c" stroke-width="1.8"/>
  <path d="M 230 110 Q 250 120 230 140 M 270 110 Q 250 120 270 140" fill="none" stroke="#8b6f1c" stroke-width="1.8"/>
  <text x="220" y="180" font-size="11" fill="#8b6f1c">双叶双曲</text>
  <path d="M 310 140 Q 350 50 390 140" fill="#fef6e4" stroke="#2d6e2d" stroke-width="1.8"/>
  <ellipse cx="350" cy="140" rx="40" ry="6" fill="none" stroke="#2d6e2d" stroke-width="1.4"/>
  <text x="312" y="180" font-size="11" fill="#2d6e2d">椭圆抛物面</text>
  <path d="M 410 80 Q 430 60 450 80 M 410 130 Q 430 150 450 130" fill="none" stroke="#991b1b" stroke-width="1.8"/>
  <path d="M 420 65 L 440 145 M 440 65 L 420 145" fill="none" stroke="#991b1b" stroke-width="1" opacity="0.4"/>
  <text x="408" y="180" font-size="11" fill="#991b1b">双曲抛物面(鞍)</text>
</svg>
<figcaption>图 8.3.2 二次曲面五兄弟形态对照:椭球 / 单叶双曲 / 双叶双曲 / 椭圆抛物面 / 双曲抛物面(马鞍)。</figcaption>
::endsvg

'''),

    # ch9 9.6 梯度场(向量场+箭头)
    ('chapter09-multivariate.md', '### 9.6.2 梯度', r'''
::svg
<svg viewBox="0 0 360 240" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="gf1" markerWidth="8" markerHeight="8" refX="7" refY="2.5" orient="auto"><path d="M0,0 L0,5 L7,2.5 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="180" cy="120" rx="120" ry="80" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 3"/>
  <ellipse cx="180" cy="120" rx="80" ry="55" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 3"/>
  <ellipse cx="180" cy="120" rx="40" ry="28" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 3"/>
  <circle cx="180" cy="120" r="3" fill="#1a365d"/>
  <text x="186" y="123" font-size="11" fill="#1a365d">峰</text>
  <line x1="80" y1="60" x2="100" y2="80" stroke="#c2410c" stroke-width="1.4" marker-end="url(#gf1)"/>
  <line x1="280" y1="60" x2="260" y2="80" stroke="#c2410c" stroke-width="1.4" marker-end="url(#gf1)"/>
  <line x1="80" y1="180" x2="100" y2="160" stroke="#c2410c" stroke-width="1.4" marker-end="url(#gf1)"/>
  <line x1="280" y1="180" x2="260" y2="160" stroke="#c2410c" stroke-width="1.4" marker-end="url(#gf1)"/>
  <line x1="40" y1="120" x2="65" y2="120" stroke="#c2410c" stroke-width="1.6" marker-end="url(#gf1)"/>
  <line x1="320" y1="120" x2="295" y2="120" stroke="#c2410c" stroke-width="1.6" marker-end="url(#gf1)"/>
  <line x1="180" y1="40" x2="180" y2="65" stroke="#c2410c" stroke-width="1.6" marker-end="url(#gf1)"/>
  <line x1="180" y1="200" x2="180" y2="175" stroke="#c2410c" stroke-width="1.6" marker-end="url(#gf1)"/>
  <line x1="130" y1="80" x2="150" y2="100" stroke="#c2410c" stroke-width="1.2" marker-end="url(#gf1)"/>
  <line x1="230" y1="80" x2="210" y2="100" stroke="#c2410c" stroke-width="1.2" marker-end="url(#gf1)"/>
  <text x="30" y="225" font-size="11" fill="#666">梯度场 ∇f: 箭头永远垂直于等高线, 指向最速上升方向</text>
</svg>
<figcaption>图 9.6.2 梯度向量场:每点处梯度 $\nabla f$(红箭头)垂直于过该点的等高线,指向函数值升高最快方向。</figcaption>
::endsvg

'''),

    # ch9 9.4 链式法则 DAG (神经网络反向传播)
    ('chapter09-multivariate.md', '### 9.4.4 反向传播(Backpropagation)', r'''
::svg
<svg viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="bp1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="bp2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="40" cy="100" r="22" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="32" y="105" font-size="12" font-style="italic">x</text>
  <line x1="62" y1="100" x2="113" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#bp1)"/>
  <text x="70" y="92" font-size="10" fill="#1a365d">W₁</text>
  <circle cx="135" cy="100" r="22" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="124" y="105" font-size="12" font-style="italic">σ(·)</text>
  <line x1="157" y1="100" x2="208" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#bp1)"/>
  <text x="170" y="92" font-size="10" fill="#1a365d">W₂</text>
  <circle cx="230" cy="100" r="22" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="217" y="105" font-size="11" font-style="italic">ŷ</text>
  <line x1="252" y1="100" x2="303" y2="100" stroke="#1a365d" stroke-width="1.5" marker-end="url(#bp1)"/>
  <circle cx="330" cy="100" r="25" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="316" y="106" font-size="12" font-weight="bold" fill="#b91c1c">L</text>
  <text x="80" y="40" font-size="11" fill="#1a365d">forward →</text>
  <path d="M 308 130 Q 200 165 88 130" fill="none" stroke="#c2410c" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#bp2)"/>
  <text x="160" y="180" font-size="11" fill="#c2410c">← backprop: ∂L/∂Wₖ 链式回传</text>
</svg>
<figcaption>图 9.4.1 神经网络 forward + backprop:前向 x→σ→ŷ→L,反向 L 的梯度按链式法则回传到每个 $W_k$。</figcaption>
::endsvg

'''),

    # ch10 10.4 引力 (Newton 球壳定理 + 距离不同情形)
    ('chapter10-multiple-integrals.md', '### 10.4.4 引力 / 静电场', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="gv1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="120" cy="110" r="50" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="105" y="115" font-size="13" fill="#1a365d" font-weight="bold">M</text>
  <circle cx="120" cy="110" r="2" fill="#1a365d"/>
  <line x1="120" y1="110" x2="280" y2="110" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="180" y="103" font-size="11" fill="#888">d</text>
  <circle cx="280" cy="110" r="4" fill="#c2410c"/>
  <text x="287" y="114" font-size="12" fill="#c2410c">P</text>
  <line x1="280" y1="110" x2="240" y2="110" stroke="#c2410c" stroke-width="2.5" marker-end="url(#gv1)"/>
  <text x="245" y="100" font-size="11" fill="#c2410c">F = GM/d²</text>
  <text x="30" y="180" font-size="11" fill="#444">Newton 球壳定理: 均匀球外引力 ≡ 把全部质量集中在球心</text>
</svg>
<figcaption>图 10.4.1 球壳定理:均匀球(质量 $M$)对外部一点 $P$ 的引力 $=\frac{GM}{d^2}$,与"质量集中在球心一个质点"完全相同。</figcaption>
::endsvg

'''),

    # ch11 11.5 Maxwell 静电场 (Gauss 定律应用)
    ('chapter11-line-surface-integrals.md', '### 11.5.4 Gauss 公式(散度定理)', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="me1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="100" ry="65" fill="none" stroke="#1a365d" stroke-width="1.8" stroke-dasharray="5 3"/>
  <circle cx="170" cy="95" r="4" fill="#c2410c"/>
  <circle cx="185" cy="105" r="4" fill="#c2410c"/>
  <circle cx="195" cy="92" r="4" fill="#c2410c"/>
  <text x="160" y="125" font-size="11" fill="#c2410c">+Q (电荷)</text>
  <line x1="180" y1="100" x2="260" y2="55" stroke="#c2410c" stroke-width="2" marker-end="url(#me1)"/>
  <line x1="180" y1="100" x2="280" y2="100" stroke="#c2410c" stroke-width="2" marker-end="url(#me1)"/>
  <line x1="180" y1="100" x2="260" y2="145" stroke="#c2410c" stroke-width="2" marker-end="url(#me1)"/>
  <line x1="180" y1="100" x2="100" y2="55" stroke="#c2410c" stroke-width="2" marker-end="url(#me1)"/>
  <line x1="180" y1="100" x2="80" y2="100" stroke="#c2410c" stroke-width="2" marker-end="url(#me1)"/>
  <line x1="180" y1="100" x2="100" y2="145" stroke="#c2410c" stroke-width="2" marker-end="url(#me1)"/>
  <text x="280" y="35" font-size="11" fill="#1a365d">Σ = ∂V</text>
  <text x="40" y="185" font-size="11" fill="#444">∮ E⃗·dS⃗ = Q_enc/ε₀  (Maxwell 第一条 / 高中"高斯定理")</text>
</svg>
<figcaption>图 11.5.2 Gauss 电场定理:闭曲面电通量正比于内部电荷,由 Gauss 公式 + $\nabla\cdot\vec{E}=\rho/\varepsilon_0$ 立得。</figcaption>
::endsvg

'''),

    # ch12 12.4 复变收敛圆盘(实轴幂级数是它的截面)
    ('chapter12-infinite-series.md', '### 12.4.4 内部的一致收敛与解析性', r'''
::svg
<svg viewBox="0 0 320 240" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="120" x2="290" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="20" x2="160" y2="220" stroke="#888" stroke-width="1"/>
  <text x="295" y="125" font-size="11" fill="#888">Re(z)</text>
  <text x="165" y="20" font-size="11" fill="#888">Im(z)</text>
  <circle cx="160" cy="120" r="70" fill="#eef4fb" fill-opacity="0.6" stroke="#1a365d" stroke-width="2"/>
  <circle cx="160" cy="120" r="3" fill="#1a365d"/>
  <text x="166" y="115" font-size="11" fill="#1a365d">z₀</text>
  <line x1="160" y1="120" x2="216" y2="78" stroke="#c2410c" stroke-width="1.5"/>
  <text x="178" y="92" font-size="11" fill="#c2410c">R</text>
  <line x1="90" y1="120" x2="230" y2="120" stroke="#2d6e2d" stroke-width="3"/>
  <text x="100" y="148" font-size="11" fill="#2d6e2d">实轴收敛区</text>
  <text x="35" y="200" font-size="11" fill="#666">∑aₙ(z−z₀)ⁿ 在复平面收敛区是圆盘, 实数情形是它的弦截面</text>
</svg>
<figcaption>图 12.4.2 复变幂级数收敛域是以 $z_0$ 为心、$R$ 为半径的**圆盘**;实数轴上 $\sum a_n(x-x_0)^n$ 是其在实轴的截面(粗绿线)。</figcaption>
::endsvg

'''),

    # ch12 12.5 Newton 法迭代图
    ('chapter12-infinite-series.md', '### 12.5.4 应用:数值计算 / Newton 法 / 物理近似', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="130" x2="330" y2="130" stroke="#888" stroke-width="1"/>
  <line x1="60" y1="20" x2="60" y2="200" stroke="#888" stroke-width="1"/>
  <text x="335" y="135" font-size="11" fill="#888">x</text>
  <text x="65" y="20" font-size="11" fill="#888">g(x)</text>
  <path d="M 60 35 Q 130 60 200 130 Q 270 200 330 215" fill="none" stroke="#1a365d" stroke-width="2"/>
  <circle cx="80" cy="40" r="4" fill="#c2410c"/>
  <text x="86" y="45" font-size="11" fill="#c2410c">x_k</text>
  <line x1="80" y1="40" x2="80" y2="130" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="40" y1="55" x2="200" y2="135" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="80" y="73" font-size="11" fill="#c2410c">切线 g'(x_k)</text>
  <circle cx="160" cy="130" r="4" fill="#2d6e2d"/>
  <text x="158" y="148" font-size="11" fill="#2d6e2d">x_{k+1}</text>
  <line x1="160" y1="130" x2="160" y2="115" stroke="#2d6e2d" stroke-width="0.8" stroke-dasharray="2 2"/>
  <circle cx="200" cy="130" r="3" fill="#1a365d"/>
  <text x="205" y="145" font-size="11" fill="#1a365d">x*</text>
  <text x="35" y="195" font-size="11" fill="#666">x_{k+1} = x_k − g(x_k)/g'(x_k) 一阶 Taylor 求零</text>
</svg>
<figcaption>图 12.5.2 Newton 迭代法:在 $x_k$ 做切线,与 x 轴交点为下一个估计 $x_{k+1}$。来自一阶 Taylor 展开求零。</figcaption>
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
