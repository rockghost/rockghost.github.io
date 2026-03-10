"""
Bundles all HTML files into a single MHTML (.mht) file.
MHTML uses MIME multipart format with Content-Location headers
so the browser can resolve internal links between pages.
"""

import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import quopri
import base64
from datetime import datetime

DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(DIR, "Claude_Code_in_Action.mht")

# index.html first, then the rest in alphabetical order
html_files = []
others = []
for f in sorted(os.listdir(DIR)):
    if f.lower().endswith('.html'):
        if f == 'index.html':
            html_files.insert(0, f)
        else:
            others.append(f)
html_files.extend(others)

print(f"Found {len(html_files)} HTML files to bundle")

# Build MHTML manually (email lib adds unwanted headers)
boundary = "----=_NextPart_Claude_Course_Bundle"
base_url = "file:///android_asset/course/"

lines = []
lines.append("From: <Saved by Claude Code>")
lines.append(f"Subject: Claude Code in Action")
lines.append(f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S')} +0900")
lines.append("MIME-Version: 1.0")
lines.append(f'Content-Type: multipart/related; boundary="{boundary}"; type="text/html"')
lines.append("")

for i, fname in enumerate(html_files):
    filepath = os.path.join(DIR, fname)
    print(f"  [{i+1}/{len(html_files)}] Adding: {fname}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Base64 encode to handle large files with embedded images
    encoded = base64.b64encode(content.encode('utf-8')).decode('ascii')

    lines.append(f"--{boundary}")
    lines.append(f"Content-Type: text/html; charset=\"utf-8\"")
    lines.append(f"Content-Transfer-Encoding: base64")
    lines.append(f"Content-Location: {fname}")
    lines.append("")

    # Split base64 into 76-char lines per MIME spec
    for j in range(0, len(encoded), 76):
        lines.append(encoded[j:j+76])
    lines.append("")

lines.append(f"--{boundary}--")
lines.append("")

print(f"\nWriting {OUTPUT}...")
with open(OUTPUT, 'w', encoding='utf-8', newline='\r\n') as f:
    f.write('\n'.join(lines))

size_mb = os.path.getsize(OUTPUT) / (1024 * 1024)
print(f"Done! Output: {OUTPUT} ({size_mb:.1f} MB)")
