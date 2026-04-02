#!/usr/bin/env python3
import sys

filepath = 'src/Log and progress notifications.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Line 227
    ("Logging and progress notifications are simple to implement but make a huge difference in user experience when working with MCP servers. They help users understand what's happening during long-running operations instead of wondering if something has broken.",
     "\ub85c\uae45 \ubc0f \uc9c4\ud589 \uc0c1\ud669 \uc54c\ub9bc\uc740 \uad6c\ud604\uc774 \uac04\ub2e8\ud558\uc9c0\ub9cc MCP \uc11c\ubc84\ub97c \uc0ac\uc6a9\ud560 \ub54c \uc0ac\uc6a9\uc790 \uacbd\ud5d8\uc5d0 \ud070 \ucc28\uc774\ub97c \ub9cc\ub4ed\ub2c8\ub2e4. \uc7a5\uc2dc\uac04 \uc2e4\ud589\ub418\ub294 \uc791\uc5c5 \uc911\uc5d0 \ubb38\uc81c\uac00 \ubc1c\uc0dd\ud55c \uac83\uc778\uc9c0 \uad81\uae08\ud574\ud558\ub294 \ub300\uc2e0 \ubb34\uc2a8 \uc77c\uc774 \uc77c\uc5b4\ub098\uace0 \uc788\ub294\uc9c0 \uc0ac\uc6a9\uc790\uac00 \uc774\ud574\ud560 \uc218 \uc788\ub3c4\ub85d \ub3c4\uc640\uc90d\ub2c8\ub2e4."),
    # Line 228
    ("When Claude calls a tool that takes time to complete - like researching a topic or processing data - users typically see nothing until the operation finishes. This can be frustrating because they don't know if the tool is working or has stalled.",
     "Claude\uac00 \uc8fc\uc81c \uc870\uc0ac\ub098 \ub370\uc774\ud130 \ucc98\ub9ac\uc640 \uac19\uc774 \uc2dc\uac04\uc774 \uac78\ub9ac\ub294 \ub3c4\uad6c\ub97c \ud638\ucd9c\ud560 \ub54c, \uc0ac\uc6a9\uc790\ub294 \uc77c\ubc18\uc801\uc73c\ub85c \uc791\uc5c5\uc774 \uc644\ub8cc\ub420 \ub54c\uae4c\uc9c0 \uc544\ubb34\uac83\ub3c4 \ubcfc \uc218 \uc5c6\uc2b5\ub2c8\ub2e4. \ub3c4\uad6c\uac00 \uc791\ub3d9 \uc911\uc778\uc9c0 \uba48\ucda4 \uac83\uc778\uc9c0 \uc54c \uc218 \uc5c6\uae30 \ub54c\ubb38\uc5d0 \ub2f5\ub2f5\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
    # Line 229
    ("With logging and progress notifications enabled, users get real-time feedback showing exactly what's happening behind the scenes. They can see progress bars, status messages, and detailed logs as the operation runs.",
     "\ub85c\uae45 \ubc0f \uc9c4\ud589 \uc0c1\ud669 \uc54c\ub9bc\uc744 \ud65c\uc131\ud654\ud558\uba74, \uc0ac\uc6a9\uc790\ub294 \ub4a4\uc5d0\uc11c \uc815\ud655\ud788 \ubb34\uc2a8 \uc77c\uc774 \uc77c\uc5b4\ub098\uace0 \uc788\ub294\uc9c0 \uc2e4\uc2dc\uac04 \ud53c\ub4dc\ubc31\uc744 \ubc1b\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uc791\uc5c5\uc774 \uc2e4\ud589\ub418\ub294 \ub3d9\uc548 \uc9c4\ud589\ub960 \ud45c\uc2dc\uc904, \uc0c1\ud0dc \uba54\uc2dc\uc9c0, \uc0c1\uc138 \ub85c\uadf8\ub97c \ud655\uc778\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
    # Line 231
    ("In the Python MCP SDK, logging and progress notifications work through the Context argument that's automatically provided to your tool functions. This context object gives you methods to communicate back to the client during execution.",
     "Python MCP SDK\uc5d0\uc11c \ub85c\uae45 \ubc0f \uc9c4\ud589 \uc0c1\ud669 \uc54c\ub9bc\uc740 \ub3c4\uad6c \ud568\uc218\uc5d0 \uc790\ub3d9\uc73c\ub85c \uc81c\uacf5\ub418\ub294 Context \uc778\uc218\ub97c \ud1b5\ud574 \uc791\ub3d9\ud569\ub2c8\ub2e4. \uc774 context \uac1d\uccb4\ub294 \uc2e4\ud589 \uc911\uc5d0 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uc0c1\ud0dc\ub97c \ub2e4\uc2dc \uc804\ub2ec\ud558\ub294 \uba54\uc11c\ub4dc\ub97c \uc81c\uacf5\ud569\ub2c8\ub2e4."),
    # Line 283
    ("You provide the logging callback when creating the client session, and the progress callback when making individual tool calls. This gives you flexibility to handle different types of notifications appropriately.",
     "\ud074\ub77c\uc774\uc5b8\ud2b8 \uc138\uc158\uc744 \uc0dd\uc131\ud560 \ub54c \ub85c\uae45 \ucf5c\ubc31\uc744 \uc81c\uacf5\ud558\uace0, \uac1c\ubcc4 \ub3c4\uad6c \ud638\ucd9c \uc2dc \uc9c4\ud589 \uc0c1\ud669 \ucf5c\ubc31\uc744 \uc81c\uacf5\ud569\ub2c8\ub2e4. \uc774\ub97c \ud1b5\ud574 \ub2e4\uc591\ud55c \uc720\ud615\uc758 \uc54c\ub9bc\uc744 \uc801\uc808\ud558\uac8c \ucc98\ub9ac\ud560 \uc218 \uc788\ub294 \uc720\uc5f0\uc131\uc744 \uc5bb\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
    # Line 291
    ("Remember that implementing these notifications is entirely optional. You can choose to ignore them completely, show only certain types, or present them however makes sense for your application. They're purely user experience enhancements to help users understand what's happening during long-running operations.",
     "\uc774\ub7ec\ud55c \uc54c\ub9bc \uad6c\ud604\uc740 \uc644\uc804\ud788 \uc120\ud0dd \uc0ac\ud56d\uc774\ub77c\ub294 \uc810\uc744 \uae30\uc5b5\ud558\uc138\uc694. \uc644\uc804\ud788 \ubb34\uc2dc\ud558\uac70\ub098, \ud2b9\uc815 \uc720\ud615\ub9cc \ud45c\uc2dc\ud558\uac70\ub098, \uc560\ud50c\ub9ac\ucf00\uc774\uc158\uc5d0 \uc801\ud569\ud55c \ubc29\uc2dd\uc73c\ub85c \ud45c\uc2dc\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uc774\ub4e4\uc740 \uc7a5\uc2dc\uac04 \uc2e4\ud589\ub418\ub294 \uc791\uc5c5 \uc911\uc5d0 \ubb34\uc2a8 \uc77c\uc774 \uc77c\uc5b4\ub098\uace0 \uc788\ub294\uc9c0 \uc0ac\uc6a9\uc790\uac00 \uc774\ud574\ud560 \uc218 \uc788\ub3c4\ub85d \ub3c4\uc640\uc8fc\ub294 \uc21c\uc218\ud55c \uc0ac\uc6a9\uc790 \uacbd\ud5d8 \ud5a5\uc0c1 \uae30\ub2a5\uc785\ub2c8\ub2e4."),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'OK: {old[:50]}...', file=sys.stderr)
    else:
        print(f'NOT FOUND: {repr(old[:80])}', file=sys.stderr)

# Fix corrupted line 283 if still present
lines = content.split('\n')
for i, line in enumerate(lines):
    stripped = line.strip()
    # Detect mojibake/corrupted Korean
    if stripped.startswith('<p>') and any(ord(c) > 0xF000 for c in stripped[:20]):
        lines[i] = '<p>\ud074\ub77c\uc774\uc5b8\ud2b8 \uc138\uc158\uc744 \uc0dd\uc131\ud560 \ub54c \ub85c\uae45 \ucf5c\ubc31\uc744 \uc81c\uacf5\ud558\uace0, \uac1c\ubcc4 \ub3c4\uad6c \ud638\ucd9c \uc2dc \uc9c4\ud589 \uc0c1\ud669 \ucf5c\ubc31\uc744 \uc81c\uacf5\ud569\ub2c8\ub2e4. \uc774\ub97c \ud1b5\ud574 \ub2e4\uc591\ud55c \uc720\ud615\uc758 \uc54c\ub9bc\uc744 \uc801\uc808\ud558\uac8c \ucc98\ub9ac\ud560 \uc218 \uc788\ub294 \uc720\uc5f0\uc131\uc744 \uc5bb\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4.</p>'
        count += 1
        print(f'Fixed corrupted line {i+1}', file=sys.stderr)

content = '\n'.join(lines)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

korean_count = sum(1 for c in content if '\uac00' <= c <= '\ud7a3')
print(f'Replaced {count} segments. Korean chars: {korean_count}', file=sys.stderr)
