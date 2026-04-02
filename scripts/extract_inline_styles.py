"""
src/ 디렉토리 내 HTML 파일에서 인라인 <style> 블록을 외부 CSS 파일로 추출하는 스크립트.

처리:
1. 공유 스타일 (2개 이상 파일에서 동일) → assets/shared-{n}.css
2. 페이지별 고유 스타일 → assets/css/{basename}.css (여러 블록은 하나로 합침)
3. HTML 내 <style>...</style>을 <link rel="stylesheet" href="...">로 교체
"""

import glob
import hashlib
import os
import re
import sys

STYLE_RE = re.compile(r'<style[^>]*>(.*?)</style>', flags=re.DOTALL)


def hash_css(css: str) -> str:
    """CSS 내용의 짧은 해시를 반환한다."""
    return hashlib.md5(css.strip().encode()).hexdigest()[:12]


def scan_styles(html_files: list[str]) -> dict[str, dict]:
    """모든 HTML 파일을 스캔하여 <style> 블록별 정보를 수집한다."""
    style_info = {}  # hash -> {css, files: set, order: int}
    order = 0
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        for m in STYLE_RE.finditer(content):
            css = m.group(1).strip()
            if not css:
                continue
            h = hash_css(css)
            if h not in style_info:
                style_info[h] = {'css': css, 'files': set(), 'order': order}
                order += 1
            style_info[h]['files'].add(fpath)
    return style_info


def extract_styles(src_dir: str):
    """메인 추출 로직."""
    html_files = sorted(
        f for f in glob.glob(os.path.join(src_dir, '*.html'))
        if os.path.basename(f) != 'index.html'
    )
    if not html_files:
        print(f"No HTML files found in {src_dir}/")
        return

    print(f"Found {len(html_files)} HTML file(s) in {src_dir}/")

    # 1단계: 모든 파일 스캔
    print("Scanning <style> blocks...")
    style_info = scan_styles(html_files)
    if not style_info:
        print("  No <style> blocks found.")
        return

    shared = {h: info for h, info in style_info.items() if len(info['files']) > 1}
    unique = {h: info for h, info in style_info.items() if len(info['files']) == 1}
    print(f"  Found {len(shared)} shared style(s), {len(unique)} unique style(s)")

    # 2단계: 디렉토리 생성
    assets_dir = os.path.join(src_dir, 'assets')
    css_dir = os.path.join(assets_dir, 'css')
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(css_dir, exist_ok=True)

    # 3단계: CSS 파일 저장 & 해시→경로 매핑
    path_map = {}  # hash -> relative path

    # 공유 스타일 → assets/shared-{n}.css
    for idx, (h, info) in enumerate(
        sorted(shared.items(), key=lambda x: x[1]['order'])
    ):
        fname = f'shared-{idx}.css'
        fpath = os.path.join(assets_dir, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(info['css'])
        path_map[h] = f'assets/{fname}'
        size_kb = len(info['css'].encode('utf-8')) / 1024
        print(f"  [SHARED] {fname} ({size_kb:.0f}KB, in {len(info['files'])} files)")

    # 고유 스타일 → assets/css/{basename}.css (파일당 합침)
    # 먼저 파일별로 고유 블록들을 모은다
    file_unique = {}  # fpath -> [(order, css)]
    for h, info in unique.items():
        fpath = next(iter(info['files']))
        file_unique.setdefault(fpath, []).append((info['order'], h, info['css']))

    for fpath, blocks in sorted(file_unique.items()):
        blocks.sort(key=lambda x: x[0])
        basename = os.path.splitext(os.path.basename(fpath))[0]
        # 파일명에서 안전하지 않은 문자 제거
        safe_name = re.sub(r'[^\w\s-]', '', basename).strip().replace(' ', '-')
        fname = f'{safe_name}.css'
        css_path = os.path.join(css_dir, fname)
        merged_css = '\n\n'.join(css for _, _, css in blocks)
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(merged_css)
        # 각 블록의 해시를 같은 파일로 매핑
        for _, h, _ in blocks:
            path_map[h] = f'assets/css/{fname}'
        size_kb = len(merged_css.encode('utf-8')) / 1024
        print(f"  [UNIQUE] css/{fname} ({size_kb:.0f}KB)")

    # 4단계: HTML 내 <style> 블록을 <link>로 교체
    print("\nReplacing <style> blocks in HTML files...")
    total_saved = 0

    for fpath in html_files:
        basename = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        original_len = len(content)

        seen_links = set()  # 이미 삽입한 <link> 경로 (중복 방지)

        def replace_style(m: re.Match) -> str:
            css = m.group(1).strip()
            if not css:
                return ''
            h = hash_css(css)
            if h in path_map:
                href = path_map[h]
                if href in seen_links:
                    return ''  # 이미 삽입됨 — 중복 블록 제거
                seen_links.add(href)
                return f'<link rel="stylesheet" href="{href}">'
            return m.group(0)  # 매핑 없으면 원본 유지

        new_content = STYLE_RE.sub(replace_style, content)

        if len(new_content) != original_len:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            saved_kb = (original_len - len(new_content)) / 1024
            total_saved += saved_kb
            print(f"  [UPDATED] {basename} (-{saved_kb:.0f}KB)")
        else:
            print(f"  [SKIP]    {basename}")

    print(f"\nDone: {len(path_map)} style(s) extracted, {total_saved:.0f}KB total saved.")


def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else 'src'
    extract_styles(src_dir)


if __name__ == '__main__':
    main()
