#!/usr/bin/env python3
import sys

filepath = 'src/The STDIO transport.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

count = 0

for i, line in enumerate(lines):
    # Fix line 227 - partial translation with trailing English
    if 'from HTTP requests to WebSockets to even writing JSON' in line:
        lines[i] = '<p>MCP \ud074\ub77c\uc774\uc5b8\ud2b8\uc640 \uc11c\ubc84\ub294 JSON \uba54\uc2dc\uc9c0\ub97c \uad50\ud658\ud558\uc5ec \ud1b5\uc2e0\ud558\uc9c0\ub9cc, \uc774 \uba54\uc2dc\uc9c0\ub4e4\uc740 \uc2e4\uc81c\ub85c \uc5b4\ub5bb\uac8c \uc804\uc1a1\ub420\uae4c\uc694? \uc0ac\uc6a9\ub418\ub294 \ud1b5\uc2e0 \ucc44\ub110\uc744 <strong>\uc804\uc1a1(transport)</strong>\uc774\ub77c\uace0 \ud558\uba70, HTTP \uc694\uccad\ubd80\ud130 WebSocket, \uc2ec\uc9c0\uc5b4 \uc5fd\uc11c\uc5d0 JSON\uc744 \uc4f0\ub294 \uac83\uae4c\uc9c0 \ub2e4\uc591\ud55c \ubc29\ubc95\uc73c\ub85c \uad6c\ud604\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4(\ub9c8\uc9c0\ub9c9 \ubc29\ubc95\uc740 \ud504\ub85c\ub355\uc158\uc5d0\ub294 \uad8c\uc7a5\ud558\uc9c0 \uc54a\uc9c0\ub9cc\uc694).</p>\n'
        count += 1
        print(f'Fixed line {i+1}: partial translation in first paragraph', file=sys.stderr)

    # Fix line 239 - partial translation with trailing English
    if 'When you run a server with <code>uv run server.py</code>' in line:
        lines[i] = '<p>\ubcc4\ub3c4\uc758 \ud074\ub77c\uc774\uc5b8\ud2b8\ub97c \uc791\uc131\ud558\uc9c0 \uc54a\uace0\ub3c4 \ud130\ubbf8\ub110\uc5d0\uc11c \uc9c1\uc811 MCP \uc11c\ubc84\ub97c \ud14c\uc2a4\ud2b8\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. <code>uv run server.py</code>\ub85c \uc11c\ubc84\ub97c \uc2e4\ud589\ud558\uba74 stdin\uc744 \uc218\uc2e0 \ub300\uae30\ud558\uace0 stdout\uc73c\ub85c \uc751\ub2f5\uc744 \uc791\uc131\ud569\ub2c8\ub2e4. \uc989, JSON \uba54\uc2dc\uc9c0\ub97c \ud130\ubbf8\ub110\uc5d0 \uc9c1\uc811 \ubd99\uc5ec\ub123\uace0 \uc11c\ubc84\uc758 \uc751\ub2f5\uc744 \uc989\uc2dc \ud655\uc778\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.</p>\n'
        count += 1
        print(f'Fixed line {i+1}: partial translation in Stdio in Action paragraph', file=sys.stderr)

    # Fix lines 259-262 - mixed Korean/English in arrow list items
    if '<strong>\ud074\ub77c\uc774\uc5b8\ud2b8 \u2192 Server \uc694\uccad</strong>' in line:
        lines[i] = line.replace('\ud074\ub77c\uc774\uc5b8\ud2b8 \u2192 Server \uc694\uccad', '\ud074\ub77c\uc774\uc5b8\ud2b8 \u2192 \uc11c\ubc84 \uc694\uccad')
        count += 1
        print(f'Fixed line {i+1}: Server -> \uc11c\ubc84', file=sys.stderr)
    if '<strong>\uc11c\ubc84 \u2192 Client \uc751\ub2f5</strong>' in line:
        lines[i] = line.replace('\uc11c\ubc84 \u2192 Client \uc751\ub2f5', '\uc11c\ubc84 \u2192 \ud074\ub77c\uc774\uc5b8\ud2b8 \uc751\ub2f5')
        count += 1
        print(f'Fixed line {i+1}: Client -> \ud074\ub77c\uc774\uc5b8\ud2b8', file=sys.stderr)
    if '<strong>\uc11c\ubc84 \u2192 Client \uc694\uccad</strong>' in line:
        lines[i] = line.replace('\uc11c\ubc84 \u2192 Client \uc694\uccad', '\uc11c\ubc84 \u2192 \ud074\ub77c\uc774\uc5b8\ud2b8 \uc694\uccad')
        count += 1
        print(f'Fixed line {i+1}: Client -> \ud074\ub77c\uc774\uc5b8\ud2b8', file=sys.stderr)
    if '<strong>\ud074\ub77c\uc774\uc5b8\ud2b8 \u2192 Server \uc751\ub2f5</strong>' in line:
        lines[i] = line.replace('\ud074\ub77c\uc774\uc5b8\ud2b8 \u2192 Server \uc751\ub2f5', '\ud074\ub77c\uc774\uc5b8\ud2b8 \u2192 \uc11c\ubc84 \uc751\ub2f5')
        count += 1
        print(f'Fixed line {i+1}: Server -> \uc11c\ubc84', file=sys.stderr)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f'Fixed {count} issues', file=sys.stderr)
