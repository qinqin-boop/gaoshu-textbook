## 9.6 方向导数与梯度

偏导数只能告诉我们沿坐标轴方向的变化率。如果一个登山者站在山坡上想知道「往东北方向走、高度变化多快」,偏导给不出直接答案。**方向导数**把这件事扩展到任意方向;**梯度**则把所有方向的变化率压成一个向量,并且这个向量本身就指向「**变化最快**」的方向。这是后续条件极值、机器学习中梯度下降、最速下降法的代数基础。

### 9.6.1 方向导数

::def
设函数 $f(x,y)$ 在点 $P_0(x_0,y_0)$ 的某邻域内有定义,$\vec{l}=(\cos\alpha,\cos\beta)$ 为**单位向量**(方向角 $\alpha,\beta$ 满足 $\cos^2\alpha+\cos^2\beta=1$)。若极限
$$\frac{\partial f}{\partial\vec{l}}\bigg|_{P_0}=\lim_{t\to 0^+}\frac{f(x_0+t\cos\alpha,\,y_0+t\cos\beta)-f(x_0,y_0)}{t}$$
存在,则称该极限为 $f$ 在 $P_0$ 沿方向 $\vec{l}$ 的**方向导数**。
::end

::intuition
站在曲面 $z=f(x,y)$ 对应的点 $(x_0,y_0,f(x_0,y_0))$,把曲面被竖直平面(沿 $\vec{l}$ 方向)截下来得到一条曲线,方向导数就是这条曲线在该点的**斜率**。
::end

注意定义中要求 $t\to 0^+$(单侧极限),因此沿 $\vec{l}$ 与沿 $-\vec{l}$ 的方向导数一般不互为相反数(对不可微但偏导存在的函数尤其要小心)。但**对可微函数**有下面的乘法公式,符号取反时方向导数也取反:

::thm
(方向导数的偏导计算公式)若 $f$ 在 $P_0$ **可微**,则对任意单位方向 $\vec{l}=(\cos\alpha,\cos\beta)$,
$$\frac{\partial f}{\partial\vec{l}}\bigg|_{P_0}=f_x(P_0)\cos\alpha+f_y(P_0)\cos\beta.$$
::end

::proof
由可微定义,
$$f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0)=f_x(P_0)\Delta x+f_y(P_0)\Delta y+o(\rho),\quad\rho=\sqrt{\Delta x^2+\Delta y^2}.$$
取 $\Delta x=t\cos\alpha$,$\Delta y=t\cos\beta$,则 $\rho=t$(因为 $\vec{l}$ 是单位向量),代入得
$$\frac{f(x_0+t\cos\alpha,y_0+t\cos\beta)-f(x_0,y_0)}{t}=f_x\cos\alpha+f_y\cos\beta+\frac{o(t)}{t}.$$
令 $t\to 0^+$,$o(t)/t\to 0$。证毕。
::end

::pitfall
**关键前提是「可微」**。仅「两个偏导存在」并不能推出方向导数公式成立。一个经典反例:
$$f(x,y)=\begin{cases}\dfrac{xy}{x^2+y^2},&(x,y)\neq(0,0)\\ 0,&(x,y)=(0,0)\end{cases}$$
在 $(0,0)$ 处 $f_x(0,0)=f_y(0,0)=0$,但沿 $\vec{l}=(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2})$ 的方向导数 $=\lim_{t\to 0^+}\frac{(t/\sqrt2)^2/(t^2)}{t}=\lim_{t\to 0^+}\frac{1}{2t}=+\infty$。公式失败因为 $f$ 在原点不可微。
::end

### 9.6.2 梯度

::def
设 $f$ 在 $P_0$ 可偏导,**梯度**(gradient)定义为偏导数构成的向量:
$$\nabla f(P_0)=\bigg(\frac{\partial f}{\partial x}(P_0),\frac{\partial f}{\partial y}(P_0)\bigg)\quad(\text{二维});\quad\nabla f=(f_x,f_y,f_z)\quad(\text{三维}).$$
$\nabla$ 读作「nabla」或「del」,可视为算子 $\nabla=\big(\tfrac{\partial}{\partial x},\tfrac{\partial}{\partial y}\big)$。
::end

把方向导数公式用点乘改写:
$$\frac{\partial f}{\partial\vec{l}}=f_x\cos\alpha+f_y\cos\beta=\nabla f\cdot\vec{l}.$$

这一改写极其重要——它把「沿某方向的变化率」表达成「梯度向量与方向向量的点乘」。下面的定理是梯度的灵魂。

::thm
(梯度方向是最速上升方向)若 $f$ 在 $P_0$ 可微,$\nabla f(P_0)\neq\vec{0}$,则在所有单位方向 $\vec{l}$ 中:
1. **最大方向导数**$=|\nabla f(P_0)|$,在 $\vec{l}=\dfrac{\nabla f}{|\nabla f|}$(即沿梯度方向)时取得;
2. **最小方向导数**$=-|\nabla f(P_0)|$,在 $\vec{l}=-\dfrac{\nabla f}{|\nabla f|}$(沿负梯度方向)时取得;
3. **零方向导数**(函数瞬时不变方向)在 $\vec{l}\perp\nabla f$ 时取得——这正是等高线的切线方向。
::end

::proof
设 $\vec{l}$ 与 $\nabla f$ 的夹角为 $\theta$,$|\vec{l}|=1$。由方向导数公式与 Cauchy-Schwarz:
$$\frac{\partial f}{\partial\vec{l}}=\nabla f\cdot\vec{l}=|\nabla f|\cdot 1\cdot\cos\theta=|\nabla f|\cos\theta.$$
$\cos\theta\in[-1,1]$,取 $+1$($\theta=0$,$\vec{l}$ 与 $\nabla f$ 同向)时最大、取 $-1$($\theta=\pi$)时最小、取 $0$($\theta=\tfrac{\pi}{2}$)时为零。证毕。
::end

::svg
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ag1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="ag2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
    <marker id="ag3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c2410c"/></marker>
  </defs>
  <ellipse cx="180" cy="110" rx="140" ry="60" fill="none" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <ellipse cx="180" cy="110" rx="100" ry="42" fill="none" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <ellipse cx="180" cy="110" rx="60" ry="25" fill="none" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="316" y="115" fill="#999" font-size="11">f=1</text>
  <text x="276" y="115" fill="#999" font-size="11">f=2</text>
  <text x="236" y="115" fill="#999" font-size="11">f=3</text>
  <circle cx="180" cy="110" r="3" fill="#000"/>
  <text x="186" y="125" font-size="11">P₀</text>
  <line x1="180" y1="110" x2="260" y2="110" stroke="#1a365d" stroke-width="2.5" marker-end="url(#ag1)"/>
  <text x="200" y="103" fill="#1a365d" font-size="12" font-style="italic">∇f (最速上升)</text>
  <line x1="180" y1="110" x2="100" y2="110" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#ag2)"/>
  <text x="105" y="103" fill="#2d6e2d" font-size="12" font-style="italic">-∇f (下降)</text>
  <line x1="180" y1="110" x2="180" y2="50" stroke="#c2410c" stroke-width="2.5" marker-end="url(#ag3)"/>
  <text x="186" y="60" fill="#c2410c" font-size="12" font-style="italic">l⊥∇f (沿等高线)</text>
</svg>
<figcaption>图 9.6.1 梯度方向是最速上升方向,负梯度方向是最速下降方向,与梯度垂直的方向沿等高线(瞬时不变)。</figcaption>
::endsvg

::intuition
把等高线类比成水平面投影,梯度恰好**垂直于过该点的等高线**,且指向函数值更高的一侧——所以爬山时「最陡的方向」总是垂直于脚下的等高线,这件事在物理 / GIS / 流体力学里反复出现。
::end

### 9.6.3 例题

::ex
**例 1**(直接计算)设 $f(x,y)=x^2+2y^2$,求在 $(1,1)$ 处沿 $\vec{u}=(1,1)$ 方向的方向导数。

**解**:先单位化 $\vec{l}=\vec{u}/|\vec{u}|=(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2})$。偏导 $f_x=2x$,$f_y=4y$,在 $(1,1)$ 处 $\nabla f=(2,4)$。
$$\frac{\partial f}{\partial\vec{l}}=\nabla f\cdot\vec{l}=\frac{2}{\sqrt2}+\frac{4}{\sqrt2}=\frac{6}{\sqrt2}=3\sqrt 2.$$
::end

::ex
**例 2**(找最速方向)$f(x,y)=x^2+y^2$ 在 $(1,2)$ 处,问最快上升方向、最快下降方向、不变方向各是什么?最大变化率多少?

**解**:$\nabla f(1,2)=(2,4)$,$|\nabla f|=\sqrt{20}=2\sqrt 5$。
- 最快上升:$\vec{l}=\tfrac{1}{2\sqrt 5}(2,4)=(\tfrac{1}{\sqrt 5},\tfrac{2}{\sqrt 5})$,变化率 $+2\sqrt 5$;
- 最快下降:反向 $(-\tfrac{1}{\sqrt 5},-\tfrac{2}{\sqrt 5})$,变化率 $-2\sqrt 5$;
- 不变:垂直方向 $(\tfrac{2}{\sqrt 5},-\tfrac{1}{\sqrt 5})$ 或反向,变化率 $0$。
::end

::ex
**例 3**(梯度下降一步)对凸二次函数 $L(\theta_1,\theta_2)=\theta_1^2+\theta_2^2$,初始参数 $\theta^{(0)}=(4,3)$,学习率 $\eta=0.1$,执行一次梯度下降。

**解**:$\nabla L(\theta)=(2\theta_1,2\theta_2)$。在 $\theta^{(0)}$ 处 $\nabla L=(8,6)$,
$$\theta^{(1)}=\theta^{(0)}-\eta\nabla L=(4,3)-0.1\cdot(8,6)=(3.2,2.4).$$
再迭代一步:$\nabla L(3.2,2.4)=(6.4,4.8)$,$\theta^{(2)}=(3.2-0.64,2.4-0.48)=(2.56,1.92)$。每步距离最优点 $(0,0)$ 的范数比上一步缩小一个固定比例 $1-2\eta=0.8$,这就是凸二次问题的**几何收敛**。
::end

### 9.6.4 与 AI 优化的联系

机器学习把模型参数记作 $\theta\in\mathbb{R}^d$,把训练损失记作 $L(\theta)$。**最速下降 / 梯度下降**就是把上面定理 9.6.B 的「负梯度方向是最速下降方向」直接搬到 $d$ 维:
$$\theta^{(k+1)}=\theta^{(k)}-\eta_k\,\nabla L(\theta^{(k)}).$$

实际中常见的变体:

| 方法 | 公式核心 | 解决什么问题 |
| --- | --- | --- |
| **SGD** | 用单样本(或 mini-batch)估计 $\nabla L$ | 大数据集,全量梯度算不起 |
| **Momentum** | $v\gets\beta v+\nabla L$,$\theta\gets\theta-\eta v$ | 鞍点 / 长山谷震荡 |
| **Adam** | 一阶矩 $m$ + 二阶矩 $v$ 自适应缩放 | 不同参数尺度差异大 |
| **Newton** | $\theta\gets\theta-\eta\,H^{-1}\nabla L$,$H$ 是 Hessian | 二阶曲率快收敛,但 $H^{-1}$ 贵 |

::thm
(下降引理 / Descent Lemma)若 $\nabla L$ 是 $L$-Lipschitz 的(即 $\|\nabla L(\theta_1)-\nabla L(\theta_2)\|\le L\|\theta_1-\theta_2\|$),则梯度下降步骤满足
$$L(\theta^{(k+1)})\le L(\theta^{(k)})-\eta\bigg(1-\frac{\eta L}{2}\bigg)\|\nabla L(\theta^{(k)})\|^2.$$
::end

::proof
由 $L$-平滑性的二阶展开式(可由 Taylor 余项 + Lipschitz 条件得)
$$L(\theta')\le L(\theta)+\nabla L(\theta)\cdot(\theta'-\theta)+\tfrac{L}{2}\|\theta'-\theta\|^2.$$
代入 $\theta'=\theta-\eta\nabla L(\theta)$:
$$L(\theta')\le L(\theta)-\eta\|\nabla L\|^2+\tfrac{L\eta^2}{2}\|\nabla L\|^2=L(\theta)-\eta(1-\tfrac{L\eta}{2})\|\nabla L\|^2.\;\square$$
::end

这个不等式告诉我们:当 $\eta\le\tfrac{1}{L}$ 时,每一步**至少**让损失下降 $\tfrac{\eta}{2}\|\nabla L\|^2$,从而梯度范数最终趋零(收敛到稳定点)。这是机器学习里收敛性分析的最基本工具。

::pitfall
**易错点**:
- 计算方向导数前**必须把方向向量单位化**;若代入未单位化的向量,结果会被它的模放大。
- 「方向导数 $=$ 梯度点乘方向」**要求函数在该点可微**;偏导存在不够。
- 梯度方向是**最速上升**,要做最小化时记得取**负梯度**;符号搞反 = 算法朝错方向跑。
- 高维非凸问题里,$\nabla L=0$ 不一定是极小,可能是鞍点或局部极大;需用 Hessian 进一步判别(§9.8)。
::end

---

