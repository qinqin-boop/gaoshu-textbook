"""把 chapter*.md 里的 Unicode-hack 公式批量转 KaTeX 标记.

只处理「行内 + 块外」的 hack 表达式; 已经在 $...$ / $$...$$ 里的不动.
ch8 8.2 已是新模板, 用 `## 8.2 数量积` 标题块跳过.
"""
import io, sys, re, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC_DIR = 'D:/github/wechat-decrypt/notes/textbook'

# 输入用 hack, 输出用 LaTeX. 顺序敏感(从长到短).
VEC_LETTERS = list('abcdfgnprstuvwxyzABCDFGNPRSTUVWXYZ')  # 跳过 e/i/j/k 单字母容易误伤 (i→ 是 i hat 我们保留)


def protect_existing_math(s):
    """已经在 $...$ 内的部分先 stash, 不被替换破坏."""
    stash = []
    def repl(m):
        stash.append(m.group(0))
        return f'\x00MATH{len(stash)-1}\x00'
    # block math
    s = re.sub(r'\$\$[\s\S]+?\$\$', repl, s)
    # inline math
    s = re.sub(r'\$[^\$\n]+?\$', repl, s)
    return s, stash


def restore(s, stash):
    for i, m in enumerate(stash):
        s = s.replace(f'\x00MATH{i}\x00', m)
    return s


def inject_inline(text):
    """行内变换."""
    # 1. |a→| → $|\vec a|$  (字母 + 箭头 + |)
    text = re.sub(r'\|([a-zA-Z])→\|', r'$|\\vec{\1}|$', text)
    text = re.sub(r'\|([a-zA-Z])→\|²', r'$|\\vec{\1}|^2$', text)
    # 2. AB→ / CD→ → $\vec{AB}$ (两字母 + 箭头)
    text = re.sub(r'([A-Z][A-Z])→', r'$\\vec{\1}$', text)
    # 3. 单字母 + → (向量)  e.g. a→, b→
    text = re.sub(r'(?<![\w$\\])([a-zA-Z])→', r'$\\vec{\1}$', text)
    # 4. 0→ → $\vec{0}$
    text = text.replace('0→', '$\\vec{0}$')
    # 5. i→ j→ k→ standard basis (已被上面规则吃了, ok)
    # 6. cosθ / sinθ / tanθ → $\cos\theta$
    text = re.sub(r'cos\s*θ', r'$\\cos\\theta$', text)
    text = re.sub(r'sin\s*θ', r'$\\sin\\theta$', text)
    text = re.sub(r'tan\s*θ', r'$\\tan\\theta$', text)
    text = re.sub(r'\bθ\b', r'$\\theta$', text)
    text = re.sub(r'\bφ\b', r'$\\varphi$', text)
    text = re.sub(r'\bα\b', r'$\\alpha$', text)
    text = re.sub(r'\bβ\b', r'$\\beta$', text)
    text = re.sub(r'\bγ\b', r'$\\gamma$', text)
    text = re.sub(r'\bλ\b', r'$\\lambda$', text)
    text = re.sub(r'\bμ\b', r'$\\mu$', text)
    text = re.sub(r'\bπ\b', r'$\\pi$', text)
    text = re.sub(r'\bΩ\b', r'$\\Omega$', text)
    text = re.sub(r'\b∞\b', r'$\\infty$', text)
    text = re.sub(r'\b∇\b', r'$\\nabla$', text)
    text = re.sub(r'\b∂\b', r'$\\partial$', text)
    text = re.sub(r'\b∫\b', r'$\\int$', text)
    text = re.sub(r'\b∑\b', r'$\\sum$', text)
    text = re.sub(r'\b∪\b', r'$\\cup$', text)
    text = re.sub(r'\b∩\b', r'$\\cap$', text)
    text = re.sub(r'\b∈\b', r'$\\in$', text)
    text = re.sub(r'\b⊂\b', r'$\\subset$', text)
    text = re.sub(r'\b⊥\b', r'$\\perp$', text)
    text = re.sub(r'\b∥\b', r'$\\parallel$', text)
    text = re.sub(r'\b≤\b', r'$\\le$', text)
    text = re.sub(r'\b≥\b', r'$\\ge$', text)
    text = re.sub(r'\b≠\b', r'$\\neq$', text)
    text = re.sub(r'\b≈\b', r'$\\approx$', text)
    text = re.sub(r'\b⟺\b', r'$\\iff$', text)
    text = re.sub(r'\b⟹\b', r'$\\Rightarrow$', text)
    text = re.sub(r'\b√\b', r'$\\sqrt{}$', text)
    return text


def merge_adjacent_dollars(text):
    """把相邻的 $X$$Y$ 合并成 $XY$ 让 KaTeX 渲染更顺."""
    # 这步谨慎: 只合并紧贴(无空格)的相邻 inline math
    # $\vec{a}$ + $\cdot$ → $\vec{a}\cdot$
    for _ in range(5):
        new = re.sub(r'\$([^\$\n]+)\$\$([^\$\n]+)\$', r'$\1\2$', text)
        if new == text:
            break
        text = new
    return text


def process_file(path, skip_82=False):
    with open(path, 'r', encoding='utf-8') as f:
        raw = f.read()

    # 把整体按行处理, 但跳过已经是 KaTeX 重写过的 8.2 节
    sections = []
    cur = []
    in_skip = False
    for line in raw.split('\n'):
        if skip_82 and line.startswith('## 8.2'):
            if cur:
                sections.append(('process', cur))
                cur = []
            in_skip = True
            sections.append(('skip', [line]))
            continue
        if in_skip:
            if line.startswith('## ') and not line.startswith('## 8.2'):
                in_skip = False
                cur = [line]
                continue
            sections[-1][1].append(line)
            continue
        cur.append(line)
    if cur:
        sections.append(('process', cur))

    out = []
    for kind, lines in sections:
        if kind == 'skip':
            out.extend(lines)
            continue
        block = '\n'.join(lines)
        block, stash = protect_existing_math(block)
        block = inject_inline(block)
        block = restore(block, stash)
        block = merge_adjacent_dollars(block)
        out.append(block)
    new = '\n'.join(out)

    if new != raw:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        return True
    return False


def main():
    for fn in sorted(os.listdir(SRC_DIR)):
        if not (fn.startswith('chapter') and fn.endswith('.md')):
            continue
        path = os.path.join(SRC_DIR, fn)
        skip = (fn == 'chapter08-vectors.md')
        changed = process_file(path, skip_82=skip)
        print(f'{"CHG" if changed else "---"} {fn} (skip 8.2={skip})')


if __name__ == '__main__':
    main()
