#!/usr/bin/env python3
import sys

filepath = 'src/The STDIO transport.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<title>The STDIO transport</title>', '<title>STDIO \uc804\uc1a1</title>'),
    ('<h2 id=header-links-navigation class="hide sf-hidden">Header Navigation</h2>',
     '<h2 id=header-links-navigation class="hide sf-hidden">\ud5e4\ub354 \ub0b4\ube44\uac8c\uc774\uc158</h2>'),
    ('Anthropic Academy', 'Anthropic \uc544\uce74\ub370\ubbf8'),
    ('aria-label=Lessons', 'aria-label=\uac15\uc758\ubaa9\ub85d'),
    ('alt="Go home"', 'alt="\ud648\uc73c\ub85c \uc774\ub3d9"'),
    ('aria-label="Open menu"', 'aria-label="\uba54\ub274 \uc5f4\uae30"'),
    ('aria-label="User settings menu"', 'aria-label="\uc0ac\uc6a9\uc790 \uc124\uc815 \uba54\ub274"'),
    ('<span>My Profile</span>', '<span>\ub0b4 \ud504\ub85c\ud544</span>'),
    ('Sign Out', '\ub85c\uadf8\uc544\uc6c3'),
    ('<h2>The STDIO transport</h2>', '<h2>STDIO \uc804\uc1a1</h2>'),
    ('<span>Open in Claude</span>', '<span>Claude\uc5d0\uc11c \uc5f4\uae30</span>'),
    ('Ask questions about this course', '\uc774 \uac15\uc88c\uc5d0 \ub300\ud574 \uc9c8\ubb38\ud558\uae30'),
    ('Copy notes', '\ub178\ud2b8 \ubcf5\uc0ac'),
    ('Copy full course notes for LLMs', 'LLM\uc6a9 \uc804\uccb4 \uac15\uc88c \ub178\ud2b8 \ubcf5\uc0ac'),
    ('aria-label="Toggle fullscreen"', 'aria-label="\uc804\uccb4\ud654\uba74 \uc804\ud658"'),
    ('<span>Previous</span>', '<span>\uc774\uc804</span>'),
    ('<span>Next</span>', '<span>\ub2e4\uc74c</span>'),
    ('<h4 class=sj-text-downloads><span>Downloads</span></h4>', '<h4 class=sj-text-downloads><span>\ub2e4\uc6b4\ub85c\ub4dc</span></h4>'),
]

# Line-based replacements for content
line_replacements = {
    179: ('Open in Claude', 'Claude\uc5d0\uc11c \uc5f4\uae30'),
    70: ('Courses', '\uac15\uc88c'),
}

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

lines = content.split('\n')
for lineno, (old, new) in line_replacements.items():
    if lineno - 1 < len(lines) and old in lines[lineno - 1]:
        lines[lineno - 1] = lines[lineno - 1].replace(old, new)
        count += 1

# Content paragraphs - line-based replacement
para_replacements = [
    (227, "MCP clients and servers communicate by exchanging JSON messages, but how do these messages actually get transmitted? The communication channel used is called a <strong>transport</strong>, and there are several ways to implement this",
     "MCP \ud074\ub77c\uc774\uc5b8\ud2b8\uc640 \uc11c\ubc84\ub294 JSON \uba54\uc2dc\uc9c0\ub97c \uad50\ud658\ud558\uc5ec \ud1b5\uc2e0\ud558\uc9c0\ub9cc, \uc774 \uba54\uc2dc\uc9c0\ub4e4\uc740 \uc2e4\uc81c\ub85c \uc5b4\ub5bb\uac8c \uc804\uc1a1\ub420\uae4c\uc694? \uc0ac\uc6a9\ub418\ub294 \ud1b5\uc2e0 \ucc44\ub110\uc744 <strong>\uc804\uc1a1(transport)</strong>\uc774\ub77c\uace0 \ud558\uba70, \uc774\ub97c \uad6c\ud604\ud558\ub294 \uc5ec\ub7ec \ubc29\ubc95\uc774 \uc788\uc2b5\ub2c8\ub2e4"),
    (228, '<h2>The Stdio Transport</h2>', '<h2>Stdio \uc804\uc1a1</h2>'),
    (229, "When you're first developing an MCP server or client, the most commonly used transport is the <strong>stdio transport</strong>. This approach is straightforward: the client launches the MCP server as a subprocess and communicates through standard input and output streams.",
     "MCP \uc11c\ubc84\ub098 \ud074\ub77c\uc774\uc5b8\ud2b8\ub97c \ucc98\uc74c \uac1c\ubc1c\ud560 \ub54c \uac00\uc7a5 \ub9ce\uc774 \uc0ac\uc6a9\ub418\ub294 \uc804\uc1a1\uc740 <strong>stdio \uc804\uc1a1</strong>\uc785\ub2c8\ub2e4. \uc774 \ubc29\uc2dd\uc740 \uac04\ub2e8\ud569\ub2c8\ub2e4: \ud074\ub77c\uc774\uc5b8\ud2b8\uac00 MCP \uc11c\ubc84\ub97c \ud558\uc704 \ud504\ub85c\uc138\uc2a4\ub85c \uc2e4\ud589\ud558\uace0 \ud45c\uc900 \uc785\ucd9c\ub825 \uc2a4\ud2b8\ub9bc\uc744 \ud1b5\ud574 \ud1b5\uc2e0\ud569\ub2c8\ub2e4."),
    (231, "Here's how it works:", "\uc791\ub3d9 \ubc29\uc2dd\uc740 \ub2e4\uc74c\uacfc \uac19\uc2b5\ub2c8\ub2e4:"),
    (233, "Client sends messages to the server using the server's <code>stdin</code>",
     "\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uc11c\ubc84\uc758 <code>stdin</code>\uc744 \uc0ac\uc6a9\ud558\uc5ec \uc11c\ubc84\uc5d0 \uba54\uc2dc\uc9c0\ub97c \ubcf4\ub0c5\ub2c8\ub2e4"),
    (234, "Server responds by writing to <code>stdout</code>",
     "\uc11c\ubc84\uac00 <code>stdout</code>\uc5d0 \uc791\uc131\ud558\uc5ec \uc751\ub2f5\ud569\ub2c8\ub2e4"),
    (235, "Either the server or client can send a message at any time",
     "\uc11c\ubc84\ub098 \ud074\ub77c\uc774\uc5b8\ud2b8 \uc5b4\ub290 \ucabd\uc774\ub4e0 \uc5b8\uc81c\ub4e0\uc9c0 \uba54\uc2dc\uc9c0\ub97c \ubcf4\ub0bc \uc218 \uc788\uc2b5\ub2c8\ub2e4"),
    (236, "Only works when client and server run on the same machine",
     "\ud074\ub77c\uc774\uc5b8\ud2b8\uc640 \uc11c\ubc84\uac00 \uac19\uc740 \uba38\uc2e0\uc5d0\uc11c \uc2e4\ud589\ub420 \ub54c\ub9cc \uc791\ub3d9\ud569\ub2c8\ub2e4"),
    (238, '<h2>Seeing Stdio in Action</h2>', '<h2>Stdio \ub3d9\uc791 \ud655\uc778</h2>'),
    (239, "You can actually test an MCP server directly from your terminal without writing a separate client.",
     "\ubcc4\ub3c4\uc758 \ud074\ub77c\uc774\uc5b8\ud2b8\ub97c \uc791\uc131\ud558\uc9c0 \uc54a\uace0\ub3c4 \ud130\ubbf8\ub110\uc5d0\uc11c \uc9c1\uc811 MCP \uc11c\ubc84\ub97c \ud14c\uc2a4\ud2b8\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
    (240, "The terminal output shows the complete message exchange, including example messages for initialization and tool calls.",
     "\ud130\ubbf8\ub110 \ucd9c\ub825\uc740 \ucd08\uae30\ud654 \ubc0f \ub3c4\uad6c \ud638\ucd9c\uc758 \uc608\uc81c \uba54\uc2dc\uc9c0\ub97c \ud3ec\ud568\ud55c \uc804\uccb4 \uba54\uc2dc\uc9c0 \uad50\ud658\uc744 \ubcf4\uc5ec\uc90d\ub2c8\ub2e4."),
    (241, '<h2>MCP Connection Sequence</h2>', '<h2>MCP \uc5f0\uacb0 \uc2dc\ud000\uc2a4</h2>'),
    (242, "Every MCP connection must start with a specific three-message handshake:",
     "\ubaa8\ub4e0 MCP \uc5f0\uacb0\uc740 \ud2b9\uc815\ud55c 3\uac1c \uba54\uc2dc\uc9c0 \ud578\ub4dc\uc170\uc774\ud06c\ub85c \uc2dc\uc791\ud574\uc57c \ud569\ub2c8\ub2e4:"),
    (245, "<li><strong>Initialize Request</strong> - Client sends this first</li>",
     "<li><strong>Initialize Request</strong> - \ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uba3c\uc800 \ubcf4\ub0c5\ub2c8\ub2e4</li>"),
    (246, "<li><strong>Initialize Result</strong> - Server responds with capabilities</li>",
     "<li><strong>Initialize Result</strong> - \uc11c\ubc84\uac00 \uae30\ub2a5 \ubaa9\ub85d\uc73c\ub85c \uc751\ub2f5\ud569\ub2c8\ub2e4</li>"),
    (247, "<li><strong>Initialized Notification</strong> - Client confirms (no response expected)</li>",
     "<li><strong>Initialized Notification</strong> - \ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \ud655\uc778\ud569\ub2c8\ub2e4 (\uc751\ub2f5 \ubd88\ud544\uc694)</li>"),
    (249, "Only after this handshake can you send other requests like tool calls or prompt listings.",
     "\uc774 \ud578\ub4dc\uc170\uc774\ud06c \ud6c4\uc5d0\ub9cc \ub3c4\uad6c \ud638\ucd9c\uc774\ub098 \ud504\ub86c\ud504\ud2b8 \ubaa9\ub85d\uacfc \uac19\uc740 \ub2e4\ub978 \uc694\uccad\uc744 \ubcf4\ub0bc \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
    (250, '<h2>Message Types and Flow</h2>', '<h2>\uba54\uc2dc\uc9c0 \uc720\ud615\uacfc \ud750\ub984</h2>'),
    (251, "MCP supports various message types that flow in both directions:",
     "MCP\ub294 \uc591\ubc29\ud5a5\uc73c\ub85c \ud750\ub974\ub294 \ub2e4\uc591\ud55c \uba54\uc2dc\uc9c0 \uc720\ud615\uc744 \uc9c0\uc6d0\ud569\ub2c8\ub2e4:"),
    (254, '<h2>Four Communication Scenarios</h2>', '<h2>\ub124 \uac00\uc9c0 \ud1b5\uc2e0 \uc2dc\ub098\ub9ac\uc624</h2>'),
    (255, "With any transport, you need to handle four different communication patterns:",
     "\uc5b4\ub5a4 \uc804\uc1a1\uc744 \uc0ac\uc6a9\ud558\ub4e0 \ub124 \uac00\uc9c0 \ub2e4\ub978 \ud1b5\uc2e0 \ud328\ud134\uc744 \ucc98\ub9ac\ud574\uc57c \ud569\ub2c8\ub2e4:"),
    (264, '<h2>Why This Matters</h2>', '<h2>\uc774\uac83\uc774 \uc911\uc694\ud55c \uc774\uc720</h2>'),
]

for lineno, old, new in para_replacements:
    idx = lineno - 1
    if idx < len(lines) and old in lines[idx]:
        lines[idx] = lines[idx].replace(old, new)
        count += 1
    else:
        print(f'Line {lineno} NOT FOUND: {old[:60]}...', file=sys.stderr)

# Handle special lines with arrows and full-line content
special = [
    (253, "The key insight is that some messages require responses (requests",
     lines[252].strip() if 252 < len(lines) else "",
     "\ud575\uc2ec\uc740 \uc77c\ubd80 \uba54\uc2dc\uc9c0\ub294 \uc751\ub2f5\uc774 \ud544\uc694\ud558\uace0(\uc694\uccad \u2192 \uacb0\uacfc) \ub2e4\ub978 \uba54\uc2dc\uc9c0\ub294 \ud544\uc694\ud558\uc9c0 \uc54a\ub2e4\ub294 \uac83\uc785\ub2c8\ub2e4(\uc54c\ub9bc). \ud074\ub77c\uc774\uc5b8\ud2b8\uc640 \uc11c\ubc84 \ubaa8\ub450 \uc5b8\uc81c\ub4e0\uc9c0 \ud1b5\uc2e0\uc744 \uc2dc\uc791\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
]

for lineno, check, full_old, new_text in special:
    idx = lineno - 1
    if idx < len(lines) and check in lines[idx]:
        lines[idx] = f'<p>{new_text}</p>\n'
        count += 1

# Lines 258-261 (arrow list items)
arrow_replacements = [
    (258, 'Client writes to stdin', '\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 stdin\uc5d0 \uc791\uc131'),
    (259, 'Server writes to stdout', '\uc11c\ubc84\uac00 stdout\uc5d0 \uc791\uc131'),
    (260, 'Server writes to stdout', '\uc11c\ubc84\uac00 stdout\uc5d0 \uc791\uc131'),
    (261, 'Client writes to stdin', '\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 stdin\uc5d0 \uc791\uc131'),
    (258, 'Client', '\ud074\ub77c\uc774\uc5b8\ud2b8'),
    (259, 'Server', '\uc11c\ubc84'),
    (260, 'Server', '\uc11c\ubc84'),
    (261, 'Client', '\ud074\ub77c\uc774\uc5b8\ud2b8'),
    (258, ' request</strong>', ' \uc694\uccad</strong>'),
    (259, ' response</strong>', ' \uc751\ub2f5</strong>'),
    (260, ' request</strong>', ' \uc694\uccad</strong>'),
    (261, ' response</strong>', ' \uc751\ub2f5</strong>'),
]

for lineno, old, new in arrow_replacements:
    idx = lineno - 1
    if idx < len(lines) and old in lines[idx]:
        lines[idx] = lines[idx].replace(old, new, 1)
        count += 1

# Lines 263, 265, 266
more_lines = [
    (263, "The beauty of stdio transport is its simplicity - either party can initiate communication at any time using these two channels.",
     "stdio \uc804\uc1a1\uc758 \uc7a5\uc810\uc740 \uac04\uacb0\ud568\uc785\ub2c8\ub2e4 - \uc591\ucabd \ubaa8\ub450 \uc774 \ub450 \ucc44\ub110\uc744 \uc0ac\uc6a9\ud558\uc5ec \uc5b8\uc81c\ub4e0\uc9c0 \ud1b5\uc2e0\uc744 \uc2dc\uc791\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
]

for lineno, old, new in more_lines:
    idx = lineno - 1
    if idx < len(lines) and old in lines[idx]:
        lines[idx] = lines[idx].replace(old, new)
        count += 1

# Handle lines 265-266 which may have smart quotes
for i in [264, 265]:
    line = lines[i]
    if 'Understanding stdio transport is crucial' in line:
        lines[i] = '<p>stdio \uc804\uc1a1\uc744 \uc774\ud574\ud558\ub294 \uac83\uc774 \uc911\uc694\ud55c \uc774\uc720\ub294 \uc591\ubc29\ud5a5 \ud1b5\uc2e0\uc774 \uc6d0\ud65c\ud55c "\uc774\uc0c1\uc801\uc778" \uacbd\uc6b0\ub97c \ub098\ud0c0\ub0b4\uae30 \ub54c\ubb38\uc785\ub2c8\ub2e4. HTTP\uc640 \uac19\uc740 \ub2e4\ub978 \uc804\uc1a1\uc73c\ub85c \uc774\ub3d9\ud558\uba74 \uc11c\ubc84\uac00 \ud56d\uc0c1 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uc694\uccad\uc744 \uc2dc\uc791\ud560 \uc218 \uc5c6\ub294 \uc81c\ud55c\uc744 \ub9cc\ub098\uac8c \ub429\ub2c8\ub2e4. stdio \uc804\uc1a1\uc740 \uae30\uc900\uc810\uc5d0\uc11c \ub2e4\ub978 \uc804\uc1a1\uc758 \uc808\ucda9\uc548\uc744 \uc774\ud574\ud558\ub294 \ub370 \ub3c4\uc6c0\uc774 \ub429\ub2c8\ub2e4.</p>\n'
        count += 1
    if 'For development and testing, stdio transport is perfect' in line:
        lines[i] = '<p>\uac1c\ubc1c \ubc0f \ud14c\uc2a4\ud2b8\uc5d0\ub294 stdio \uc804\uc1a1\uc774 \uc644\ubcbd\ud569\ub2c8\ub2e4. \ud074\ub77c\uc774\uc5b8\ud2b8\uc640 \uc11c\ubc84\uac00 \ub2e4\ub978 \uba38\uc2e0\uc5d0\uc11c \uc2e4\ud589\ub418\uc5b4\uc57c \ud558\ub294 \ud504\ub85c\ub355\uc158 \ubc30\ud3ec\uc5d0\uc11c\ub294 \uac01\uac01\uc758 \uc808\ucda9\uc548\uc774 \uc788\ub294 \ub2e4\ub978 \uc804\uc1a1 \uc635\uc158\uc744 \uace0\ub824\ud574\uc57c \ud569\ub2c8\ub2e4.</p>\n'
        count += 1

content = '\n'.join(lines)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

korean = sum(1 for c in content if '\uac00' <= c <= '\ud7a3')
print(f'Replaced {count} segments. Korean chars: {korean}', file=sys.stderr)
