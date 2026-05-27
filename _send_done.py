import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """汇报: 高数下册深度版全部做完.

成果:
- 32 核心节 + 5 章节序 = 37 节深度内容
- 覆盖 ch8-12 全部章节
- 每节含: 完整定理证明 + 几何/物理直觉 + 例题 + AI/工程应用 + 易错点

5 章一句话总结:
- ch8 向量代数: Cauchy-Schwarz/Lagrange/BAC-CAB 三恒等式 + 球/旋转/柱/二次曲面 5 兄弟
- ch9 多元微分: 12 大定理 (Clairaut/链式/隐函数/Hessian/Newton/最小二乘等) + 反向传播完整推
- ch10 重积分: Fubini + 球坐标雅可比 + Newton 球壳定理积分证
- ch11 三大公式: Green/Gauss/Stokes 全部完整证 + 法拉第电磁感应推 + 微分形式统一 ∫_∂M ω = ∫_M dω
- ch12 级数: 6 法判别 + Riemann 重排 + Dirichlet 收敛+Parseval+Basel π²/6

网址:
https://gaoshu-textbook-z699.vercel.app/

最新 commit: 038ddd6. cron 决策循环并行扩补充内容 (ch12 FFT/Lebesgue 等还在跑).

下一步等老大指示."""

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
