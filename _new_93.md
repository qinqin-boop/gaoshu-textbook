## 9.3 全微分

一元中**可导 $\iff$ 可微**——这两个概念在一元下等价。但在多元里**偏导数存在不蕴含可微**(§9.2 反例),要单独定义可微并给出**可微 $\Rightarrow$ 连续 + 偏导存在**的严格关系。本节给定义、几何意义(切平面)、判别充分条件,以及与雅可比矩阵的连接。

### 9.3.1 全微分的定义

::def
设 $f(x,y)$ 在 $(x_0,y_0)$ 邻域内有定义。称 $f$ 在 $(x_0,y_0)$ **可微**,若存在两个数 $A,B$ 使得
$$\Delta z=f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0)=A\Delta x+B\Delta y+o(\rho),\quad\rho=\sqrt{\Delta x^2+\Delta y^2}.$$
此时 $df=A\Delta x+B\Delta y$ 称为 $f$ 在该点的**全微分**(线性主部)。
::end

::thm
若 $f$ 在 $(x_0,y_0)$ 可微,则:
1. $f$ 在 $(x_0,y_0)$ **连续**;
2. 两个偏导 $f_x(x_0,y_0)=A$,$f_y(x_0,y_0)=B$ 都**存在**;
3. 全微分 $df=f_x\Delta x+f_y\Delta y$,常写成 $df=f_x\,dx+f_y\,dy$。
::end

::proof
**连续**:$\Delta z\to 0$ 当 $(\Delta x,\Delta y)\to(0,0)$,因为 $A\Delta x+B\Delta y\to 0$、$o(\rho)\to 0$。
**偏导存在 + 给出 $A,B$**:取 $\Delta y=0$,
$$\Delta z=A\Delta x+o(|\Delta x|)\Rightarrow\frac{\Delta z}{\Delta x}=A+o(1)\to A=f_x(x_0,y_0).$$
同理 $\Delta x=0$ 得 $B=f_y$。证毕。
::end

::intuition
**全微分的几何意义**:在 $(x_0,y_0)$ 附近 $f$ 可由一个**线性函数**(切平面)极好逼近,误差是 $o(\rho)$ 即比一阶项更高阶。**可微 = 局部能用切平面近似**。
::end

### 9.3.2 可微 vs 偏导存在 vs 连续 — 三者关系

::thm
(三者关系图)
$$\boxed{f\text{ 可微}\;\Rightarrow\;f\text{ 连续}+\text{偏导存在}}.$$
反向**不成立**——偏导存在不蕴含连续(§9.2 例 2)、不蕴含可微。
::end

::thm
(可微的充分条件)若 $f_x,f_y$ 在 $(x_0,y_0)$ 邻域内**存在且连续**,则 $f$ 在 $(x_0,y_0)$ 可微。
::end

::proof
增量 $\Delta z=f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0)$ 可拆为两步:
$$\Delta z=\underbrace{[f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0+\Delta y)]}_{\text{先动 }x}+\underbrace{[f(x_0,y_0+\Delta y)-f(x_0,y_0)]}_{\text{再动 }y}.$$
对第一段(固定 $y=y_0+\Delta y$)用一元中值定理:存在 $\theta_1\in(0,1)$ 使
$$f(x_0+\Delta x,y_0+\Delta y)-f(x_0,y_0+\Delta y)=f_x(x_0+\theta_1\Delta x,y_0+\Delta y)\Delta x.$$
对第二段:$f(x_0,y_0+\Delta y)-f(x_0,y_0)=f_y(x_0,y_0+\theta_2\Delta y)\Delta y$。
由 $f_x,f_y$ 连续:
$$f_x(x_0+\theta_1\Delta x,y_0+\Delta y)=f_x(x_0,y_0)+\varepsilon_1,\quad\varepsilon_1\to 0,$$
$$f_y(x_0,y_0+\theta_2\Delta y)=f_y(x_0,y_0)+\varepsilon_2,\quad\varepsilon_2\to 0.$$
代回:
$$\Delta z=f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y+\varepsilon_1\Delta x+\varepsilon_2\Delta y.$$
$|\varepsilon_1\Delta x+\varepsilon_2\Delta y|\le(|\varepsilon_1|+|\varepsilon_2|)\rho=o(\rho)$,$f$ 可微,且 $A=f_x,B=f_y$。证毕。
::end

::intuition
**完整版关系图**:
$$f\in C^1\text{(偏导连续)}\Rightarrow f\text{ 可微}\Rightarrow f\text{ 连续}+\text{偏导存在}.$$
反向都**不成立**(可微但 $f_x,f_y$ 不连续的反例存在,但在工程实际中 $C^1$ 几乎总成立,所以可微一般不必单独验证,只要偏导连续就行)。
::end

::ex
**例 1**(全微分计算)$f(x,y)=x^2y+\sin(xy)$。$f_x=2xy+y\cos(xy),f_y=x^2+x\cos(xy)$,连续 $\Rightarrow$ $f\in C^1\Rightarrow$ 可微。
$$df=(2xy+y\cos(xy))\,dx+(x^2+x\cos(xy))\,dy.$$
::end

### 9.3.3 全微分的近似计算应用

::thm
(线性近似)若 $f$ 在 $(x_0,y_0)$ 可微,则对小 $\Delta x,\Delta y$:
$$f(x_0+\Delta x,y_0+\Delta y)\approx f(x_0,y_0)+f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y.$$
误差 $o(\rho)$,即比 $\rho$ 更高阶。
::end

::ex
**例 2** 估计 $\sqrt{(1.02)^2+(2.97)^2}$。

**解**:取 $f(x,y)=\sqrt{x^2+y^2}$,$x_0=1,y_0=3$,$\Delta x=0.02,\Delta y=-0.03$。$f(1,3)=\sqrt{10}\approx 3.162$。$f_x=x/\sqrt{x^2+y^2}=1/\sqrt{10}$,$f_y=3/\sqrt{10}$,在 $(1,3)$。
$$f(1.02,2.97)\approx\sqrt{10}+\frac{0.02-0.09}{\sqrt{10}}\approx 3.162+\frac{-0.07}{3.162}\approx 3.140.$$
真实值 $\sqrt{1.0404+8.8209}=\sqrt{9.8613}\approx 3.140$,误差在 $10^{-3}$ 数量级。
::end

### 9.3.4 雅可比矩阵预热

把全微分写成矩阵形式:
$$df=\big(f_x,\;f_y\big)\begin{pmatrix}dx\\ dy\end{pmatrix}=Df\cdot d\vec{x},\quad Df=(\,f_x\;\;f_y\,)\text{ 称为 }f\text{ 的 Jacobian}.$$

对 $\vec{F}:\mathbb{R}^n\to\mathbb{R}^m$,$d\vec{F}=J_{\vec{F}}\cdot d\vec{x}$,$J_{\vec{F}}$ 是 $m\times n$ 矩阵。**$\vec{F}$ 可微 $\iff$ 存在 $J$ 使 $\vec{F}(\vec{x}+\vec{h})=\vec{F}(\vec{x})+J\vec{h}+o(|\vec{h}|)$**——这是 §9.4 链式法则、§10.2 二重积分换元中雅可比因子、§9.5 隐函数定理的统一定义。

::pitfall
**易错点**:
- 偏导存在**不蕴含**可微——可能沿直线方向行但沿曲线方向不行(§9.2 例 2);
- 可微的**充分**条件是「偏导连续」($f\in C^1$),不是「偏导存在」;
- 全微分公式 $df=f_x\,dx+f_y\,dy$ 中 $dx,dy$ 是**自变量增量**,跟函数无关;
- 近似计算时**$\Delta x,\Delta y$ 必须够小**,否则误差不再可控;
- 「可微」对应一元的「可导」(同含意),但在多元下"可导"指偏导,不等同于「可微」——汉语词混用陷阱要小心。
::end

---

