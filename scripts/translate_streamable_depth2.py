#!/usr/bin/env python3
import sys

filepath = 'src/StreamableHTTP in depth.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0

for i, line in enumerate(lines):
    stripped = line.strip()

    if stripped == 'Courses':
        lines[i] = line.replace('Courses', '\uac15\uc88c')
        count += 1
    elif stripped == 'Open in Claude':
        lines[i] = line.replace('Open in Claude', 'Claude\uc5d0\uc11c \uc5f4\uae30')
        count += 1
    elif stripped.startswith("<p>StreamableHTTP is MCP's solution"):
        lines[i] = "<p>StreamableHTTP\ub294 \uadfc\ubcf8\uc801\uc778 \ubb38\uc81c\uc5d0 \ub300\ud55c MCP\uc758 \ud574\uacb0\ucc45\uc785\ub2c8\ub2e4: \uc77c\ubd80 MCP \uae30\ub2a5\uc740 \uc11c\ubc84\uac00 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uc694\uccad\uc744 \ubcf4\ub0b4\uc57c \ud558\uc9c0\ub9cc, HTTP\ub294 \uc774\ub97c \uc5b4\ub835\uac8c \ub9cc\ub4ed\ub2c8\ub2e4. StreamableHTTP\uac00 \uc774 \uc81c\ud55c\uc744 \uc5b4\ub5bb\uac8c \ud574\uacb0\ud558\ub294\uc9c0, \uadf8\ub9ac\uace0 \uc5b8\uc81c \uadf8 \uc6b0\ud68c \ubc29\ubc95\uc744 \ubb34\ud6a8\ud654\ud574\uc57c \ud558\ub294\uc9c0 \uc0b4\ud3b4\ubcf4\uaca0\uc2b5\ub2c8\ub2e4.</p>\n"
        count += 1
    elif stripped.startswith("<p>StreamableHTTP is more complex"):
        lines[i] = "<p>StreamableHTTP\ub294 HTTP\uc758 \uc81c\ud55c\uc744 \uc6b0\ud68c\ud574\uc57c \ud558\uae30 \ub54c\ubb38\uc5d0 \ub2e4\ub978 MCP \uc804\uc1a1 \ubc29\uc2dd\ubcf4\ub2e4 \ubcf5\uc7a1\ud569\ub2c8\ub2e4. SSE \uae30\ubc18 \uc6b0\ud68c \ubc29\ubc95\uc740 HTTP\ub97c \ud1b5\ud55c \uc804\uccb4 MCP \uae30\ub2a5\uc744 \uac00\ub2a5\ud558\uac8c \ud558\uc9c0\ub9cc, \ub514\ubc84\uae45\uacfc \ucd5c\uc801\ud654\ub97c \uc704\ud574 \uc774\uc911 \uc5f0\uacb0 \ubaa8\ub378\uc744 \uc774\ud574\ud558\ub294 \uac83\uc774 \uc911\uc694\ud569\ub2c8\ub2e4.</p>\n"
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

korean = sum(1 for c in ''.join(lines) if '\uac00' <= c <= '\ud7a3')
print(f'Fixed {count} remaining segments. Korean chars: {korean}', file=sys.stderr)
