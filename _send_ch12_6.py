import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """第八波: ch12 12.6 Fourier 级数收敛性完整证 push (commit 8c7eeaa):
https://gaoshu-textbook-z699.vercel.app/chapter12-infinite-series.html#12-6

加:
- 三角函数系正交性完整证 (积化和差)
- 内积空间几何: L²[-π,π] 完备正交基 (函数当无穷维向量, 投影即 Fourier 系数)
- 系数公式从正交性投影推导
- **Dirichlet 收敛定理完整证**: Dirichlet 核 D_N(u) = sin((N+½)u)/sin(u/2) 闭式 + 部分和写成卷积形式 + 误差化为 Riemann-Lebesgue 引理应用 + 有界变差保证 g(u) 可积
- 间断点 → 平均值 (f(x+)+f(x-))/2 的几何意义 (核函数偶对称强行平均)
- Bessel 不等式完整证 + Parseval 恒等式 = 无穷维勾股定理
- 用 Parseval 算 Basel 问题 Σ 1/n² = π²/6 (欧拉 1735, 这是 Fourier 给出的最简证之一)
- 收敛三模式表 (逐点 vs L² vs 一致) + Gibbs 现象数学解释 (8.95% 永不消除) + Fejér 求和补救
- 物理/工程应用速览: MP3 DCT / JPEG / CT-MRI / QM 动量本征态 / 热方程分量独立衰减 / NeRF 位置编码
- Fourier 局限 (周期/时频不同时定位/FFT O(NlogN) 20 世纪 Top 10 算法)

本会话累计 10 节深度模板 push:
1) ch8 8.2 数量积/向量积/混合积
2) ch9 9.6 方向导数+梯度+Descent Lemma
3) ch9 9.8 Hessian+凸优化+Newton
4) ch10 10.2 二重 (Fubini+Gauss积分+极坐标)
5) ch10 10.3 三重 (球坐标雅可比+Newton 球壳定理)
6) ch11 11.3 Green
7) ch11 11.4 第一类曲面积分
8) ch11 11.5 第二类曲面积分 + Gauss
9) ch11 11.6 Stokes (完整证 + 旋度内蕴 + 微分形式统一)
10) ch12 12.6 Fourier (Dirichlet+Bessel+Parseval+Basel+Gibbs)

ch11 三大公式 + ch12 三大级数 (幂级数 cron 已做 + Taylor cron 已做 + Fourier 我做) 完整覆盖. ch10 二重+三重也覆盖. ch8/ch9 核心节(数量积/梯度/Hessian) 覆盖.

剩 ch8 其它节 (8.1 向量代数/8.3-8.5 平面方程) + ch9 其它节 (9.5 隐函数/9.7 几何应用/9.9 Taylor/9.10 最小二乘) — 这些 cron 在持续推 callout 化, 完整证还可以慢慢补.

Monitor 守 inbox."""

entry = {
    'id': uuid.uuid4().hex[:12],
    'room': 'wxid_kf02vaylid4x22',
    'room_name': '湫桃🐠',
    'text': text,
    'for': '',
    'created': time.strftime('%H:%M:%S'),
}
with open('D:/github/wechat-decrypt/queue/outbox.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
print('outbox appended:', entry['id'])
