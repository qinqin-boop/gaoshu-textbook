## 9.0 整章在干啥?

一元微分 $\frac{dy}{dx}$ 描述「单变量函数」局部变化率;但**现实世界几乎所有现象都依赖多个变量**:温度依赖位置 $(x,y,z)$ 和时间 $t$,损失函数依赖神经网络的百万个参数,经济模型依赖价格 / 利率 / 货币供应。本章把"微分"扩展到多元函数:偏导(单方向)、全微分(线性主部)、方向导数 + 梯度(任意方向)、Hessian(二阶)、链式法则(复合)、隐函数定理(约束)、Taylor(高阶逼近)、极值(最优化)。这就是**所有现代优化、机器学习、物理 PDE 的微分语言**。

### 9.0.1 全章地图

```
§9.1 概念 ─→ 多元极限 + 连续 (路径敏感)
              │
§9.2 偏导 ←──┴── 偏导存在 ≠ 连续 (经典反例 xy/(x²+y²))
              │
§9.3 全微分 ←─ 可微 ⇒ 连续 + 偏导存在; 偏导连续 ⇒ 可微
              │
§9.4 链式 ←── 雅可比 J_{g∘f} = J_g · J_f (反向传播底层)
              │
§9.5 隐函数 ← 隐函数定理 + 流形定义 + 逆函数定理
              │
§9.6 方向导/梯度 ← 梯度最速上升 (Cauchy-Schwarz 证) + Descent Lemma
              │
§9.7 几何应用 ← 切平面 + 法线 (∇F ⊥ 等量面)
              │
§9.8 极值 ← Fermat + Hessian 判别 (Taylor 二阶配方推 D=AC-B²)
              │
§9.9 二元 Taylor ← 一阶 = 全微分; 二阶 = Hessian 二次型
              │
§9.10 最小二乘 ← OLS 正规方程 + 几何投影 + Ridge L2
```

### 9.0.2 核心定理速查

| 概念 | 关键定理 / 公式 | 后续应用 |
| --- | --- | --- |
| 可微 | $f$ 可微 $\Rightarrow$ 连续 + 偏导 | §9.6 方向导数前提 |
| 可微充分 | 偏导**连续** $\Rightarrow$ $f$ 可微 | 实操判别 |
| Clairaut | $f_{xy}=f_{yx}$(混合偏导连续时) | Hessian 对称 / Green 公式 |
| 方向导数 | $\partial f/\partial\vec{l}=\nabla f\cdot\vec{l}$ | 梯度下降基础 |
| 梯度方向 | $\nabla f$ 是最速上升方向 | ML 优化 / PDE |
| 链式 | $J_{g\circ f}=J_g\cdot J_f$ | 反向传播 |
| 隐函数 | $\partial F/\partial(\vec{y})$ 满秩 ⇒ 局部解出 | KKT / 流形 |
| Fermat | 极值点 $\Rightarrow\nabla f=\vec{0}$ | 极值必要 |
| Hessian | $D>0,A>0\Rightarrow$ 极小 | 极值充分 |
| Newton 法 | $\theta\gets\theta-H^{-1}\nabla f$ | 二阶优化 |
| Taylor | $f=f(\vec{x}_0)+\nabla f\cdot\vec{h}+\tfrac12\vec{h}^\top H\vec{h}+\dots$ | 高阶近似 |
| 最小二乘 | $\hat\beta=(X^\top X)^{-1}X^\top\vec{y}$ | 线性回归 |

### 9.0.3 学这章的意义

- **优化算法**:梯度下降 / Newton / Adam / Lagrange 乘子全建立在本章上;
- **机器学习**:神经网络反向传播 = 链式法则;损失景观 = 多元函数图;
- **物理 PDE**:Maxwell / N-S / Heat 方程的"算子"$\nabla$、$\nabla^2$ 在本章定义;
- **经济 / 工程**:Hessian 矩阵在比较静态分析、稳定性判别中无处不在;
- **微分几何**:本章 + §11 三大公式是微分流形(Riemann / Symplectic)、广义相对论的入门。

---

