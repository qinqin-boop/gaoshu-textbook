## 8.5 空间直线及其方程

空间直线由「**一点 + 方向向量**」唯一确定,这一节给出参数式、对称式、一般式三种表达,推导直线-直线、直线-平面的位置关系,以及点到直线、两异面直线的距离公式。所有公式的几何根基都是 §8.1 与 §8.2 的向量代数(数量积、向量积、混合积)。

### 8.5.1 三种方程形式

::def
设直线 $\ell$ 过点 $M_0(x_0,y_0,z_0)$,方向向量 $\vec{s}=(m,n,p)$($\vec{s}\neq\vec{0}$)。$\ell$ 上任意点 $M(x,y,z)$ 满足 $\overrightarrow{M_0M}\parallel\vec{s}$,即 $\overrightarrow{M_0M}=t\vec{s}$。三种形式:

**参数式**:
$$x=x_0+mt,\quad y=y_0+nt,\quad z=z_0+pt,\quad t\in\mathbb{R}.$$

**对称式(点向式)**:
$$\frac{x-x_0}{m}=\frac{y-y_0}{n}=\frac{z-z_0}{p}.$$
约定:若某一方向分量为 $0$(比如 $m=0$),对应分子也为 $0$(即 $x=x_0$),其余照常。

**一般式**:由两个不平行的平面相交给出
$$\begin{cases}A_1x+B_1y+C_1z+D_1=0\\ A_2x+B_2y+C_2z+D_2=0\end{cases}$$
方向向量 $\vec{s}=\vec{n}_1\times\vec{n}_2=(A_1,B_1,C_1)\times(A_2,B_2,C_2)$。
::end

::ex
**例 1**(三式互换)直线 $\ell$:$\dfrac{x-1}{2}=\dfrac{y+2}{-1}=\dfrac{z-3}{4}$,化为参数式与一般式。

**解**:参数式 $x=1+2t,y=-2-t,z=3+4t$。一般式由两式相等截两次:
$$\frac{x-1}{2}=\frac{y+2}{-1}\Rightarrow x+2y+3=0,\quad\frac{y+2}{-1}=\frac{z-3}{4}\Rightarrow 4y+z+5=0.$$
::end

### 8.5.2 直线与直线位置关系

::thm
两直线 $\ell_1$($M_1,\vec{s}_1$)、$\ell_2$($M_2,\vec{s}_2$),令 $\vec{c}=\overrightarrow{M_1M_2}$:
1. **共面** $\iff[\vec{c},\vec{s}_1,\vec{s}_2]=0$(三向量混合积为零);
2. **平行** $\iff\vec{s}_1\parallel\vec{s}_2$ 且 $\vec{c}\not\parallel\vec{s}_1$;
3. **相交** $\iff[\vec{c},\vec{s}_1,\vec{s}_2]=0$ 且 $\vec{s}_1\not\parallel\vec{s}_2$;
4. **异面**(不在同一平面)$\iff[\vec{c},\vec{s}_1,\vec{s}_2]\neq 0$;
5. **垂直**($\ell_1\perp\ell_2$)$\iff\vec{s}_1\cdot\vec{s}_2=0$。
::end

::proof
$\ell_1,\ell_2$ 共面 $\iff M_1M_2$、$\vec{s}_1$、$\vec{s}_2$ 三向量共面 $\iff$ 混合积 $=0$。其余分类:在共面情形下,若方向平行则平行(不重合)或重合;若方向不平行则相交。不共面即异面。证毕。
::end

::ex
**例 2** $\ell_1:\frac{x-1}{1}=\frac{y}{2}=\frac{z+1}{0}$(注意 $p=0$:意味 $z=-1$),$\ell_2:\frac{x}{2}=\frac{y-1}{0}=\frac{z-2}{1}$(意味 $y=1$)。判位置关系。

**解**:$\vec{s}_1=(1,2,0)$,$\vec{s}_2=(2,0,1)$,$\vec{s}_1\times\vec{s}_2=(2,-1,-4)\neq\vec{0}$,不平行。$\vec{c}=(0-1,1-0,2-(-1))=(-1,1,3)$。混合积
$$[\vec{c},\vec{s}_1,\vec{s}_2]=\vec{c}\cdot(\vec{s}_1\times\vec{s}_2)=(-1)(2)+1(-1)+3(-4)=-2-1-12=-15\neq 0.$$
**异面**。
::end

### 8.5.3 直线与平面位置关系

::thm
直线 $\ell$(方向 $\vec{s}$,过点 $M_0$)与平面 $\pi$(法向 $\vec{n}$):
1. **$\ell\parallel\pi$**($\ell$ 不在 $\pi$ 内)$\iff\vec{s}\cdot\vec{n}=0$ 且 $M_0\notin\pi$;
2. **$\ell\subset\pi$** $\iff\vec{s}\cdot\vec{n}=0$ 且 $M_0\in\pi$;
3. **$\ell\perp\pi$** $\iff\vec{s}\parallel\vec{n}$;
4. **相交一点** $\iff\vec{s}\cdot\vec{n}\neq 0$。

夹角 $\theta\in[0,\pi/2]$(直线与平面的夹角约定取与法向夹角的余角)由
$$\sin\theta=\frac{|\vec{s}\cdot\vec{n}|}{|\vec{s}|\,|\vec{n}|}.$$
::end

::proof
$\ell\parallel\pi\iff\vec{s}\perp\vec{n}$。$\ell\perp\pi$ 即 $\ell$ 与平面任一向量都垂直 $\iff\vec{s}\parallel\vec{n}$。夹角:直线与平面所成角为直线与法向所成角的余角,所以用 $\sin\theta=\cos(\pi/2-\theta)=|\cos\langle\vec{s},\vec{n}\rangle|$。
::end

### 8.5.4 距离公式

::thm
(点到直线的距离)点 $P_1$ 到直线 $\ell$(过 $M_0$,方向 $\vec{s}$)的距离
$$d=\frac{|\overrightarrow{M_0P_1}\times\vec{s}|}{|\vec{s}|}.$$
::end

::proof
$\overrightarrow{M_0P_1}\times\vec{s}$ 的模 $=|\overrightarrow{M_0P_1}|\cdot|\vec{s}|\sin\varphi$(平行四边形面积,$\varphi$ 是 $\overrightarrow{M_0P_1}$ 与 $\vec{s}$ 的夹角)。$|\overrightarrow{M_0P_1}|\sin\varphi$ 就是 $P_1$ 到 $\ell$ 的距离。除以 $|\vec{s}|$ 即得。
::end

::thm
(异面直线公垂线距离)两条异面直线 $\ell_1$($M_1,\vec{s}_1$)、$\ell_2$($M_2,\vec{s}_2$)的公垂线段长度
$$d=\frac{|[\overrightarrow{M_1M_2},\vec{s}_1,\vec{s}_2]|}{|\vec{s}_1\times\vec{s}_2|}.$$
::end

::proof
公垂线方向 $=\vec{s}_1\times\vec{s}_2$(同时垂直两条直线)。距离 $=\overrightarrow{M_1M_2}$ 在 $\vec{s}_1\times\vec{s}_2$ 方向上的投影绝对值:
$$d=\frac{|\overrightarrow{M_1M_2}\cdot(\vec{s}_1\times\vec{s}_2)|}{|\vec{s}_1\times\vec{s}_2|}=\frac{|[\overrightarrow{M_1M_2},\vec{s}_1,\vec{s}_2]|}{|\vec{s}_1\times\vec{s}_2|}.$$
**分子是混合积绝对值,即平行六面体体积;分母是底面(共垂直方向围成)的面积;距离 = 体积 / 底面积 = 高。**
::end

::ex
**例 3**(异面距离)续例 2,求两异面直线 $\ell_1,\ell_2$ 距离。

**解**:$|\vec{s}_1\times\vec{s}_2|=|(2,-1,-4)|=\sqrt{21}$,$|[\vec{c},\vec{s}_1,\vec{s}_2]|=15$。$d=15/\sqrt{21}=\frac{15\sqrt{21}}{21}=\frac{5\sqrt{21}}{7}$。
::end

::pitfall
**易错点**:
- 对称式 $\frac{x-x_0}{m}=\dots$ 当某 $m=0$ 时**约定式**(对应分子也为零),不要写成除以零;
- 一般式由两平面相交决定,**两平面必须不平行**;
- 异面 $\iff$ 混合积非零;考试常把"异面距离"算成"投影距离"——记牢用**公垂线长度公式**(混合积 / $|\vec{s}_1\times\vec{s}_2|$);
- 直线与平面**夹角用 $\sin$**(因为是法向余角),不要直接套两向量夹角的 $\cos$ 公式。
::end

---

