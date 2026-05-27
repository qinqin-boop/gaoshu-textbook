import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """第六波: ch11 11.4 第一类曲面积分 + 11.5 第二类曲面积分 + Gauss 公式深度版 push (commit 5df57cf):
https://gaoshu-textbook-z699.vercel.app/chapter11-line-surface-integrals.html#11-4

11.4 加:
- dS 显式公式 √(1+z_x²+z_y²) 切平面 cos α 投影几何证 + 切平面倾斜 SVG
- 参数化 dS = |r_u × r_v| du dv 平行四边形面积证 + 两种参数化等价性
- 半球面 2πR² / 球参数化 r_φ × r_θ = R²sinφ / 锥面 √2π 例

11.5 加:
- 双侧 (可定向) vs 单侧 (Möbius/Klein) 区分
- 通量定义 + 投影公式 ± 号几何来源
- Gauss 公式完整证 (Type I-z 区域三分量 + 上盖下底+铅直面)
- 单位球通量 4π / 反算 V = ∮z dxdy / 立方体 (x²,y²,z²) 通量 3 例
- Gauss 电场定理 Φ_E = Q_enc/ε₀ (Maxwell 第一条) 物理证
- 三大公式统一: ∫_∂M ω = ∫_M dω 广义 Stokes / 4 种维度对应 / de Rham 上同调连接

本会话累计 8 节深度模板 push:
1) ch8 8.2 数量积/向量积/混合积
2) ch9 9.6 方向导数+梯度+Descent Lemma
3) ch9 9.8 Hessian+凸优化+Newton
4) ch10 10.2 二重 (Fubini+Gauss积分+极坐标)
5) ch10 10.3 三重 (球坐标雅可比+Newton 球壳定理)
6) ch11 11.3 Green
7) ch11 11.4 第一类曲面积分
8) ch11 11.5 第二类曲面积分 + Gauss

ch11 还差 11.6 Stokes 深度证 (前次会话已 callout 化, 但 Stokes 完整证还要补). cron 在持续推 ch12.

Monitor 守 inbox 等下条指令."""

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
