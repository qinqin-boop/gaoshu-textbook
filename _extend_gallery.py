# -*- coding: utf-8 -*-
"""把 18 个新动画卡片插入 animations-gallery.html 各章网格 (插在该章最后一张已知卡片后)。"""
import os
BASE=os.path.dirname(os.path.abspath(__file__))
GAL=os.path.join(BASE,"animations-gallery.html")

# anim名 -> (标题, 说明, 链接href, 链接文字)
CARDS={
 "projection":("投影 · 投影向量",r"$\vec a$ 在 $\vec b$ 上的投影向量 $\mathrm{proj}_{\vec b}\vec a=(|\vec a|\cos\theta)\,\hat b$。","chapter08-vectors.html#8-1-5","§8.1.5 投影"),
 "triple-product":("混合积 · 平行六面体",r"$(\vec a\times\vec b)\cdot\vec c$ 的绝对值 = 三向量张成的平行六面体体积。","chapter08-vectors.html#8-2-3","§8.2.3 混合积"),
 "sphere":("球面",r"球面 $x^2+y^2+z^2=R^2$: 到球心距离为常数 $R$ 的点集。","chapter08-vectors.html#8-3-1","§8.3.1 球面方程"),
 "quadric-surfaces":("二次曲面五兄弟","椭球面 / 椭圆抛物面 / 双曲抛物面(鞍) / 圆锥面 等标准型轮播。","chapter08-vectors.html#8-3-4","§8.3.4 二次曲面"),
 "cross-section":("截痕法画曲面",r"用一族平面 $z=C$ 切曲面, 截痕曲线帮你还原整张曲面的形状。","chapter08-vectors.html#8-3-5","§8.3.5 截痕法"),
 "bivariate-limit":("二元极限 · 路径依赖",r"$f=\dfrac{xy}{x^2+y^2}$ 沿不同方向趋于原点得不同值, 极限不存在。","chapter09-multivariate.html#9-1-2","§9.1.2 二元极限"),
 "level-curves":("等高线与曲面","等高线是曲面被水平面切出的曲线在地面的投影; 线越密越陡。","chapter09-multivariate.html#9-1-4","§9.1.4 等高线"),
 "tangent-plane":("切平面",r"曲面在一点的切平面 $z=z_0+f_x(x-x_0)+f_y(y-y_0)$, 随切点移动而倾斜。","chapter09-multivariate.html#9-7-3-z-f-x-y","§9.7.3 切平面"),
 "extrema-hessian":("极值与鞍点 (Hessian)","Hessian 判别: 碗形→极小, 穹形→极大, 马鞍形→鞍点。","chapter09-multivariate.html#9-8-3-hessian","§9.8.3 Hessian 判别"),
 "volume-under-surface":("曲顶柱体 = 二重积分",r"$\iint_D f\,dA$ = 以 $D$ 为底、$z=f(x,y)$ 为顶的曲顶柱体体积。","chapter10-multiple-integrals.html#10-1-2","§10.1.2 几何意义"),
 "cylindrical-coords":("柱坐标体积元",r"$dV=r\,dr\,d\theta\,dz$: 圆柱面+半平面+水平面切出的小块。","chapter10-multiple-integrals.html#10-3-2","§10.3.2 柱坐标"),
 "spherical-coords":("球坐标体积元",r"$dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$; $\rho^2\sin\varphi$ 即雅可比因子。","chapter10-multiple-integrals.html#10-3-3","§10.3.3 球坐标"),
 "line-integral-scalar":("第一类曲线积分 (曲帘)",r"$\int_L f\,ds$ = 以曲线 $L$ 为底、$f$ 为高的'曲帘'面积。","chapter11-line-surface-integrals.html#11-1-1","§11.1.1 第一类曲线积分"),
 "gauss-flux":("Gauss 散度定理 · 通量",r"穿出闭曲面的总通量 $\oiint\vec F\cdot d\vec S$ = 内部散度的体积分。","chapter11-line-surface-integrals.html#11-5-4-gauss","§11.5.4 Gauss 公式"),
 "curl-paddle":("旋度 · 小风车","小风车放进向量场, 旋度≠0 时被场带着转; 旋度量化局部旋转。","chapter11-line-surface-integrals.html#11-6-1","§11.6.1 旋度"),
 "p-series":("p-级数判敛",r"$p$-级数 $\sum 1/n^p$: $p>1$ 收敛, $p\le 1$ (含调和级数) 发散。","chapter12-infinite-series.html#12-1-3","§12.1.3 参考级数"),
 "ratio-test":("比值判别法",r"若 $\lim a_{n+1}/a_n=L<1$ 收敛; $\sum 2^n/n!$ 比值 $\to0$ 收敛。","chapter12-infinite-series.html#12-2-2-d-alembert","§12.2.2 比值判别"),
 "power-series-radius":("幂级数收敛域",r"$\sum x^n$ 在 $|x|<R$ 收敛 ($R=1$, 和为 $1/(1-x)$), $|x|>R$ 发散。","chapter12-infinite-series.html#12-4-1","§12.4.1 收敛半径"),
}
# 每章: 在该已存在卡片(锚 src)之后插入新卡片列表
AFTER={
 "vector-add不用":None,
}
INSERT=[
 ("surface-revolution",["projection","triple-product","sphere","quadric-surfaces","cross-section"]),
 ("gradient-descent",["bivariate-limit","level-curves","tangent-plane","extrema-hessian"]),
 ("polar-element",["volume-under-surface","cylindrical-coords","spherical-coords"]),
 ("vector-field-flow",["line-integral-scalar","gauss-flux","curl-paddle"]),
 ("fourier-square",["p-series","ratio-test","power-series-radius"]),
]
def card(nm):
    t,cap,href,ltxt=CARDS[nm]
    return ('\n  <figure class="gal-card"><video src="./anim/%s.mp4" loop muted playsinline preload="metadata"></video>'
            '<div class="gc-body"><div class="gc-title">%s</div><div class="gc-cap">%s</div>'
            '<div class="gc-link"><a href="./%s">→ %s</a></div></div></figure>')%(nm,t,cap,href,ltxt)

s=open(GAL,encoding="utf-8").read()
total=0
for anchor,names in INSERT:
    if ('anim/%s.mp4'%names[0]) in s:   # 已插过
        continue
    key='src="./anim/%s.mp4"'%anchor
    i=s.find(key)
    if i<0: print("!! 锚 %s 未找到"%anchor); continue
    j=s.find("</figure>",i)+len("</figure>")
    block="".join(card(n) for n in names)
    s=s[:j]+block+s[j:]; total+=len(names)
open(GAL,"w",encoding="utf-8").write(s)
print("汇总页新增卡片:",total)
