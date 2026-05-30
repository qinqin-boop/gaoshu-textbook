# -*- coding: utf-8 -*-
"""把章节里的 <figure class="concept-anim" data-anim="X"></figure> 占位
   替换成静态 <video> (anim/X.mp4) + 说明; 并移除 concept-anim.js 脚本引用。"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
CAP = {
 "vector-add": r"把 $\vec b$ 平移到 $\vec a$ 的终点首尾相接, 得和 $\vec a+\vec b$ (绿); 它正是平行四边形的对角线。",
 "dot-product": r"$\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta$ = ($\vec a$ 在 $\vec b$ 上的投影长) × $|\vec b|$; 钝角时投影为负 → 点乘变负。",
 "cross-product": r"$\vec a\times\vec b$ 垂直于 $\vec a,\vec b$ 所在平面, 模 = 平行四边形面积 $|\vec a||\vec b|\sin\theta$, 方向由右手定则定。",
 "surface-revolution": r"一条母线绕轴旋转一周扫出旋转曲面; 每个点的轨迹是一个垂直于轴的圆 (纬圆)。",
 "partial-derivative": r"固定 $y=y_0$ 用平面切曲面得切片曲线 (红), 它在某点的切线斜率 (绿) 就是偏导数 $\partial z/\partial x$。",
 "gradient-descent": r"沿负梯度 $-\nabla f$ 方向每步下降, 逐步滚到最低点 —— SGD 等优化算法的几何原型。",
 "directional-derivative": r"方向导数 $D_{\vec u}f=\nabla f\cdot\vec u$; $\vec u$ 与梯度 $\nabla f$ 同向时最大, 垂直时为 0。",
 "riemann-sum": r"小矩形求和逼近曲边面积, 分得越细越准; 二重积分把这一思想推广到平面区域上的小块求和。",
 "polar-element": r"极坐标下小块是扇环, 面积 $dA=r\,dr\,d\theta$; 离原点越远块越大 —— 这就是雅可比因子 $r$。",
 "vector-field-flow": r"质点沿曲线移动, 每步累加 $\vec F\cdot d\vec r$ (力在位移上的投影), 总和即曲线积分 $\oint\vec F\cdot d\vec r$。",
 "partial-sum": r"几何级数 $\sum 1/2^n=1$; 部分和 $S_n$ 随 $n$ 增大越来越接近极限线, 这就是级数收敛。",
 "taylor-approx": r"$\sin x$ 的 Taylor 多项式 (红) 随阶数升高, 在越来越宽的区间上贴合原函数 (蓝)。",
 "fourier-square": r"叠加越来越多正弦谐波逼近方波; 谐波越多越像, 跳变处的小过冲即 Gibbs 现象。",
}
FILES = ["chapter08-vectors.html","chapter09-multivariate.html","chapter10-multiple-integrals.html",
         "chapter11-line-surface-integrals.html","chapter12-infinite-series.html"]

def video_html(name):
    cap = CAP[name]
    return ('<figure class="concept-video">'
            '<video src="./anim/%s.mp4" controls autoplay loop muted playsinline preload="metadata"></video>'
            '<figcaption>%s</figcaption></figure>') % (name, cap)

ph = re.compile(r'<figure class="concept-anim" data-anim="([a-z\-]+)"></figure>')
total = 0
for fn in FILES:
    p = os.path.join(BASE, fn)
    s = open(p, encoding="utf-8").read()
    cnt = [0]
    def repl(m):
        cnt[0]+=1
        return video_html(m.group(1))
    s2 = ph.sub(repl, s)
    # 移除 concept-anim.js 引用 (改用静态视频)
    s2 = s2.replace('<script src="./concept-anim.js" defer></script>\n','')
    open(p,"w",encoding="utf-8").write(s2)
    total += cnt[0]
    print("%-42s 替换 %d 个" % (fn, cnt[0]))
print("总计替换 video:", total)
