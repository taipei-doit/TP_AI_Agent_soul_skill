#!/usr/bin/env python3
"""把網頁與程式檔裡給人看的中文抓出來，另存成一個文字檔，供用語檢查工具檢查。

用法：
    python extract_zh_text.py 檔案或資料夾 [...] -o 輸出檔.md

只讀取指定的 .html、.htm、.js、.jsx、.ts、.tsx、.vue、.py 檔案，
其他檔案（例如 Excel、Word、資料庫）一律略過，不會讀取。
只使用 Python 標準函式庫，不連網路。
"""
import argparse
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

EXTS = {'.html', '.htm', '.js', '.jsx', '.ts', '.tsx', '.vue', '.py'}
HAS_ZH = re.compile(r'[㐀-鿿豈-﫿]')
ATTRS = {'alt', 'title', 'aria-label', 'placeholder', 'content', 'value', 'label'}
SKIP_DIRS = {'node_modules', '.git', '.venv', 'venv', '__pycache__', 'dist', 'build'}
CJK = r'[\u3000-\u303f\u3400-\u9fff\uf900-\ufaff\uff00-\uffef]'
CJK_GAP = re.compile(rf'(?<={CJK})[ \t]*\n\s*(?={CJK})')


def tidy(s):
    """兩個中文字或全形標點之間的換行直接接起來，其餘連續空白縮成一格。"""
    return ' '.join(CJK_GAP.sub('', s).split())


class HtmlText(HTMLParser):
    """收集文字節點、指定屬性與註解裡的中文，略過 script 與 style。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        for name, value in attrs:
            if name in ATTRS and value and HAS_ZH.search(value):
                self.out.append((self.getpos()[0], tidy(value)))

    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip and HAS_ZH.search(data):
            self.out.append((self.getpos()[0], tidy(data)))

    def handle_comment(self, data):
        if HAS_ZH.search(data):
            self.out.append((self.getpos()[0], tidy(data)))


def from_code(text, python=False):
    """逐字掃描程式碼，取出字串與註解裡含中文的部分。"""
    found = []
    i, n, line = 0, len(text), 1

    def add(start_line, s):
        if HAS_ZH.search(s):
            found.append((start_line, tidy(s)))

    while i < n:
        c = text[i]
        if c == '\n':
            line += 1
            i += 1
        elif not python and text.startswith('//', i) or python and c == '#':
            end = text.find('\n', i)
            end = n if end == -1 else end
            add(line, text[i + (1 if python else 2):end])
            i = end
        elif not python and text.startswith('/*', i):
            end = text.find('*/', i + 2)
            end = n if end == -1 else end
            add(line, text[i + 2:end])
            line += text.count('\n', i, end)
            i = end + 2
        elif python and (text.startswith('"""', i) or text.startswith("'''", i)):
            q = text[i:i + 3]
            end = text.find(q, i + 3)
            end = n if end == -1 else end
            add(line, text[i + 3:end])
            line += text.count('\n', i, end)
            i = end + 3
        elif c in '\'"' or (c == '`' and not python):
            start_line, j, buf = line, i + 1, []
            while j < n and text[j] != c:
                if text[j] == '\\' and j + 1 < n:
                    buf.append(text[j + 1])
                    j += 2
                    continue
                if text[j] == '\n':
                    if c != '`':
                        break
                    line += 1
                buf.append(text[j])
                j += 1
            add(start_line, ''.join(buf))
            i = j + 1
        else:
            i += 1
    return sorted(set(found))


def extract(path):
    text = path.read_text(encoding='utf-8', errors='replace')
    if path.suffix in ('.html', '.htm', '.vue'):
        parser = HtmlText()
        parser.feed(text)
        items = parser.out
        if path.suffix == '.vue':
            items += from_code(text)
        return sorted(set(items))
    return from_code(text, python=path.suffix == '.py')


def iter_files(targets):
    for t in targets:
        p = Path(t)
        if p.is_dir():
            for f in sorted(p.rglob('*')):
                if f.is_file() and f.suffix in EXTS and not SKIP_DIRS & set(f.parts):
                    yield f
        elif p.is_file() and p.suffix in EXTS:
            yield p


def main():
    ap = argparse.ArgumentParser(description='抓出網頁與程式檔裡的中文，供用語檢查')
    ap.add_argument('targets', nargs='+', help='要檢查的檔案或資料夾')
    ap.add_argument('-o', '--output', required=True, help='輸出的文字檔')
    args = ap.parse_args()

    lines, count = [], 0
    for f in iter_files(args.targets):
        items = extract(f)
        if not items:
            continue
        lines.append(f'<!-- {f} -->')
        for lineno, s in items:
            lines.append(f'{html.unescape(s)}　〔{f.name}:{lineno}〕')
            count += 1
        lines.append('')
    Path(args.output).write_text('\n'.join(lines), encoding='utf-8')
    print(f'已抓出 {count} 段中文，存在 {args.output}', file=sys.stderr)


if __name__ == '__main__':
    main()
