from html.parser import HTMLParser
import re

FILE_PATH = r"D:\Git\rockghost.github.io\src\Try it out 2.html"

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content):,} bytes")

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip_tags = {'script', 'style', 'code', 'pre', 'kbd', 'svg', 'math'}
        self.skip_stack = []
        self.texts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip_stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.skip_tags and self.skip_stack and self.skip_stack[-1] == tag:
            self.skip_stack.pop()

    def handle_data(self, data):
        if self.skip_stack:
            return
        stripped = data.strip()
        if not stripped:
            return
        if 'base64' in stripped or stripped.startswith('data:'):
            return
        # Skip purely numeric/symbol strings
        if re.match(r'^[\d\s.,\-+\[\]()\{\}<>=;:!?@#$%^&*/\\\'\"_~`|]+$', stripped):
            return
        if stripped.startswith('http') or stripped.startswith('www.'):
            return
        self.texts.append(stripped)

extractor = TextExtractor()
extractor.feed(content)

seen = set()
unique_texts = []
for t in extractor.texts:
    if t not in seen:
        seen.add(t)
        unique_texts.append(t)

print(f"Found {len(unique_texts)} unique text nodes:")
for i, t in enumerate(unique_texts):
    print(f"[{i:3d}] {repr(t[:120])}")
