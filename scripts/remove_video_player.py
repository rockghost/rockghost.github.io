"""
src/ 디렉토리 내 싱글파일 HTML에서 동영상 플레이어 섹션을 제거하는 스크립트.

처리 패턴:
1. YouTube iframe: <iframe srcdoc="...video-player..."></iframe> 제거
2. sjwc 비디오 패턴: <sjwc-lesson-content-item> 중 sjwc-video를 포함하는 블록만 제거
3. 일반 패턴: <div class=course-fixed-content-video> 블록 제거
4. JWPlayer CSS: 인라인 <style> 내 .jwplayer, .jw-* 셀렉터 CSS 규칙 제거
5. 빈 JWPlayer <style data-jwplayer-id=...> 태그 제거
"""

import glob
import os
import re
import sys


def remove_youtube_iframes(content: str) -> str:
    """YouTube 동영상이 포함된 <iframe srcdoc="..."> 태그를 제거한다."""
    # iframe with srcdoc containing video-player or movie_player
    # srcdoc 안에 "가 &quot;로 인코딩되어 있으므로 </iframe>으로 끝나는 것을 찾으면 됨
    pattern = re.compile(
        r'<iframe\b[^>]*\bsrcdoc="[^"]*(?:video-player|movie_player|html5-video-player)[^"]*"[^>]*>\s*</iframe>',
        re.DOTALL,
    )
    return pattern.sub('', content)


def remove_div_block(content: str, start_pos: int) -> str:
    """start_pos에서 시작하는 <div ...> 블록을 닫는 </div>까지 제거한다."""
    depth = 0
    i = start_pos
    while i < len(content):
        if content[i:i+4] == '<div':
            next_char = content[i+4:i+5]
            if next_char in (' ', '>', '\t', '\n', '\r'):
                depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return content[:start_pos] + content[i+6:]
        i += 1
    return content


def _is_jw_selector(selector: str) -> bool:
    """셀렉터가 JWPlayer 관련인지 판별한다."""
    return '.jwplayer' in selector or '.jw-' in selector


def _parse_css_rules(css: str) -> list[tuple[str, int, int]]:
    """Minified CSS에서 각 규칙의 (셀렉터, 시작위치, 끝위치)를 파싱한다."""
    rules = []
    i = 0
    length = len(css)
    while i < length:
        if css[i] in (' ', '\n', '\r', '\t'):
            i += 1
            continue

        start = i

        # @keyframes 블록
        if css[i] == '@' and ('keyframes ' in css[i:i+30]):
            depth = 0
            while i < length:
                if css[i] == '{':
                    depth += 1
                elif css[i] == '}':
                    depth -= 1
                    if depth == 0:
                        i += 1
                        selector = css[start:css.index('{', start)]
                        rules.append((selector.strip(), start, i))
                        break
                i += 1
            continue

        # @media 등 at-rule
        if css[i] == '@':
            depth = 0
            while i < length:
                if css[i] == '{':
                    depth += 1
                elif css[i] == '}':
                    depth -= 1
                    if depth == 0:
                        i += 1
                        selector = css[start:css.index('{', start)]
                        rules.append((selector.strip(), start, i))
                        break
                i += 1
            continue

        # 일반 규칙
        brace_pos = css.find('{', i)
        if brace_pos < 0:
            break
        selector = css[i:brace_pos].strip()
        depth = 1
        j = brace_pos + 1
        while j < length and depth > 0:
            if css[j] == '{':
                depth += 1
            elif css[j] == '}':
                depth -= 1
            j += 1
        rules.append((selector, start, j))
        i = j

    return rules


def remove_jwplayer_css(content: str) -> str:
    """인라인 <style> 블록에서 JWPlayer 관련 CSS 규칙을 제거한다."""

    def _clean_style_block(match: re.Match) -> str:
        style_open = match.group(1)
        css = match.group(2)
        style_close = match.group(3)

        rules = _parse_css_rules(css)
        if not rules:
            return match.group(0)

        removed = False
        for selector, start, end in reversed(rules):
            if _is_jw_selector(selector):
                css = css[:start] + css[end:]
                removed = True

        if not removed:
            return match.group(0)
        return style_open + css + style_close

    pattern = re.compile(r'(<style[^>]*>)(.*?)(</style>)', re.DOTALL)
    return pattern.sub(_clean_style_block, content)


def remove_video_player(content: str) -> tuple[str, bool]:
    """HTML content에서 동영상 플레이어를 제거한다. (변경된 content, 변경 여부) 반환."""
    original_len = len(content)

    # 패턴 1: YouTube iframe (srcdoc에 비디오 플레이어가 포함된 iframe)
    content = remove_youtube_iframes(content)

    # 패턴 2: sjwc 패턴 — sjwc-video를 포함하는 블록만 제거
    pattern_sjwc = re.compile(
        r'<sjwc-lesson-content-item\b[^>]*>.*?</sjwc-lesson-content-item>',
        re.DOTALL,
    )

    def _remove_only_video_sjwc(match: re.Match) -> str:
        block = match.group(0)
        if '<sjwc-video' in block:
            return ''
        return block

    content = pattern_sjwc.sub(_remove_only_video_sjwc, content)

    # 패턴 3: 일반 패턴 - course-fixed-content-video div 제거
    marker = 'class=course-fixed-content-video>'
    pos = content.find(marker)
    if pos < 0:
        marker = 'class="course-fixed-content-video">'
        pos = content.find(marker)
    if pos >= 0:
        div_start = content.rfind('<div', 0, pos)
        if div_start >= 0:
            content = remove_div_block(content, div_start)

    # 패턴 4: JWPlayer CSS 규칙 제거
    content = remove_jwplayer_css(content)

    # 패턴 5: 빈 JWPlayer <style> 태그 제거
    content = re.sub(r'<style\s+data-jwplayer-id=[^>]*>\s*</style>', '', content)

    changed = len(content) != original_len
    return content, changed


def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else 'src'
    html_files = glob.glob(os.path.join(src_dir, '*.html'))

    if not html_files:
        print(f"No HTML files found in {src_dir}/")
        return

    print(f"Found {len(html_files)} HTML file(s) in {src_dir}/")
    changed_count = 0

    for filepath in sorted(html_files):
        basename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, changed = remove_video_player(content)

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            saved_kb = (len(content) - len(new_content)) / 1024
            print(f"  [CLEANED] {basename} (-{saved_kb:.0f}KB)")
            changed_count += 1
        else:
            print(f"  [SKIP]    {basename} (no video player found)")

    print(f"\nDone: {changed_count}/{len(html_files)} file(s) cleaned.")


if __name__ == '__main__':
    main()
