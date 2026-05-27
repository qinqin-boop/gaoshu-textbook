import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """第七波: ch11 11.6 Stokes 公式完整证 push (被 cron 24c1944 包进去 — 工作树 clean):
https://gaoshu-textbook-z699.vercel.app/chapter11-line-surface-integrals.html#11-6

加:
- 旋度定义 + 小风车直觉 (转速 = curl·n)
- 曲面定向 + 右手系边界正向规则
- **Stokes 公式完整证**: 分三分量, 每个用 Green 公式 (链式法则展开 + 两类曲面积分转换), 三式相加合并
- 旋度的不依赖坐标定义: curl·n = lim 环量/面积 (微圆盘极限) — 这是 GR / 规范场论里外微分 d 的原型
- 物理: Maxwell ∇×E = -∂B/∂t → 法拉第电磁感应 ∮E·dr = -dΦ_B/dt 完整推
- 例: 单位圆环流 2π 直接+Stokes 双验证 / 三角形顶点环流 -1 / 单连通保守场判别 + (-y,x)/(x²+y²) 非单连通反例
- 微分形式统一表: ∫_∂M ω = ∫_M dω 在 5 个维度下展开 + d²=0 ↔ ∇·(∇×F)=0 / ∇×(∇φ)=0 经典恒等式

dedupe: 删了旧版重复 "11.6 斯托克斯公式" section.

本会话累计 9 节深度模板 push:
1) ch8 8.2 数量积/向量积/混合积
2) ch9 9.6 方向导数+梯度+Descent Lemma
3) ch9 9.8 Hessian+凸优化+Newton
4) ch10 10.2 二重 (Fubini+Gauss积分+极坐标)
5) ch10 10.3 三重 (球坐标雅可比+Newton 球壳定理)
6) ch11 11.3 Green
7) ch11 11.4 第一类曲面积分
8) ch11 11.5 第二类曲面积分 + Gauss
9) ch11 11.6 Stokes (完整证 + 旋度内蕴 + 微分形式统一)

ch11 三大公式 Green/Gauss/Stokes 全部带完整证明 + 物理应用 (Maxwell). cron 在持续推 ch12 (Cauchy 准则/解析延拓/FFT 等).

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
