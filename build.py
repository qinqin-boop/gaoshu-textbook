"""独立网站 builder: 高数下册教材."""
import os, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC_DIR = "D:/github/wechat-decrypt/notes/textbook"
OUT_DIR = "D:/github/gaoshu-textbook"


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def format_inline(s):
    s = escape(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return s


BOX_MARKERS = {
    "::def": "box-def", "::thm": "box-thm", "::proof": "box-proof",
    "::ex": "box-example", "::intuition": "box-intuition", "::pitfall": "box-pitfall",
    "::answer": "box-answer",  # 可折叠答案/详解 (用 <details>)
}


def protect_math(s):
    """临时把 $...$ 和 $$...$$ 换成占位符避免 HTML escape 破坏 LaTeX."""
    placeholders = []
    def stash(m):
        placeholders.append(m.group(0))
        return f"\x00MATH{len(placeholders)-1}\x00"
    s = re.sub(r"\$\$[\s\S]+?\$\$", stash, s)
    s = re.sub(r"\$[^\$\n]+?\$", stash, s)
    return s, placeholders


def restore_math(s, placeholders):
    for i, m in enumerate(placeholders):
        s = s.replace(f"\x00MATH{i}\x00", m)
    return s


def format_inline_math_safe(s):
    s, ph = protect_math(s)
    s = escape(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    s = restore_math(s, ph)
    return s


def md_to_html(md):
    out = []
    lines = md.split("\n")
    in_p = False
    in_ul = False
    ul_tag = "ul"
    in_box = None
    in_fig = False
    for line in lines:
        line = line.rstrip()

        # figure block: ![alt](path "caption")
        fig_m = re.match(r"^!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)$", line)
        if fig_m:
            if in_p: out.append("</p>"); in_p = False
            if in_ul: out.append(f"</{ul_tag}>"); in_ul = False
            alt, src, cap = fig_m.group(1), fig_m.group(2), fig_m.group(3) or fig_m.group(1)
            out.append(f'<figure><img src="{escape(src)}" alt="{escape(alt)}">'
                       f'<figcaption>{escape(cap)}</figcaption></figure>')
            continue

        # inline SVG block: ::svg ... ::endsvg
        if line.strip() == "::svg":
            if in_p: out.append("</p>"); in_p = False
            out.append('<figure>')
            in_fig = True
            continue
        if line.strip() == "::endsvg":
            out.append('</figure>')
            in_fig = False
            continue
        if in_fig:
            out.append(line)
            continue

        # callout box open/close
        box_open = re.match(r"^(::def|::thm|::proof|::ex|::intuition|::pitfall|::answer)\s*(.*)$", line)
        if box_open:
            if in_p: out.append("</p>"); in_p = False
            if in_ul: out.append(f"</{ul_tag}>"); in_ul = False
            in_box = BOX_MARKERS[box_open.group(1)]
            rest = box_open.group(2).strip()
            if in_box == "box-answer":
                # 可折叠答案: 用 <details> 渲染
                summary = format_inline_math_safe(rest) if rest else "📖 点击展开答案 / 详解"
                out.append(f'<details class="box-answer"><summary>{summary}</summary>')
            else:
                out.append(f'<div class="{in_box}">')
                if rest:
                    out.append(f"<p>{format_inline_math_safe(rest)}</p>")
            continue
        # box-example 内自动把"**解**:"或"**思路**:"之后内容包成可折叠 (老大要求的"开关")
        ans_marker = re.match(r"^\*\*(解|思路|证明|证)\*\*[::]?", line)
        if in_box == "box-example" and ans_marker:
            if in_p: out.append("</p>"); in_p = False
            if in_ul: out.append(f"</{ul_tag}>"); in_ul = False
            if not getattr(md_to_html, "_in_ans", False):
                marker_name = ans_marker.group(1)
                label = "📖 点击展开答案 / 详解" if marker_name in ("解","思路") else f"🔍 点击展开{marker_name}"
                out.append(f'<details class="box-answer"><summary>{label}</summary>')
                setattr(md_to_html, "_in_ans", True)
            after = re.sub(r"^\*\*(解|思路|证明|证)\*\*[::]?\s*", "", line).strip()
            if after:
                out.append(f"<p>{format_inline_math_safe(after)}</p>")
            continue
        if line.strip() == "::end" and in_box:
            if in_p: out.append("</p>"); in_p = False
            if in_ul: out.append(f"</{ul_tag}>"); in_ul = False
            # 若 box-example 内打开了 details, 先关
            if in_box == "box-example" and getattr(md_to_html, "_in_ans", False):
                out.append("</details>")
                setattr(md_to_html, "_in_ans", False)
            if in_box == "box-answer":
                out.append("</details>")
            else:
                out.append("</div>")
            in_box = None
            continue

        if not line.strip():
            if in_p:
                out.append("</p>"); in_p = False
            if in_ul:
                out.append(f"</{ul_tag}>"); in_ul = False
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            if in_p: out.append("</p>"); in_p = False
            if in_ul: out.append(f"</{ul_tag}>"); in_ul = False
            level = len(m.group(1))
            content = format_inline_math_safe(m.group(2))
            slug = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")[:60]
            out.append(f'<h{level} id="{slug}">{content}</h{level}>')
            continue
        if line.startswith("> "):
            if in_p: out.append("</p>"); in_p = False
            out.append(f"<blockquote>{format_inline_math_safe(line[2:])}</blockquote>")
            continue
        if re.match(r"^[-*]\s", line):
            if in_p: out.append("</p>"); in_p = False
            if not in_ul:
                out.append("<ul>"); in_ul = True; ul_tag = "ul"
            out.append(f"<li>{format_inline_math_safe(line[2:])}</li>")
            continue
        m2 = re.match(r"^(\d+)\.\s+(.+)$", line)
        if m2:
            if in_p: out.append("</p>"); in_p = False
            if not in_ul:
                out.append("<ol>"); in_ul = True; ul_tag = "ol"
            out.append(f"<li>{format_inline_math_safe(m2.group(2))}</li>")
            continue
        if in_ul:
            out.append(f"</{ul_tag}>"); in_ul = False
        if not in_p:
            out.append("<p>"); in_p = True
        out.append(format_inline_math_safe(line))
    if in_p: out.append("</p>")
    if in_ul: out.append(f"</{ul_tag}>")
    if in_box: out.append("</div>")
    return "\n".join(out)


def build_toc(html):
    """从生成的 HTML 抽 h2/h3 id+text 给侧栏目录."""
    items = []
    for m in re.finditer(r'<(h[23])\s+id="([^"]+)">([^<]+)</\1>', html):
        items.append((m.group(1), m.group(2), m.group(3)))
    return items


def main():
    chapters = sorted([f for f in os.listdir(SRC_DIR) if f.startswith("chapter") and f.endswith(".md")])
    toc = []
    for ch in chapters:
        path = os.path.join(SRC_DIR, ch)
        md = open(path, encoding="utf-8").read()
        title_match = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
        title_text = title_match.group(1) if title_match else ch
        slug = ch.replace(".md", "")
        html_body = md_to_html(md)
        toc_items = build_toc(html_body)
        toc_sidebar = '<aside class="toc-sidebar"><h3>本章目录</h3><ul>'
        for level, sid, txt in toc_items:
            cls = "h2" if level == "h2" else "h3"
            toc_sidebar += f'<li><a class="{cls}" href="#{sid}">{escape(txt)}</a></li>'
        toc_sidebar += "</ul></aside>"
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title_text)} · 高数下册教材</title>
<script>
function toggleAllAnswers() {{
  var btn = document.getElementById('ans-toggle-all');
  var allDetails = document.querySelectorAll('details.box-answer');
  var anyClosed = Array.from(allDetails).some(d => !d.open);
  allDetails.forEach(d => {{ d.open = anyClosed; }});
  btn.textContent = anyClosed ? '🔽 全部收起答案' : '📖 全部展开答案';
}}
</script>
<link rel="stylesheet" href="./style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}},
            {{left: '\\\\(', right: '\\\\)', display: false}},
            {{left: '\\\\[', right: '\\\\]', display: true}}
          ],
          throwOnError: false
        }});"></script>
</head>
<body>
<header>
  <h1>高等数学 · 下册</h1>
  <p class="tagline">{escape(title_text)}</p>
  <nav>
    <a href="./index.html">← 章节列表</a>
    <button id="ans-toggle-all" onclick="toggleAllAnswers()" style="background:transparent;border:1px solid rgba(255,216,156,0.4);color:#ffd89c;padding:4px 14px;border-radius:4px;font-size:0.85rem;cursor:pointer;font-family:inherit;margin-left:8px;">📖 全部展开答案</button>
  </nav>
</header>
<div class="layout">
{toc_sidebar}
<main class="textbook">
{html_body}
</main>
</div>
<footer>
  <p>富贵 (AI 助理) 编 · 同济大学《高等数学》第七版下册 · 含证明 / 几何直觉 / 例题 / 常见误区</p>
</footer>
</body>
</html>
"""
        out_path = os.path.join(OUT_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        toc.append({"slug": slug, "title": title_text, "chars": len(md)})
        print(f"built {slug}.html ({len(html)} chars)")

    # toc index
    CH_DESCRIPTIONS = {
        "chapter08-vectors": "向量代数 / 空间直角坐标系 / 数量积叉乘混合积 / 平面方程 / 曲面方程. 工科 3D 几何与 AI embedding 的代数基础.",
        "chapter09-multivariate": "多元函数极限连续 / 偏导数 / 全微分 / 方向导数与梯度 / 多元 Taylor / 极值与 Lagrange 乘子. 优化算法 (SGD / KKT) 的理论根.",
        "chapter10-multiple-integrals": "二重积分 / 三重积分 / 柱面与球面坐标. 物理质量重心转动惯量 + 概率密度联合分布.",
        "chapter11-line-surface-integrals": "曲线积分两类 / 曲面积分两类 / Green / Gauss / Stokes 三大公式. 电磁场 Maxwell 方程组的几何形式.",
        "chapter12-infinite-series": "数项级数收敛判别 / 幂级数 / Taylor 级数 / Fourier 级数. 数值计算与信号处理的核心工具.",
    }
    toc_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>高数下册教材</title>
<link rel="stylesheet" href="./style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
</head>
<body>
<header>
  <h1>高等数学 · 下册</h1>
  <p class="tagline">同济大学《高等数学》第七版下册 · 含证明 / 几何直觉 / 例题 / 常见误区</p>
</header>
<main class="textbook-toc">
<h2>章节列表</h2>
<ul class="ch-list">
"""
    for t in toc:
        desc = CH_DESCRIPTIONS.get(t["slug"], "")
        toc_html += (f'<li><a href="./{t["slug"]}.html">{escape(t["title"])}</a>'
                     f' <span class="meta">({t["chars"]:,} 字符)</span>'
                     f'<div class="ch-desc">{escape(desc)}</div></li>\n')
    toc_html += """</ul>
<h2>编写体例</h2>
<ul>
<li>每节按 <strong>动机 → 定义 → 定理 + 证明 → 几何直觉 → 例题 → 常见误区</strong> 顺序展开</li>
<li>对照同济大学《高等数学》第七版下册官方教材, 5 章完整覆盖</li>
<li>所有公式用 KaTeX 渲染, 关键概念配图(SVG / matplotlib)</li>
<li>含工科应用 motivation: 机器人 / 计算机图形学 / AI optimization / 信号处理 / 电磁学</li>
</ul>
</main>
<footer>
  <p>富贵 (AI 助理) 编 · 2026-05</p>
</footer>
</body>
</html>
"""
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(toc_html)
    print("built index.html")


if __name__ == "__main__":
    main()
