#!/usr/bin/env python3
"""Convert HTML lesson files into an EPUB ebook."""

import os, zipfile, uuid, html
from pathlib import Path

BASE = Path(__file__).parent

# Ordered chapters (matches index.html sidebar)
CHAPTERS = [
    ("What is a coding assistant？.html", "What is a coding assistant?"),
    ("Claude Code in action.html", "Claude Code in action"),
    ("Claude Code setup.html", "Claude Code setup"),
    ("Project setup.html", "Project setup"),
    ("Adding context.html", "Adding context"),
    ("Making changes.html", "Making changes"),
    ("Controlling context.html", "Controlling context"),
    ("Custom commands.html", "Custom commands"),
    ("MCP servers with Claude Code.html", "MCP servers with Claude Code"),
    ("Github integration.html", "Github integration"),
    ("Introducing hooks.html", "Introducing hooks"),
    ("Defining hooks.html", "Defining hooks"),
    ("Implementing a hook.html", "Implementing a hook"),
    ("Gotchas around hooks.html", "Gotchas around hooks"),
    ("Useful hooks!.html", "Useful hooks!"),
    ("Another useful hook.html", "Another useful hook"),
    ("The Claude Code SDK.html", "The Claude Code SDK"),
]

SECTIONS = {
    0: "What is Claude Code?",
    2: "Getting hands on",
    10: "Hooks and the SDK",
}

book_id = str(uuid.uuid4())
out_path = BASE / "Claude_Code_in_Action.epub"

def make_chapter_id(i):
    return f"ch{i:02d}"

def build_manifest_items():
    items = []
    for i, (fname, title) in enumerate(CHAPTERS):
        cid = make_chapter_id(i)
        items.append(f'    <item id="{cid}" href="{cid}.xhtml" media-type="application/xhtml+xml"/>')
    return "\n".join(items)

def build_spine():
    refs = []
    for i in range(len(CHAPTERS)):
        refs.append(f'    <itemref idref="{make_chapter_id(i)}"/>')
    return "\n".join(refs)

def build_toc_ncx():
    points = []
    order = 1
    for i, (fname, title) in enumerate(CHAPTERS):
        cid = make_chapter_id(i)
        points.append(f"""    <navPoint id="nav-{cid}" playOrder="{order}">
      <navLabel><text>{html.escape(title)}</text></navLabel>
      <content src="{cid}.xhtml"/>
    </navPoint>""")
        order += 1
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{book_id}"/>
  </head>
  <docTitle><text>Claude Code in Action</text></docTitle>
  <navMap>
{chr(10).join(points)}
  </navMap>
</ncx>"""

def build_nav_xhtml():
    items = []
    for i, (fname, title) in enumerate(CHAPTERS):
        cid = make_chapter_id(i)
        items.append(f'      <li><a href="{cid}.xhtml">{html.escape(title)}</a></li>')
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Table of Contents</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>목차</h1>
    <ol>
{chr(10).join(items)}
    </ol>
  </nav>
</body>
</html>"""

def wrap_chapter(raw_html, title):
    """Keep the full HTML body content but wrap in XHTML envelope."""
    # Try to extract <body> content; if no body tag, use the whole thing
    import re
    body_match = re.search(r'<body[^>]*>(.*)</body>', raw_html, re.DOTALL | re.IGNORECASE)
    if body_match:
        body = body_match.group(1)
    else:
        body = raw_html

    # Extract <style> blocks from <head>
    styles = re.findall(r'<style[^>]*>.*?</style>', raw_html, re.DOTALL | re.IGNORECASE)
    style_block = "\n".join(styles) if styles else ""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8"/>
  <title>{html.escape(title)}</title>
  {style_block}
</head>
<body>
  <h1 style="font-size:1.5em; margin-bottom:1em;">{html.escape(title)}</h1>
  {body}
</body>
</html>"""

print("Building EPUB...")
with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    # mimetype must be first and uncompressed
    zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)

    # META-INF/container.xml
    zf.writestr("META-INF/container.xml", """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""")

    # content.opf
    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{book_id}</dc:identifier>
    <dc:title>Claude Code in Action</dc:title>
    <dc:language>ko</dc:language>
    <dc:creator>Anthropic Academy</dc:creator>
    <meta property="dcterms:modified">2026-03-10T00:00:00Z</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
{build_manifest_items()}
  </manifest>
  <spine toc="ncx">
{build_spine()}
  </spine>
</package>"""
    zf.writestr("OEBPS/content.opf", opf)
    zf.writestr("OEBPS/toc.ncx", build_toc_ncx())
    zf.writestr("OEBPS/nav.xhtml", build_nav_xhtml())

    # Chapters
    for i, (fname, title) in enumerate(CHAPTERS):
        src = BASE / fname
        if not src.exists():
            print(f"  SKIP (not found): {fname}")
            continue
        print(f"  Adding: {fname} ({src.stat().st_size // 1024} KB)")
        raw = src.read_text(encoding="utf-8", errors="replace")
        xhtml = wrap_chapter(raw, title)
        zf.writestr(f"OEBPS/{make_chapter_id(i)}.xhtml", xhtml)

size_mb = out_path.stat().st_size / (1024 * 1024)
print(f"\nDone! {out_path.name} ({size_mb:.1f} MB)")
