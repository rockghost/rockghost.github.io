"""
HTML 파일의 영문 텍스트를 한국어로 번역하는 스크립트.
BeautifulSoup을 사용하지 않고 정규식으로 텍스트 노드를 추출하여 번역.

사용법: python scripts/translate_to_korean.py "src/Defining tools with MCP.html"
"""

import re
import sys
import os

# ---------------------------------------------------------------------------
# Translation dictionary — English phrase -> Korean translation
# ---------------------------------------------------------------------------
TRANSLATIONS = {
    # Page title / headings
    "Defining tools with MCP": "MCP로 도구 정의하기",
    "Overview": "개요",
    "Tool definition structure": "도구 정의 구조",
    "Tool properties": "도구 속성",
    "Input schema": "입력 스키마",
    "Tool execution flow": "도구 실행 흐름",
    "Best practices": "모범 사례",
    "Common tool patterns": "일반적인 도구 패턴",
    "Error handling": "오류 처리",
    "Testing tools": "도구 테스트",
    "Summary": "요약",
    "Next steps": "다음 단계",
    "Table of Contents": "목차",
    "Introduction": "소개",
    "Prerequisites": "사전 요구 사항",
    "Getting Started": "시작하기",
    "Examples": "예제",
    "Example": "예제",
    "Notes": "참고",
    "Note": "참고",
    "Warning": "경고",
    "Important": "중요",
    "Tip": "팁",
    "See also": "참고 항목",
    "Related": "관련 항목",
    "References": "참조",
    "Conclusion": "결론",

    # Common UI text
    "Back to top": "맨 위로",
    "Previous": "이전",
    "Next": "다음",
    "Home": "홈",
    "Search": "검색",
    "Menu": "메뉴",
    "Close": "닫기",
    "Open": "열기",
    "Submit": "제출",
    "Cancel": "취소",
    "Save": "저장",
    "Delete": "삭제",
    "Edit": "편집",
    "View": "보기",
    "Download": "다운로드",
    "Upload": "업로드",
    "Copy": "복사",
    "Paste": "붙여넣기",
    "Cut": "잘라내기",
    "Undo": "실행 취소",
    "Redo": "다시 실행",
    "Help": "도움말",
    "Settings": "설정",
    "Profile": "프로필",
    "Logout": "로그아웃",
    "Login": "로그인",
    "Sign up": "회원가입",
    "Sign in": "로그인",
    "Sign out": "로그아웃",

    # Navigation
    "Contents": "목차",
    "On this page": "이 페이지에서",
    "In this article": "이 글에서",
}

# ---------------------------------------------------------------------------
# Regex-based text extraction and replacement
# We process only visible text nodes (not inside <script>, <style>, <code>)
# ---------------------------------------------------------------------------

SKIP_TAGS = re.compile(
    r'<(script|style|code|pre|kbd|samp|var|math|svg)[^>]*>.*?</\1>',
    re.DOTALL | re.IGNORECASE
)

TAG_RE = re.compile(r'<[^>]+>')


def translate_text(text: str) -> str:
    """Apply known translations to a text segment."""
    for en, ko in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        text = text.replace(en, ko)
    return text


def process_html(content: str) -> str:
    """
    Process HTML content: skip script/style/code blocks,
    translate visible text nodes only.
    """
    # We'll rebuild the content piece by piece.
    # Strategy: split on tag boundaries, translate non-tag segments
    # but skip segments inside script/style/code/pre blocks.

    result = []
    pos = 0
    skip_depth = 0
    skip_tag_name = None

    OPEN_SKIP = re.compile(
        r'<(script|style|code|pre|kbd|samp|var)(\s[^>]*)?>', re.IGNORECASE
    )
    CLOSE_SKIP = re.compile(
        r'</(script|style|code|pre|kbd|samp|var)\s*>', re.IGNORECASE
    )
    ANY_TAG = re.compile(r'<[^>]*>', re.DOTALL)

    i = 0
    length = len(content)

    while i < length:
        # Find next tag
        m = ANY_TAG.search(content, i)
        if m is None:
            # No more tags — translate remaining text if not skipping
            segment = content[i:]
            if skip_depth == 0:
                segment = translate_text(segment)
            result.append(segment)
            break

        # Text before this tag
        text_before = content[i:m.start()]
        if text_before:
            if skip_depth == 0:
                text_before = translate_text(text_before)
            result.append(text_before)

        tag = m.group(0)

        # Check if opening skip tag
        om = OPEN_SKIP.match(tag)
        if om:
            skip_depth += 1
            skip_tag_name = om.group(1).lower()
            result.append(tag)
            i = m.end()
            continue

        # Check if closing skip tag
        cm = CLOSE_SKIP.match(tag)
        if cm:
            if skip_depth > 0:
                skip_depth -= 1
                if skip_depth == 0:
                    skip_tag_name = None
            result.append(tag)
            i = m.end()
            continue

        # Regular tag — also translate alt/title/placeholder attributes
        if skip_depth == 0:
            # Translate title="..." placeholder="..." alt="..." value="..." aria-label="..."
            def translate_attr(m2):
                attr_name = m2.group(1)
                quote = m2.group(2)
                attr_val = m2.group(3)
                translated = translate_text(attr_val)
                return f'{attr_name}={quote}{translated}{quote}'

            tag = re.sub(
                r'(title|placeholder|alt|aria-label|value)(=["\'])([^"\']*?)(["\'])',
                lambda m2: f'{m2.group(1)}={m2.group(2)}{translate_text(m2.group(3))}{m2.group(4)}',
                tag
            )

        result.append(tag)
        i = m.end()

    return ''.join(result)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_to_korean.py <html_file>")
        sys.exit(1)

    fpath = sys.argv[1]
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        sys.exit(1)

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Read {len(content)} characters from {fpath}")
    translated = process_html(content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(translated)

    print(f"Written {len(translated)} characters to {fpath}")

    # Verify
    with open(fpath, 'r', encoding='utf-8') as f:
        sample = f.read(500)
    assert '??' not in sample, 'Encoding corrupted!'
    print("OK: encoding verified")


if __name__ == '__main__':
    main()
