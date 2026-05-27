"""第十二批 SVG."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

INJECTIONS = [
    # ch9 9.1 二元函数 3D 曲面 + 等高线投影
    ('chapter09-multivariate.md', '### 9.1.1 定义域与函数图像', r'''
::svg
<svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 40 170 Q 120 60 220 90 Q 290 110 340 70" fill="none" stroke="#1a365d" stroke-width="2"/>
  <path d="M 40 170 Q 100 130 130 80" fill="none" stroke="#1a365d" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="35" y="40" font-size="12" fill="#1a365d">3D 曲面 z=f(x,y)</text>
  <ellipse cx="180" cy="200" rx="120" ry="14" fill="none" stroke="#888" stroke-width="0.8"/>
  <ellipse cx="180" cy="200" rx="80" ry="9" fill="none" stroke="#c2410c" stroke-width="1.2"/>
  <ellipse cx="180" cy="200" rx="40" ry="5" fill="none" stroke="#c2410c" stroke-width="1.2"/>
  <text x="35" y="215" font-size="11" fill="#c2410c">xy 投影: 等高线</text>
  <line x1="180" y1="100" x2="180" y2="200" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
</svg>
<figcaption>图 9.1.2 二元函数 $z=f(x,y)$ 图像 = 3D 曲面 + 投影到 $xy$ 平面 = 等高线集合。两种表示等价,等高线密度刻画梯度大小。</figcaption>
::endsvg

'''),

    # ch10 10.1 七大性质 (区域可加 + 比较)
    ('chapter10-multiple-integrals.md', '### 10.1.4 七大基本性质', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 30 100 Q 80 40 130 60 Q 180 80 130 130 Q 80 150 30 100 Z" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="60" y="105" font-size="13" font-style="italic">D₁</text>
  <path d="M 170 110 Q 230 50 290 80 Q 340 100 290 150 Q 230 170 170 110 Z" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="225" y="120" font-size="13" font-style="italic">D₂</text>
  <line x1="130" y1="100" x2="180" y2="110" stroke="#2d6e2d" stroke-width="3"/>
  <text x="138" y="92" font-size="11" fill="#2d6e2d">共边</text>
  <text x="30" y="190" font-size="11" fill="#444">区域可加: ∬_{D₁∪D₂} f = ∬_{D₁} f + ∬_{D₂} f (无内部重叠)</text>
</svg>
<figcaption>图 10.1.3 二重积分区域可加性:两个无内部重叠区域 $D_1,D_2$(只在边界相接)的积分可分开计算后相加。</figcaption>
::endsvg

'''),

    # ch11 11.1 第一类曲线 (弧长 + 半圆质心 4R/(3π))
    ('chapter11-line-surface-integrals.md', '### 11.1.3 物理 / 几何应用', r'''
::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <path d="M 60 140 A 80 80 0 0 1 220 140" fill="none" stroke="#1a365d" stroke-width="3"/>
  <line x1="60" y1="140" x2="220" y2="140" stroke="#888" stroke-width="0.8" stroke-dasharray="2 2"/>
  <text x="35" y="155" font-size="11" fill="#888">-R</text>
  <text x="225" y="155" font-size="11" fill="#888">R</text>
  <polygon points="140,108 130,90 150,90" fill="#c2410c"/>
  <text x="155" y="100" font-size="12" fill="#c2410c">质心 (0, 2R/π)</text>
  <line x1="140" y1="140" x2="140" y2="100" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="3 2"/>
  <text x="30" y="185" font-size="11" fill="#444">ȳ = (1/L) ∫_L y ds, 半圆 L=πR ⇒ ȳ=2R/π</text>
</svg>
<figcaption>图 11.1.2 半圆形丝质心 $\bar y=2R/\pi$(比半圆板质心 $4R/(3\pi)\approx 0.42R$ 更高,因质量集中在弧上)。</figcaption>
::endsvg

'''),

    # ch12 12.5 Padé 逼近 vs Taylor
    ('chapter12-infinite-series.md', '### 12.5.5 多元 Taylor 公式概览', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="100" x2="330" y2="100" stroke="#888" stroke-width="1"/>
  <line x1="180" y1="20" x2="180" y2="180" stroke="#888" stroke-width="1"/>
  <text x="345" y="105" font-size="11" fill="#888">x</text>
  <path d="M 30 130 Q 90 60 180 80 Q 270 100 330 60" fill="none" stroke="#1a365d" stroke-width="2.5"/>
  <text x="30" y="40" font-size="11" fill="#1a365d">原函数</text>
  <path d="M 30 -100 Q 90 -20 180 80 Q 270 180 330 280" fill="none" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="60" y="60" font-size="11" fill="#c2410c">Taylor N 阶 (远处偏离)</text>
  <path d="M 30 135 Q 100 90 180 80 Q 260 70 330 65" fill="none" stroke="#2d6e2d" stroke-width="1.5"/>
  <text x="200" y="55" font-size="11" fill="#2d6e2d">Padé[N/M] (更广)</text>
  <circle cx="180" cy="80" r="3" fill="#1a365d"/>
  <text x="35" y="190" font-size="11" fill="#444">Padé: 用有理函数 P_N(x)/Q_M(x) 拟合, 远离展开点也精确</text>
</svg>
<figcaption>图 12.5.3 Padé 逼近 vs Taylor:Padé[N/M](有理函数)在远离展开点比 N+M 阶 Taylor 多项式精确得多 — 数值分析 / 物理 perturbation theory 常用。</figcaption>
::endsvg

'''),

    # ch12 12.6 时频权衡 (Fourier 局限)
    ('chapter12-infinite-series.md', '### 12.6.5 收敛模式的三种区分', r'''
::svg
<svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <rect x="30" y="40" width="140" height="120" fill="#eef4fb" stroke="#1a365d" stroke-width="1.5"/>
  <text x="35" y="35" font-size="12" font-weight="bold" fill="#1a365d">Fourier</text>
  <line x1="30" y1="160" x2="170" y2="160" stroke="#1a365d" stroke-width="1"/>
  <text x="155" y="170" font-size="11" fill="#888">t</text>
  <text x="35" y="160" font-size="11" fill="#888">f</text>
  <rect x="30" y="40" width="140" height="120" fill="#c2410c" opacity="0.2"/>
  <text x="50" y="100" font-size="11" fill="#c2410c">全时间</text>
  <text x="50" y="115" font-size="11" fill="#c2410c">全频率</text>
  <rect x="190" y="40" width="140" height="120" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <text x="195" y="35" font-size="12" font-weight="bold" fill="#8b6f1c">小波</text>
  <line x1="190" y1="160" x2="330" y2="160" stroke="#8b6f1c" stroke-width="1"/>
  <text x="315" y="170" font-size="11" fill="#888">t</text>
  <text x="195" y="160" font-size="11" fill="#888">f</text>
  <rect x="200" y="50" width="30" height="30" fill="#2d6e2d" opacity="0.5"/>
  <rect x="240" y="90" width="50" height="30" fill="#2d6e2d" opacity="0.5"/>
  <rect x="295" y="130" width="30" height="20" fill="#2d6e2d" opacity="0.5"/>
  <text x="200" y="195" font-size="11" fill="#2d6e2d">时频局部</text>
</svg>
<figcaption>图 12.6.4 Fourier vs 小波:Fourier 系数是"全时间全频率"积分,无时间定位;小波系数在时频面上局部,适合非平稳信号。</figcaption>
::endsvg

'''),

    # ch9 9.10 残差直方图 (高斯分布)
    ('chapter09-multivariate.md', '### 9.10.1 线性回归的问题陈述', r'''
::svg
<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <line x1="30" y1="140" x2="290" y2="140" stroke="#888" stroke-width="1"/>
  <line x1="160" y1="20" x2="160" y2="160" stroke="#888" stroke-width="1"/>
  <text x="295" y="145" font-size="11" fill="#888">残差 e</text>
  <text x="165" y="20" font-size="11" fill="#888">频次</text>
  <rect x="80" y="120" width="15" height="20" fill="#1a365d" opacity="0.7"/>
  <rect x="100" y="100" width="15" height="40" fill="#1a365d" opacity="0.75"/>
  <rect x="120" y="70" width="15" height="70" fill="#1a365d" opacity="0.8"/>
  <rect x="140" y="40" width="15" height="100" fill="#1a365d" opacity="0.9"/>
  <rect x="160" y="35" width="15" height="105" fill="#1a365d" opacity="0.95"/>
  <rect x="180" y="40" width="15" height="100" fill="#1a365d" opacity="0.9"/>
  <rect x="200" y="70" width="15" height="70" fill="#1a365d" opacity="0.8"/>
  <rect x="220" y="100" width="15" height="40" fill="#1a365d" opacity="0.75"/>
  <rect x="240" y="120" width="15" height="20" fill="#1a365d" opacity="0.7"/>
  <path d="M 60 130 Q 130 60 160 35 Q 200 60 270 130" fill="none" stroke="#c2410c" stroke-width="1.8"/>
  <text x="195" y="60" font-size="11" fill="#c2410c">理论 N(0,σ²)</text>
  <text x="35" y="170" font-size="11" fill="#666">OLS 假设残差独立同分布 ~ N(0,σ²) ⇒ BLUE</text>
</svg>
<figcaption>图 9.10.3 OLS 残差直方图 ≈ 正态分布:Gauss-Markov 定理在残差 iid 正态前提下,OLS 是线性无偏估计中方差最小的(BLUE)。</figcaption>
::endsvg

'''),

    # ch11 11.5 立体角 4π (整球)
    ('chapter11-line-surface-integrals.md', '### 11.5.6 与三大公式的统一', r'''
::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <circle cx="160" cy="100" r="70" fill="#eef4fb" fill-opacity="0.6" stroke="#1a365d" stroke-width="1.8"/>
  <circle cx="160" cy="100" r="3" fill="#c2410c"/>
  <text x="135" y="115" font-size="11" fill="#c2410c">点电荷 q</text>
  <line x1="160" y1="100" x2="220" y2="60" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="160" y1="100" x2="100" y2="60" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="160" y1="100" x2="220" y2="140" stroke="#c2410c" stroke-width="1.5"/>
  <line x1="160" y1="100" x2="100" y2="140" stroke="#c2410c" stroke-width="1.5"/>
  <text x="240" y="105" font-size="11" fill="#1a365d">全空间 Ω = 4π</text>
  <text x="35" y="185" font-size="11" fill="#444">点电荷电通量 ∮E·dS = q/ε₀ · (Ω/4π) = q/ε₀ (整球)</text>
</svg>
<figcaption>图 11.5.5 立体角 $\Omega$ 守恒:点电荷对包围它的任意闭曲面通量都是 $q/\varepsilon_0$,因为整球 $\Omega=4\pi$ 球面度。</figcaption>
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
