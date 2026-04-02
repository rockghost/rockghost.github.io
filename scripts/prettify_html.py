"""
Prettify HTML files using BeautifulSoup, then collapse inline elements
back to single lines to prevent broken rendering.

Usage: python3 scripts/prettify_html.py <directory>
"""

import glob
import os
import re
import sys

from bs4 import BeautifulSoup

INLINE_TAGS = r'(?:code|strong|em|b|i|a|span|small|sub|sup|abbr|kbd|mark|u|s)'


def collapse_inline_tags(html):
    """Collapse prettify-expanded inline tags back to single lines."""
    # Step 1: Collapse <tag>\n   content\n  </tag> to <tag>content</tag> for inline tags
    pattern = re.compile(
        r'(<' + INLINE_TAGS + r'(?:\s[^>]*)?>)\s*\n\s*(.*?)\s*\n\s*(</' + INLINE_TAGS + r'>)',
        re.DOTALL
    )
    prev = None
    while prev != html:
        prev = html
        html = pattern.sub(lambda m: m.group(1) + m.group(2).strip() + m.group(3), html)

    # Step 2: Inside block elements, collapse multi-line inline content to one line
    block_pattern = re.compile(
        r'(<(?:li|p|td|th|h[1-6])(?:\s[^>]*)?>)\s*\n(.*?)\n(\s*</(?:li|p|td|th|h[1-6])>)',
        re.DOTALL
    )

    def collapse_block(m):
        open_tag = m.group(1)
        content = m.group(2)
        close_tag = m.group(3)
        if re.search(r'<(?:div|ul|ol|table|pre|blockquote|dl|figure|section|article|nav|header|footer)', content):
            return m.group(0)
        collapsed = re.sub(r'\s*\n\s*', ' ', content).strip()
        indent = re.match(r'(\s*)', m.group(3)).group(1)
        return open_tag + '\n' + indent + ' ' + collapsed + '\n' + close_tag

    html = block_pattern.sub(collapse_block, html)
    return html


def prettify_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    pretty = soup.prettify()
    pretty = collapse_inline_tags(pretty)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(pretty)
    lines = pretty.count('\n') + 1
    print(f'  [OK] {os.path.basename(fpath)} -> {lines} lines')
    return lines


def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else 'src'
    files = [f for f in glob.glob(os.path.join(directory, '*.html'))
             if os.path.basename(f) != 'index.html']
    if not files:
        print(f'No HTML files found in {directory}/')
        return
    for fpath in sorted(files):
        prettify_file(fpath)
    print(f'Done: {len(files)} files prettified')


if __name__ == '__main__':
    main()
