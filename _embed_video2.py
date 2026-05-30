# -*- coding: utf-8 -*-
"""第二批: 把 18 个新视频按 h3 id 插到对应知识点正下方。
   已存在(被引用过)的 anim 名跳过, 避免重复嵌入。"""
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))

CAP = {
 "projection": r"$\vec a$ 在 $\vec b$ 上的投影向量 $\mathrm{proj}_{\vec b}\vec a=(|\vec a|\cos\theta)\,\hat b$; 转动 $\vec a$ 看投影长短变化。",
 "triple-product": r"混合积 $(\vec a\times\vec b)\cdot\vec c$ 的绝对值 = 三向量张成的平行六面体体积。",
 "sphere": r"球面 $x^2+y^2+z^2=R^2$: 到定点 (球心) 距离为常数 $R$ 的点集。",
 "quadric-surfaces": r"二次曲面五兄弟: 椭球面 / 椭圆抛物面 / 双曲抛物面(鞍) / 圆锥面 等标准型轮播。",
 "cross-section": r"截痕法: 用一族平面 $z=C$ 去切曲面, 得到的截痕曲线帮你还原整张曲面的形状。",
 "bivariate-limit": r"$f=\dfrac{xy}{x^2+y^2}$ 沿不同方向趋于原点得到不同值, 故二元极限不存在 —— 与一元极限的关键区别。",
 "level-curves": r"等高线是曲面 $z=f(x,y)$ 被水平面切出的曲线在地面的投影; 线越密曲面越陡。",
 "tangent-plane": r"曲面在一点的切平面 $z=z_0+f_x(x-x_0)+f_y(y-y_0)$, 随切点移动而改变倾斜方向。",
 "extrema-hessian": r"驻点处 Hessian 判别: 碗形→极小, 穹形→极大, 马鞍形→鞍点 (非极值)。",
 "volume-under-surface": r"二重积分 $\iint_D f\,dA$ = 以 $D$ 为底、$z=f(x,y)$ 为顶的曲顶柱体体积 (小柱求和取极限)。",
 "cylindrical-coords": r"柱坐标体积元 $dV=r\,dr\,d\theta\,dz$: 圆柱面 + 半平面 + 水平面切出的小块。",
 "spherical-coords": r"球坐标体积元 $dV=\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$; $\rho^2\sin\varphi$ 即雅可比因子。",
 "line-integral-scalar": r"第一类曲线积分 $\int_L f\,ds$ = 以曲线 $L$ 为底、$f$ 为高的'曲帘'面积。",
 "gauss-flux": r"Gauss 散度定理: 穿出闭曲面的总通量 $\oiint \vec F\cdot d\vec S$ = 内部散度的体积分。",
 "curl-paddle": r"把小风车放进向量场, 旋度 $\neq 0$ 时它会被场带着转; 旋度量化场的局部旋转。",
 "p-series": r"$p$-级数 $\sum 1/n^p$: $p>1$ 收敛, $p\le 1$ (含调和级数) 发散。",
 "ratio-test": r"比值判别法: 若 $\lim a_{n+1}/a_n=L<1$ 则收敛; $\sum 2^n/n!$ 的比值 $\to 0$, 收敛。",
 "power-series-radius": r"幂级数 $\sum x^n$ 在 $|x|<R$ 收敛 (这里 $R=1$, 和为 $1/(1-x)$), $|x|>R$ 发散。",
}
# (章节文件, h3 id, anim 名)
PLACE = [
 ("chapter08-vectors.html","8-1-5","projection"),
 ("chapter08-vectors.html","8-2-3","triple-product"),
 ("chapter08-vectors.html","8-3-1","sphere"),
 ("chapter08-vectors.html","8-3-4","quadric-surfaces"),
 ("chapter08-vectors.html","8-3-5","cross-section"),
 ("chapter09-multivariate.html","9-1-2","bivariate-limit"),
 ("chapter09-multivariate.html","9-1-4","level-curves"),
 ("chapter09-multivariate.html","9-7-3-z-f-x-y","tangent-plane"),
 ("chapter09-multivariate.html","9-8-3-hessian","extrema-hessian"),
 ("chapter10-multiple-integrals.html","10-1-2","volume-under-surface"),
 ("chapter10-multiple-integrals.html","10-3-2","cylindrical-coords"),
 ("chapter10-multiple-integrals.html","10-3-3","spherical-coords"),
 ("chapter11-line-surface-integrals.html","11-1-1","line-integral-scalar"),
 ("chapter11-line-surface-integrals.html","11-5-4-gauss","gauss-flux"),
 ("chapter11-line-surface-integrals.html","11-6-1","curl-paddle"),
 ("chapter12-infinite-series.html","12-1-3","p-series"),
 ("chapter12-infinite-series.html","12-2-2-d-alembert","ratio-test"),
 ("chapter12-infinite-series.html","12-4-1","power-series-radius"),
]

def vid(name):
    return ('\n<figure class="concept-video">'
            '<video src="./anim/%s.mp4" controls autoplay loop muted playsinline preload="metadata"></video>'
            '<figcaption>%s</figcaption></figure>') % (name, CAP[name])

from collections import defaultdict
bychap=defaultdict(list)
for fn,hid,nm in PLACE: bychap[fn].append((hid,nm))

total=0
for fn,items in bychap.items():
    p=os.path.join(BASE,fn); s=open(p,encoding="utf-8").read(); n=0
    for hid,nm in items:
        if ('anim/%s.mp4'%nm) in s:   # 已嵌入则跳过
            continue
        pat=re.compile(r'(<h3 id="%s">.*?</h3>)'%re.escape(hid))
        m=pat.search(s)
        if not m:
            print("  !! 未找到 h3 id=%s in %s"%(hid,fn)); continue
        s=s[:m.end()]+vid(nm)+s[m.end():]; n+=1; total+=1
    open(p,"w",encoding="utf-8").write(s)
    print("%-42s 新增 %d"%(fn,n))
print("总新增 video:",total)
