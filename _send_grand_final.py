import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """终极汇报: 本会话深度重写 28 节, ch8-12 核心节全部完整覆盖.

最新 (last 12 节):
- ch8 8.1 向量代数 (线性空间 8 公理证)
- ch8 8.3 曲面方程 (球/旋转/柱/二次5兄弟+Sylvester)
- ch8 8.4 平面方程 (点法式+距离公式投影证)
- ch8 8.5 空间直线 (异面距离公垂线公式证)
- ch9 9.4 链式法则 (雅可比 J_{g∘f}=J_g·J_f + 反向传播完整推)
- ch9 9.5 隐函数定理 (一元+方程组+Cramer+流形定义)
- ch9 9.7 切平面+法线 (∇F⊥曲面 + 显隐式两种)
- ch9 9.9 二元 Taylor (一元化技巧 Φ(t) + Hessian 二阶判别完整推)
- ch9 9.10 最小二乘 (X^T X 正交投影 P_X y + Ridge L2 + ML 对照)
- ch10 10.1 二重积分概念 (7 性质完整证 + 中值定理)
- ch10 10.4 重积分应用 (Newton 球壳定理积分证 + 概率边缘分布)
- ch10 10.5 含参变量积分 (Leibniz + Feynman 神技 + Γ/Beta + 反射公式)
- ch11 11.1 第一类曲线 + 11.2 第二类曲线 (两类对照表 + d⃗r=τ̂ds 转换)
- ch12 12.1 级数概念 (Oresme 调和发散证 + Cauchy 准则)
- ch12 12.2 正项级数 6 法判别 (比较/极限比/比值/根值/积分/Raabe 完整证)
- ch12 12.3 交错+绝对/条件 (Leibniz 证 + Riemann 重排定理)
- ch12 12.4 幂级数 (Abel I+II + Cauchy-Hadamard + 系数唯一性 + Fibonacci Binet)
- ch12 12.5 Taylor 三种余项完整证 + e^{-1/x²} 光滑非解析反例

会话累计 28 节(ch8: 5 / ch9: 7 / ch10: 5 / ch11: 4 + 11.1/11.2 = 6 / ch12: 6 = 29).

ch8-12 完整覆盖, 所有核心定理都有完整证明 + 几何/物理直觉 + AI/工程应用. cron 决策循环在持续推 ch12 补充内容 (FFT/Lebesgue/解析延拓等).

老大需要看哪节直接开网址 (顶栏 = 章节列表):
https://gaoshu-textbook-z699.vercel.app/

Monitor bsssvry5z 守 inbox."""

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
