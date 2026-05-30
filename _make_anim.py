# -*- coding: utf-8 -*-
"""生成 13 个概念动画 mp4 -> anim/  (libx264 + yuv420p, 浏览器 <video> 可播)"""
import os, math, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

matplotlib.rcParams["animation.ffmpeg_path"] = shutil.which("ffmpeg")
matplotlib.rcParams["font.family"] = "sans-serif"
matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "SimSun"]
matplotlib.rcParams["axes.unicode_minus"] = False

NAVY="#1a365d"; GOLD="#c9a227"; RUST="#8b3a0a"; GREEN="#2d6e2d"; ORANGE="#c2410c"; GREY="#94a3b8"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anim")
os.makedirs(OUT, exist_ok=True)
FPS = 25

def writer(): return animation.FFMpegWriter(fps=FPS, codec="libx264", bitrate=1800,
                                            extra_args=["-pix_fmt","yuv420p"])
def arrow2(ax,x1,y1,x2,y2,color,lw=2.4):
    ax.annotate("", xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0))
def save(name, fig, update, frames):
    an = animation.FuncAnimation(fig, update, frames=frames, interval=1000/FPS, blit=False)
    p = os.path.join(OUT, name+".mp4")
    an.save(p, writer=writer(), dpi=100, savefig_kwargs={"facecolor":"white"})
    plt.close(fig); print("OK", name)

# ---------- 1 向量加法 ----------
def vector_add():
    fig,ax=plt.subplots(figsize=(6,3.6)); a=np.array([3,1.2]); b=np.array([1.2,2.0]); N=100
    def up(f):
        ax.clear(); ax.set_xlim(-.5,5); ax.set_ylim(-.5,3.6); ax.axis("off")
        k=(1-math.cos(2*math.pi*f/N))/2
        ax.plot([a[0],a[0]+b[0]],[a[1],a[1]+b[1]],"--",color=GREY,lw=1)
        ax.plot([b[0],a[0]+b[0]],[b[1],a[1]+b[1]],"--",color=GREY,lw=1)
        arrow2(ax,0,0,a[0],a[1],NAVY); arrow2(ax,0,0,b[0],b[1],RUST)
        s=a*k; arrow2(ax,s[0],s[1],s[0]+b[0],s[1]+b[1],ORANGE,2)
        arrow2(ax,0,0,a[0]+b[0],a[1]+b[1],GREEN,3)
        ax.text(a[0]/2+.05,a[1]/2-.2,"a",color=NAVY,fontsize=13)
        ax.text(b[0]/2-.3,b[1]/2,"b",color=RUST,fontsize=13)
        ax.text((a[0]+b[0])/2-.1,(a[1]+b[1])/2+.15,"a+b",color=GREEN,fontsize=13)
        ax.set_title("向量加法·平行四边形法则",color=NAVY,fontsize=12)
    save("vector-add",fig,up,N)

# ---------- 2 数量积投影 ----------
def dot_product():
    fig,ax=plt.subplots(figsize=(6,3.6)); N=100; La=2.6; Lb=3.2
    def up(f):
        ax.clear(); ax.set_xlim(-3,3.6); ax.set_ylim(-.6,3); ax.axis("off")
        th=math.radians(90-80*math.cos(2*math.pi*f/N))
        arrow2(ax,0,0,Lb,0,RUST)
        ax_=La*math.cos(th); ay=La*math.sin(th)
        arrow2(ax,0,0,ax_,ay,NAVY)
        ax.plot([ax_,ax_],[ay,0],":",color=GREY,lw=1.2)
        ax.plot([0,ax_],[0,0],color=GREEN,lw=5,solid_capstyle="butt")
        ax.text(ax_+.05,ay,"a",color=NAVY,fontsize=13); ax.text(Lb+.05,.05,"b",color=RUST,fontsize=13)
        dot=La*Lb*math.cos(th)
        ax.text(-2.9,2.7,"a·b = |a||b|cosθ = %.2f"%dot,color=(ORANGE if dot<0 else NAVY),fontsize=12)
        ax.text(-2.9,-.45,"投影 |a|cosθ %s"%("< 0 (钝角)" if math.cos(th)<0 else "≥ 0"),color=GREEN,fontsize=11)
        ax.set_title("数量积·投影几何意义",color=NAVY,fontsize=12)
    save("dot-product",fig,up,N)

# ---------- 3 向量积右手定则 (3D) ----------
def cross_product():
    fig=plt.figure(figsize=(5.2,3.6)); ax=fig.add_subplot(111,projection="3d")
    a=np.array([2,0,0]); b=np.array([.6,1.7,0]); N=100
    def up(f):
        ax.clear(); ax.set_xlim(-.5,2.8); ax.set_ylim(-.5,2.3); ax.set_zlim(0,2.2)
        ax.set_box_aspect((1,1,.8)); ax.set_axis_off()
        verts=[[(0,0,0),tuple(a),tuple(a+b),tuple(b)]]
        ax.add_collection3d(Poly3DCollection(verts,facecolor=GOLD,alpha=.25,edgecolor=GOLD))
        ax.quiver(0,0,0,*a,color=NAVY,lw=2.5,arrow_length_ratio=.12)
        ax.quiver(0,0,0,*b,color=RUST,lw=2.5,arrow_length_ratio=.12)
        ax.quiver(0,0,0,0,0,1.8,color=GREEN,lw=3,arrow_length_ratio=.15)
        ax.text(*a,"a",color=NAVY); ax.text(*b,"b",color=RUST); ax.text(0,0,1.9,"a×b",color=GREEN)
        ax.view_init(elev=20,azim=f/N*360)
        ax.set_title("向量积·右手定则 (面积=|a×b|)",color=NAVY,fontsize=11)
    save("cross-product",fig,up,N)

# ---------- 4 旋转曲面 (3D) ----------
def surface_revolution():
    fig=plt.figure(figsize=(5.2,3.6)); ax=fig.add_subplot(111,projection="3d"); N=100
    zc=np.linspace(-1,1,30); prof=lambda z:0.55+0.5*z*z
    def up(f):
        ax.clear(); ax.set_axis_off(); ax.set_box_aspect((1,1,1))
        sweep=math.pi*(1-math.cos(2*math.pi*f/N))
        th=np.linspace(0,max(sweep,1e-3),40); T,Z=np.meshgrid(th,zc); R=prof(Z)
        X=R*np.cos(T); Y=R*np.sin(T)
        ax.plot_surface(X,Y,Z,color=NAVY,alpha=.35,linewidth=0,antialiased=True)
        ax.plot(prof(zc),0*zc,zc,color=NAVY,lw=2)          # 原母线
        ax.plot(prof(zc)*math.cos(sweep),prof(zc)*math.sin(sweep),zc,color=RUST,lw=2.4)
        ax.view_init(elev=18,azim=35)
        ax.set_title("旋转曲面的生成 (母线扫出)",color=NAVY,fontsize=11)
    save("surface-revolution",fig,up,N)

# ---------- 5 偏导数=切片斜率 (3D) ----------
def partial_derivative():
    fig=plt.figure(figsize=(5.2,3.6)); ax=fig.add_subplot(111,projection="3d"); N=100
    xs=np.linspace(-1.5,1.5,30); f2=lambda x,y:0.45*(x*x-y*y)
    Xg,Yg=np.meshgrid(xs,xs); Zg=f2(Xg,Yg)
    def up(f):
        ax.clear(); ax.set_axis_off(); ax.set_box_aspect((1,1,.8))
        ax.plot_surface(Xg,Yg,Zg,color=NAVY,alpha=.18,linewidth=0)
        y0=1.2*math.sin(2*math.pi*f/N); x0=0.9*math.cos(2*math.pi*f/N)
        ax.plot(xs,0*xs+y0,f2(xs,y0),color=RUST,lw=2.6)     # 切片
        m=0.9*x0; d=0.55; z0=f2(x0,y0)
        ax.plot([x0-d,x0+d],[y0,y0],[z0-m*d,z0+m*d],color=GREEN,lw=2.6)  # 切线
        ax.scatter([x0],[y0],[z0],color=GREEN,s=25)
        ax.view_init(elev=22,azim=-60)
        ax.set_title("偏导数 ∂z/∂x = 切片曲线的切线斜率",color=NAVY,fontsize=10.5)
    save("partial-derivative",fig,up,N)

# ---------- 等高线助手 ----------
def draw_ellipses(ax):
    th=np.linspace(0,2*math.pi,80)
    for c in [0.5,1,2,4,7]:
        ax.plot(2*math.sqrt(c)*np.cos(th), math.sqrt(c)*np.sin(th), color=NAVY, alpha=.28, lw=1)

# ---------- 6 梯度下降 ----------
def gradient_descent():
    fig,ax=plt.subplots(figsize=(6,3.6)); N=34; lr=.12
    def up(f):
        ax.clear(); ax.set_xlim(-5,5); ax.set_ylim(-3.2,3.2); ax.axis("off"); draw_ellipses(ax)
        steps=int((f/N)* (26+6)); px,py=3.6,2.4; xs=[px]; ys=[py]
        for i in range(min(steps,26)):
            px-=lr*(px/2)*2; py-=lr*(2*py)*2; xs.append(px); ys.append(py)
        ax.plot(xs,ys,color=NAVY,lw=1.8)
        gx,gy=px/2,2*py; n=math.hypot(gx,gy) or 1
        arrow2(ax,px,py,px-gx/n*1.1,py-gy/n*1.1,ORANGE,2.2)
        ax.scatter([px],[py],color=RUST,s=40,zorder=5)
        ax.text(px-gx/n*1.3,py-gy/n*1.3,r"$-\nabla f$",color=ORANGE,fontsize=12)
        ax.text(-4.8,2.8,"沿负梯度方向下降, 步 %d/26"%min(steps,26),color=NAVY,fontsize=11)
        ax.set_title("梯度下降·滚向谷底",color=NAVY,fontsize=12)
    save("gradient-descent",fig,up,N)

# ---------- 7 方向导数 ----------
def directional_derivative():
    fig,ax=plt.subplots(figsize=(6,3.6)); N=100; x0,y0=2.2,1.0
    gx,gy=x0/2,2*y0; gn=math.hypot(gx,gy)
    def up(f):
        ax.clear(); ax.set_xlim(-5,5.5); ax.set_ylim(-3.2,3.2); ax.axis("off"); draw_ellipses(ax)
        ang=2*math.pi*f/N; ux,uy=math.cos(ang),math.sin(ang); Dv=gx*ux+gy*uy
        arrow2(ax,x0,y0,x0+gx/gn*1.3,y0+gy/gn*1.3,ORANGE,2.6)
        arrow2(ax,x0,y0,x0+ux*1.2,y0+uy*1.2,NAVY,2.2)
        ax.scatter([x0],[y0],color=NAVY,s=30,zorder=5)
        ax.text(x0+gx/gn*1.4,y0+gy/gn*1.4,r"$\nabla f$",color=ORANGE,fontsize=12)
        ax.text(x0+ux*1.3,y0+uy*1.3,r"$\vec u$",color=NAVY,fontsize=12)
        # 数值条
        bx=4.6; ax.add_patch(plt.Rectangle((bx,-2.6),.5,5.2,color="#eee"))
        frac=max(0,Dv)/gn; ax.add_patch(plt.Rectangle((bx,-2.6),.5,frac*5.2,color=(GREEN if Dv>=0 else ORANGE)))
        ax.text(bx-1.5,2.9,r"$D_{\vec u}f=%.2f$"%Dv,color=(GREEN if Dv>=0 else ORANGE),fontsize=11)
        ax.set_title("方向导数·梯度方向最陡",color=NAVY,fontsize=12)
    save("directional-derivative",fig,up,N)

# ---------- 8 黎曼和 ----------
def riemann_sum():
    fig,ax=plt.subplots(figsize=(6,3.6)); ns=[2,4,8,16,32,64]; N=len(ns)*12
    fx=lambda x:0.55+0.32*np.sin(x*2.2)+0.18*x; xs=np.linspace(0,1,200)
    def up(f):
        ax.clear(); ax.set_xlim(-.05,1.05); ax.set_ylim(0,1.2); ax.axis("off")
        n=ns[(f//12)%len(ns)]
        for i in range(n):
            u=(i+.5)/n; h=fx(u); ax.add_patch(plt.Rectangle((i/n,0),1/n,h,
                facecolor=GREEN,alpha=.22,edgecolor=GREEN,lw=.6))
        ax.plot(xs,fx(xs),color=NAVY,lw=2.4)
        ax.text(.02,1.12,"n = %d 个小矩形"%n,color=GREEN,fontsize=12)
        ax.set_title("积分 = 黎曼和的极限",color=NAVY,fontsize=12)
    save("riemann-sum",fig,up,N)

# ---------- 9 极坐标面积元 ----------
def polar_element():
    fig,ax=plt.subplots(figsize=(6,3.6)); N=100
    def up(f):
        ax.clear(); ax.set_xlim(-1.1,1.1); ax.set_ylim(-.1,1.15); ax.axis("off"); ax.set_aspect("equal")
        for r in np.arange(.2,1.01,.2):
            t=np.linspace(0,math.pi,60); ax.plot(r*np.cos(t),r*np.sin(t),color=GREY,lw=.8)
        for a in np.arange(0,math.pi+.01,math.pi/8):
            ax.plot([0,math.cos(a)],[0,math.sin(a)],color=GREY,lw=.8)
        th=0.5*math.pi*(1-math.cos(2*math.pi*f/N)); dth=math.pi/8
        r=0.4+0.4*(0.5-0.5*math.cos(4*math.pi*f/N)); dr=0.18
        aa=np.linspace(th,th+dth,12)
        xs=np.concatenate([r*np.cos(aa),(r+dr)*np.cos(aa[::-1])])
        ys=np.concatenate([r*np.sin(aa),(r+dr)*np.sin(aa[::-1])])
        ax.fill(xs,ys,facecolor=GOLD,alpha=.5,edgecolor=RUST,lw=1.6)
        ax.text(-1.05,1.05,"dA = r·dr·dθ  (r=%.2f)"%r,color=RUST,fontsize=12)
        ax.set_title("极坐标面积元 (雅可比因子 r)",color=NAVY,fontsize=12)
    save("polar-element",fig,up,N)

# ---------- 10 向量场环流 ----------
def vector_field_flow():
    fig,ax=plt.subplots(figsize=(5.6,3.6)); N=100; R=1.4
    gx,gy=np.meshgrid(np.arange(-2,2.1,1),np.arange(-1.5,1.6,1))
    def up(f):
        ax.clear(); ax.set_xlim(-2.6,2.6); ax.set_ylim(-2,2); ax.axis("off"); ax.set_aspect("equal")
        ax.quiver(gx,gy,-gy,gx,color=GREY,scale=22,width=.004)
        t=np.linspace(0,2*math.pi,80); ax.plot(R*np.cos(t),R*np.sin(t),"--",color=GOLD,lw=1.4)
        ang=2*math.pi*f/N; qx,qy=R*math.cos(ang),R*math.sin(ang)
        arrow2(ax,qx,qy,qx-qy*.5,qy+qx*.5,RUST,2.2)
        arrow2(ax,qx,qy,qx-math.sin(ang)*.6,qy+math.cos(ang)*.6,NAVY,2)
        ax.scatter([qx],[qy],color=GREEN,s=45,zorder=5)
        ax.text(qx-qy*.5,qy+qx*.5,"F",color=RUST,fontsize=11)
        ax.text(-2.5,-1.9,"∮ F·dr  (旋转场 → 环流 > 0)",color=GREEN,fontsize=11)
        ax.set_title("向量场·沿路径做功",color=NAVY,fontsize=12)
    save("vector-field-flow",fig,up,N)

# ---------- 11 部分和收敛 ----------
def partial_sum():
    fig,ax=plt.subplots(figsize=(6,3.6)); Nn=12; N=Nn*8
    def up(f):
        ax.clear(); ax.set_xlim(0,Nn+1); ax.set_ylim(0,1.15); ax.axis("off")
        ax.axhline(1,ls="--",color=RUST,lw=1.4); ax.text(Nn-3,1.04,"极限 = 1",color=RUST,fontsize=11)
        shown=1+(f//8)%Nn; xs=list(range(1,shown+1)); ys=[1-1/2**n for n in xs]
        ax.plot(xs,ys,color=NAVY,lw=1.4,alpha=.5); ax.scatter(xs,ys,color=NAVY,s=22,zorder=5)
        ax.text(.3,1.08,"S%d = %.4f"%(shown,ys[-1]),color=NAVY,fontsize=12)
        ax.set_title("部分和收敛  Σ 1/2ⁿ → 1",color=NAVY,fontsize=12)
    save("partial-sum",fig,up,N)

# ---------- 12 Taylor 逼近 ----------
def taylor_approx():
    fig,ax=plt.subplots(figsize=(6,3.6)); degs=[1,3,5,7,9,11]; N=len(degs)*14
    xs=np.linspace(-6.5,6.5,400)
    def up(f):
        ax.clear(); ax.set_xlim(-6.5,6.5); ax.set_ylim(-2.2,2.2); ax.axhline(0,color=GREY,lw=.8); ax.axvline(0,color=GREY,lw=.8); ax.axis("off")
        ax.plot(xs,np.sin(xs),color=NAVY,lw=2.4)
        deg=degs[(f//14)%len(degs)]; y=np.zeros_like(xs)
        for k in range(0,deg//2+1):
            y=y+(-1)**k*xs**(2*k+1)/math.factorial(2*k+1)
        y=np.clip(y,-2.2,2.2); ax.plot(xs,y,color=RUST,lw=2.2)
        ax.text(-6.3,2,"sin x 的 Taylor 多项式  阶数 = %d"%deg,color=RUST,fontsize=11)
        ax.set_title("Taylor 多项式逐阶逼近",color=NAVY,fontsize=12)
    save("taylor-approx",fig,up,N)

# ---------- 13 Fourier 方波 ----------
def fourier_square():
    fig,ax=plt.subplots(figsize=(6,3.6)); Ns=[1,2,3,5,8,15]; N=len(Ns)*14
    xs=np.linspace(0,4*math.pi,600)
    def up(f):
        ax.clear(); ax.set_xlim(0,4*math.pi); ax.set_ylim(-1.5,1.5); ax.axhline(0,color=GREY,lw=.8); ax.axis("off")
        ax.plot(xs,np.sign(np.sin(xs)),color=GREY,lw=1.6)
        Nh=Ns[(f//14)%len(Ns)]; y=np.zeros_like(xs)
        for k in range(1,2*Nh,2): y=y+(4/math.pi)*np.sin(k*xs)/k
        ax.plot(xs,y,color=RUST,lw=2.2)
        ax.text(.2,1.35,"谐波数 = %d"%Nh,color=RUST,fontsize=12)
        ax.set_title("Fourier 级数逼近方波 (Gibbs)",color=NAVY,fontsize=12)
    save("fourier-square",fig,up,N)

if __name__=="__main__":
    # 中文字体: 尝试常见 Windows 字体, 否则标题用拼音回退由 matplotlib 处理
    for fam in ["Microsoft YaHei","SimHei","Noto Sans CJK SC"]:
        try:
            matplotlib.rcParams["font.sans-serif"]=[fam]; matplotlib.rcParams["axes.unicode_minus"]=False
            break
        except Exception: pass
    for fn in [vector_add,dot_product,cross_product,surface_revolution,partial_derivative,
               gradient_descent,directional_derivative,riemann_sum,polar_element,
               vector_field_flow,partial_sum,taylor_approx,fourier_square]:
        fn()
    print("ALL DONE ->", OUT)
