## 9.4 多元复合函数求导(链式法则)

一元链式法则 $\frac{d}{dx}g(f(x))=g'(f(x))f'(x)$ 解决「函数套函数」的求导。多元函数的"套"远比一元复杂——一个函数可能依赖多个中间变量,每个中间变量又依赖多个自变量,**导数关系成网状而非链状**。本节系统给出多元链式法则、用 **矩阵 / 雅可比** 写法把它紧凑表达,并指出这是机器学习**反向传播算法**(backprop)的数学根。

### 9.4.1 一元中间变量

::thm
(单中间变量链式)若 $z=f(u)$ 在 $u$ 处可微,$u=\varphi(x,y)$ 在 $(x,y)$ 处可偏导,则 $z=f(\varphi(x,y))$ 关于 $x,y$ 的偏导:
$$\frac{\partial z}{\partial x}=f'(u)\frac{\partial u}{\partial x},\qquad\frac{\partial z}{\partial y}=f'(u)\frac{\partial u}{\partial y}.$$
::end

::ex
**例 1** $z=\sin(x^2+y)$。取 $u=x^2+y$,$z=\sin u$:
$$z_x=\cos u\cdot 2x=2x\cos(x^2+y),\quad z_y=\cos u\cdot 1=\cos(x^2+y).$$
::end

### 9.4.2 多中间变量(核心情形)

::thm
若 $z=f(u,v)$ 在 $(u,v)$ 可微,$u=\varphi(x,y)$、$v=\psi(x,y)$ 在 $(x,y)$ 可偏导,则
$$\boxed{\frac{\partial z}{\partial x}=\frac{\partial f}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial f}{\partial v}\frac{\partial v}{\partial x},\quad\frac{\partial z}{\partial y}=\frac{\partial f}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial f}{\partial v}\frac{\partial v}{\partial y}.}$$
::end

::proof
$z=f(u(x,y),v(x,y))$。对 $x$ 求偏导(把 $y$ 看作常量)。给 $x$ 增量 $\Delta x$,$u$、$v$ 都跟着变 $\Delta u=u_x\Delta x+o(\Delta x)$、$\Delta v=v_x\Delta x+o(\Delta x)$。$f$ 在 $(u,v)$ 处可微,所以
$$\Delta z=f_u\Delta u+f_v\Delta v+o(\sqrt{\Delta u^2+\Delta v^2})=f_u(u_x\Delta x)+f_v(v_x\Delta x)+o(\Delta x).$$
除 $\Delta x$ 取极限,$\partial z/\partial x=f_u u_x+f_v v_x$。对 $y$ 同理。证毕。
::end

::intuition
**画"传导树状图"**:$z$ 沿两条路径($u\to x$、$v\to x$)同时受 $x$ 影响,每条路径贡献「上游导数 $\times$ 下游导数」,然后**所有路径的贡献相加**——这是链式法则的几何图像。
::end

::ex
**例 2** $z=e^{xy}\ln(x+y)$,设 $u=xy,v=x+y$,$z=f(u,v)=e^u\ln v$。
- $f_u=e^u\ln v$,$f_v=e^u/v$;
- $u_x=y$,$v_x=1$;
- $z_x=e^{xy}\ln(x+y)\cdot y+e^{xy}\cdot\frac{1}{x+y}\cdot 1=e^{xy}\big(y\ln(x+y)+\tfrac{1}{x+y}\big)$。
::end

### 9.4.3 一般情形:雅可比矩阵语言

把链式法则写成矩阵形式,是把它推广到任意维数与多输入多输出的关键。

::def
设 $\vec{F}:\mathbb{R}^n\to\mathbb{R}^m$ 各分量可偏导,**雅可比矩阵**
$$J_{\vec{F}}=\begin{pmatrix}\dfrac{\partial F_1}{\partial x_1}&\cdots&\dfrac{\partial F_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial F_m}{\partial x_1}&\cdots&\dfrac{\partial F_m}{\partial x_n}\end{pmatrix}_{m\times n}.$$
特例:$m=1$ 是梯度的转置 $\nabla F^\top$;$m=n$ 时 $\det J$ 是变量替换的雅可比行列式(§10.2-10.3)。
::end

::thm
(矩阵形式链式法则)若 $\vec{F}=\vec{g}\circ\vec{f}$,即 $\vec{F}(\vec{x})=\vec{g}(\vec{f}(\vec{x}))$,$\vec{f}:\mathbb{R}^n\to\mathbb{R}^k$、$\vec{g}:\mathbb{R}^k\to\mathbb{R}^m$ 都可微,则
$$J_{\vec{F}}(\vec{x})=J_{\vec{g}}(\vec{f}(\vec{x}))\cdot J_{\vec{f}}(\vec{x}).$$
即**复合的雅可比 = 雅可比的矩阵乘积**(注意顺序:外函数 $\vec{g}$ 的雅可比在左)。
::end

::proof
对 $J_{\vec{F}}$ 的 $(i,j)$ 元素 $\partial F_i/\partial x_j$,用单变量链式
$$\frac{\partial F_i}{\partial x_j}=\sum_{l=1}^k\frac{\partial g_i}{\partial f_l}\cdot\frac{\partial f_l}{\partial x_j},$$
即 $J_{\vec{g}}$ 第 $i$ 行与 $J_{\vec{f}}$ 第 $j$ 列做内积——正是矩阵乘积 $(J_{\vec{g}}J_{\vec{f}})_{ij}$。证毕。
::end

::intuition
**矩阵形式是一元链式 $g'(f(x))\cdot f'(x)$ 的多元自然版本**:把"导数"看成"线性近似",链式说"复合函数的局部线性近似 = 每一步线性近似相乘"。这是**微分几何**的核心范畴论:`微分(d) 是函子,把"复合"映为"矩阵乘积"`。
::end

### 9.4.4 反向传播(Backpropagation)

::intuition
神经网络是一个**深度复合函数**:
$$L(\vec{\theta})=\ell\big(\vec{y},\;f_N(f_{N-1}(\dots f_1(\vec{x};\theta_1);\dots);\theta_N)\big),$$
其中 $f_k$ 是第 $k$ 层(线性变换 + 激活),$\theta_k$ 是该层参数。训练目标是最小化损失 $L$,需要对每个 $\theta_k$ 算偏导 $\partial L/\partial\theta_k$。

由矩阵形式链式法则:
$$\frac{\partial L}{\partial\theta_k}=\underbrace{\frac{\partial L}{\partial f_N}\cdot J_{f_N}\cdot\dots\cdot J_{f_{k+1}}}_{\text{从输出反向传到第 }k\text{ 层}}\cdot\frac{\partial f_k}{\partial\theta_k}.$$

朴素地从前往后(forward)按层算每个 $J$ 再乘要 $O(N^2 D^3)$;**反向传播**(从损失开始向输入方向传)只需 $O(ND^2)$ 一次扫——把上游导数(adjoint variable)从后往前传,每层乘以局部雅可比。这就是 **PyTorch / TensorFlow 自动微分** 引擎的核心。
::end

::ex
**例 3**(简单两层网络 backprop)$\vec{h}=\sigma(W_1\vec{x}+\vec{b}_1)$,$\hat y=W_2\vec{h}+b_2$,$L=\tfrac12(\hat y-y)^2$。

- $\frac{\partial L}{\partial\hat y}=\hat y-y$;
- $\frac{\partial L}{\partial W_2}=\frac{\partial L}{\partial\hat y}\cdot\vec{h}^\top=(\hat y-y)\vec{h}^\top$;
- $\frac{\partial L}{\partial\vec{h}}=W_2^\top(\hat y-y)$;
- $\frac{\partial L}{\partial(W_1\vec{x}+\vec{b}_1)}=\frac{\partial L}{\partial\vec{h}}\odot\sigma'(W_1\vec{x}+\vec{b}_1)$($\odot$ 元素乘);
- $\frac{\partial L}{\partial W_1}=\big[\frac{\partial L}{\partial(W_1\vec{x}+\vec{b}_1)}\big]\vec{x}^\top$。

每步都是一次矩阵乘,从损失逐层向前(向输入)传。这就是 backprop 的全部数学——**链式法则的有效计算实现**。
::end

### 9.4.5 高阶导数

链式法则用一次可以算一阶。**二阶混合偏导**需要把链式应用两次,公式繁琐但机械:
$$\frac{\partial^2 z}{\partial x^2}=\frac{\partial}{\partial x}\bigg(f_u u_x+f_v v_x\bigg)=f_{uu}u_x^2+2f_{uv}u_xv_x+f_{vv}v_x^2+f_u u_{xx}+f_v v_{xx}.$$
注意 **$f_u u_{xx}$ / $f_v v_{xx}$** 项不可忘——这是初学者最易遗漏的"高阶项",在 PDE 推导中遇到。

::pitfall
**易错点**:
- **所有路径都要写**:$z=f(u,v)$,$u,v$ 都依赖 $x$ 时,$z_x=f_u u_x+f_v v_x$ 两项,**漏一个就错**;
- **区分 $\partial$ vs $d$**:$\frac{\partial z}{\partial x}$(偏导,固定其它变量)和 $\frac{dz}{dx}$(全导,$y$ 也随 $x$ 变)概念不同;
- 雅可比乘积**顺序**:$J_{g\circ f}=J_g\cdot J_f$,从外到内,反过来会得到错乘积;
- **高阶混合**:$\partial^2 z/(\partial x\partial y)\neq\partial^2 z/(\partial y\partial x)$ 一般不必成立,但 $z\in C^2$ 时由 Clairaut 定理相等(§9.2);
- 反向传播实现时**梯度形状必须匹配**;debug 神经网络最常见 bug 是 `RuntimeError: shape mismatch`。
::end

---

