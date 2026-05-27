## 8.4 平面及其方程

空间中给定一个**点** $P_0$ 与一个**法向量** $\vec{n}$ 就唯一确定一张平面——这是平面方程的几何起源。本节给出点法式、一般式、截距式、三点式四种等价表达,推导平面与点的距离公式,并把所有形式串成「同一个平面看不同角度」。这些公式是后续直线与平面位置关系、曲面切平面、最小二乘法几何意义的代数底座。

### 8.4.1 点法式与一般式

::def
设平面 $\pi$ 过点 $P_0(x_0,y_0,z_0)$,有法向量 $\vec{n}=(A,B,C)$($\vec{n}\neq\vec{0}$)。对平面上任意点 $P(x,y,z)$,$\overrightarrow{P_0P}\perp\vec{n}$,即 $\vec{n}\cdot\overrightarrow{P_0P}=0$。这就是
$$\boxed{A(x-x_0)+B(y-y_0)+C(z-z_0)=0}\qquad\text{(点法式)}$$
展开常数项,可写成
$$\boxed{Ax+By+Cz+D=0}\qquad\text{(一般式)},\quad D=-(Ax_0+By_0+Cz_0).$$
::end

::intuition
**法向量决定方向,点决定位置**。把法向量类比成"竖直的旗杆"——所有"水平地面"上的点(满足 $\vec{n}\cdot\overrightarrow{P_0P}=0$)就组成了平面。一般式 $Ax+By+Cz+D=0$ 中,系数 $(A,B,C)$ **就是**法向量;$D$ 控制平移。
::end

::ex
**例 1** 过点 $P_0(1,-2,3)$,法向量 $\vec{n}=(2,1,-1)$ 的平面?

**解**:点法式 $2(x-1)+(y+2)-(z-3)=0$,化简 $2x+y-z+3=0$。
::end

### 8.4.2 三点式与截距式

::thm
过三点 $A,B,C$(不共线)的平面方程为
$$\big[(x-A_x,y-A_y,z-A_z),\;\vec{AB},\;\vec{AC}\big]=0,$$
即三个向量 $\overrightarrow{AP},\overrightarrow{AB},\overrightarrow{AC}$ 的**混合积** $=0$(共面)。等价地,
$$\begin{vmatrix}x-A_x&y-A_y&z-A_z\\ B_x-A_x&B_y-A_y&B_z-A_z\\ C_x-A_x&C_y-A_y&C_z-A_z\end{vmatrix}=0.$$
::end

::proof
法向量取 $\vec{n}=\vec{AB}\times\vec{AC}$(垂直于平面)。$P$ 在平面上 $\iff\overrightarrow{AP}\cdot\vec{n}=0\iff\overrightarrow{AP}\cdot(\vec{AB}\times\vec{AC})=0\iff[\overrightarrow{AP},\vec{AB},\vec{AC}]=0$。混合积写成行列式即得公式。证毕。
::end

::def
(截距式)若平面与三坐标轴分别相交于 $(a,0,0),(0,b,0),(0,0,c)$(称为**截距**,$a,b,c\neq 0$),则方程为
$$\boxed{\frac{x}{a}+\frac{y}{b}+\frac{z}{c}=1.}$$
::end

::proof
代入三个截距点验证:$a/a=1$,余两项 $=0$,等式成立。其它点由平面唯一性即在该方程上。
::end

### 8.4.3 点到平面的距离

::thm
点 $P_1(x_1,y_1,z_1)$ 到平面 $\pi:Ax+By+Cz+D=0$ 的距离
$$d(P_1,\pi)=\frac{|Ax_1+By_1+Cz_1+D|}{\sqrt{A^2+B^2+C^2}}=\frac{|\vec{n}\cdot\overrightarrow{P_0P_1}|}{|\vec{n}|}.$$
::end

::proof
取平面上任一点 $P_0$($Ax_0+By_0+Cz_0+D=0$,即 $D=-\vec{n}\cdot\overrightarrow{OP_0}$)。$P_1$ 到平面的距离 $=$ $\overrightarrow{P_0P_1}$ 在 $\vec{n}$ 方向上的**有向投影绝对值**:
$$d=\frac{|\overrightarrow{P_0P_1}\cdot\vec{n}|}{|\vec{n}|}=\frac{|A(x_1-x_0)+B(y_1-y_0)+C(z_1-z_0)|}{\sqrt{A^2+B^2+C^2}}=\frac{|Ax_1+By_1+Cz_1+D|}{\sqrt{A^2+B^2+C^2}}.$$
证毕。
::end

::intuition
这就是 §8.1.5 「向量沿另一向量的投影」公式在平面情形的应用——把"点离平面有多远"翻译成"$P_0P_1$ 沿法向 $\vec{n}$ 的投影长度"。**点到直线距离**(平面情形)、**SVM 间隔最大化**(机器学习里用 $|w\cdot x+b|/|w|$ 作为分类间隔)、**最小二乘法**(把数据点垂直投影到回归直线)都是同一公式的不同应用。
::end

::ex
**例 2** $P_1(1,1,1)$ 到平面 $x-2y+2z+5=0$ 的距离?

**解**:$\vec{n}=(1,-2,2)$,$|\vec{n}|=3$。$1-2+2+5=6$。$d=|6|/3=2$。
::end

### 8.4.4 两平面的位置关系

::thm
两平面 $\pi_1:A_1x+B_1y+C_1z+D_1=0$,$\pi_2:A_2x+B_2y+C_2z+D_2=0$,法向 $\vec{n}_1,\vec{n}_2$。
- **平行** $\iff\vec{n}_1\parallel\vec{n}_2$,即 $(A_1,B_1,C_1)$ 与 $(A_2,B_2,C_2)$ 成比例;若 $D$ 也成同比例则**重合**,否则**严格平行**;
- **垂直** $\iff\vec{n}_1\cdot\vec{n}_2=0\iff A_1A_2+B_1B_2+C_1C_2=0$;
- 一般情形,夹角 $\theta\in[0,\pi/2]$ 由 $\cos\theta=|\vec{n}_1\cdot\vec{n}_2|/(|\vec{n}_1|\,|\vec{n}_2|)$ 给出。
::end

::pitfall
**易错点**:
- 一般式中 $(A,B,C)$ **必须不全为零**,否则不是平面方程;
- 三点共线 $\Rightarrow$ $\vec{AB}\times\vec{AC}=\vec{0}$ $\Rightarrow$ 无法用三点式定唯一平面;
- 计算距离公式时 **$|$内容$|$ 是绝对值不是平方**;
- 两平面夹角约定取 $[0,\pi/2]$,所以分子带绝对值;若不取绝对值则方向相反时夹角变补角。
::end

---

