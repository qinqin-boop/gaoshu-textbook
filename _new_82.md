## 8.2 数量积 · 向量积 · 混合积

向量加法和数乘还停留在「方向 + 长度」的一维操控。这一节我们引入**两种向量间的乘法**:点乘把两向量压成一个**标量**(用来量「相似度 / 投影 / 夹角」),叉乘生成一个**新向量**(用来量「平行四边形 / 平面法向」)。再把它们组合成混合积(三向量的「带号体积」)。这三件套是后续曲面方程、Maxwell 方程组、计算机图形学渲染的代数底座。

### 8.2.1 数量积(点乘 / 内积)

::def
**数量积**(scalar product / dot product / inner product)是把两个向量映射为一个实数的二元运算。在 $\mathbb{R}^3$ 中,设 $\vec{a}=(a_1,a_2,a_3)$,$\vec{b}=(b_1,b_2,b_3)$,夹角为 $\theta\in[0,\pi]$,则
$$\vec{a}\cdot\vec{b}=|\vec{a}|\,|\vec{b}|\cos\theta\quad\text{(几何式)}\qquad\vec{a}\cdot\vec{b}=a_1b_1+a_2b_2+a_3b_3\quad\text{(坐标式)}.$$
::end

两个表达式给出**同一个数**——这是定理,不是定义,需要证明。

::thm
(两种定义的等价性)对任意 $\vec{a},\vec{b}\in\mathbb{R}^3$,$|\vec{a}|\,|\vec{b}|\cos\theta = a_1b_1+a_2b_2+a_3b_3$。
::end

::proof
记 $\vec{c}=\vec{a}-\vec{b}$。在以 $\vec{a},\vec{b}$ 为两边的三角形中应用余弦定理:
$$|\vec{c}|^2 = |\vec{a}|^2+|\vec{b}|^2-2|\vec{a}|\,|\vec{b}|\cos\theta.\qquad(\star)$$
而由坐标
$$|\vec{c}|^2=\sum_{i=1}^3(a_i-b_i)^2=\sum a_i^2-2\sum a_ib_i+\sum b_i^2=|\vec{a}|^2-2\sum a_ib_i+|\vec{b}|^2.\qquad(\star\star)$$
比较 $(\star)$ 与 $(\star\star)$ 得 $|\vec{a}|\,|\vec{b}|\cos\theta=\sum_{i=1}^3 a_ib_i$。证毕。
::end

::intuition
把 $\vec{b}$ 投影到 $\vec{a}$ 方向得到一段长度为 $|\vec{b}|\cos\theta$ 的有向线段;再把它**乘上** $|\vec{a}|$ 就是点乘。所以点乘 $=$「我」的方向上「你」走了多远 $\times$「我」的长度。$\theta<90°$ 同向贡献为正,$\theta=90°$ 互相垂直贡献为 $0$,$\theta>90°$ 反向贡献为负。
::end

::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ah" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/>
    </marker>
    <marker id="ah2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#8b3a0a"/>
    </marker>
  </defs>
  <line x1="40" y1="160" x2="280" y2="160" stroke="#1a365d" stroke-width="2" marker-end="url(#ah)"/>
  <text x="280" y="178" fill="#1a365d" font-size="14" font-style="italic">a</text>
  <line x1="40" y1="160" x2="180" y2="60" stroke="#8b3a0a" stroke-width="2" marker-end="url(#ah2)"/>
  <text x="190" y="55" fill="#8b3a0a" font-size="14" font-style="italic">b</text>
  <line x1="180" y1="60" x2="180" y2="160" stroke="#888" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="40" y1="160" x2="180" y2="160" stroke="#c2410c" stroke-width="3"/>
  <text x="100" y="180" fill="#c2410c" font-size="13">|b| cos θ (投影长度)</text>
  <path d="M 80 160 A 40 40 0 0 0 60 140" fill="none" stroke="#444" stroke-width="1"/>
  <text x="68" y="150" fill="#444" font-size="12">θ</text>
</svg>
<figcaption>图 8.2.1 数量积的几何解释:$\vec{a}\cdot\vec{b}$ 等于 $\vec{b}$ 在 $\vec{a}$ 方向投影长度乘 $|\vec{a}|$。</figcaption>
::endsvg

**运算律**(由坐标式直接验证):
1. **对称性**:$\vec{a}\cdot\vec{b}=\vec{b}\cdot\vec{a}$
2. **关于数乘双线性**:$(\lambda\vec{a})\cdot\vec{b}=\lambda(\vec{a}\cdot\vec{b})$
3. **关于加法双线性**:$\vec{a}\cdot(\vec{b}+\vec{c})=\vec{a}\cdot\vec{b}+\vec{a}\cdot\vec{c}$
4. **正定性**:$\vec{a}\cdot\vec{a}=|\vec{a}|^2\ge 0$,等号成立当且仅当 $\vec{a}=\vec{0}$

::thm
(Cauchy-Schwarz 不等式)对任意 $\vec{a},\vec{b}\in\mathbb{R}^3$,
$$|\vec{a}\cdot\vec{b}|\le|\vec{a}|\,|\vec{b}|,$$
等号成立当且仅当 $\vec{a},\vec{b}$ 线性相关(共线)。
::end

::proof
若 $\vec{b}=\vec{0}$ 两边为零,显然。设 $\vec{b}\neq\vec{0}$,对任意 $t\in\mathbb{R}$ 由正定性有
$$0\le|\vec{a}-t\vec{b}|^2=|\vec{a}|^2-2t(\vec{a}\cdot\vec{b})+t^2|\vec{b}|^2.$$
这是关于 $t$ 的二次多项式且非负,判别式 $\le 0$:
$$4(\vec{a}\cdot\vec{b})^2-4|\vec{a}|^2|\vec{b}|^2\le 0\;\Longrightarrow\;(\vec{a}\cdot\vec{b})^2\le|\vec{a}|^2|\vec{b}|^2.$$
开方即得不等式。等号 $\Leftrightarrow$ 二次式有重根 $t_0$ $\Leftrightarrow$ $\vec{a}=t_0\vec{b}$ 共线。证毕。
::end

这个证明的副产品是几何定义里的 $\cos\theta$ **总是落在 $[-1,1]$**——否则就破坏 Cauchy-Schwarz 了。

**核心推论**:
- **求夹角**:$\displaystyle\cos\theta=\frac{\vec{a}\cdot\vec{b}}{|\vec{a}|\,|\vec{b}|}$
- **判垂直**:$\vec{a}\perp\vec{b}\iff\vec{a}\cdot\vec{b}=0$(包含约定 $\vec{0}$ 与任何向量垂直)
- **求投影**:$\vec{b}$ 在 $\vec{a}$ 方向上的标量投影 $\displaystyle\operatorname{prj}_{\vec{a}}\vec{b}=\frac{\vec{a}\cdot\vec{b}}{|\vec{a}|}$,向量投影 $\displaystyle\frac{\vec{a}\cdot\vec{b}}{|\vec{a}|^2}\vec{a}$
- **向量版完全平方公式**:$|\vec{a}+\vec{b}|^2=|\vec{a}|^2+2\vec{a}\cdot\vec{b}+|\vec{b}|^2$
- **极化恒等式**:$\displaystyle\vec{a}\cdot\vec{b}=\tfrac14\big(|\vec{a}+\vec{b}|^2-|\vec{a}-\vec{b}|^2\big)$

::ex
**例 1**(计算夹角)设 $\vec{a}=(1,2,3)$,$\vec{b}=(-1,1,1)$,求 $\vec{a}\cdot\vec{b}$ 和夹角 $\theta$。

**解**:$\vec{a}\cdot\vec{b}=-1+2+3=4$。$|\vec{a}|=\sqrt{14}$,$|\vec{b}|=\sqrt{3}$。
$$\cos\theta=\frac{4}{\sqrt{14}\cdot\sqrt{3}}=\frac{4}{\sqrt{42}}\approx 0.617,\quad\theta\approx 51.9°.$$
::end

::ex
**例 2**(向量投影)将 $\vec{a}=(3,4,0)$ 投影到 $\vec{b}=(1,0,0)$ 方向上。

**解**:$\vec{a}\cdot\vec{b}=3$,$|\vec{b}|^2=1$,所以向量投影 $=\frac{3}{1}\vec{b}=(3,0,0)$,正好是 $\vec{a}$ 的 $x$ 分量——投影到 $x$ 轴方向时,几何意义就是「丢掉 $y$、$z$ 分量」。
::end

::ex
**例 3**(余弦相似度)在词嵌入中,词向量 $\vec{u}=(0.8,0.6,0)$(「国王」)与 $\vec{v}=(0.7,0.5,0.2)$(「王子」)的相似度为
$$\cos\theta=\frac{\vec{u}\cdot\vec{v}}{|\vec{u}|\,|\vec{v}|}=\frac{0.86}{1\cdot\sqrt{0.78}}\approx 0.974.$$
非常接近 $1$,语义相近。这就是 word2vec / GloVe / BERT 比较语义距离的核心运算。
::end

::pitfall
**易错点**:
- 点乘**结果是数**不是向量,$(\vec{a}\cdot\vec{b})\vec{c}$ 才是向量;别写 $\vec{a}\cdot\vec{b}\cdot\vec{c}$,因为 $(\vec{a}\cdot\vec{b})$ 已是数,跟 $\vec{c}$ 用数乘符号是 $(\vec{a}\cdot\vec{b})\vec{c}$,跟 $\vec{c}$ 再点乘是 $((\vec{a}\cdot\vec{b}))(\vec{c}\cdot ?)$ 没有第二个向量,无意义。
- 点乘**没有结合律**:$(\vec{a}\cdot\vec{b})\vec{c}\neq\vec{a}(\vec{b}\cdot\vec{c})$。前者沿 $\vec{c}$ 方向,后者沿 $\vec{a}$ 方向,一般不同向。
- $\vec{a}\cdot\vec{b}=0$ **不**能推出 $\vec{a}=\vec{0}$ 或 $\vec{b}=\vec{0}$,因为可能两者**互相垂直**。
::end

### 8.2.2 向量积(叉乘)

::def
**向量积**(vector product / cross product)$\vec{a}\times\vec{b}$ 定义为满足下列三条的**新向量**:
1. **模**:$|\vec{a}\times\vec{b}|=|\vec{a}|\,|\vec{b}|\sin\theta$,其中 $\theta\in[0,\pi]$ 为夹角;
2. **方向**:与 $\vec{a},\vec{b}$ 同时垂直,且 $\{\vec{a},\vec{b},\vec{a}\times\vec{b}\}$ 构成**右手系**;
3. 若 $\vec{a}\parallel\vec{b}$(含零向量)则 $\vec{a}\times\vec{b}=\vec{0}$。
::end

::intuition
模等于 $\vec{a},\vec{b}$ 张成的**平行四边形面积**(底 $|\vec{a}|$、高 $|\vec{b}|\sin\theta$);方向用右手——四指从 $\vec{a}$ 经小角度转向 $\vec{b}$,拇指指向 $\vec{a}\times\vec{b}$。叉乘是「方向化的面积」。
::end

::svg
<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" style="background:#fff">
  <defs>
    <marker id="ah3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1a365d"/></marker>
    <marker id="ah4" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#8b3a0a"/></marker>
    <marker id="ah5" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2d6e2d"/></marker>
  </defs>
  <polygon points="60,160 220,160 280,60 120,60" fill="#fef6e4" stroke="#c9a227" stroke-width="1.5"/>
  <line x1="60" y1="160" x2="220" y2="160" stroke="#1a365d" stroke-width="2.5" marker-end="url(#ah3)"/>
  <text x="225" y="178" fill="#1a365d" font-size="14" font-style="italic">a</text>
  <line x1="60" y1="160" x2="120" y2="60" stroke="#8b3a0a" stroke-width="2.5" marker-end="url(#ah4)"/>
  <text x="100" y="55" fill="#8b3a0a" font-size="14" font-style="italic">b</text>
  <line x1="140" y1="110" x2="140" y2="30" stroke="#2d6e2d" stroke-width="2.5" marker-end="url(#ah5)"/>
  <text x="148" y="40" fill="#2d6e2d" font-size="14" font-style="italic">a × b</text>
  <text x="135" y="120" fill="#8b6f1c" font-size="12">面积</text>
</svg>
<figcaption>图 8.2.2 $\vec{a}\times\vec{b}$ 的模等于平行四边形面积,方向由右手定则定。</figcaption>
::endsvg

::thm
(坐标公式)设 $\vec{a}=(a_1,a_2,a_3)$,$\vec{b}=(b_1,b_2,b_3)$,则
$$\vec{a}\times\vec{b}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix}=(a_2b_3-a_3b_2)\vec{i}-(a_1b_3-a_3b_1)\vec{j}+(a_1b_2-a_2b_1)\vec{k}.$$
::end

::proof
(思路)在标准正交基 $\{\vec{i},\vec{j},\vec{k}\}$ 上验证 $\vec{i}\times\vec{j}=\vec{k}$,$\vec{j}\times\vec{k}=\vec{i}$,$\vec{k}\times\vec{i}=\vec{j}$(由几何定义直接得:模为 $1$、方向由右手定则)。再由叉乘对加法、数乘的双线性(由定义验证,从略),展开 $\vec{a}=a_1\vec{i}+a_2\vec{j}+a_3\vec{k}$,$\vec{b}=b_1\vec{i}+b_2\vec{j}+b_3\vec{k}$ 的乘积并合并同类项即得行列式公式。
::end

**运算律**:
1. **反对称**:$\vec{a}\times\vec{b}=-\vec{b}\times\vec{a}$
2. **双线性**:$(\lambda\vec{a}+\mu\vec{a}')\times\vec{b}=\lambda(\vec{a}\times\vec{b})+\mu(\vec{a}'\times\vec{b})$
3. **自零**:$\vec{a}\times\vec{a}=\vec{0}$(由反对称推出)
4. **Jacobi 恒等式**:$\vec{a}\times(\vec{b}\times\vec{c})+\vec{b}\times(\vec{c}\times\vec{a})+\vec{c}\times(\vec{a}\times\vec{b})=\vec{0}$

::thm
(BAC-CAB / 二重向量积展开)
$$\vec{a}\times(\vec{b}\times\vec{c})=\vec{b}(\vec{a}\cdot\vec{c})-\vec{c}(\vec{a}\cdot\vec{b}).$$
::end

::proof
按坐标展开两边,逐分量比对——是纯计算证明,详尽过程见附录 §A.1。一个不依赖坐标的证法:固定 $\vec{b},\vec{c}$ 不共线,$\vec{a}\times(\vec{b}\times\vec{c})$ 与 $\vec{b}\times\vec{c}$ 垂直,故落在 $\vec{b},\vec{c}$ 张成的平面里,写成 $\alpha\vec{b}+\beta\vec{c}$;再令 $\vec{a}=\vec{b}$ 与 $\vec{a}=\vec{c}$ 反代定出 $\alpha=\vec{a}\cdot\vec{c}$、$\beta=-\vec{a}\cdot\vec{b}$。
::end

::thm
(Lagrange 恒等式)
$$|\vec{a}\times\vec{b}|^2+(\vec{a}\cdot\vec{b})^2=|\vec{a}|^2|\vec{b}|^2.$$
::end

::proof
左边 $=|\vec{a}|^2|\vec{b}|^2\sin^2\theta+|\vec{a}|^2|\vec{b}|^2\cos^2\theta=|\vec{a}|^2|\vec{b}|^2(\sin^2\theta+\cos^2\theta)=|\vec{a}|^2|\vec{b}|^2$。证毕。
::end

这条恒等式把点乘与叉乘绑在一起:它实际上是 Cauchy-Schwarz 不等式的「等式版本加上一个非负余项 $|\vec{a}\times\vec{b}|^2$」。

::ex
**例 4**(平面法向量)求过三点 $A(1,0,0)$,$B(0,1,0)$,$C(0,0,1)$ 的平面法向量与三角形面积。

**解**:$\vec{AB}=(-1,1,0)$,$\vec{AC}=(-1,0,1)$。
$$\vec{AB}\times\vec{AC}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&1&0\\-1&0&1\end{vmatrix}=(1\cdot 1-0\cdot 0)\vec{i}-((-1)\cdot 1-0\cdot(-1))\vec{j}+((-1)\cdot 0-1\cdot(-1))\vec{k}=(1,1,1).$$
法向量 $\vec{n}=(1,1,1)$。三角形面积 $S=\tfrac12|\vec{AB}\times\vec{AC}|=\tfrac{\sqrt{3}}{2}$。
::end

::ex
**例 5**(力矩)杠杆从原点伸到 $\vec{r}=(2,0,0)$,在末端施加 $\vec{F}=(0,3,0)$ 的力,求力矩 $\vec{M}=\vec{r}\times\vec{F}$。

**解**:$\vec{M}=(0\cdot 0-0\cdot 3,\,0\cdot 0-2\cdot 0,\,2\cdot 3-0\cdot 0)=(0,0,6)$,方向沿 $+z$,大小 $6\,\mathrm{N\cdot m}$。这正是物理学里「力矩 $=$ 力臂 $\times$ 力」的向量定义。
::end

::pitfall
**易错点**:
- 叉乘**不可交换**:$\vec{a}\times\vec{b}=-\vec{b}\times\vec{a}$,顺序写错符号反掉。
- 叉乘**不结合**:$(\vec{a}\times\vec{b})\times\vec{c}\neq\vec{a}\times(\vec{b}\times\vec{c})$。可用 BAC-CAB 验证差一项。
- $\vec{a}\times\vec{b}=\vec{0}$ **不**意味着 $\vec{a}=\vec{0}$ 或 $\vec{b}=\vec{0}$,可能 $\vec{a}\parallel\vec{b}$。
- 叉乘**只在 $\mathbb{R}^3$ 里有**(以及不太常用的 $\mathbb{R}^7$);$\mathbb{R}^2$、$\mathbb{R}^4$ 没有标准叉乘。高维"叉乘"要用外代数 $\wedge$ 推广。
::end

### 8.2.3 混合积

::def
三个向量 $\vec{a},\vec{b},\vec{c}\in\mathbb{R}^3$ 的**混合积**(三重积)记作 $[\vec{a},\vec{b},\vec{c}]$,定义为
$$[\vec{a},\vec{b},\vec{c}]=(\vec{a}\times\vec{b})\cdot\vec{c}.$$
::end

::thm
(行列式表达 / 几何意义)
$$[\vec{a},\vec{b},\vec{c}]=\begin{vmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{vmatrix},$$
其绝对值等于以 $\vec{a},\vec{b},\vec{c}$ 为棱的平行六面体体积;符号给出右手系/左手系定向。
::end

::proof
代入叉乘的行列式公式与点积的坐标式,逐项展开即得三阶行列式;这是一行计算。
**几何部分**:$\vec{a}\times\vec{b}$ 模为底面面积,方向垂直底面。$\vec{c}$ 与底面法向夹角 $\varphi$,则 $(\vec{a}\times\vec{b})\cdot\vec{c}=|\vec{a}\times\vec{b}|\,|\vec{c}|\cos\varphi$。而 $|\vec{c}|\cos\varphi$ 正是 $\vec{c}$ 在法向上的有向投影 $=$ 平行六面体的高。所以
$$|[\vec{a},\vec{b},\vec{c}]|=\text{底面积}\times\text{高}=\text{体积}.$$
::end

混合积有**轮换不变性**:$[\vec{a},\vec{b},\vec{c}]=[\vec{b},\vec{c},\vec{a}]=[\vec{c},\vec{a},\vec{b}]$;**对换变号**:$[\vec{a},\vec{c},\vec{b}]=-[\vec{a},\vec{b},\vec{c}]$。这两条对应行列式的行轮换 / 行对换性质。

**核心推论**:
- **三向量共面** $\iff [\vec{a},\vec{b},\vec{c}]=0$
- **四面体体积**:以 $A,B,C,D$ 为顶点的四面体体积 $V=\tfrac16|[\vec{AB},\vec{AC},\vec{AD}]|$

::ex
**例 6**(判共面)判断 $\vec{a}=(1,1,0)$,$\vec{b}=(0,1,1)$,$\vec{c}=(1,0,-1)$ 是否共面。

**解**:
$$[\vec{a},\vec{b},\vec{c}]=\begin{vmatrix}1&1&0\\ 0&1&1\\ 1&0&-1\end{vmatrix}=1\cdot(1\cdot(-1)-1\cdot 0)-1\cdot(0\cdot(-1)-1\cdot 1)+0=-1+1=0.$$
共面。
::end

::ex
**例 7**(四面体体积)求顶点 $A(0,0,0)$,$B(2,0,0)$,$C(0,3,0)$,$D(0,0,5)$ 的四面体体积。

**解**:$\vec{AB}=(2,0,0)$,$\vec{AC}=(0,3,0)$,$\vec{AD}=(0,0,5)$。混合积 $=2\cdot 3\cdot 5=30$。$V=\tfrac{30}{6}=5$。
::end

### 8.2.4 三件套总览

| 运算 | 输入 | 输出 | 几何意义 | 主要应用 |
| --- | --- | --- | --- | --- |
| $\vec{a}\cdot\vec{b}$ | 两向量 | **标量** | 投影 $\times$ 长度 | 夹角 / 投影 / 相似度 / 功 |
| $\vec{a}\times\vec{b}$ | 两向量 | **向量** | 带向的平行四边形面积 | 法向 / 面积 / 力矩 / 角动量 |
| $[\vec{a},\vec{b},\vec{c}]$ | 三向量 | **标量** | 带号的平行六面体体积 | 共面判定 / 四面体体积 / 行列式 |

后续的偏导、方向导数(§9)、Gauss/Stokes 公式(§11)都会反复用到这套语言——尤其是「梯度 $\cdot$ 切向 $=$ 方向导数」、「磁场 $=$ $\nabla\times\vec{A}$」、「散度 $=$ $\nabla\cdot\vec{F}$」都直接套用本节代数。

---

