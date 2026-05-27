import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """第五波: ch10 10.2 二重 + 10.3 三重积分深度版 push (commit 52a1250):
https://gaoshu-textbook-z699.vercel.app/chapter10-multiple-integrals.html#10-2

10.2 二重积分加:
- X-型/Y-型区域 SVG + Fubini 切片直觉证
- 交换次序破解 ∫∫ e^{x²} 经典例
- 极坐标雅可比 r 的扇环几何来源 + 行列式两种证 + 极坐标网格 SVG
- Gauss 积分 ∫e^{-x²}dx=√π 二重极坐标完整推 (正态分布归一化 1/√(2π) 来源)
- 一般换元公式 + 椭圆面积 πab 例

10.3 三重积分加:
- 先一后二 / 先二后一 对比 + 球 4πR³/3 体积例
- 柱坐标 r dr dθ dz 推导 + 圆锥例
- 球坐标 ρ²sinφ 完整行列式展开证 + 球坐标 (ρ,φ,θ) SVG
- ∭ρ² 球内积分 4πR⁵/5 例
- Newton 球壳定理积分证: 均匀球外引力 = 集中球心 (-GM/d) — 电磁学等效点电荷同源
- 坐标选择口诀表 + 4 条易错点

本会话累计 6 节深度模板 push:
1) ch8 8.2 数量积/向量积/混合积
2) ch9 9.6 方向导数+梯度+Descent Lemma
3) ch9 9.8 Hessian+凸优化+Newton
4) ch11 11.3 Green
5) ch10 10.2 二重积分 (Gauss积分+Fubini+极坐标)
6) ch10 10.3 三重积分 (柱/球坐标雅可比完整证+Newton 球壳定理)

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
