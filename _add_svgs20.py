"""第二十批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.2 三件套总览 矩阵图
    ('chapter08-vectors.md', '### 8.2.4 三件套总览', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="30" width="100" height="60" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="30" y="50" font-size="13" font-weight="bold" fill="#1a365d">a⃗·b⃗</text>
  <text x="30" y="68" font-size="11" fill="#1a365d">→ 标量</text>
  <text x="30" y="82" font-size="10" fill="#888">投影/角度</text>
  <rect x="140" y="30" width="100" height="60" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="150" y="50" font-size="13" font-weight="bold" fill="#8b6f1c">a⃗×b⃗</text>
  <text x="150" y="68" font-size="11" fill="#8b6f1c">→ 向量</text>
  <text x="150" y="82" font-size="10" fill="#888">平行四边形面积</text>
  <rect x="260" y="30" width="100" height="60" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="270" y="50" font-size="13" font-weight="bold" fill="#2d6e2d">[a,b,c]</text>
  <text x="270" y="68" font-size="11" fill="#2d6e2d">→ 标量</text>
  <text x="270" y="82" font-size="10" fill="#888">六面体体积</text>
  <text x="30" y="120" font-size="11" fill="#444">应用对照:</text>
  <text x="30" y="140" font-size="11" fill="#666">点乘: 余弦相似度 / 物理功 / 投影</text>
  <text x="30" y="160" font-size="11" fill="#666">叉乘: 力矩 / 角动量 / 平面法向</text>
  <text x="30" y="180" font-size="11" fill="#666">混合积: 共面判别 / 四面体体积 / 行列式</text>
</svg>
<figcaption>图 8.2.4 三件套总览:点乘(→标量,投影)/ 叉乘(→向量,面积+法向)/ 混合积(→标量,带号体积);维度 + 应用对照。</figcaption>
::endsvg

'''),

    # ch9 9.6 梯度+方向导数 全套关系
    ('chapter09-multivariate.md', '### 9.6.4 与 AI 优化的联系', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="oa1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <text x="35" y="40" font-size="14" font-weight="bold" fill="#444">优化算法演化:</text>
  <rect x="20" y="60" width="100" height="30" fill="#eef4fb" stroke="#1a365d"/>
  <text x="28" y="80" font-size="11">梯度下降 (1 阶)</text>
  <line x1="120" y1="75" x2="140" y2="75" stroke="#1a365d" marker-end="url(#oa1)"/>
  <rect x="140" y="60" width="100" height="30" fill="#fef6e4" stroke="#c9a227"/>
  <text x="158" y="80" font-size="11">+ Momentum</text>
  <line x1="240" y1="75" x2="260" y2="75" stroke="#1a365d" marker-end="url(#oa1)"/>
  <rect x="260" y="60" width="90" height="30" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="270" y="80" font-size="11">Adam (自适应)</text>
  <rect x="20" y="105" width="100" height="30" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="32" y="125" font-size="11">Newton (2 阶)</text>
  <line x1="120" y1="120" x2="140" y2="120" stroke="#1a365d" marker-end="url(#oa1)"/>
  <rect x="140" y="105" width="100" height="30" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="160" y="125" font-size="11">BFGS 拟 Newton</text>
  <line x1="240" y1="120" x2="260" y2="120" stroke="#1a365d" marker-end="url(#oa1)"/>
  <rect x="260" y="105" width="90" height="30" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="270" y="125" font-size="11">K-FAC / 共轭</text>
  <text x="35" y="170" font-size="11" fill="#444">SGD/Adam 主流 (大模型); Newton 系列适合精确小问题</text>
</svg>
<figcaption>图 9.6.6 优化算法演化谱:一阶(SGD→Momentum→Adam)vs 二阶(Newton→BFGS→K-FAC),tradeoff = 收敛速度 vs 内存 / 计算成本。</figcaption>
::endsvg

'''),

    # ch10 10.3 一阶矩 / 二阶矩 物理量对照
    ('chapter10-multiple-integrals.md', '### 10.4.3 转动惯量', r'''
::svg
<svg viewBox="0 0 380 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="30" y="30" font-size="13" font-weight="bold" fill="#1a365d">∭_Ω x^k ρ dV 物理量对照</text>
  <line x1="30" y1="40" x2="350" y2="40" stroke="#888" stroke-width="0.8"/>
  <text x="30" y="65" font-size="13" font-family="serif" fill="#1a365d">k=0:</text>
  <text x="100" y="65" font-size="13" fill="#444">M (总质量)</text>
  <text x="30" y="90" font-size="13" font-family="serif" fill="#c2410c">k=1:</text>
  <text x="100" y="90" font-size="13" fill="#444">质心矩 Mx̄</text>
  <text x="30" y="115" font-size="13" font-family="serif" fill="#2d6e2d">k=2:</text>
  <text x="100" y="115" font-size="13" fill="#444">转动惯量 I / 概率方差</text>
  <text x="30" y="140" font-size="13" font-family="serif" fill="#b91c1c">k=3,4:</text>
  <text x="100" y="140" font-size="13" fill="#444">偏度 / 峰度 (高阶统计量)</text>
  <text x="30" y="165" font-size="11" fill="#666">概率分布的"形状"由各阶矩刻画 (矩生成函数 MGF)</text>
</svg>
<figcaption>图 10.4.8 高阶矩对照表:0 阶 $=$ 质量,1 阶 $=$ 质心,2 阶 $=$ 转动惯量 $=$ 方差,3-4 阶 $=$ 偏度峰度 — 统一物理 / 统计两套语言。</figcaption>
::endsvg

'''),

    # ch11 11.6 涡度场 (流体)
    ('chapter11-line-surface-integrals.md', '### 11.6.6 三大公式与微分形式视角', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="vo1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <line x1="40" y1="40" x2="100" y2="40" stroke="#1a365d" stroke-width="1.5" marker-end="url(#vo1)"/>
  <line x1="40" y1="60" x2="100" y2="60" stroke="#1a365d" stroke-width="1.5" marker-end="url(#vo1)"/>
  <line x1="40" y1="80" x2="100" y2="80" stroke="#1a365d" stroke-width="1.5" marker-end="url(#vo1)"/>
  <text x="35" y="100" font-size="11" fill="#1a365d">均匀流 ω=0</text>
  <circle cx="240" cy="60" r="20" fill="none" stroke="#c2410c" stroke-width="1.5"/>
  <path d="M 250 50 A 12 12 0 0 1 250 70" fill="none" stroke="#c2410c" stroke-width="2" marker-end="url(#vo1)"/>
  <path d="M 230 70 A 12 12 0 0 1 230 50" fill="none" stroke="#c2410c" stroke-width="2" marker-end="url(#vo1)"/>
  <text x="220" y="100" font-size="11" fill="#c2410c">涡旋 ω≠0</text>
  <line x1="40" y1="150" x2="320" y2="150" stroke="#888" stroke-width="0.8"/>
  <text x="35" y="180" font-size="12" fill="#444">ω = ∇×v⃗ (流场涡度): 局部"转速向量"</text>
</svg>
<figcaption>图 11.6.9 涡度场 $\omega=\nabla\times\vec{v}$:均匀流(均匀箭头)$\omega=0$ 无旋;涡旋(同心圆)$|\omega|$ 大 — 流体力学中区分层流 / 湍流的核心量。</figcaption>
::endsvg

'''),

    # ch12 12.3 绝对收敛 vs 条件收敛 决策树
    ('chapter12-infinite-series.md', '### 12.3.2 绝对收敛 vs 条件收敛', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="tr1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <ellipse cx="180" cy="35" rx="80" ry="20" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="120" y="40" font-size="12" font-weight="bold">含负项级数 ∑u_n</text>
  <line x1="180" y1="55" x2="180" y2="80" stroke="#1a365d" marker-end="url(#tr1)"/>
  <text x="190" y="73" font-size="11">查 ∑|u_n|?</text>
  <rect x="40" y="90" width="120" height="40" rx="5" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="55" y="115" font-size="12" font-weight="bold" fill="#2d6e2d">∑|u_n| 收敛</text>
  <text x="60" y="145" font-size="11" fill="#2d6e2d">→ 绝对收敛 ✓</text>
  <text x="55" y="162" font-size="10" fill="#666">任意重排不变</text>
  <rect x="200" y="90" width="120" height="40" rx="5" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="220" y="115" font-size="12" font-weight="bold" fill="#b91c1c">∑|u_n| 发散</text>
  <line x1="260" y1="130" x2="260" y2="155" stroke="#b91c1c" marker-end="url(#tr1)"/>
  <text x="265" y="148" font-size="10">∑u_n 自身?</text>
  <rect x="200" y="165" width="60" height="30" fill="#fef6e4" stroke="#c9a227"/>
  <text x="208" y="183" font-size="11" fill="#8b6f1c">收敛: 条件</text>
  <rect x="265" y="165" width="55" height="30" fill="#888" fill-opacity="0.3"/>
  <text x="275" y="183" font-size="11">发散</text>
</svg>
<figcaption>图 12.3.3 含负项级数判别流程图:先查 $\sum|u_n|$;收敛 → 绝对收敛(最强);发散 + $\sum u_n$ 收敛 → 条件收敛(脆弱);全发散 → 发散。</figcaption>
::endsvg

'''),

    # ch12 12.6 三角恒等式 + 内积投影
    ('chapter12-infinite-series.md', '### 12.6.2 系数公式从正交性的推导', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="pj1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="pj2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <line x1="60" y1="160" x2="280" y2="160" stroke="#1a365d" stroke-width="2.5" marker-end="url(#pj2)"/>
  <text x="240" y="180" font-size="13" font-style="italic" fill="#1a365d">cos nx 基</text>
  <line x1="60" y1="160" x2="180" y2="50" stroke="#c2410c" stroke-width="2.5" marker-end="url(#pj1)"/>
  <text x="185" y="50" font-size="13" font-style="italic" fill="#c2410c">f(x)</text>
  <line x1="180" y1="50" x2="180" y2="160" stroke="#888" stroke-width="1" stroke-dasharray="3 2"/>
  <line x1="60" y1="160" x2="180" y2="160" stroke="#2d6e2d" stroke-width="4"/>
  <text x="90" y="180" font-size="13" fill="#2d6e2d">aₙ = ⟨f, cos nx⟩/π (投影)</text>
  <path d="M 85 160 A 20 20 0 0 0 80 140" fill="none" stroke="#444" stroke-width="0.8"/>
  <text x="80" y="148" font-size="11" fill="#444">θ_n</text>
  <text x="30" y="35" font-size="11" fill="#666">Fourier 系数 = f 在三角基上的"投影长度"</text>
</svg>
<figcaption>图 12.6.9 Fourier 系数 $a_n=\frac{1}{\pi}\int f\cos nx\,dx$ 几何 = $f$ 在 $\cos nx$ 方向上的内积"投影长度",跟向量到坐标轴投影完全同源。</figcaption>
::endsvg

'''),

    # ch10 10.5 Stirling 公式 (n! 渐近)
    ('chapter10-multiple-integrals.md', '### 10.5.4 Gamma 函数与 Beta 函数', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="40" y1="140" x2="330" y2="140" stroke="#888" stroke-width="1"/>
  <line x1="40" y1="20" x2="40" y2="160" stroke="#888" stroke-width="1"/>
  <text x="335" y="145" font-size="11" fill="#888">n</text>
  <text x="22" y="22" font-size="11" fill="#888">n!</text>
  <path d="M 50 138 L 80 132 L 110 120 L 140 100 L 175 75 L 215 50 L 260 30" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="160" y="60" font-size="11" fill="#1a365d">n! = Γ(n+1)</text>
  <path d="M 50 138 L 80 130 L 110 120 L 140 105 L 175 80 L 215 55 L 260 35" fill="none" stroke="#c2410c" stroke-width="1.6" stroke-dasharray="4 3"/>
  <text x="170" y="105" font-size="11" fill="#c2410c">Stirling: n!~√(2πn)(n/e)ⁿ</text>
  <text x="35" y="170" font-size="11" fill="#666">大 n 时相对误差 ~ 1/(12n), 极精确 (热力学/组合)</text>
</svg>
<figcaption>图 10.5.5 Stirling 公式 $n!\approx\sqrt{2\pi n}(n/e)^n$:阶乘的渐近展开,大 $n$ 时误差 $\sim 1/(12n)$ — 概率论 / 统计力学 / 信息论关键工具。</figcaption>
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
