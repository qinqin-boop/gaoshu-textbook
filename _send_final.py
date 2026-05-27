import json, uuid, time, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

text = """第四波: ch9 9.8 Hessian 极值判别深度版 push (commit 1001c43):
https://gaoshu-textbook-z699.vercel.app/chapter09-multivariate.html#9-8

加: Fermat 必要条件证 + x²-y² 鞍点反例 / Hessian 矩阵定义 + D=AC-B² 从二元 Taylor 配方完整推 (含 A=0 退化情形) / 特征值版本判定 (det=λ₁λ₂, tr=λ₁+λ₂) / x³-3xy+y³ 鞍点+极小判别例 / n 维 Sylvester 判据 / 凸 ⟺ Hessian 半正定 / Newton 法二次收敛 / 神经网络鞍点 >> 极小经验法则 + Adam 对角近似动机.

本会话累计深度重写 4 节 (核心模板):
1) ch8 8.2 数量积/向量积/混合积 (Cauchy-Schwarz/Lagrange/BAC-CAB)
2) ch9 9.6 方向导数+梯度 (Descent Lemma)
3) ch9 9.8 Hessian 极值 + 凸优化 + Newton
4) ch11 11.3 Green 公式 (Type I/II 证 + 复连通反例)

加基础设施 (一次性 push):
- build.py / style.css 全站排版重做 (KaTeX CDN + 侧栏 + 6 callout 模板)
- latex_inject.py 跨章批量符号化
- _splice_generic.py 通用切片插入工具

cron 自动扩 ch12 内容并未停, 我看到这小时 ch12 又被推了 8 条 commit (DFT/Cooley-Tukey/Lebesgue/Padé 等).

未完成实事:
- ch8 8.1/8.3/8.4/8.5 深度版 (老内容已有 callout 化但证明不够)
- ch9 9.7/9.9/9.10 深度版
- ch10 全部 (二重三重积分几何最需要 SVG)
- ch11 11.4 第一类曲面积分 / 11.5 第二类曲面积分 (Gauss 公式深度)
- ch12 12.6 Fourier 完整证明 (有 callout 但收敛性定理缺证)
- 宋浩 B站抽样 yt-dlp 还没开 (跟 8:00 deadline 冲突, 抽样要 2-3h)
- MemeHub 删高数下册入口 (单独任务)
- 学习总结 100 / 梗 100 / 热点 100 (这三个本会话没碰)

token budget 这会话深度内容写作差不多到顶了. 上面这些剩余项请你 (a) 起新 Claude Code 会话续做, 或 (b) 等 cron 决策循环慢慢推 (它对 ch12 这种已经在跑). 我守 inbox monitor 等你下条指令."""

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
