## 8.1 向量及其线性运算

向量是高等数学下册的「字母表」——所有曲面方程、偏导数、重积分、级数、Maxwell 方程都用向量语言写。这一节给出向量的严格定义(从等价类出发,而不只是「带方向的线段」)、加法 / 数乘的运算律(线性空间 8 条公理的雏形)、标准基与分量唯一性,以及向量投影的几何与代数双定义。它打下后续所有几何运算与抽象代数化的地基。

### 8.1.1 为什么需要向量?

::intuition
**只有方向不行,只有大小也不行**。物理量分两类:
- **标量**(scalar):质量 / 温度 / 时间 / 体积 / 概率——只有大小;
- **矢量**(vector):位移 / 速度 / 加速度 / 力 / 电场 / 角动量——既有大小,又有方向。

把两个标量相加是数的加法;把两个矢量相加要按**平行四边形法则**(同时考虑方向)——经典力学里"合力"概念的代数化。

**应用栈**:
- **工科 3D**:计算机图形(顶点 / 法向)、机器人(关节坐标)、CAD;
- **AI**:词嵌入 / 图像特征 / 隐藏层激活都是高维向量,余弦相似度、注意力机制都是向量运算;
- **量子力学**:态向量 $|\psi\rangle$ 是 Hilbert 空间向量;
- **统计**:数据点 / 主成分 / 协方差矩阵都建立在向量空间上。
::end

### 8.1.2 向量的严格定义

直观的「带箭头的线段」有一个问题:从 $A$ 到 $B$ 的箭头跟从 $A'$ 到 $B'$(平行、同向、等长)的箭头**算不算同一向量**?物理上不该区分——力作用线可以平移。所以:

::def
在 $\mathbb{R}^3$ 中,**有向线段** $\overrightarrow{AB}$ 由起点 $A$ 与终点 $B$ 决定。两条有向线段 $\overrightarrow{AB}$、$\overrightarrow{CD}$ **等价**($\overrightarrow{AB}\sim\overrightarrow{CD}$)若它们**长度相等、方向相同**(即 $B-A=D-C$)。**自由向量**是有向线段在该等价关系下的等价类。
::end

::intuition
**等价类**意味:可以平移,选哪个代表都行。两类特殊情形:
- **位置向量**(positionvector):规定起点为原点 $O$,$\vec{r}=\overrightarrow{OP}=(x_P,y_P,z_P)$;
- **滑动向量**:起点可在某一直线上滑动(刚体力学的力矢用此)。

本书默认讨论自由向量。**记号**:$\vec{a}$ 或粗体 $\mathbf{a}$。
::end

::def
向量 $\vec{a}=\overrightarrow{AB}$ 的**模长**(magnitude / norm)
$$|\vec{a}|=\sqrt{(B_1-A_1)^2+(B_2-A_2)^2+(B_3-A_3)^2}.$$
- $|\vec{a}|=0$ $\iff$ $\vec{a}=\vec{0}$(**零向量**,起点 $=$ 终点,方向任意);
- $|\vec{a}|=1$ 的向量称为**单位向量**;
- 与 $\vec{a}$ 共线、模长相同、方向相反的向量 $-\vec{a}$ 叫 $\vec{a}$ 的**负向量**。
::end

### 8.1.3 加法、减法、数乘

::def
- **加法**:用「三角形法则」或等价的「平行四边形法则」。代数式 $\vec{a}+\vec{b}=(a_1+b_1,a_2+b_2,a_3+b_3)$。
- **减法**:$\vec{a}-\vec{b}=\vec{a}+(-\vec{b})$。几何上从 $\vec{b}$ 终点指向 $\vec{a}$ 终点(同起点放置时)。
- **数乘**:$\lambda\in\mathbb{R}$,$\lambda\vec{a}=(\lambda a_1,\lambda a_2,\lambda a_3)$,几何上长度乘 $|\lambda|$,$\lambda>0$ 保持方向,$\lambda<0$ 反向。
::end

::svg
<svg viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="a8a" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="a8b" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#8b3a0a"/></marker>
    <marker id="a8c" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <line x1="40" y1="150" x2="180" y2="150" stroke="#1a365d" stroke-width="2.5" marker-end="url(#a8a)"/>
  <text x="100" y="167" font-size="13" fill="#1a365d" font-style="italic">a</text>
  <line x1="180" y1="150" x2="280" y2="60" stroke="#8b3a0a" stroke-width="2.5" marker-end="url(#a8b)"/>
  <text x="240" y="105" font-size="13" fill="#8b3a0a" font-style="italic">b</text>
  <line x1="40" y1="150" x2="280" y2="60" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#a8c)" stroke-dasharray="6 3"/>
  <text x="140" y="100" font-size="13" fill="#2d6e2d" font-style="italic">a + b</text>
</svg>
<figcaption>图 8.1.1 三角形法则:把 $\vec{b}$ 的起点接到 $\vec{a}$ 的终点,$\vec{a}+\vec{b}$ 即从 $\vec{a}$ 起点到 $\vec{b}$ 终点的箭头。</figcaption>
::endsvg

::thm
(线性运算 8 条公理)对所有 $\vec{a},\vec{b},\vec{c}\in\mathbb{R}^3$ 与 $\lambda,\mu\in\mathbb{R}$:
1. $\vec{a}+\vec{b}=\vec{b}+\vec{a}$(加法交换律)
2. $(\vec{a}+\vec{b})+\vec{c}=\vec{a}+(\vec{b}+\vec{c})$(结合律)
3. $\vec{a}+\vec{0}=\vec{a}$(零元)
4. $\vec{a}+(-\vec{a})=\vec{0}$(负元)
5. $1\cdot\vec{a}=\vec{a}$
6. $(\lambda\mu)\vec{a}=\lambda(\mu\vec{a})$(数乘结合)
7. $\lambda(\vec{a}+\vec{b})=\lambda\vec{a}+\lambda\vec{b}$(对向量分配)
8. $(\lambda+\mu)\vec{a}=\lambda\vec{a}+\mu\vec{a}$(对标量分配)
::end

::proof
全部由坐标定义 $\vec{a}=(a_1,a_2,a_3)$ 直接验证——把实数加法 / 乘法的对应运算律搬过来。例如交换律:$\vec{a}+\vec{b}=(a_1+b_1,a_2+b_2,a_3+b_3)$,实数加法交换 $a_i+b_i=b_i+a_i$,故 $=\vec{b}+\vec{a}$。其它七条同理。
::end

::intuition
这 **8 条**是**线性空间(向量空间)**的公理。任何集合 + 加法 + 数乘只要满足这 8 条,就能"当向量空间研究"。多项式集合 $\mathbb{R}[x]$、连续函数空间 $C[0,1]$、$n\times n$ 矩阵集合、Hilbert 空间——都是线性空间。**这一抽象正是 ch12 把 Fourier 系数视为函数在三角基上"坐标"的基础**,也是机器学习把数据看成向量来运算的代数前提。
::end

### 8.1.4 标准基与分量分解

::def
$\mathbb{R}^3$ 中的**标准基**:
$$\vec{i}=(1,0,0),\quad\vec{j}=(0,1,0),\quad\vec{k}=(0,0,1).$$
它们两两垂直、长度都为 $1$,称作**标准正交基**(orthonormal basis)。
::end

::thm
(分解唯一性)对任意 $\vec{a}\in\mathbb{R}^3$,存在**唯一**的三元组 $(a_1,a_2,a_3)\in\mathbb{R}^3$ 使
$$\vec{a}=a_1\vec{i}+a_2\vec{j}+a_3\vec{k}.$$
此即 $\vec{a}=(a_1,a_2,a_3)$ 在坐标系下的**分量**或**坐标表示**。
::end

::proof
**存在性**:取 $a_i=$ $\vec{a}$ 与 $\vec{e}_i$ 的对应坐标,直接验证 $a_1\vec{i}+a_2\vec{j}+a_3\vec{k}=(a_1,0,0)+(0,a_2,0)+(0,0,a_3)=(a_1,a_2,a_3)=\vec{a}$。
**唯一性**:若 $\vec{a}=b_1\vec{i}+b_2\vec{j}+b_3\vec{k}=c_1\vec{i}+c_2\vec{j}+c_3\vec{k}$,作差得 $(b_1-c_1)\vec{i}+(b_2-c_2)\vec{j}+(b_3-c_3)\vec{k}=\vec{0}$。由 $\vec{i},\vec{j},\vec{k}$ 的**线性无关**(三向量非共面)得各系数为 $0$,即 $b_i=c_i$。证毕。
::end

::intuition
"线性无关 $\Rightarrow$ 系数唯一" 是线性代数的核心规则。换基(从 $\vec{i},\vec{j},\vec{k}$ 换成另一组三个线性无关向量)时,**同一向量的分量会变,向量本身不变**——这就是为什么物理学要区分「向量」(几何对象)与「分量」(依赖于坐标系)。Einstein 在写广义相对论时坚持「方程必须坐标无关」也就是这个意思。
::end

### 8.1.5 投影

向量到向量、向量到平面的投影,在曲面切平面、最小二乘、机器学习正交化(Gram-Schmidt)中反复出现。这里给二维基本版。

::def
设 $\vec{a},\vec{b}\in\mathbb{R}^3$,$\vec{b}\neq\vec{0}$,**$\vec{a}$ 在 $\vec{b}$ 方向上的标量投影**
$$\operatorname{prj}_{\vec{b}}\vec{a}=|\vec{a}|\cos\theta\quad(\theta\text{ 为 }\vec{a},\vec{b}\text{ 夹角}),$$
**向量投影**
$$\vec{a}_{\parallel}=(\operatorname{prj}_{\vec{b}}\vec{a})\cdot\frac{\vec{b}}{|\vec{b}|}.$$
::def
::end

由 §8.2.1 数量积的定义直接得:

::thm
(投影的代数公式)
$$\operatorname{prj}_{\vec{b}}\vec{a}=\frac{\vec{a}\cdot\vec{b}}{|\vec{b}|},\qquad\vec{a}_{\parallel}=\frac{\vec{a}\cdot\vec{b}}{|\vec{b}|^2}\,\vec{b}.$$
此外,$\vec{a}=\vec{a}_{\parallel}+\vec{a}_{\perp}$,其中 $\vec{a}_{\perp}=\vec{a}-\vec{a}_{\parallel}$ 与 $\vec{b}$ 垂直。
::end

::proof
$\vec{a}\cdot\vec{b}=|\vec{a}|\,|\vec{b}|\cos\theta\Rightarrow|\vec{a}|\cos\theta=\frac{\vec{a}\cdot\vec{b}}{|\vec{b}|}$,即 $\operatorname{prj}_{\vec{b}}\vec{a}$ 公式。向量投影 $=$ 标量投影乘上 $\vec{b}$ 单位向量,即 $\vec{a}_{\parallel}=\frac{\vec{a}\cdot\vec{b}}{|\vec{b}|^2}\vec{b}$。验证垂直:$\vec{a}_{\perp}\cdot\vec{b}=(\vec{a}-\vec{a}_{\parallel})\cdot\vec{b}=\vec{a}\cdot\vec{b}-\frac{\vec{a}\cdot\vec{b}}{|\vec{b}|^2}|\vec{b}|^2=0$。证毕。
::end

::svg
<svg viewBox="0 0 320 160" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="p1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="p2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#8b3a0a"/></marker>
    <marker id="p3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <line x1="40" y1="130" x2="280" y2="130" stroke="#1a365d" stroke-width="2" marker-end="url(#p1)"/>
  <text x="270" y="148" font-size="13" fill="#1a365d" font-style="italic">b</text>
  <line x1="40" y1="130" x2="180" y2="40" stroke="#8b3a0a" stroke-width="2" marker-end="url(#p2)"/>
  <text x="186" y="38" font-size="13" fill="#8b3a0a" font-style="italic">a</text>
  <line x1="180" y1="40" x2="180" y2="130" stroke="#888" stroke-width="1.2" stroke-dasharray="4 3"/>
  <line x1="40" y1="130" x2="180" y2="130" stroke="#2d6e2d" stroke-width="3" marker-end="url(#p3)"/>
  <text x="80" y="150" font-size="12" fill="#2d6e2d" font-style="italic">a∥ (投影)</text>
  <text x="185" y="90" font-size="11" fill="#888">a⊥</text>
</svg>
<figcaption>图 8.1.2 向量 $\vec{a}$ 沿 $\vec{b}$ 的投影 $\vec{a}_\parallel$ 与垂直分量 $\vec{a}_\perp$,$\vec{a}=\vec{a}_\parallel+\vec{a}_\perp$。</figcaption>
::endsvg

::ex
**例 1**(标准基分量即投影)$\vec{a}=(3,-2,5)$。其 $x$-分量 $a_1=3$ 正是 $\vec{a}$ 在 $\vec{i}=(1,0,0)$ 上的标量投影:
$$\operatorname{prj}_{\vec{i}}\vec{a}=\frac{\vec{a}\cdot\vec{i}}{|\vec{i}|}=\frac{3}{1}=3.$$
::end

::ex
**例 2**(力分解)$5\,\mathrm{N}$ 的力 $\vec{F}=(3,4,0)$ 拉一个沿 $\vec{b}=(1,0,0)$ 方向滑动的物体。沿运动方向有效的力是
$$\operatorname{prj}_{\vec{b}}\vec{F}=\frac{(3,4,0)\cdot(1,0,0)}{1}=3\,\mathrm{N}.$$
垂直方向 $\vec{F}_\perp=(0,4,0)$ 对运动无用(在物理上转为对地面的压力)。**这就是斜面问题里把重力分解成沿斜面与垂直斜面两部分的代数化版本**。
::end

### 8.1.6 方向余弦

::def
$\vec{a}\neq\vec{0}$ 与三个坐标轴的夹角 $\alpha,\beta,\gamma$ 的余弦 $\cos\alpha,\cos\beta,\cos\gamma$ 称为 $\vec{a}$ 的**方向余弦**:
$$\cos\alpha=\frac{a_1}{|\vec{a}|},\quad\cos\beta=\frac{a_2}{|\vec{a}|},\quad\cos\gamma=\frac{a_3}{|\vec{a}|}.$$
满足约束 $\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1$(即 $|\vec{a}|^2/|\vec{a}|^2=1$),也就是说**方向余弦构成 $\vec{a}$ 的单位向量分量**。
::end

::pitfall
**易错点**:
- 「自由向量」可平移,但**绑定向量**(如位置向量、力臂)有起点限制,搞混会得错误结论;
- 向量等式 $\vec{a}=\vec{b}$ 要求**模、方向同时一致**,只对应一个就不算;
- 数乘 $\lambda\vec{a}$ 中,**$\lambda=0$ 给零向量**(任意方向),不要写"方向不变";
- 投影 $\operatorname{prj}_{\vec{b}}\vec{a}$ 是**有符号标量**,$\theta>\pi/2$ 时为负;
- 标准基分解唯一性**依赖线性无关**——如果只有 $\vec{i},\vec{j}$ 在三维空间里展开 $\vec{a}$,无法覆盖到 $z$ 方向的成分,这就是「不完备基」无法表达整个空间的几何根源。
::end

---

