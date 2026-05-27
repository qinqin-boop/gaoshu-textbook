"""给每章末尾加同济高数下册风格课后习题 + 折叠答案."""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

EXERCISES = {
    'chapter08-vectors.md': """
## 课后习题(同济高数下册风格)

> 仿照同济大学《高等数学》第七版下册第八章习题精选,完整解答可点击展开。

::ex
**习题 1**(向量运算)已知 $\\vec{a}=(2,-1,3)$,$\\vec{b}=(1,2,-1)$。求:
(1) $\\vec{a}\\cdot\\vec{b}$;(2) $\\vec{a}\\times\\vec{b}$;(3) $\\vec{a}$ 与 $\\vec{b}$ 的夹角余弦;(4) $\\vec{a}$ 在 $\\vec{b}$ 方向上的投影。

**解**:
(1) $\\vec{a}\\cdot\\vec{b}=2-2-3=-3$。
(2) $\\vec{a}\\times\\vec{b}=(-1\\cdot(-1)-3\\cdot 2,\\,3\\cdot 1-2\\cdot(-1),\\,2\\cdot 2-(-1)\\cdot 1)=(-5,5,5)$。
(3) $|\\vec{a}|=\\sqrt{14}$,$|\\vec{b}|=\\sqrt 6$,$\\cos\\theta=\\frac{-3}{\\sqrt{84}}=-\\frac{\\sqrt{21}}{14}$。
(4) $\\operatorname{prj}_{\\vec{b}}\\vec{a}=\\frac{\\vec{a}\\cdot\\vec{b}}{|\\vec{b}|}=\\frac{-3}{\\sqrt 6}=-\\frac{\\sqrt 6}{2}$。
::end

::ex
**习题 2**(平面方程)求过点 $P_0(1,-2,3)$ 且与平面 $2x-y+3z=0$ 平行的平面方程。

**解**:平行平面法向相同,$\\vec{n}=(2,-1,3)$。点法式:$2(x-1)-(y+2)+3(z-3)=0$,化简 $2x-y+3z-13=0$。
::end

::ex
**习题 3**(空间直线)求过点 $(1,0,2)$ 且与直线 $\\frac{x-1}{2}=\\frac{y+1}{3}=\\frac{z}{-1}$ 平行的直线方程。

**解**:方向向量沿用 $\\vec{s}=(2,3,-1)$。对称式:$\\frac{x-1}{2}=\\frac{y}{3}=\\frac{z-2}{-1}$。
::end

::ex
**习题 4**(二次曲面)指出曲面 $x^2-y^2+z^2=4$ 是什么曲面,并描述其几何形态。

**解**:系数 $(+,-,+)$,标准型 $\\frac{x^2}{4}-\\frac{y^2}{4}+\\frac{z^2}{4}=1$ 即 $\\frac{x^2}{4}+\\frac{z^2}{4}-\\frac{y^2}{4}=1$ — **单叶双曲面**,绕 $y$ 轴旋转生成,"腰部"在 $y=0$ 处为圆 $x^2+z^2=4$。
::end

::ex
**习题 5**(点到平面距离)求点 $(2,1,-1)$ 到平面 $x+2y-2z+5=0$ 的距离。

**解**:$d=\\frac{|2+2+2+5|}{\\sqrt{1+4+4}}=\\frac{11}{3}$。
::end

""",

    'chapter09-multivariate.md': """
## 课后习题(同济高数下册风格)

> 仿同济第九章习题精选。

::ex
**习题 1**(偏导数)$z=\\sin(xy)+x^2 y$,求 $z_x,z_y,z_{xy}$。

**解**:$z_x=y\\cos(xy)+2xy$,$z_y=x\\cos(xy)+x^2$,$z_{xy}=\\cos(xy)-xy\\sin(xy)+2x$。
::end

::ex
**习题 2**(链式法则)$z=f(u,v)$,$u=x+y$,$v=xy$。求 $\\partial z/\\partial x$。

**解**:$\\partial z/\\partial x=f_u\\cdot u_x+f_v\\cdot v_x=f_u+y f_v$。
::end

::ex
**习题 3**(方向导数)$f(x,y,z)=x^2+y^2+z^2$ 在 $(1,1,1)$ 处沿 $\\vec{l}=(1,2,2)$ 方向的方向导数。

**解**:$\\nabla f=(2x,2y,2z)\\big|_{(1,1,1)}=(2,2,2)$。$|\\vec{l}|=3$,$\\vec{l}_0=(1/3,2/3,2/3)$。$\\partial f/\\partial\\vec{l}=\\nabla f\\cdot\\vec{l}_0=\\frac{2+4+4}{3}=\\frac{10}{3}$。
::end

::ex
**习题 4**(极值)求 $f(x,y)=x^3+y^3-3xy$ 的极值。

**解**:$f_x=3x^2-3y=0,f_y=3y^2-3x=0\\Rightarrow y=x^2,x=y^2\\Rightarrow (0,0),(1,1)$。Hessian:$A=6x,B=-3,C=6y$,$D=36xy-9$。
$(0,0)$:$D=-9<0$ 鞍点;$(1,1)$:$D=27>0,A=6>0$ 极小,极小值 $1+1-3=-1$。
::end

::ex
**习题 5**(条件极值 / Lagrange)在约束 $x^2+y^2=1$ 下求 $f=xy$ 的最大最小值。

**解**:$\\nabla f=\\lambda\\nabla g$:$y=2\\lambda x$,$x=2\\lambda y$。代入 $x^2+y^2=1$ 得 $x=\\pm y=\\pm\\frac{1}{\\sqrt 2}$。最大值 $f=1/2$,最小值 $f=-1/2$。
::end

::ex
**习题 6**(隐函数)由 $xyz+\\sin(x+y+z)=0$ 在 $(0,0,0)$ 邻域可解出 $z=z(x,y)$ 吗?若可,求 $\\partial z/\\partial x|_{(0,0)}$。

**解**:$F=xyz+\\sin(x+y+z)$。$F_z=xy+\\cos(x+y+z)\\big|_{(0,0,0)}=0+1=1\\neq 0$,可解。$F_x=yz+\\cos(x+y+z)\\big|_{(0,0,0)}=1$。$\\partial z/\\partial x=-F_x/F_z=-1$。
::end

""",

    'chapter10-multiple-integrals.md': """
## 课后习题(同济高数下册风格)

> 仿同济第十章习题精选。

::ex
**习题 1**(二重积分)计算 $\\iint_D xy\\,d\\sigma$,$D$:$0\\le x\\le 1,\\,0\\le y\\le x^2$。

**解**:$I=\\int_0^1\\!dx\\int_0^{x^2}xy\\,dy=\\int_0^1 x\\cdot\\frac{x^4}{2}dx=\\frac{1}{2}\\cdot\\frac{1}{6}=\\frac{1}{12}$。
::end

::ex
**习题 2**(极坐标二重)计算 $\\iint_D e^{-(x^2+y^2)}\\,d\\sigma$,$D$:$x^2+y^2\\le R^2$。

**解**:极坐标 $I=\\int_0^{2\\pi}\\!d\\theta\\int_0^R\\!e^{-r^2}r\\,dr=2\\pi\\cdot\\frac{1-e^{-R^2}}{2}=\\pi(1-e^{-R^2})$。
::end

::ex
**习题 3**(三重积分)用柱坐标算 $\\iiint_\\Omega(x^2+y^2)\\,dV$,$\\Omega$ 由 $z=x^2+y^2$ 与 $z=4$ 围成。

**解**:$\\Omega$ 在柱坐标:$0\\le\\theta\\le 2\\pi,0\\le r\\le 2,r^2\\le z\\le 4$。$I=\\int_0^{2\\pi}\\!\\!\\int_0^2\\!\\!\\int_{r^2}^4 r^2\\cdot r\\,dz\\,dr\\,d\\theta=2\\pi\\int_0^2 r^3(4-r^2)dr=2\\pi(16-\\frac{64}{6})=\\frac{32\\pi}{3}$。
::end

::ex
**习题 4**(球坐标)算 $\\iiint_\\Omega\\sqrt{x^2+y^2+z^2}\\,dV$,$\\Omega$ 为 $x^2+y^2+z^2\\le R^2$。

**解**:球坐标 $I=\\int_0^{2\\pi}\\!d\\theta\\int_0^\\pi\\!\\sin\\varphi\\,d\\varphi\\int_0^R\\!\\rho\\cdot\\rho^2 d\\rho=2\\pi\\cdot 2\\cdot\\frac{R^4}{4}=\\pi R^4$。
::end

::ex
**习题 5**(质心)均匀薄板 $D:x^2+y^2\\le 1,y\\ge 0$ 的质心。

**解**:面密度 $\\mu$ 常数,$M=\\mu\\cdot\\pi/2$。对称性 $\\bar x=0$。$\\bar y=\\frac{1}{M}\\iint y\\mu\\,d\\sigma$,极坐标 $\\int_0^\\pi\\!\\!\\int_0^1(r\\sin\\theta)r\\,dr\\,d\\theta=\\frac{1}{3}\\cdot 2=\\frac{2}{3}$。$\\bar y=\\frac{2/3}{\\pi/2}=\\frac{4}{3\\pi}$。
::end

::ex
**习题 6**(Γ 函数)算 $\\int_0^\\infty x^3 e^{-2x}dx$。

**解**:换元 $u=2x$,$dx=du/2$:$I=\\int_0^\\infty(u/2)^3 e^{-u}\\frac{du}{2}=\\frac{1}{16}\\Gamma(4)=\\frac{3!}{16}=\\frac{3}{8}$。
::end

""",

    'chapter11-line-surface-integrals.md': """
## 课后习题(同济高数下册风格)

> 仿同济第十一章习题精选。

::ex
**习题 1**(第一类曲线积分)$L:y=x^2,\\,0\\le x\\le 1$,算 $\\int_L y\\,ds$。

**解**:$ds=\\sqrt{1+4x^2}dx$。$I=\\int_0^1 x^2\\sqrt{1+4x^2}dx$。设 $u=1+4x^2,du=8x\\,dx$,数值 $\\approx 0.566$。
::end

::ex
**习题 2**(第二类曲线积分 / 用 Green)算 $\\oint_C(2x-y)dx+(x+3y)dy$,$C$ 是单位圆 $x^2+y^2=1$ 正向。

**解**:$P=2x-y,Q=x+3y$,$\\partial_x Q-\\partial_y P=1-(-1)=2$。Green:$\\oint=\\iint_D 2\\,d\\sigma=2\\pi$。
::end

::ex
**习题 3**(用 Gauss 公式)算 $\\oiint_\\Sigma\\vec{F}\\cdot d\\vec{S}$,$\\vec{F}=(x^3,y^3,z^3)$,$\\Sigma$ 为单位球外侧。

**解**:$\\nabla\\cdot\\vec{F}=3(x^2+y^2+z^2)$。球坐标 $\\iiint 3\\rho^2\\cdot\\rho^2\\sin\\varphi\\,d\\rho d\\varphi d\\theta=3\\cdot 2\\pi\\cdot 2\\cdot\\frac{1}{5}=\\frac{12\\pi}{5}$。
::end

::ex
**习题 4**(用 Stokes)$\\vec{F}=(y,z,x)$,$L$ 为三角形 $A(1,0,0)\\to B(0,1,0)\\to C(0,0,1)\\to A$,求 $\\oint_L\\vec{F}\\cdot d\\vec{r}$。

**解**:$\\nabla\\times\\vec{F}=(\\partial_y x-\\partial_z z,\\,\\partial_z y-\\partial_x x,\\,\\partial_x z-\\partial_y y)=(-1,-1,-1)$。三角形所在平面 $x+y+z=1$,法向 $\\vec{n}=(1,1,1)/\\sqrt 3$,面积 $\\sqrt 3/2$。$\\oint=(\\nabla\\times\\vec{F})\\cdot\\vec{n}\\cdot S=(-3/\\sqrt 3)\\cdot(\\sqrt 3/2)=-3/2$。
::end

::ex
**习题 5**(曲面面积)算锥面 $z=\\sqrt{x^2+y^2}$($0\\le z\\le 1$)侧面积。

**解**:$z_x=x/r,z_y=y/r$,$\\sqrt{1+z_x^2+z_y^2}=\\sqrt 2$。$S=\\iint_{r\\le 1}\\sqrt 2\\,d\\sigma=\\sqrt 2\\pi$。
::end

::ex
**习题 6**(保守场判别)$\\vec{F}=(2xy+z^2,\\,x^2-3,\\,2xz)$ 是否保守?若是,求势函数。

**解**:$\\nabla\\times\\vec{F}=(\\partial_y(2xz)-\\partial_z(x^2-3),\\partial_z(2xy+z^2)-\\partial_x(2xz),\\partial_x(x^2-3)-\\partial_y(2xy+z^2))=(0,2z-2z,2x-2x)=\\vec{0}$。保守。$\\phi$:$\\partial\\phi/\\partial x=2xy+z^2\\Rightarrow\\phi=x^2y+xz^2+g(y,z)$;$\\partial\\phi/\\partial y=x^2+g_y=x^2-3\\Rightarrow g=-3y+h(z)$;$\\partial\\phi/\\partial z=2xz+h'(z)=2xz\\Rightarrow h=$常数。所以 $\\phi=x^2y+xz^2-3y+C$。
::end

""",

    'chapter12-infinite-series.md': """
## 课后习题(同济高数下册风格)

> 仿同济第十二章习题精选。

::ex
**习题 1**(数项级数判敛)判别 $\\sum_{n=1}^\\infty\\frac{n!}{n^n}$ 的敛散性。

**解**:比值 $\\rho=\\lim\\frac{(n+1)!/(n+1)^{n+1}}{n!/n^n}=\\lim\\frac{n^n}{(n+1)^n}=\\lim(1+1/n)^{-n}=1/e<1$。收敛。
::end

::ex
**习题 2**(交错级数)判别 $\\sum_{n=1}^\\infty\\frac{(-1)^{n-1}}{\\sqrt n}$ 是绝对收敛 / 条件收敛 / 发散?

**解**:$|u_n|=1/\\sqrt n$,$\\sum 1/\\sqrt n$ 是 $p$-级数 $p=1/2<1$ 发散。但 $1/\\sqrt n\\downarrow 0$,Leibniz 收敛。结论:**条件收敛**。
::end

::ex
**习题 3**(收敛半径)求 $\\sum_{n=1}^\\infty\\frac{x^n}{n\\cdot 2^n}$ 的收敛半径与收敛区间。

**解**:$R=\\lim\\frac{|a_n|}{|a_{n+1}|}=\\lim\\frac{(n+1)2^{n+1}}{n\\cdot 2^n}=2$。端点 $x=2$:$\\sum 1/n$ 发散;$x=-2$:$\\sum(-1)^n/n$ Leibniz 收敛。收敛区间 $[-2,2)$。
::end

::ex
**习题 4**(Taylor 展开)求 $f(x)=\\ln(1+x)$ 的 Maclaurin 展开式与收敛区间。

**解**:$f'(x)=1/(1+x)=\\sum(-1)^n x^n$($|x|<1$),逐项积分 $f(x)=\\sum_{n=0}^\\infty\\frac{(-1)^n x^{n+1}}{n+1}=x-\\frac{x^2}{2}+\\frac{x^3}{3}-\\dots$。$R=1$;端点 $x=1$ Leibniz 收敛,$x=-1$ 调和发散。收敛区间 $(-1,1]$。
::end

::ex
**习题 5**(Fourier 系数)$f(x)=x,\\,x\\in[-\\pi,\\pi]$ 周期延拓后,求 Fourier 系数 $a_n,b_n$。

**解**:$f$ 奇函数,$a_n=0$。$b_n=\\frac{1}{\\pi}\\int_{-\\pi}^\\pi x\\sin nx\\,dx=\\frac{2}{\\pi}\\int_0^\\pi x\\sin nx\\,dx$。分部积分 $=\\frac{2}{\\pi}\\big[-\\frac{x\\cos nx}{n}+\\frac{\\sin nx}{n^2}\\big]_0^\\pi=\\frac{2(-1)^{n+1}}{n}$。即 $b_n=\\frac{2(-1)^{n+1}}{n}$。
::end

::ex
**习题 6**(Parseval 应用)由 $f(x)=x$ 的 Fourier 展开 $\\sum b_n^2=\\sum\\frac{4}{n^2}$,用 Parseval 求 $\\sum 1/n^2$。

**解**:Parseval $\\sum b_n^2=\\frac{1}{\\pi}\\int_{-\\pi}^\\pi x^2 dx=\\frac{2\\pi^2}{3}$。所以 $\\sum\\frac{4}{n^2}=\\frac{2\\pi^2}{3}\\Rightarrow\\sum\\frac{1}{n^2}=\\frac{\\pi^2}{6}$(Basel 问题答案)。
::end

""",
}

for fname, body in EXERCISES.items():
    path = f'D:/github/wechat-decrypt/notes/textbook/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 在"## 第X章 小结"之前插入,如果没有就在末尾追加
    if '课后习题' in content:
        print(f'SKIP {fname}: 已含课后习题')
        continue
    summary_match = re.search(r'^## 第.{1,3}章 小结', content, re.MULTILINE)
    if summary_match:
        idx = summary_match.start()
        new_content = content[:idx] + body.strip() + '\n\n' + content[idx:]
    else:
        new_content = content.rstrip() + '\n\n' + body.strip() + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'OK  {fname}')
