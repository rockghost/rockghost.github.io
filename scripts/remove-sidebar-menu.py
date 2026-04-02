#!/usr/bin/env python3
"""Remove the left sidebar navigation and its CSS margin from HTML files in src/."""

import re
import sys
import glob
import os

def remove_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    name = os.path.basename(filepath)

    # 1. Remove <nav id=lp-left-nav ...> ... </nav> block (with or without quotes)
    pattern = r'\s*<nav[^>]*id=["\']?lp-left-nav["\']?[^>]*>.*?</nav>'
    new_content, count = re.subn(pattern, '', content, count=1, flags=re.DOTALL)
    if count > 0:
        content = new_content
        changed = True
        print(f"  Removed sidebar nav from: {name}")

    # 2. Remove CSS margin-left on #lp-wrapper caused by sidebar
    # Matches: body.cbp-spmenu-fixed.sj-page-lesson:not(.lesson-fullscreen) #lp-wrapper{margin-left:420px}
    margin_pattern = r'body\.cbp-spmenu-fixed\.sj-page-lesson:not\(\.lesson-fullscreen\)\s*#lp-wrapper\{margin-left:[^}]*\}'
    new_content, count2 = re.subn(margin_pattern, '', content)
    if count2 > 0:
        content = new_content
        changed = True
        print(f"  Removed sidebar margin CSS from: {name}")

    # 3. Remove CSS width/styles for #lp-left-nav
    leftnav_pattern = r'body\.cbp-spmenu-fixed\.sj-page-lesson:not\(\.lesson-fullscreen\)\s*#lp-left-nav\{[^}]*\}'
    new_content, count3 = re.subn(leftnav_pattern, '', content)
    if count3 > 0:
        content = new_content
        changed = True
        print(f"  Removed sidebar width CSS from: {name}")

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"  No sidebar found in: {name}")

def main():
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    files = [f for f in files if os.path.basename(f) != 'index.html']

    if not files:
        print("No HTML files found in src/")
        return

    print(f"Processing {len(files)} HTML files...")
    for f in files:
        remove_sidebar(f)
    print("Done.")

if __name__ == '__main__':
    main()
