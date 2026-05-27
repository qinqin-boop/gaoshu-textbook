## 9.9 二元函数的 Taylor 公式

一元 Taylor 公式 $f(x)=f(x_0)+f'(x_0)\Delta x+\tfrac12 f''(x_0)\Delta x^2+\dots+R_n$ 把 $f$ 在 $x_0$ 附近展开成多项式。二元情形:在 $\vec{x}_0=(x_0,y_0)$ 附近展开 $f(x,y)$,**一阶项是梯度**、**二阶项是 Hessian 二次型**——这两条已经在 §9.6(梯度)、§9.8(Hessian 极值判别)反复用过。本节给出二元 Taylor 公式的严格形式与证明,把分散的零碎结果归位。

### 9.9.1 二元 Taylor 公式

记 $\vec{h}=(\Delta x,\Delta y)=(x-x_0,y-y_0)$。引入算子记号:
$$D=\Delta x\frac{\partial}{\partial x}+\Delta y\frac{\partial}{\partial y},\qquad D^k=\bigg(\Delta x\frac{\partial}{\partial x}+\Delta y\frac{\partial}{\partial y}\bigg)^k\;\text{(用二项展开)}.$$
比如 $D^2 f=\Delta x^2 f_{xx}+2\Delta x\Delta y f_{xy}+\Delta y^2 f_{yy}$。

::thm
(二元 Taylor 公式)若 $f$ 在 $\vec{x}_0$ 邻域内有 $n+1$ 阶连续偏导,则
$$f(x_0+\Delta x,y_0+\Delta y)=\sum_{k=0}^n\frac{1}{k!}D^k f(\vec{x}_0)+R_n,$$
**Lagrange 余项**:存在 $\theta\in(0,1)$ 使
$$R_n=\frac{1}{(n+1)!}D^{n+1}f(x_0+\theta\Delta x,y_0+\theta\Delta y).$$
::end

::proof
**一元化技巧**:定义辅助函数 $\Phi(t)=f(x_0+t\Delta x,y_0+t\Delta y)$,$t\in[0,1]$,则 $\Phi$ 是一元函数。$\Phi(0)=f(\vec{x}_0)$,$\Phi(1)=f(\vec{x}_0+\vec{h})$。

链式法则:$\Phi'(t)=f_x\cdot\Delta x+f_y\cdot\Delta y=Df$。一般地 $\Phi^{(k)}(t)=D^k f$(归纳证)。

对 $\Phi$ 在 $[0,1]$ 上用**一元 Taylor 公式**(带 Lagrange 余项)在 $t=0$ 展开到 $t=1$:
$$\Phi(1)=\sum_{k=0}^n\frac{\Phi^{(k)}(0)}{k!}\cdot 1^k+\frac{\Phi^{(n+1)}(\theta)}{(n+1)!}\cdot 1^{n+1},\quad\theta\in(0,1).$$
代回 $\Phi^{(k)}=D^k f$ 即得二元 Taylor 公式。证毕。
::end

### 9.9.2 一阶 / 二阶展开:专门写出

**一阶**(全微分形式):
$$f(x_0+\Delta x,y_0+\Delta y)\approx f(\vec{x}_0)+f_x(\vec{x}_0)\Delta x+f_y(\vec{x}_0)\Delta y=f(\vec{x}_0)+\nabla f(\vec{x}_0)\cdot\vec{h}.$$
误差为 $o(|\vec{h}|)$(Peano 余项)。

**二阶**:
$$f(\vec{x}_0+\vec{h})\approx f(\vec{x}_0)+\nabla f(\vec{x}_0)\cdot\vec{h}+\tfrac12\vec{h}^\top H_f(\vec{x}_0)\,\vec{h}.$$
误差 $o(|\vec{h}|^2)$。**二次型** $\vec{h}^\top H_f\vec{h}$ 决定局部极值类型(§9.8)——这是为什么 $D=AC-B^2$ 判别式正是 $\det H_f$。

### 9.9.3 例题

::ex
**例 1**(线性近似算)$f(x,y)=e^x\sin y$,在 $(0,0)$ 处展开到二阶。

**解**:$f(0,0)=0$。$f_x=e^x\sin y,\,f_y=e^x\cos y$,在 $(0,0)$ 为 $(0,1)$。$f_{xx}=e^x\sin y=0$,$f_{xy}=e^x\cos y=1$,$f_{yy}=-e^x\sin y=0$,在 $(0,0)$。所以
$$f(x,y)\approx 0+0\cdot x+1\cdot y+\tfrac12(0\cdot x^2+2\cdot 1\cdot xy+0\cdot y^2)=y+xy.$$
::end

::ex
**例 2**(Peano vs Lagrange 的对照)$f(x,y)=\sqrt{1+x^2+y^2}$ 在 $(0,0)$ 处一阶展开。

**解**:$f(0,0)=1$。$f_x=x/\sqrt{1+x^2+y^2},f_y=y/\sqrt{\,\dots}$,在原点为零。
一阶展开 $f\approx 1+0\cdot x+0\cdot y=1$,误差 $\sim$ 二次量 $(x^2+y^2)/2$(可由二阶展开得)。

Lagrange 余项 $R_1=\tfrac12 D^2 f(\theta x,\theta y)$,展开
$$D^2 f=x^2 f_{xx}+2xy f_{xy}+y^2 f_{yy}.$$
$|R_1|$ 受 $|\nabla^2 f|$ 在邻域内的最大值控制。
::end

### 9.9.4 用 Taylor 推 Hessian 二阶判别(完整连接)

驻点 $\vec{x}_0$ 处 $\nabla f(\vec{x}_0)=\vec{0}$,二阶 Taylor 简化为
$$f(\vec{x}_0+\vec{h})-f(\vec{x}_0)=\tfrac12\vec{h}^\top H_f(\vec{x}_0)\,\vec{h}+o(|\vec{h}|^2).$$
**$H_f$ 正定 $\Rightarrow$ 局部极小**:对所有小 $\vec{h}\neq\vec{0}$,二次型 $>0$,余项可忽略,$f(\vec{x}_0+\vec{h})>f(\vec{x}_0)$。**负定 $\Rightarrow$ 极大**;**不定 $\Rightarrow$ 鞍点**——这正是 §9.8.3 的二阶判别定理,完整推导在这里。

### 9.9.5 多元 Taylor 在数值优化的角色

| 方法 | 用到的 Taylor 阶 | 公式 |
| --- | --- | --- |
| 梯度下降 | 1 阶 | $\theta_{k+1}=\theta_k-\eta\nabla f$ |
| Newton 法 | 2 阶 | $\theta_{k+1}=\theta_k-H^{-1}\nabla f$ |
| 拟 Newton(BFGS) | 2 阶近似 | $H$ 用低秩更新近似 |
| 信赖域(Trust Region) | 2 阶 + 球约束 | 在 $\|\vec{h}\|\le\Delta_k$ 内最小化二次模型 |
| Adam / RMSProp | 1 阶 + 自适应缩放 | 用二阶矩近似 Hessian 对角 |

**机器学习实践要点**:大模型(参数 $> 10^9$)中 Hessian 完整存不下($n^2$ 矩阵),所以二阶方法要么用**对角近似**(Adam)、要么用 **Hessian-向量积**(无需存 $H$ 也能算 $Hv$,共轭梯度法核心)、要么用 **K-FAC** 等分块近似。Taylor 公式不变,只是怎么近似 $H$ 是工程问题。

::pitfall
**易错点**:
- $D^k f$ 的二项展开**对偏导次数要按 $k$ 求**,不要漏中间项,如 $D^3f$ 有 4 项:$\Delta x^3 f_{xxx}+3\Delta x^2\Delta y f_{xxy}+3\Delta x\Delta y^2 f_{xyy}+\Delta y^3 f_{yyy}$;
- 一阶 Peano 余项 $o(|\vec{h}|)$ 与 $o(\sqrt{\Delta x^2+\Delta y^2})$ 同意,**不要写成 $o(\Delta x)+o(\Delta y)$**(可能丢主项);
- Lagrange 余项的 $\theta$ **依赖** $\vec{h}$ 和 $n$,不是固定值;
- 多元 Taylor 跟一元一样:**光滑不保证 Taylor 级数处处收敛到原函数**(§12.5 反例 $e^{-1/x^2}$);
- 三元及更高变量同样的算子记号,只是项数更多——一般用矩阵 / 张量记法更方便。
::end

---

