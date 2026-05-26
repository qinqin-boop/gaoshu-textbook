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


def md_to_html(md):
    out = []
    lines = md.split("\n")
    in_p = False
    in_ul = False
    for line in lines:
        line = line.rstrip()
        if not line.strip():
            if in_p:
                out.append("</p>")
                in_p = False
            if in_ul:
                out.append("</ul>")
                in_ul = False
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            if in_p:
                out.append("</p>")
                in_p = False
            if in_ul:
                out.append("</ul>")
                in_ul = False
            level = len(m.group(1))
            content = format_inline(m.group(2))
            out.append(f"<h{level}>{content}</h{level}>")
            continue
        if line.startswith("> "):
            if in_p:
                out.append("</p>")
                in_p = False
            out.append(f"<blockquote>{format_inline(line[2:])}</blockquote>")
            continue
        if re.match(r"^[-*]\s", line):
            if in_p:
                out.append("</p>")
                in_p = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{format_inline(line[2:])}</li>")
            continue
        m2 = re.match(r"^(\d+)\.\s+(.+)$", line)
        if m2:
            if in_p:
                out.append("</p>")
                in_p = False
            if not in_ul:
                out.append("<ol>")
                in_ul = True
            out.append(f"<li>{format_inline(m2.group(2))}</li>")
            continue
        if in_ul:
            out.append("</ul>" if "<ul>" in "".join(out[-5:]) else "</ol>")
            in_ul = False
        if not in_p:
            out.append("<p>")
            in_p = True
        out.append(format_inline(line))
    if in_p:
        out.append("</p>")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


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
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title_text)} · 高数下册教材</title>
<link rel="stylesheet" href="./style.css">
</head>
<body>
<header>
  <h1>📘 高数下册教材</h1>
  <p class="tagline">{escape(title_text)}</p>
  <nav><a href="./index.html">← 章节列表</a></nav>
</header>
<main class="textbook">
{html_body}
</main>
<footer>
  <p>富贵 (AI 助理) 编 · 同济大学《高等数学》第七版下册 · 零基础类比+例题</p>
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
    toc_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>高数下册教材 (富贵编)</title>
<link rel="stylesheet" href="./style.css">
</head>
<body>
<header>
  <h1>📘 高数下册教材 (富贵编)</h1>
  <p class="tagline">同济大学《高等数学》第七版下册 · 5 章完整版 · 零基础类比+例题</p>
</header>
<main class="textbook-toc">
<h2>📖 章节列表</h2>
<ul class="ch-list">
"""
    for t in toc:
        toc_html += f'<li><a href="./{t["slug"]}.html">{escape(t["title"])}</a> <span class="meta">({t["chars"]:,} 字符)</span></li>\n'
    toc_html += """</ul>
<h2>💡 这本教材怎么用</h2>
<ul>
<li>每节按 <strong>"想干啥 → 生活类比 → 公式推理 → 例题"</strong> 顺序读</li>
<li>对照同济大学《高等数学》第七版下册官方教材, 内容覆盖向量代数/多元函数微分/重积分/曲线曲面积分/无穷级数</li>
<li>零基础友好, 用做饭/开车/身体/钱等生活类比替代抽象定义</li>
<li>每个公式给推理过程, 不直接抛公式</li>
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
