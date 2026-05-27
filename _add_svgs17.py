"""第十七批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch8 8.3 截痕法画曲面 (椭球三族截面)
    ('chapter08-vectors.md', '### 8.3.5 截痕法画曲面', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="80" cy="100" rx="50" ry="35" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="80" cy="100" rx="35" ry="25" fill="none" stroke="#1a365d" stroke-width="1.1"/>
  <ellipse cx="80" cy="100" rx="20" ry="14" fill="none" stroke="#1a365d" stroke-width="0.9"/>
  <text x="55" y="170" font-size="11" fill="#1a365d">z=c 切片 (椭圆)</text>
  <ellipse cx="200" cy="100" rx="40" ry="55" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <ellipse cx="200" cy="100" rx="28" ry="38" fill="none" stroke="#c9a227" stroke-width="1.1"/>
  <text x="175" y="170" font-size="11" fill="#8b6f1c">x=c 切片 (椭圆)</text>
  <ellipse cx="320" cy="100" rx="50" ry="40" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <ellipse cx="320" cy="100" rx="35" ry="28" fill="none" stroke="#2d6e2d" stroke-width="1.1"/>
  <text x="293" y="170" font-size="11" fill="#2d6e2d">y=c 切片 (椭圆)</text>
  <text x="60" y="30" font-size="12" font-weight="bold" fill="#444">椭球面三族截痕 (堆叠还原 3D)</text>
</svg>
<figcaption>图 8.3.3 截痕法画椭球面:用 $x=c,y=c,z=c$ 三族平面截切,得三族同心椭圆;堆叠还原 3D 曲面 — 机械绘图与 matplotlib 内部算法。</figcaption>
::endsvg

'''),

    # ch9 9.7 法线过球心 (球面特征)
    ('chapter09-multivariate.md', '### 9.7.2 曲面的切平面与法线(隐式)', r'''
::svg
<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="nm1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <circle cx="160" cy="110" r="70" fill="#eef4fb" fill-opacity="0.6" stroke="#1a365d" stroke-width="1.8"/>
  <circle cx="160" cy="110" r="3" fill="#1a365d"/>
  <text x="125" y="113" font-size="12" font-weight="bold" fill="#1a365d">球心</text>
  <circle cx="220" cy="75" r="4" fill="#c2410c"/>
  <text x="228" y="73" font-size="11" fill="#c2410c">P</text>
  <line x1="160" y1="110" x2="270" y2="45" stroke="#c2410c" stroke-width="1.8" stroke-dasharray="4 3" marker-end="url(#nm1)"/>
  <text x="225" y="48" font-size="11" fill="#c2410c">法线</text>
  <line x1="160" y1="110" x2="220" y2="75" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="35" y="200" font-size="11" fill="#666">球面性质: 任一点法线 = ∇F = 2(x,y,z) 必过球心</text>
</svg>
<figcaption>图 9.7.3 球面 $x^2+y^2+z^2=R^2$ 法线必过球心:$\nabla F=2(x,y,z)$ 方向沿 $\vec{OP}$,这是球的本质几何性质。</figcaption>
::endsvg

'''),

    # ch10 10.2 Gauss 积分极坐标推导
    ('chapter10-multiple-integrals.md', '### 10.2.3 极坐标变换与雅可比因子', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="35" y="40" font-size="13" fill="#1a365d">I = ∫_{-∞}^{∞} e^{-x²} dx = ?</text>
  <text x="35" y="65" font-size="13" fill="#c2410c">技巧: I² = (∫e^{-x²}dx)(∫e^{-y²}dy)</text>
  <text x="55" y="90" font-size="13" fill="#c2410c">       = ∬ e^{-(x²+y²)} dxdy</text>
  <text x="55" y="115" font-size="13" font-style="italic" fill="#2d6e2d">换极坐标: x²+y²=r²</text>
  <text x="55" y="140" font-size="13" fill="#2d6e2d">= ∫₀^{2π} dθ ∫₀^∞ e^{-r²}·r dr = 2π·(1/2) = π</text>
  <text x="50" y="170" font-size="14" font-weight="bold" fill="#b91c1c">⇒ I = √π</text>
  <text x="200" y="170" font-size="11" fill="#666">→ 正态分布归一化系数 1/√(2π)</text>
</svg>
<figcaption>图 10.2.6 Gauss 积分 $\int e^{-x^2}dx=\sqrt{\pi}$:平方+极坐标 = 经典推导;给出正态分布密度归一化系数 $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$。</figcaption>
::endsvg

'''),

    # ch10 10.3 球体积 4πR³/3 几何
    ('chapter10-multiple-integrals.md', '### 10.3.3 球坐标(关键)', r'''
::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="160" cy="100" r="70" fill="#eef4fb" fill-opacity="0.5" stroke="#1a365d" stroke-width="1.8"/>
  <ellipse cx="160" cy="100" rx="70" ry="14" fill="none" stroke="#1a365d" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="115" y="115" font-size="13" fill="#1a365d">球 R=R</text>
  <text x="30" y="190" font-size="12" font-weight="bold" fill="#444">V = ∫₀^{2π}∫₀^π∫₀^R ρ²sinφ dρdφdθ = 4πR³/3</text>
</svg>
<figcaption>图 10.3.4 球体积公式推导:$V=\int_0^{2\pi}d\theta\int_0^\pi\sin\varphi\,d\varphi\int_0^R\rho^2\,d\rho=2\pi\cdot 2\cdot\frac{R^3}{3}=\frac{4\pi R^3}{3}$。</figcaption>
::endsvg

'''),

    # ch11 11.6 Ampère 环路定律
    ('chapter11-line-surface-integrals.md', '### 11.6.4 物理意义:法拉第电磁感应', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="am1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <line x1="180" y1="20" x2="180" y2="180" stroke="#1a365d" stroke-width="2.5"/>
  <text x="185" y="20" font-size="12" fill="#1a365d">电流 I</text>
  <circle cx="180" cy="100" r="60" fill="none" stroke="#c2410c" stroke-width="2.5" marker-end="url(#am1)"/>
  <text x="240" y="105" font-size="12" font-weight="bold" fill="#c2410c">∂Σ 闭合回路</text>
  <text x="35" y="40" font-size="12" font-weight="bold" fill="#444">∮ B⃗·dr⃗ = μ₀ I (Ampère 定律)</text>
  <text x="35" y="175" font-size="11" fill="#666">Maxwell 第 4 条积分形式 (∇×B=μ₀J 用 Stokes)</text>
</svg>
<figcaption>图 11.6.7 Ampère 环路定律:沿任意包围电流的闭合曲线 $\oint\vec{B}\cdot d\vec{r}=\mu_0 I$ — Stokes + $\nabla\times\vec{B}=\mu_0\vec{J}$ 立得。</figcaption>
::endsvg

'''),

    # ch12 12.6 Fourier 反变换 (信号重构)
    ('chapter12-infinite-series.md', '### 12.6.6 物理 / 工程应用速览', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ift1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="40" width="100" height="60" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="38" y="65" font-size="12" font-weight="bold" fill="#1a365d">时域 f(t)</text>
  <text x="30" y="85" font-size="11" fill="#1a365d">原始信号</text>
  <line x1="120" y1="70" x2="155" y2="70" stroke="#1a365d" stroke-width="2" marker-end="url(#ift1)"/>
  <text x="125" y="63" font-size="10" fill="#888">F</text>
  <rect x="155" y="40" width="100" height="60" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="173" y="65" font-size="12" font-weight="bold" fill="#8b6f1c">频域 F(ω)</text>
  <text x="165" y="85" font-size="11" fill="#8b6f1c">谱 (MP3 编)</text>
  <line x1="255" y1="70" x2="290" y2="70" stroke="#c2410c" stroke-width="2" marker-end="url(#ift1)"/>
  <text x="262" y="63" font-size="10" fill="#c2410c">F⁻¹</text>
  <rect x="290" y="40" width="60" height="60" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="297" y="65" font-size="11" font-weight="bold" fill="#2d6e2d">重构 f̃</text>
  <line x1="155" y1="120" x2="180" y2="160" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="35" y="170" font-size="11" fill="#b91c1c">压缩: 丢人耳不敏感的高频, F→F̃</text>
  <text x="35" y="190" font-size="11" fill="#666">MP3/AAC/JPEG 的灵魂 = Fourier 域有损压缩</text>
</svg>
<figcaption>图 12.6.7 Fourier 正反变换 = 信号压缩管线:F 把时域 $f(t)$ → 频域 $F(\omega)$ → 丢高频 → F$^{-1}$ 重构 $\tilde f$。MP3 / JPEG 算法核心。</figcaption>
::endsvg

'''),

    # ch9 9.10 神经网络 forward + backward
    ('chapter09-multivariate.md', '### 9.10.5 与机器学习的关系', r'''
::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="nf1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="nf2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <text x="35" y="40" font-size="12" font-weight="bold" fill="#1a365d">forward (正向: 用链式法则)</text>
  <circle cx="50" cy="80" r="15" fill="#eef4fb" stroke="#1a365d"/>
  <text x="44" y="85" font-size="12">x</text>
  <line x1="65" y1="80" x2="95" y2="80" stroke="#1a365d" marker-end="url(#nf1)"/>
  <circle cx="115" cy="80" r="15" fill="#fef6e4" stroke="#c9a227"/>
  <text x="105" y="85" font-size="11">σ(W₁)</text>
  <line x1="130" y1="80" x2="160" y2="80" stroke="#1a365d" marker-end="url(#nf1)"/>
  <circle cx="180" cy="80" r="15" fill="#fef6e4" stroke="#c9a227"/>
  <text x="170" y="85" font-size="11">σ(W₂)</text>
  <line x1="195" y1="80" x2="225" y2="80" stroke="#1a365d" marker-end="url(#nf1)"/>
  <circle cx="245" cy="80" r="15" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="242" y="85" font-size="12">ŷ</text>
  <line x1="260" y1="80" x2="290" y2="80" stroke="#1a365d" marker-end="url(#nf1)"/>
  <circle cx="310" cy="80" r="15" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="306" y="85" font-size="12">L</text>
  <text x="35" y="135" font-size="12" font-weight="bold" fill="#c2410c">backprop (反向: 应用矩阵链式)</text>
  <path d="M 310 100 Q 200 165 50 100" fill="none" stroke="#c2410c" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#nf2)"/>
  <text x="155" y="200" font-size="11" fill="#c2410c">∂L/∂Wₖ = ∂L/∂ŷ · ∂ŷ/∂Wₖ (链式回传)</text>
</svg>
<figcaption>图 9.10.5 神经网络训练 = 多元链式法则的工程实现:forward 用链式合并;backprop 用矩阵链式从损失逐层回传到每个 $W_k$。</figcaption>
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
