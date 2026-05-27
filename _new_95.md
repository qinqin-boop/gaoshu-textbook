## 9.5 隐函数求导

很多关系无法显式写成 $y=f(x)$,只能写成 $F(x,y)=0$ 这种**隐式**形式(如圆 $x^2+y^2=1$、椭圆、Cobb-Douglas 等产函数)。本节给出**隐函数存在定理**——什么时候 $F(x,y)=0$ 局部能解出 $y=f(x)$——并推导隐函数的求导公式。随后推广到多元 / 方程组情形,引出**雅可比矩阵**作为「可解性」的核心判据。这是约束优化、流形(Manifold)、最优传输(Optimal Transport)的代数底座。

### 9.5.1 一元隐函数

::thm
(隐函数存在定理 / 一元)设 $F(x,y)$ 在 $(x_0,y_0)$ 邻域内连续可偏导,且
1. $F(x_0,y_0)=0$;
2. $F_y(x_0,y_0)\neq 0$。

则方程 $F(x,y)=0$ 在 $(x_0,y_0)$ 附近**唯一确定**一个连续可微函数 $y=f(x)$,使 $f(x_0)=y_0$ 且 $F(x,f(x))\equiv 0$。其导数
$$\frac{dy}{dx}=-\frac{F_x(x,y)}{F_y(x,y)}.$$
::end

::proof
**存在唯一性**:由 $F_y(x_0,y_0)\neq 0$,不妨设 $F_y>0$,故 $F(x_0,y)$ 关于 $y$ 严格递增,$F(x_0,y_0-\varepsilon)<0<F(x_0,y_0+\varepsilon)$($\varepsilon$ 小)。由 $F$ 连续,对 $x$ 接近 $x_0$ 同样有 $F(x,y_0-\varepsilon)<0<F(x,y_0+\varepsilon)$,由中间值定理存在唯一 $y\in(y_0-\varepsilon,y_0+\varepsilon)$ 使 $F(x,y)=0$。记 $y=f(x)$。

**可微性**:对 $F(x,f(x))\equiv 0$ 求 $x$ 偏导,用链式
$$F_x(x,f(x))+F_y(x,f(x))\cdot f'(x)=0\Rightarrow f'(x)=-\frac{F_x(x,f(x))}{F_y(x,f(x))}.$$
$F_x,F_y$ 连续 $\Rightarrow f'$ 连续。证毕。
::end

::ex
**例 1**(圆的隐函数)$F=x^2+y^2-1=0$。$F_x=2x$,$F_y=2y$。$F_y\neq 0$ 即 $y\neq 0$,在 $y\neq 0$ 的点附近都能解出 $y=\pm\sqrt{1-x^2}$ 之一。
$$\frac{dy}{dx}=-\frac{2x}{2y}=-\frac{x}{y}.$$
$y=0$ 时(即 $(\pm 1,0)$ 两点)$F_y=0$,隐函数定理失效——几何上看这两点切线竖直,$y$ 不能写成 $x$ 的函数(同一个 $x$ 对应两 $y$)。
::end

### 9.5.2 二元隐函数

::thm
(二元隐函数)设 $F(x,y,z)$ 在 $(x_0,y_0,z_0)$ 邻域连续可偏导,$F(x_0,y_0,z_0)=0$,$F_z(x_0,y_0,z_0)\neq 0$。则方程 $F(x,y,z)=0$ 在该点附近确定 $z=f(x,y)$,且
$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z},\quad\frac{\partial z}{\partial y}=-\frac{F_y}{F_z}.$$
::end

::proof
$F(x,y,f(x,y))\equiv 0$,对 $x$ 求偏导:$F_x+F_z\cdot z_x=0\Rightarrow z_x=-F_x/F_z$。对 $y$ 同理。
::end

::ex
**例 2**(球面)$F=x^2+y^2+z^2-R^2=0$ 在 $z\neq 0$ 处可解 $z=\pm\sqrt{R^2-x^2-y^2}$:
$$z_x=-\frac{2x}{2z}=-\frac{x}{z},\quad z_y=-\frac{y}{z}.$$
代入 §9.7 切平面 / 法线方程可立得 $(x_0,y_0,z_0)$ 处切平面 $x\,x_0+y\,y_0+z\,z_0=R^2$。
::end

### 9.5.3 方程组 / 隐函数组

::thm
(方程组隐函数)设
$$\begin{cases}F(x,y,u,v)=0\\ G(x,y,u,v)=0\end{cases}$$
在 $(x_0,y_0,u_0,v_0)$ 满足两方程,$F,G$ 连续可偏导,且**雅可比行列式**
$$J=\frac{\partial(F,G)}{\partial(u,v)}=\det\begin{pmatrix}F_u&F_v\\ G_u&G_v\end{pmatrix}\bigg|_{(x_0,\dots,v_0)}\neq 0.$$
则方程组在该点附近唯一确定 $u=u(x,y)$、$v=v(x,y)$,且
$$\frac{\partial u}{\partial x}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(x,v)},\quad\frac{\partial v}{\partial x}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(u,x)},$$
$\partial u/\partial y,\partial v/\partial y$ 同理(把 $x$ 换为 $y$)。
::end

::proof
对方程组两边关于 $x$ 求偏导(把 $u,v$ 视为 $x,y$ 的函数):
$$\begin{cases}F_x+F_u u_x+F_v v_x=0\\ G_x+G_u u_x+G_v v_x=0\end{cases}.$$
关于 $(u_x,v_x)$ 是线性方程组,系数矩阵 $\begin{pmatrix}F_u&F_v\\G_u&G_v\end{pmatrix}$ 行列式 $J\neq 0$,**用 Cramer 法则**:
$$u_x=\frac{1}{J}\det\begin{pmatrix}-F_x&F_v\\ -G_x&G_v\end{pmatrix}=-\frac{1}{J}\frac{\partial(F,G)}{\partial(x,v)}.$$
同理 $v_x$。证毕。
::end

::ex
**例 3**(方程组) $F=x+y-u-v=0,\,G=x-y-u^2-v^2=0$ 在 $(1,1,1,0)$ 附近($F=0,G=0$ 都满足)。求 $u_x$。

**解**:$F_u=-1,F_v=-1,G_u=-2u=-2,G_v=-2v=0$,$J=(-1)(0)-(-1)(-2)=-2\neq 0$。$F_x=1,G_x=1$。
$$\frac{\partial(F,G)}{\partial(x,v)}=\det\begin{pmatrix}1&-1\\ 1&0\end{pmatrix}=0-(-1)=1.$$
$u_x=-1/(-2)=1/2$。
::end

### 9.5.4 几何意义:隐函数定理与流形

::intuition
**$F:\mathbb{R}^{n+m}\to\mathbb{R}^m$,$F=\vec{0}$ 局部可解 $m$ 个变量 $\iff$ 雅可比 $\partial F/\partial(\vec{y})$ 满秩**——这就是**隐函数定理**的核心,也是**流形**(manifold)定义的核心:
> $n$ 维流形 $M\subset\mathbb{R}^{n+m}$ 局部等价于 $\mathbb{R}^n$,因为 $m$ 个方程的雅可比满秩允许局部用 $n$ 个变量参数化。

这是抽象代数几何 / 微分几何 / 优化(KKT)/ 神经网络架构(NN 的损失曲面流形结构)的共同代数底。
::end

::thm
(逆函数定理,隐函数定理的特例)若 $\vec{F}:\mathbb{R}^n\to\mathbb{R}^n$ 在 $\vec{x}_0$ 连续可微,$J_{\vec{F}}(\vec{x}_0)$ **可逆**(行列式 $\neq 0$),则 $\vec{F}$ 在 $\vec{x}_0$ 附近**局部可逆**,反函数 $\vec{F}^{-1}$ 也连续可微,且
$$J_{\vec{F}^{-1}}(\vec{F}(\vec{x}_0))=[J_{\vec{F}}(\vec{x}_0)]^{-1}.$$
::end

这条等式是 §10.2 二重换元、§10.3 三重换元中**雅可比因子 $|J|$** 出现的根:正反变换的局部缩放因子互为倒数,所以面积 / 体积元素必须乘上 $|J|$ 来补偿。

### 9.5.5 与机器学习 / 经济学的关系

::intuition
- **隐式神经网络(implicit layer)**:输出 $z$ 满足 $F(x,z;\theta)=0$,正向传播需解方程,反向传播需用隐函数定理求 $\partial z/\partial\theta$——这是 Deep Equilibrium Model(2019)、Neural ODE 内部机制。
- **拉格朗日乘子法 / KKT** 条件:约束 $g(\vec{x})=0$ 上极值的求解本质上把 $\vec{x}$ 中一些变量看成另一些的隐函数,把约束消掉。
- **经济学比较静态分析**:供求平衡方程 $D(p,y)=S(p,w)$ 中,$p$ 是 $y,w$ 的隐函数。$\partial p/\partial w$ 用隐函数公式给出政策变量对市场价格的弹性。
::end

::pitfall
**易错点**:
- 隐函数存在的**关键条件**是 $F_y\neq 0$(单变量)或 $J\neq 0$(方程组);若此条件破坏,可能无法解、无唯一解、或解出来不可微;
- 隐函数定理只给出**局部**存在性;全局是否成立要单独分析(如圆在 $y\neq 0$ 处可解,但要走完一圈需切分为上半圆 / 下半圆);
- 计算 $\partial u/\partial x$ 时,$u,v$ 都是 $x,y$ 的函数——**用全微分**,不要把 $v$ 当独立变量;
- Cramer 法则只对方阵且非奇异时适用,$J=0$ 时要么用 LU、要么实际系统就退化;
- 物理 / 经济应用中**隐函数偏导的符号**有具体意义(价格弹性 / 边际替代率),公式中负号要保留。
::end

---

