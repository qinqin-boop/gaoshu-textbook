"""第十八批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.5 逆函数定理
    ('chapter09-multivariate.md', '### 9.5.4 几何意义:隐函数定理与流形', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="iv1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="iv2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <rect x="20" y="40" width="100" height="80" rx="6" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="40" y="80" font-size="13" font-weight="bold" fill="#1a365d">x ∈ ℝⁿ</text>
  <line x1="120" y1="80" x2="160" y2="80" stroke="#1a365d" stroke-width="2" marker-end="url(#iv1)"/>
  <text x="125" y="72" font-size="11">F (可微 J 满秩)</text>
  <rect x="160" y="40" width="100" height="80" rx="6" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="180" y="80" font-size="13" font-weight="bold" fill="#8b6f1c">y ∈ ℝⁿ</text>
  <line x1="160" y1="100" x2="120" y2="100" stroke="#c2410c" stroke-width="2" marker-end="url(#iv2)"/>
  <text x="125" y="115" font-size="11" fill="#c2410c">F⁻¹</text>
  <text x="280" y="55" font-size="11" fill="#444">J_{F⁻¹}</text>
  <text x="280" y="75" font-size="11" fill="#444">= J_F⁻¹</text>
  <text x="35" y="155" font-size="11" fill="#666">逆函数定理: J 可逆 ⇒ F 局部可逆, 雅可比互逆</text>
</svg>
<figcaption>图 9.5.3 逆函数定理:$J_F$ 可逆时 $F:\mathbb{R}^n\to\mathbb{R}^n$ 局部双射,$J_{F^{-1}}=J_F^{-1}$ — 换元雅可比因子 $|J|$ 的根。</figcaption>
::endsvg

'''),

    # ch9 9.8 Newton 法二次收敛 vs 梯度下降几何
    ('chapter09-multivariate.md', '### 9.8.5 与凸优化、机器学习的联系', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="nw1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="nw2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="180" cy="100" rx="120" ry="60" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 2"/>
  <ellipse cx="180" cy="100" rx="80" ry="40" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 2"/>
  <ellipse cx="180" cy="100" rx="40" ry="20" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 2"/>
  <circle cx="180" cy="100" r="3" fill="#1a365d"/>
  <text x="186" y="105" font-size="11" fill="#1a365d">最优</text>
  <circle cx="60" cy="50" r="3" fill="#1a365d"/>
  <text x="40" y="45" font-size="11" fill="#1a365d">起点</text>
  <path d="M 60 50 L 100 80 L 130 95 L 155 100 L 175 100 L 180 100" fill="none" stroke="#1a365d" stroke-width="1.8" marker-end="url(#nw1)"/>
  <text x="65" y="68" font-size="11" fill="#1a365d">梯度下降 (慢)</text>
  <path d="M 60 50 L 180 100" fill="none" stroke="#c2410c" stroke-width="2.5" marker-end="url(#nw2)"/>
  <text x="85" y="80" font-size="11" fill="#c2410c">Newton (一步直奔)</text>
  <text x="35" y="195" font-size="11" fill="#666">Newton 法二次收敛: 凸二次函数一步到位</text>
</svg>
<figcaption>图 9.8.4 Newton 法 vs 梯度下降:Newton 利用 Hessian 调整方向,凸二次函数一步到底;梯度下降只用一阶,需要多次"之字形"走。</figcaption>
::endsvg

'''),

    # ch10 10.1 一元→二元积分 (区间→区域)
    ('chapter10-multiple-integrals.md', '### 10.1.1 划分与黎曼和', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="100" x2="160" y2="100" stroke="#1a365d" stroke-width="2"/>
  <path d="M 30 100 L 30 60 L 50 60 L 50 40 L 80 40 L 80 65 L 110 65 L 110 50 L 140 50 L 140 100" fill="#eef4fb" stroke="#1a365d" stroke-width="1.4"/>
  <text x="60" y="125" font-size="11" fill="#1a365d">∫_a^b f(x) dx</text>
  <text x="60" y="142" font-size="11" fill="#888">(一元: 区间)</text>
  <text x="195" y="100" font-size="20" fill="#444">→</text>
  <polygon points="230,80 320,70 330,140 250,150" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="255" y="115" font-size="13" font-style="italic">D</text>
  <text x="240" y="172" font-size="11" fill="#8b6f1c">∬_D f(x,y) dσ</text>
  <text x="240" y="189" font-size="11" fill="#888">(二元: 区域)</text>
</svg>
<figcaption>图 10.1.4 一元到二元积分升级:从 1D 区间下面积 → 2D 平面区域上的体积 / 质量;思想都是 Riemann 和取极限。</figcaption>
::endsvg

'''),

    # ch11 11.1 摆线弧长
    ('chapter11-line-surface-integrals.md', '### 11.1.2 计算公式', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 30 130 Q 60 60 100 130 Q 130 60 170 130 Q 200 60 240 130 Q 270 60 310 130" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="35" y="50" font-size="12" fill="#1a365d">摆线 x=a(t−sint), y=a(1−cost)</text>
  <circle cx="100" cy="100" r="35" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="80" y="170" font-size="11" fill="#666">滚动圆生成</text>
  <text x="35" y="180" font-size="11" fill="#444">弧长 ∫₀^{2π} √(x'²+y'²) dt = 8a (一拱长度)</text>
</svg>
<figcaption>图 11.1.3 摆线弧长:圆滚一圈生成一拱摆线,长度 $8a$($a$ 为圆半径)— 一元定积分 $\int\sqrt{1+y'^2}dx$ 的经典应用。</figcaption>
::endsvg

'''),

    # ch11 11.4 球冠面积
    ('chapter11-line-surface-integrals.md', '### 11.4.5 一般参数化', r'''
::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="160" cy="120" r="70" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 2"/>
  <path d="M 90 120 A 70 70 0 0 1 230 120" fill="#fef6e4" fill-opacity="0.6" stroke="#c9a227" stroke-width="1.8"/>
  <line x1="90" y1="120" x2="230" y2="120" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="160" y1="50" x2="160" y2="120" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="165" y="80" font-size="11" fill="#888">h</text>
  <text x="125" y="115" font-size="13" font-weight="bold" fill="#8b6f1c">球冠</text>
  <text x="35" y="170" font-size="11" fill="#444">球冠面积 = 2πRh (只跟高 h 有关, 与冠的位置无关!)</text>
  <text x="35" y="190" font-size="11" fill="#666">阿基米德定理: 球面对剖面圆柱面积同</text>
</svg>
<figcaption>图 11.4.8 球冠面积 $2\pi Rh$:仅依赖于冠高 $h$,与冠在球上的位置无关 — Archimedes 著名结论(球面 $=$ 外切圆柱侧面),用曲面积分立证。</figcaption>
::endsvg

'''),

    # ch12 12.1 几何级数闭式推导 (S_N · (1-r) = ...)
    ('chapter12-infinite-series.md', '### 12.1.3 两个关键的"参考级数"', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="30" y="35" font-size="13" font-family="serif" fill="#1a365d">S_N = a + ar + ar² + ... + ar^{N-1}</text>
  <text x="30" y="60" font-size="13" font-family="serif" fill="#c2410c">rS_N =      ar + ar² + ... + ar^{N-1} + ar^N</text>
  <line x1="30" y1="70" x2="330" y2="70" stroke="#1a365d" stroke-width="1"/>
  <text x="30" y="92" font-size="13" font-family="serif" fill="#2d6e2d">S_N(1-r) = a - ar^N</text>
  <text x="30" y="115" font-size="14" font-family="serif" font-weight="bold" fill="#2d6e2d">S_N = a(1 - r^N)/(1 - r)</text>
  <text x="30" y="145" font-size="13" font-family="serif" fill="#b91c1c">|r| < 1 ⇒ r^N → 0 ⇒ S = a/(1-r)</text>
</svg>
<figcaption>图 12.1.3 几何级数闭式推导:$S_N$ 减 $rS_N$ 消去中间项得 $S_N=\frac{a(1-r^N)}{1-r}$;$|r|<1$ 时 $r^N\to 0$,$S=\frac{a}{1-r}$。</figcaption>
::endsvg

'''),

    # ch12 12.5 数值收敛速度 (Taylor 几阶逼近精度)
    ('chapter12-infinite-series.md', '### 12.5.4 应用:数值计算 / Newton 法 / 物理近似', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="160" x2="340" y2="160" stroke="#888" stroke-width="1"/>
  <line x1="40" y1="20" x2="40" y2="170" stroke="#888" stroke-width="1"/>
  <text x="345" y="165" font-size="11" fill="#888">阶 n</text>
  <text x="22" y="22" font-size="11" fill="#888">|误差|</text>
  <text x="42" y="155" font-size="10">1</text>
  <text x="105" y="155" font-size="10">2</text>
  <text x="168" y="155" font-size="10">3</text>
  <text x="231" y="155" font-size="10">4</text>
  <text x="294" y="155" font-size="10">5</text>
  <circle cx="55" cy="50" r="3" fill="#c2410c"/>
  <circle cx="118" cy="80" r="3" fill="#c2410c"/>
  <circle cx="181" cy="110" r="3" fill="#c2410c"/>
  <circle cx="244" cy="130" r="3" fill="#c2410c"/>
  <circle cx="307" cy="145" r="3" fill="#c2410c"/>
  <path d="M 55 50 L 118 80 L 181 110 L 244 130 L 307 145" stroke="#c2410c" stroke-width="2" fill="none"/>
  <text x="160" y="35" font-size="11" fill="#c2410c">误差 ~ |x-x₀|^{n+1}/(n+1)!</text>
  <text x="40" y="190" font-size="11" fill="#666">Taylor 阶越高 → 误差以阶乘速率下降</text>
</svg>
<figcaption>图 12.5.4 Taylor 多项式逼近误差:Lagrange 余项 $|R_n|\le\frac{M|x-x_0|^{n+1}}{(n+1)!}$,误差以**阶乘**速率压低 — 计算器内部 $e^x,\sin x$ 求值的精度来源。</figcaption>
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
