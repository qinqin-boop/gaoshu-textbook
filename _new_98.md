## 9.8 多元函数的极值

一元函数 $y=f(x)$ 在驻点用 $f''$ 的符号判极大极小。多元情形「二阶导数」是个**矩阵**(Hessian),判别要看这个矩阵的**正定性**——这是数值优化、机器学习二阶方法、凸优化理论的共同起点。本节既给传统的 $D=AC-B^2$ 判别式,也把它放到 Hessian 矩阵的语言里,说明判别式从哪里来。

### 9.8.1 法线方程(补完)

曲面 $F(x,y,z)=0$ 在 $P_0(x_0,y_0,z_0)$ 处的**法线**方向就是梯度 $\nabla F(P_0)=(F_x,F_y,F_z)$,法线参数式:
$$\frac{x-x_0}{F_x(P_0)}=\frac{y-y_0}{F_y(P_0)}=\frac{z-z_0}{F_z(P_0)}.$$
对显函数 $z=f(x,y)$,令 $F(x,y,z)=f(x,y)-z$,法向量取作 $(f_x,f_y,-1)$。

::ex
**例 1**(球面法线过球心)球面 $x^2+y^2+z^2=14$ 在 $(1,2,3)$ 处的法线?

**解**:$\nabla F=(2x,2y,2z)\big|_{(1,2,3)}=(2,4,6)$,方向化简为 $(1,2,3)$。法线 $\frac{x-1}{1}=\frac{y-2}{2}=\frac{z-3}{3}$,正是从球心 $(0,0,0)$ 出发的射线——球面任一点法线必过球心。
::end

### 9.8.2 极值的必要条件(Fermat)

::thm
(必要条件)若 $f(x,y)$ 在 $(x_0,y_0)$ 取得**局部极值**且在该点可偏导,则 $\nabla f(x_0,y_0)=\vec{0}$,即 $f_x=f_y=0$。
::end

::proof
固定 $y=y_0$,$g(x)=f(x,y_0)$ 是一元函数,$x_0$ 是它的局部极值点,由一元 Fermat 引理 $g'(x_0)=f_x(x_0,y_0)=0$。对 $y$ 同理。证毕。
::end

::def
$\nabla f(P)=\vec{0}$ 的点称为 $f$ 的**驻点**(stationary point)。**极值点必为驻点,但驻点未必是极值点**(可能是鞍点)。
::end

::pitfall
**经典反例**:$f(x,y)=x^2-y^2$ 在 $(0,0)$ 处 $\nabla f=\vec{0}$,沿 $x$ 轴 $f(x,0)=x^2$ 是局部极小,沿 $y$ 轴 $f(0,y)=-y^2$ 是局部极大——这就是**鞍点**。这种"沿不同方向走完全相反"的点在高维深度学习损失景观中**远比极值常见**。
::end

### 9.8.3 二阶判别(Hessian)

::def
$f(x,y)$ 在 $P_0$ 处二阶连续可偏导时,**Hessian 矩阵**定义为
$$H_f(P_0)=\begin{pmatrix}f_{xx}&f_{xy}\\ f_{yx}&f_{yy}\end{pmatrix}_{P_0}.$$
由 Clairaut 定理 $f_{xy}=f_{yx}$,所以 $H_f$ 是**对称矩阵**。记 $A=f_{xx}$,$B=f_{xy}$,$C=f_{yy}$,则
$$H_f=\begin{pmatrix}A&B\\ B&C\end{pmatrix},\quad\det H_f=AC-B^2.$$
教材中的判别式 $D=AC-B^2$ 就是 $\det H_f$。
::end

::thm
(极值二阶充分条件)设 $f$ 在 $P_0$ 处二阶连续可微,$P_0$ 是驻点($\nabla f(P_0)=\vec{0}$),记 $A=f_{xx}(P_0)$,$D=\det H_f(P_0)=AC-B^2$。则:
1. $D>0$ 且 $A>0$ $\Rightarrow$ $P_0$ 是**严格局部极小**;
2. $D>0$ 且 $A<0$ $\Rightarrow$ $P_0$ 是**严格局部极大**;
3. $D<0$ $\Rightarrow$ $P_0$ 是**鞍点**;
4. $D=0$ $\Rightarrow$ **判别失效**(需更高阶 Taylor 或直接代值)。
::end

::proof
驻点处由二元 Taylor 公式(留 Peano 余项):
$$f(P_0+\vec{h})-f(P_0)=\tfrac12\vec{h}^{\top}H_f(P_0)\vec{h}+o(|\vec{h}|^2),\quad\vec{h}=(\Delta x,\Delta y).$$
极值的局部行为由二次型 $Q(\vec{h})=\vec{h}^{\top}H_f\vec{h}=A\,\Delta x^2+2B\,\Delta x\Delta y+C\,\Delta y^2$ 决定。配方:
$$Q(\vec{h})=A\bigg(\Delta x+\frac{B}{A}\Delta y\bigg)^2+\frac{AC-B^2}{A}\Delta y^2,\quad\text{若 }A\neq 0.$$
- $D=AC-B^2>0$ 且 $A>0$:两项系数同正 $\Rightarrow Q>0$ 对所有 $\vec{h}\neq\vec{0}$,**正定**$\Rightarrow$ 极小。
- $D>0$ 且 $A<0$:配方两项系数同负 $\Rightarrow Q<0$,**负定**$\Rightarrow$ 极大。
- $D<0$:$Q$ 既能取正也能取负(沿两组特征方向符号相反),**不定**$\Rightarrow$ 鞍点。
- $A=0$ 但 $C\neq 0$:对 $\Delta y$ 配方同理。
- $A=C=0$:$Q=2B\Delta x\Delta y$,$B\neq 0$ 即不定为鞍点;$B=0$ 即 $H_f=0$ 判别失效。

线性代数等价描述:$H_f$ 是对称阵,有实特征值 $\lambda_1,\lambda_2$。由 Vieta 公式 $\lambda_1\lambda_2=\det H_f=D$,$\lambda_1+\lambda_2=A+C=\operatorname{tr}H_f$。$D>0$ 等价于两特征值同号($A$ 与同号),$D<0$ 等价于异号(不定)。
::end

::intuition
驻点附近 $f$ 的图形被 Hessian 决定:
- **正定**($D>0,\,A>0$):图形是"碗口朝上",底部最深。
- **负定**($D>0,\,A<0$):图形是"碗口朝下",顶部最高。
- **不定**($D<0$):图形是"马鞍",一个方向往上、另一个方向往下。
- **半定**($D=0$):图形是"槽"或"棱",二阶看不出来。
::end

### 9.8.4 例题与高维推广

::ex
**例 2** $f(x,y)=x^2+y^2+2x-4y+3$。

**解**:$f_x=2x+2$,$f_y=2y-4$。驻点:$x=-1,\,y=2$。$A=f_{xx}=2$,$B=f_{xy}=0$,$C=f_{yy}=2$,$D=4-0=4>0$,$A>0\Rightarrow$ 极小值。极小值 $f(-1,2)=1+4-2-8+3=-2$。
::end

::ex
**例 3**(鞍点)$f(x,y)=x^3-3xy+y^3$ 找极值。

**解**:$f_x=3x^2-3y=0$,$f_y=-3x+3y^2=0\Rightarrow y=x^2,\,x=y^2$,联立得 $(0,0)$ 与 $(1,1)$。
- 在 $(0,0)$:$A=f_{xx}=6x=0$,$B=-3$,$C=6y=0$,$D=0\cdot 0-9=-9<0$ $\Rightarrow$ 鞍点;
- 在 $(1,1)$:$A=6$,$B=-3$,$C=6$,$D=36-9=27>0$,$A>0$ $\Rightarrow$ 极小,极小值 $f(1,1)=-1$。
::end

**$n$ 维推广**:把 $f:\mathbb{R}^n\to\mathbb{R}$ 的 Hessian 写成 $H_f=(\partial^2 f/\partial x_i\partial x_j)$,驻点 $P_0$ 处局部:
- $H_f(P_0)$ **正定** $\iff$ 严格局部极小;
- $H_f(P_0)$ **负定** $\iff$ 严格局部极大;
- $H_f(P_0)$ **不定**(有正有负特征值) $\iff$ 鞍点;
- $H_f(P_0)$ **半定** $\iff$ 判别失效。

判断正定性的标准方法是 **Sylvester 判据**:$H$ 正定 $\iff$ 所有顺序主子式 $>0$;$H$ 负定 $\iff$ 顺序主子式符号交替($-,+,-,\dots$)。二维就是 $A>0,\,AC-B^2>0$,正好对应上面定理。

### 9.8.5 与凸优化、机器学习的联系

::def
$f:\mathbb{R}^n\to\mathbb{R}$ 是**凸函数** $\iff$ 对所有 $x,y$ 和 $\lambda\in[0,1]$,$f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y)$。二阶可微时等价于 $H_f(x)$ 对所有 $x$ **半正定**。**严格凸** $\iff$ $H_f$ **正定**。
::end

凸函数的关键性质:**任何驻点都是全局极小**,不存在局部陷阱。这就是凸优化(线性规划、SVM、Logistic 回归)可以「全局最优」可证的根本原因。

::thm
(Newton 法的二阶迭代)对二阶可微且 $H_f(\theta)$ 在最优点附近**正定**的函数,Newton 迭代
$$\theta^{(k+1)}=\theta^{(k)}-\big[H_f(\theta^{(k)})\big]^{-1}\nabla f(\theta^{(k)})$$
在最优点附近有**二次收敛**(每步误差平方级递减),远快于梯度下降的几何收敛。
::end

::proof
(思路)对 $\nabla f$ 在最优点 $\theta^*$ 附近做一阶 Taylor:$\nabla f(\theta)\approx H_f(\theta^*)(\theta-\theta^*)$。Newton 步取 $\theta-H^{-1}\nabla f$ 正是「猜下一步使一阶 Taylor 余项被吃掉」,从而 $\|\theta^{(k+1)}-\theta^*\|=O(\|\theta^{(k)}-\theta^*\|^2)$。完整证明需 $H$ Lipschitz 连续假设。
::end

::pitfall
**深度学习里的现实**:神经网络损失函数**非凸**,Hessian 不定;高维空间里**鞍点远多于极小点**(Dauphin 等 2014 经验法则:鞍点的"逃逸概率"远高于极小点)。这就是为何 SGD + Momentum 比纯 Newton 更受欢迎——Newton 在鞍点附近会被吸引,而带噪声的 SGD 反而能跳出。Hessian 在万亿参数模型里也算不起,所以实践用**对角近似 Hessian** 的 Adam、或者**Hessian-向量积**的 Conjugate Gradient 等近似方法。
::end

---

