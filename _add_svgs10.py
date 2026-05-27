"""第十批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch11 11.4 球面参数化 (重补,用 11.4.1 锚点)
    ('chapter11-line-surface-integrals.md', '### 11.4.1 定义与几何意义', r'''
::svg
<svg viewBox="0 0 320 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="160" cy="110" r="80" fill="#eef4fb" fill-opacity="0.5" stroke="#1a365d" stroke-width="1.5"/>
  <ellipse cx="160" cy="110" rx="80" ry="14" fill="none" stroke="#1a365d" stroke-width="0.8" stroke-dasharray="3 2"/>
  <ellipse cx="160" cy="80" rx="74" ry="12" fill="none" stroke="#888" stroke-width="0.7"/>
  <ellipse cx="160" cy="140" rx="74" ry="12" fill="none" stroke="#888" stroke-width="0.7"/>
  <line x1="160" y1="30" x2="240" y2="120" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <line x1="160" y1="30" x2="80" y2="120" stroke="#888" stroke-width="0.7" stroke-dasharray="2 2"/>
  <path d="M 197 65 L 218 73 L 217 95 L 196 87 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="195" y="55" font-size="11" fill="#8b6f1c">R²sinφ dφdθ</text>
  <text x="30" y="200" font-size="11" fill="#666">球面参数化 r⃗(φ,θ), dS=R²sinφ dφ dθ (两极退化)</text>
</svg>
<figcaption>图 11.4.5 球面参数网格 $\vec{r}(\varphi,\theta)=R(\sin\varphi\cos\theta,\sin\varphi\sin\theta,\cos\varphi)$,面积元 $R^2\sin\varphi$。</figcaption>
::endsvg

'''),

    # ch12 12.2 比值判别 ρ 区域
    ('chapter12-infinite-series.md', '### 12.2.2 比值判别法', r'''
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
  <text x="138" y="125" font-size="11" fill="#888">ρ=1 失效 → Raabe/积分判别</text>
  <text x="30" y="145" font-size="11" fill="#444">ρ = lim |a_{n+1}/a_n| (d'Alembert 比值判别)</text>
</svg>
<figcaption>图 12.2.3 比值判别 $\rho$ 临界:$\rho<1$ 收敛,$>1$ 发散,$=1$ 需更精细判别(p-级数 / Raabe)。</figcaption>
::endsvg

'''),

    # ch10 10.1 黎曼上和下和 (Darboux)
    ('chapter10-multiple-integrals.md', '### 10.1.2 几何意义与可积性', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 30 170 Q 100 50 200 80 Q 280 110 340 60" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="35" y="35" font-size="12" fill="#1a365d">z=f(x,y)</text>
  <rect x="50" y="80" width="40" height="100" fill="#fef6e4" stroke="#c9a227" stroke-width="1" opacity="0.7"/>
  <rect x="90" y="60" width="40" height="120" fill="#fef6e4" stroke="#c9a227" stroke-width="1" opacity="0.7"/>
  <rect x="130" y="60" width="40" height="120" fill="#fef6e4" stroke="#c9a227" stroke-width="1" opacity="0.7"/>
  <rect x="170" y="75" width="40" height="105" fill="#fef6e4" stroke="#c9a227" stroke-width="1" opacity="0.7"/>
  <rect x="210" y="85" width="40" height="95" fill="#fef6e4" stroke="#c9a227" stroke-width="1" opacity="0.7"/>
  <rect x="250" y="95" width="40" height="85" fill="#fef6e4" stroke="#c9a227" stroke-width="1" opacity="0.7"/>
  <line x1="30" y1="180" x2="340" y2="180" stroke="#888" stroke-width="1"/>
  <text x="50" y="195" font-size="11" fill="#8b6f1c">小柱体高 = f(ξᵢ) (代表点)</text>
  <text x="35" y="20" font-size="11" fill="#666">∬f dσ = lim Σ f(ξᵢ,ηᵢ)ΔSᵢ (柱体逼近 → 真体积)</text>
</svg>
<figcaption>图 10.1.2 Riemann 和近似:把 $D$ 划成小块,每小块上建一根柱体(高 = $f$ 在代表点的值),柱体体积之和取极限 = 二重积分。</figcaption>
::endsvg

'''),

    # ch11 11.5 立体角 (3D 立体角 Ω)
    ('chapter11-line-surface-integrals.md', '### 11.5.5 例题', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="180" cy="100" r="60" fill="none" stroke="#888" stroke-width="0.8" stroke-dasharray="3 2"/>
  <circle cx="180" cy="100" r="4" fill="#1a365d"/>
  <text x="155" y="115" font-size="11" fill="#1a365d">原点 O</text>
  <path d="M 180 100 L 260 60 A 60 60 0 0 1 290 110 L 180 100 Z" fill="#fef6e4" fill-opacity="0.7" stroke="#c9a227" stroke-width="1.5"/>
  <text x="245" y="85" font-size="12" fill="#8b6f1c">立体角 Ω</text>
  <path d="M 260 60 L 290 110" stroke="#8b6f1c" stroke-width="2"/>
  <text x="295" y="90" font-size="11" fill="#8b6f1c">球面截块 ΔS</text>
  <text x="30" y="180" font-size="11" fill="#666">Ω = ΔS / r² (球面截块面积 / 半径²),  全空间 4π sr</text>
</svg>
<figcaption>图 11.5.4 立体角 $\Omega$:从原点看向某方向,被该方向遮住的球面截块面积除以 $r^2$。整个球面对应 $4\pi$ 球面度 = Gauss 定理的 "总通量" 几何根。</figcaption>
::endsvg

'''),

    # ch9 9.0 章节地图 + 12 大定理
    ('chapter09-multivariate.md', '### 9.0.1 全章地图', r'''
::svg
<svg viewBox="0 0 380 240" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ma1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="40" width="55" height="30" rx="4" fill="#eef4fb" stroke="#1a365d"/>
  <text x="28" y="60" font-size="11">9.1 概念</text>
  <rect x="85" y="40" width="55" height="30" rx="4" fill="#eef4fb" stroke="#1a365d"/>
  <text x="95" y="60" font-size="11">9.2 偏导</text>
  <rect x="150" y="40" width="60" height="30" rx="4" fill="#eef4fb" stroke="#1a365d"/>
  <text x="158" y="60" font-size="11">9.3 全微分</text>
  <line x1="75" y1="55" x2="84" y2="55" stroke="#1a365d" marker-end="url(#ma1)"/>
  <line x1="140" y1="55" x2="149" y2="55" stroke="#1a365d" marker-end="url(#ma1)"/>
  <rect x="220" y="40" width="55" height="30" rx="4" fill="#fef6e4" stroke="#c9a227"/>
  <text x="227" y="60" font-size="11">9.4 链式</text>
  <rect x="285" y="40" width="55" height="30" rx="4" fill="#fef6e4" stroke="#c9a227"/>
  <text x="293" y="60" font-size="11">9.5 隐函数</text>
  <line x1="210" y1="55" x2="219" y2="55" stroke="#1a365d" marker-end="url(#ma1)"/>
  <line x1="275" y1="55" x2="284" y2="55" stroke="#1a365d" marker-end="url(#ma1)"/>
  <rect x="20" y="110" width="55" height="30" rx="4" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="30" y="130" font-size="11">9.6 梯度</text>
  <rect x="85" y="110" width="60" height="30" rx="4" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="92" y="130" font-size="11">9.7 切平面</text>
  <rect x="155" y="110" width="60" height="30" rx="4" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="160" y="130" font-size="11">9.8 Hessian</text>
  <rect x="225" y="110" width="60" height="30" rx="4" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="232" y="130" font-size="11">9.9 Taylor</text>
  <rect x="295" y="110" width="65" height="30" rx="4" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="298" y="130" font-size="11">9.10 OLS</text>
  <line x1="75" y1="125" x2="84" y2="125" stroke="#1a365d" marker-end="url(#ma1)"/>
  <line x1="145" y1="125" x2="154" y2="125" stroke="#1a365d" marker-end="url(#ma1)"/>
  <line x1="215" y1="125" x2="224" y2="125" stroke="#1a365d" marker-end="url(#ma1)"/>
  <line x1="285" y1="125" x2="294" y2="125" stroke="#1a365d" marker-end="url(#ma1)"/>
  <text x="20" y="180" font-size="11" font-weight="bold" fill="#444">核心定理库:</text>
  <text x="20" y="200" font-size="10" fill="#666">Clairaut · 可微 ⇒ 连续+偏导 · 雅可比链式 · 隐函数定理</text>
  <text x="20" y="218" font-size="10" fill="#666">梯度最速 · Cauchy-Schwarz · Hessian D=AC-B² · Newton 法</text>
  <text x="20" y="236" font-size="10" fill="#666">Descent Lemma · Taylor 余项 · OLS = 正交投影 · Ridge</text>
</svg>
<figcaption>图 9.0.2 ch9 学习流程:概念→偏导→全微分→链式/隐函数→梯度/切平面/Hessian/Taylor/OLS,每节对应一个核心定理。</figcaption>
::endsvg

'''),

    # ch12 12.0 章节地图
    ('chapter12-infinite-series.md', '### 12.0.1 全章地图', r'''
::svg
<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="z1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="30" width="70" height="35" rx="5" fill="#eef4fb" stroke="#1a365d"/>
  <text x="27" y="53" font-size="11" font-weight="bold">12.1 概念</text>
  <line x1="90" y1="48" x2="120" y2="48" stroke="#1a365d" stroke-width="1.5" marker-end="url(#z1)"/>
  <rect x="120" y="30" width="80" height="35" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="125" y="53" font-size="11" font-weight="bold">12.2 正项 6 法</text>
  <line x1="200" y1="48" x2="230" y2="48" stroke="#1a365d" stroke-width="1.5" marker-end="url(#z1)"/>
  <rect x="230" y="30" width="90" height="35" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="237" y="53" font-size="11" font-weight="bold">12.3 交错+绝对</text>
  <line x1="170" y1="65" x2="170" y2="90" stroke="#1a365d" stroke-width="1.5" marker-end="url(#z1)"/>
  <rect x="135" y="95" width="80" height="35" rx="5" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="140" y="118" font-size="11" font-weight="bold">12.4 幂级数</text>
  <line x1="215" y1="115" x2="240" y2="115" stroke="#1a365d" stroke-width="1.5" marker-end="url(#z1)"/>
  <rect x="240" y="95" width="70" height="35" rx="5" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="248" y="118" font-size="11" font-weight="bold">12.5 Taylor</text>
  <line x1="175" y1="130" x2="175" y2="155" stroke="#1a365d" stroke-width="1.5" marker-end="url(#z1)"/>
  <rect x="135" y="158" width="80" height="35" rx="5" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="140" y="180" font-size="11" font-weight="bold">12.6 Fourier</text>
  <text x="220" y="180" font-size="10" fill="#666">→ AI: MP3/JPEG/FFT/Diffusion</text>
</svg>
<figcaption>图 12.0.1 ch12 学习路径:常数级数(12.1-12.3)→ 幂级数(12.4)→ Taylor(12.5)→ Fourier(12.6),应用到信号 / 图像 / AI。</figcaption>
::endsvg

'''),

    # ch10 10.0 章节地图
    ('chapter10-multiple-integrals.md', '### 10.0.1 全章地图', r'''
::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="t1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
  </defs>
  <rect x="20" y="30" width="80" height="40" rx="5" fill="#eef4fb" stroke="#1a365d"/>
  <text x="30" y="55" font-size="12" font-weight="bold">10.1 概念</text>
  <line x1="100" y1="50" x2="125" y2="50" stroke="#1a365d" marker-end="url(#t1)"/>
  <rect x="125" y="30" width="80" height="40" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="130" y="55" font-size="12" font-weight="bold">10.2 二重</text>
  <line x1="205" y1="50" x2="230" y2="50" stroke="#1a365d" marker-end="url(#t1)"/>
  <rect x="230" y="30" width="80" height="40" rx="5" fill="#fef6e4" stroke="#c9a227"/>
  <text x="235" y="55" font-size="12" font-weight="bold">10.3 三重</text>
  <line x1="270" y1="70" x2="270" y2="100" stroke="#1a365d" marker-end="url(#t1)"/>
  <rect x="180" y="110" width="80" height="40" rx="5" fill="#ecf7ec" stroke="#2d6e2d"/>
  <text x="185" y="135" font-size="12" font-weight="bold">10.4 应用</text>
  <line x1="180" y1="130" x2="160" y2="130" stroke="#1a365d" marker-end="url(#t1)"/>
  <rect x="60" y="110" width="100" height="40" rx="5" fill="#fde2e2" stroke="#b91c1c"/>
  <text x="65" y="135" font-size="12" font-weight="bold">10.5 含参变量</text>
  <text x="65" y="172" font-size="11" fill="#666">→ Γ/Beta + 物理 + 概率 + AI 贝叶斯</text>
</svg>
<figcaption>图 10.0.1 ch10 学习路径:概念性质 → 二重 → 三重 → 应用 + 含参积分;落地到物理 / 概率 / 工程 / AI 贝叶斯。</figcaption>
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
