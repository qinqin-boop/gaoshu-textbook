"""第十九批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch10 10.4 平行轴定理 I_L = I_cm + Md²
    ('chapter10-multiple-integrals.md', '### 10.4.3 转动惯量', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <ellipse cx="180" cy="100" rx="80" ry="50" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <circle cx="180" cy="100" r="3" fill="#1a365d"/>
  <text x="186" y="105" font-size="11" font-weight="bold" fill="#1a365d">质心</text>
  <line x1="180" y1="40" x2="180" y2="170" stroke="#1a365d" stroke-width="2" stroke-dasharray="3 2"/>
  <text x="160" y="40" font-size="11" fill="#1a365d">轴 cm</text>
  <line x1="270" y1="40" x2="270" y2="170" stroke="#c2410c" stroke-width="2"/>
  <text x="276" y="40" font-size="11" fill="#c2410c">轴 L</text>
  <line x1="180" y1="100" x2="270" y2="100" stroke="#888" stroke-width="1.5"/>
  <text x="215" y="93" font-size="13" font-weight="bold" fill="#888">d</text>
  <text x="35" y="190" font-size="11" font-weight="bold" fill="#444">I_L = I_cm + M·d² (平行轴定理 / Huygens-Steiner)</text>
</svg>
<figcaption>图 10.4.7 平行轴定理 $I_L=I_{\text{cm}}+Md^2$:绕任意平行轴的转动惯量 = 绕质心轴的 + 整体质量 $\times$ 距离平方;刚体动力学基本工具。</figcaption>
::endsvg

'''),

    # ch11 11.5/11.6 Maxwell 4 方程总览
    ('chapter11-line-surface-integrals.md', '### 11.6.4 物理意义:法拉第电磁感应', r'''
::svg
<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="20" y="30" width="170" height="80" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="30" y="55" font-size="13" font-weight="bold" fill="#1a365d">∮ E⃗·dS⃗ = Q_enc/ε₀</text>
  <text x="30" y="80" font-size="11" fill="#1a365d">Gauss 电场 (Gauss 公式)</text>
  <text x="30" y="100" font-size="10" fill="#666">微分: ∇·E = ρ/ε₀</text>
  <rect x="200" y="30" width="170" height="80" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="210" y="55" font-size="13" font-weight="bold" fill="#8b6f1c">∮ B⃗·dS⃗ = 0</text>
  <text x="210" y="80" font-size="11" fill="#8b6f1c">无磁单极 (Gauss 磁场)</text>
  <text x="210" y="100" font-size="10" fill="#666">微分: ∇·B = 0</text>
  <rect x="20" y="120" width="170" height="80" fill="#ecf7ec" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="30" y="145" font-size="13" font-weight="bold" fill="#2d6e2d">∮ E⃗·dr⃗ = -dΦ_B/dt</text>
  <text x="30" y="170" font-size="11" fill="#2d6e2d">法拉第感应 (Stokes)</text>
  <text x="30" y="190" font-size="10" fill="#666">微分: ∇×E = -∂B/∂t</text>
  <rect x="200" y="120" width="170" height="80" fill="#fde2e2" stroke="#b91c1c" stroke-width="1.5"/>
  <text x="210" y="145" font-size="13" font-weight="bold" fill="#b91c1c">∮ B⃗·dr⃗ = μ₀I + μ₀ε₀dΦ_E/dt</text>
  <text x="210" y="170" font-size="11" fill="#b91c1c">Ampère-Maxwell</text>
  <text x="210" y="190" font-size="10" fill="#666">微分: ∇×B = μ₀J+μ₀ε₀∂E/∂t</text>
</svg>
<figcaption>图 11.6.8 Maxwell 4 方程整体:全部用 Gauss/Stokes 公式从微分形式立得积分形式 — 经典物理学最伟大的方程组。</figcaption>
::endsvg

'''),

    # ch12 12.6 DFT/FFT 实现
    ('chapter12-infinite-series.md', '### 12.6.4 Bessel 不等式与 Parseval 恒等式', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ft1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <text x="35" y="35" font-size="12" font-weight="bold" fill="#1a365d">连续 Fourier:</text>
  <text x="35" y="55" font-size="11" fill="#1a365d">cₙ = (1/2π)∫_{-π}^π f(x)e^{-inx}dx (n∈ℤ)</text>
  <line x1="40" y1="80" x2="320" y2="80" stroke="#888" stroke-width="0.8" stroke-dasharray="3 2"/>
  <text x="35" y="105" font-size="12" font-weight="bold" fill="#c2410c">离散 DFT (采样 N 点):</text>
  <text x="35" y="125" font-size="11" fill="#c2410c">X_k = Σ_{n=0}^{N-1} x_n e^{-2πink/N} (k=0..N-1)</text>
  <text x="35" y="155" font-size="12" font-weight="bold" fill="#2d6e2d">FFT (Cooley-Tukey 1965):</text>
  <text x="35" y="175" font-size="11" fill="#2d6e2d">朴素 O(N²) → 分治 O(N log N)</text>
  <text x="35" y="195" font-size="10" fill="#666">20 世纪 Top 10 算法</text>
</svg>
<figcaption>图 12.6.8 Fourier 三层级:连续→离散 DFT(采样)→FFT(快速算法):$O(N^2)\to O(N\log N)$ — 现代信号处理 / 图像 / 数字音频的基石。</figcaption>
::endsvg

'''),

    # ch12 12.2 Cauchy 浓缩判别 ∑a_n 与 ∑2^n a_{2^n}
    ('chapter12-infinite-series.md', '### 12.2.5 Raabe 判别法(比值失效时的精化)', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <text x="30" y="40" font-size="13" font-weight="bold" fill="#1a365d">Cauchy 浓缩定理</text>
  <text x="30" y="65" font-size="12">设 aₙ ≥ 0 单调递减, 则</text>
  <text x="30" y="95" font-size="13" font-family="serif" fill="#c2410c">∑ aₙ 收敛 ⇔ ∑ 2ⁿ a_{2ⁿ} 收敛</text>
  <text x="30" y="130" font-size="11" fill="#444">用法: ∑ 1/n^p, 2ⁿ·1/(2ⁿ)^p = 2^{n(1-p)}</text>
  <text x="30" y="150" font-size="11" fill="#444">几何级数收敛 ⇔ 1-p < 0 ⇔ p > 1 ✓</text>
  <text x="30" y="170" font-size="11" fill="#666">优雅证 p-级数 + 处理 ∑ 1/(n log n) 形式</text>
</svg>
<figcaption>图 12.2.5 Cauchy 浓缩定理:把 $\sum a_n$ 化为 $\sum 2^n a_{2^n}$ 比较,优雅证明 $p$-级数 + 适用于 $\sum 1/(n\log n)$ 这种边界情形。</figcaption>
::endsvg

'''),

    # ch9 9.5 KKT 条件几何 (不等式约束)
    ('chapter09-multivariate.md', '### 9.5.5 与机器学习 / 经济学的关系', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="kk1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
    <marker id="kk2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <ellipse cx="200" cy="100" rx="120" ry="65" fill="none" stroke="#1a365d" stroke-width="1"/>
  <ellipse cx="200" cy="100" rx="80" ry="42" fill="none" stroke="#1a365d" stroke-width="1.2"/>
  <ellipse cx="200" cy="100" rx="40" ry="22" fill="none" stroke="#1a365d" stroke-width="1.4"/>
  <text x="35" y="30" font-size="11" fill="#1a365d">f 等高线</text>
  <path d="M 60 50 L 320 50 L 320 170 L 60 170 Z" fill="#fde2e2" fill-opacity="0.2" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="280" y="42" font-size="11" fill="#b91c1c">约束 g(x)≤0</text>
  <line x1="60" y1="50" x2="60" y2="170" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="60" cy="100" r="4" fill="#2d6e2d"/>
  <text x="40" y="103" font-size="12" font-weight="bold" fill="#2d6e2d">P*</text>
  <line x1="60" y1="100" x2="100" y2="100" stroke="#c2410c" stroke-width="2" marker-end="url(#kk1)"/>
  <text x="100" y="92" font-size="11" fill="#c2410c">∇f</text>
  <line x1="60" y1="100" x2="30" y2="100" stroke="#2d6e2d" stroke-width="2" marker-end="url(#kk2)"/>
  <text x="20" y="93" font-size="11" fill="#2d6e2d">μ∇g (μ≥0)</text>
  <text x="30" y="195" font-size="11" fill="#444">KKT: ∇f=μ∇g+λ∇h, μg=0 (互补松弛)</text>
</svg>
<figcaption>图 9.5.4 KKT 条件几何(不等式约束):最优点 $P^*$ 在约束边界,$\nabla f$ 与 $\nabla g$ 反向($\mu\ge 0$);SVM / 凸优化 / 经济均衡的核心。</figcaption>
::endsvg

'''),

    # ch11 11.4 流形 (高维曲面)
    ('chapter11-line-surface-integrals.md', '### 11.4.1 定义与几何意义', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <linearGradient id="mfg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1a365d" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#c9b97a" stop-opacity="0.35"/>
    </linearGradient>
  </defs>
  <path d="M 30 150 Q 100 50 200 80 Q 280 100 340 60 L 340 170 Q 270 180 200 150 T 30 175 Z" fill="url(#mfg)" stroke="#1a365d" stroke-width="1.8"/>
  <ellipse cx="180" cy="110" rx="50" ry="32" fill="#fef6e4" fill-opacity="0.7" stroke="#c9a227" stroke-width="1.5"/>
  <text x="155" y="108" font-size="12" fill="#8b6f1c">小邻域 ≈ ℝ²</text>
  <text x="35" y="30" font-size="12" font-weight="bold" fill="#1a365d">2-流形 Σ ⊂ ℝ³</text>
  <text x="35" y="190" font-size="11" fill="#666">流形: 局部像 ℝⁿ, 全局可弯曲 (球/环/Möbius)</text>
</svg>
<figcaption>图 11.4.9 流形概念:曲面 $\Sigma$ 局部看起来像 $\mathbb{R}^2$ 平面(可参数化);全局可以弯曲、有孔(环面)、不可定向(Möbius)— 微分几何的核心对象。</figcaption>
::endsvg

'''),

    # ch11 11.0 三大公式衔接图
    ('chapter11-line-surface-integrals.md', '### 11.0.3 与 §9-10 的承接', r'''
::svg
<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ar9" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="30" width="80" height="40" rx="5" fill="#eef4fb" stroke="#1a365d"/>
  <text x="35" y="55" font-size="12" font-weight="bold">§9 ∇</text>
  <line x1="100" y1="50" x2="135" y2="50" stroke="#1a365d" marker-end="url(#ar9)"/>
  <rect x="135" y="30" width="100" height="40" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="148" y="55" font-size="11" font-weight="bold">∇f / ∇·F / ∇×F</text>
  <line x1="235" y1="50" x2="270" y2="50" stroke="#1a365d" marker-end="url(#ar9)"/>
  <rect x="270" y="30" width="90" height="40" rx="5" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="283" y="55" font-size="11" font-weight="bold">§11 三大公式</text>
  <line x1="180" y1="70" x2="180" y2="100" stroke="#1a365d" marker-end="url(#ar9)"/>
  <rect x="120" y="105" width="140" height="40" rx="5" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="135" y="130" font-size="11" font-weight="bold" fill="#b91c1c">∫_∂M ω = ∫_M dω</text>
  <line x1="180" y1="145" x2="180" y2="170" stroke="#1a365d" marker-end="url(#ar9)"/>
  <text x="80" y="185" font-size="11" fill="#444">物理: Maxwell + 流体 + 引力 + 量子 (全部从这一条来)</text>
  <text x="30" y="210" font-size="11" fill="#666">微分几何 / GR / 规范场论 / de Rham 上同调</text>
</svg>
<figcaption>图 11.0.2 ch9 算子 → ch11 三大公式 → 广义 Stokes 一公式统一 → 现代物理与几何全部基础。</figcaption>
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
