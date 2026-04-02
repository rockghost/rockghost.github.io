"""
src/ 디렉토리 내 싱글파일 HTML에서 인라인 base64 자산(이미지, 폰트)을 외부 파일로 추출하는 스크립트.

처리:
1. 공유 자산 (폰트, favicon, 로고 등) → assets/ 디렉토리에 한 번만 저장
2. 페이지별 고유 이미지 → assets/images/ 디렉토리에 저장
3. HTML 내 data: URI를 상대 경로로 교체
"""

import base64
import glob
import hashlib
import os
import re
import sys

# MIME → 확장자 매핑
MIME_EXT = {
    'image/png': '.png',
    'image/jpeg': '.jpg',
    'image/x-icon': '.ico',
    'image/svg+xml': '.svg',
    'font/woff2': '.woff2',
    'application/font-woff': '.woff',
}

# data: URI 패턴
DATA_URI_RE = re.compile(r'data:([\w/+.-]+);base64,([A-Za-z0-9+/=]+)')


def hash_b64(b64: str) -> str:
    """base64 데이터의 짧은 해시를 반환한다."""
    return hashlib.md5(b64.encode()).hexdigest()[:12]


def scan_all_files(html_files: list[str]) -> dict[str, dict]:
    """모든 HTML 파일을 스캔하여 data URI별 정보를 수집한다."""
    uri_info = {}  # hash -> {mime, b64, files: set}
    for fpath in html_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        for m in DATA_URI_RE.finditer(content):
            mime, b64 = m.group(1), m.group(2)
            h = hash_b64(b64)
            if h not in uri_info:
                uri_info[h] = {'mime': mime, 'b64': b64, 'files': set()}
            uri_info[h]['files'].add(fpath)
    return uri_info


def determine_filename(h: str, mime: str, is_shared: bool, idx_counter: dict) -> str:
    """자산의 파일명을 결정한다."""
    ext = MIME_EXT.get(mime, '.bin')

    if is_shared:
        # 공유 자산: 타입 기반 이름
        if mime == 'image/x-icon':
            return f'favicon{ext}'
        elif mime.startswith('font/') or mime.startswith('application/font'):
            idx = idx_counter.get('font', 0)
            idx_counter['font'] = idx + 1
            return f'font-{idx}{ext}'
        else:
            idx = idx_counter.get('shared_img', 0)
            idx_counter['shared_img'] = idx + 1
            return f'shared-{idx}{ext}'
    else:
        # 고유 자산: 해시 기반 이름
        return f'img-{h}{ext}'


def extract_assets(src_dir: str):
    """메인 추출 로직."""
    html_files = sorted(glob.glob(os.path.join(src_dir, '*.html')))
    if not html_files:
        print(f"No HTML files found in {src_dir}/")
        return

    print(f"Found {len(html_files)} HTML file(s) in {src_dir}/")

    # 1단계: 모든 파일 스캔
    print("Scanning data URIs...")
    uri_info = scan_all_files(html_files)
    shared = {h: info for h, info in uri_info.items() if len(info['files']) > 1}
    unique = {h: info for h, info in uri_info.items() if len(info['files']) == 1}
    print(f"  Found {len(shared)} shared assets, {len(unique)} unique assets")

    # 2단계: 디렉토리 생성
    assets_dir = os.path.join(src_dir, 'assets')
    images_dir = os.path.join(assets_dir, 'images')
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    # 3단계: 자산 파일 저장 & 경로 매핑 구축
    idx_counter = {}
    # hash -> relative path (HTML에서 사용할 경로)
    path_map = {}

    # 공유 자산 → assets/
    for h, info in sorted(shared.items(), key=lambda x: x[1]['mime']):
        fname = determine_filename(h, info['mime'], True, idx_counter)
        fpath = os.path.join(assets_dir, fname)
        raw = base64.b64decode(info['b64'])
        with open(fpath, 'wb') as f:
            f.write(raw)
        path_map[h] = f'assets/{fname}'
        size_kb = len(raw) / 1024
        print(f"  [SHARED] {fname} ({size_kb:.0f}KB, in {len(info['files'])} files)")

    # 고유 자산 → assets/images/
    for h, info in sorted(unique.items(), key=lambda x: x[1]['mime']):
        fname = determine_filename(h, info['mime'], False, idx_counter)
        fpath = os.path.join(images_dir, fname)
        raw = base64.b64decode(info['b64'])
        with open(fpath, 'wb') as f:
            f.write(raw)
        path_map[h] = f'assets/images/{fname}'
        size_kb = len(raw) / 1024
        print(f"  [UNIQUE] images/{fname} ({size_kb:.0f}KB)")

    # 4단계: HTML 내 data URI를 경로로 교체
    print("\nReplacing data URIs in HTML files...")
    total_saved = 0
    for fpath in html_files:
        basename = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        original_len = len(content)

        def replace_uri(m: re.Match) -> str:
            mime, b64 = m.group(1), m.group(2)
            h = hash_b64(b64)
            if h in path_map:
                return path_map[h]
            return m.group(0)  # 매핑 없으면 원본 유지

        new_content = DATA_URI_RE.sub(replace_uri, content)

        if len(new_content) != original_len:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            saved_kb = (original_len - len(new_content)) / 1024
            total_saved += saved_kb
            print(f"  [UPDATED] {basename} (-{saved_kb:.0f}KB)")
        else:
            print(f"  [SKIP]    {basename}")

    print(f"\nDone: {len(path_map)} assets extracted, {total_saved:.0f}KB total saved.")


def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else 'src'
    extract_assets(src_dir)


if __name__ == '__main__':
    main()
