#!/usr/bin/env python3
import sys

filepath = 'src/State and the StreamableHTTP transport.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<title>State and the StreamableHTTP transport</title>', '<title>\uc0c1\ud0dc\uc640 StreamableHTTP \uc804\uc1a1</title>'),
    ('<h2 id=header-links-navigation class="hide sf-hidden">Header Navigation</h2>',
     '<h2 id=header-links-navigation class="hide sf-hidden">\ud5e4\ub354 \ub0b4\ube44\uac8c\uc774\uc158</h2>'),
    ('Anthropic Academy', 'Anthropic \uc544\uce74\ub370\ubbf8'),
    ('aria-label=Lessons', 'aria-label=\uac15\uc758\ubaa9\ub85d'),
    ('alt="Go home"', 'alt="\ud648\uc73c\ub85c \uc774\ub3d9"'),
    ('aria-label="Open menu"', 'aria-label="\uba54\ub274 \uc5f4\uae30"'),
    ('aria-label="User settings menu"', 'aria-label="\uc0ac\uc6a9\uc790 \uc124\uc815 \uba54\ub274"'),
    ('<span>My Profile</span>', '<span>\ub0b4 \ud504\ub85c\ud544</span>'),
    ('Sign Out', '\ub85c\uadf8\uc544\uc6c3'),
    ('<h2>State and the StreamableHTTP transport</h2>', '<h2>\uc0c1\ud0dc\uc640 StreamableHTTP \uc804\uc1a1</h2>'),
    ('<span>Open in Claude</span>', '<span>Claude\uc5d0\uc11c \uc5f4\uae30</span>'),
    ('Ask questions about this course', '\uc774 \uac15\uc88c\uc5d0 \ub300\ud574 \uc9c8\ubb38\ud558\uae30'),
    ('Copy notes', '\ub178\ud2b8 \ubcf5\uc0ac'),
    ('Copy full course notes for LLMs', 'LLM\uc6a9 \uc804\uccb4 \uac15\uc88c \ub178\ud2b8 \ubcf5\uc0ac'),
    ('aria-label="Toggle fullscreen"', 'aria-label="\uc804\uccb4\ud654\uba74 \uc804\ud658"'),
    ('<span>Previous</span>', '<span>\uc774\uc804</span>'),
    ('<span>Next</span>', '<span>\ub2e4\uc74c</span>'),
    ('<h4 class=sj-text-downloads><span>Downloads</span></h4>', '<h4 class=sj-text-downloads><span>\ub2e4\uc6b4\ub85c\ub4dc</span></h4>'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

lines = content.split('\n')

# Line-based replacements
line_replacements = {
    179: ('Open in Claude', 'Claude\uc5d0\uc11c \uc5f4\uae30'),
    70: ('Courses', '\uac15\uc88c'),
}

for lineno, (old, new) in line_replacements.items():
    if lineno - 1 < len(lines) and old in lines[lineno - 1]:
        lines[lineno - 1] = lines[lineno - 1].replace(old, new)
        count += 1

# Content paragraphs
para_translations = [
    (227, "The <code>stateless_http</code> and <code>json_response</code> flags in MCP servers control fundamental aspects of how your server behaves. Understanding when and why to use them is crucial, especially if you're planning to scale your server or deploy it in production.",
     "MCP \uc11c\ubc84\uc758 <code>stateless_http</code>\uc640 <code>json_response</code> \ud50c\ub798\uadf8\ub294 \uc11c\ubc84 \ub3d9\uc791\uc758 \uadfc\ubcf8\uc801\uc778 \uce21\uba74\uc744 \uc81c\uc5b4\ud569\ub2c8\ub2e4. \ud2b9\ud788 \uc11c\ubc84\ub97c \ud655\uc7a5\ud558\uac70\ub098 \ud504\ub85c\ub355\uc158\uc5d0 \ubc30\ud3ec\ud560 \uacc4\ud68d\uc774\ub77c\uba74, \uc774\ub4e4\uc744 \uc5b8\uc81c \uc65c \uc0ac\uc6a9\ud558\ub294\uc9c0 \uc774\ud574\ud558\ub294 \uac83\uc774 \uc911\uc694\ud569\ub2c8\ub2e4."),
    (228, '<h2>When You Need Stateless HTTP</h2>', '<h2>Stateless HTTP\uac00 \ud544\uc694\ud55c \uacbd\uc6b0</h2>'),
    (229, "Imagine you build an MCP server that becomes popular. Initially, you might have just a few clients connecting to a single server instance:",
     "\uc778\uae30 \uc788\ub294 MCP \uc11c\ubc84\ub97c \uad6c\ucd95\ud55c\ub2e4\uace0 \uc0c1\uc0c1\ud574 \ubcf4\uc138\uc694. \ucc98\uc74c\uc5d0\ub294 \ub2e8\uc77c \uc11c\ubc84 \uc778\uc2a4\ud134\uc2a4\uc5d0 \uba87 \uac1c\uc758 \ud074\ub77c\uc774\uc5b8\ud2b8\ub9cc \uc5f0\uacb0\ub420 \uc218 \uc788\uc2b5\ub2c8\ub2e4:"),
    (231, "As your server grows, you might have thousands of clients trying to connect. Running a single server instance won't scale to handle all that traffic:",
     "\uc11c\ubc84\uac00 \uc131\uc7a5\ud558\uba74 \uc218\ucc9c \uac1c\uc758 \ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uc5f0\uacb0\uc744 \uc2dc\ub3c4\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ub2e8\uc77c \uc11c\ubc84 \uc778\uc2a4\ud134\uc2a4\ub85c\ub294 \ubaa8\ub4e0 \ud2b8\ub798\ud53d\uc744 \ucc98\ub9ac\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4:"),
    (233, "The typical solution is horizontal scaling - running multiple server instances behind a load balancer:",
     "\uc77c\ubc18\uc801\uc778 \ud574\uacb0\ucc45\uc740 \uc218\ud3c9 \ud655\uc7a5\uc785\ub2c8\ub2e4 - \ub85c\ub4dc \ubc38\ub7f0\uc11c \ub4a4\uc5d0 \uc5ec\ub7ec \uc11c\ubc84 \uc778\uc2a4\ud134\uc2a4\ub97c \uc2e4\ud589\ud558\ub294 \uac83\uc785\ub2c8\ub2e4:"),
    (237, "A GET SSE connection for receiving server-to-client requests",
     "\uc11c\ubc84\uc5d0\uc11c \ud074\ub77c\uc774\uc5b8\ud2b8\ub85c\uc758 \uc694\uccad\uc744 \uc218\uc2e0\ud558\uae30 \uc704\ud55c GET SSE \uc5f0\uacb0"),
    (238, "POST requests for calling tools and receiving responses",
     "\ub3c4\uad6c \ud638\ucd9c \ubc0f \uc751\ub2f5 \uc218\uc2e0\uc744 \uc704\ud55c POST \uc694\uccad"),
    (243, '<h2>How Stateless HTTP Solves This</h2>', '<h2>Stateless HTTP\uac00 \uc774\ub97c \ud574\uacb0\ud558\ub294 \ubc29\ubc95</h2>'),
    (244, "Setting <code>stateless_http=True</code> eliminates this coordination problem, but with significant trade-offs:",
     "<code>stateless_http=True</code>\ub97c \uc124\uc815\ud558\uba74 \uc774 \uc870\uc815 \ubb38\uc81c\uac00 \ud574\uacb0\ub418\uc9c0\ub9cc, \uc0c1\ub2f9\ud55c \uc808\ucda9\uc548\uc774 \ub530\ub985\ub2c8\ub2e4:"),
    (246, "When stateless HTTP is enabled:", "stateless HTTP\uac00 \ud65c\uc131\ud654\ub418\uba74:"),
    (248, "<li><strong>Clients don't get session IDs</strong> - the server can't track individual clients</li>",
     "<li><strong>\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uc138\uc158 ID\ub97c \ubc1b\uc9c0 \ubabb\ud568</strong> - \uc11c\ubc84\uac00 \uac1c\ubcc4 \ud074\ub77c\uc774\uc5b8\ud2b8\ub97c \ucd94\uc801\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4</li>"),
    (249, "<li><strong>No server-to-client requests</strong> - the GET SSE pathway becomes unavailable</li>",
     "<li><strong>\uc11c\ubc84\uc5d0\uc11c \ud074\ub77c\uc774\uc5b8\ud2b8\ub85c\uc758 \uc694\uccad \ubd88\uac00</strong> - GET SSE \uacbd\ub85c\ub97c \uc0ac\uc6a9\ud560 \uc218 \uc5c6\uac8c \ub429\ub2c8\ub2e4</li>"),
    (250, "<li><strong>No sampling</strong> - can't use Claude or other AI models</li>",
     "<li><strong>\uc0d8\ud50c\ub9c1 \ubd88\uac00</strong> - Claude\ub098 \ub2e4\ub978 AI \ubaa8\ub378\uc744 \uc0ac\uc6a9\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4</li>"),
    (251, "<li><strong>No progress reports</strong> - can't send progress updates during long operations</li>",
     "<li><strong>\uc9c4\ud589 \ubcf4\uace0 \ubd88\uac00</strong> - \uc7a5\uc2dc\uac04 \uc791\uc5c5 \uc911 \uc9c4\ud589 \uc5c5\ub370\uc774\ud2b8\ub97c \ubcf4\ub0bc \uc218 \uc5c6\uc2b5\ub2c8\ub2e4</li>"),
    (252, "<li><strong>No subscriptions</strong> - can't notify clients about resource updates</li>",
     "<li><strong>\uad6c\ub3c5 \ubd88\uac00</strong> - \ub9ac\uc18c\uc2a4 \uc5c5\ub370\uc774\ud2b8\uc5d0 \ub300\ud574 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uc54c\ub9bc\uc744 \ubcf4\ub0bc \uc218 \uc5c6\uc2b5\ub2c8\ub2e4</li>"),
    (254, "However, there's one benefit: <strong>client initialization is no longer required</strong>. Clients can make requests directly without the initial handshake process.",
     "\uadf8\ub7ec\ub098 \ud55c \uac00\uc9c0 \uc774\uc810\uc774 \uc788\uc2b5\ub2c8\ub2e4: <strong>\ud074\ub77c\uc774\uc5b8\ud2b8 \ucd08\uae30\ud654\uac00 \ub354 \uc774\uc0c1 \ud544\uc694\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4</strong>. \ud074\ub77c\uc774\uc5b8\ud2b8\ub294 \ucd08\uae30 \ud578\ub4dc\uc170\uc774\ud06c \uacfc\uc815 \uc5c6\uc774 \uc9c1\uc811 \uc694\uccad\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4."),
    (256, '<h2>Understanding JSON Response</h2>', '<h2>JSON Response \uc774\ud574\ud558\uae30</h2>'),
    (257, "The <code>json_response=True</code> flag is simpler - it just disables streaming for POST request responses. Instead of getting multiple SSE messages as a tool executes, you get only the final result as plain JSON.",
     "<code>json_response=True</code> \ud50c\ub798\uadf8\ub294 \ub354 \uac04\ub2e8\ud569\ub2c8\ub2e4 - POST \uc694\uccad \uc751\ub2f5\uc758 \uc2a4\ud2b8\ub9ac\ubc0d\uc744 \ube44\ud65c\uc131\ud654\ud569\ub2c8\ub2e4. \ub3c4\uad6c\uac00 \uc2e4\ud589\ub418\ub294 \ub3d9\uc548 \uc5ec\ub7ec SSE \uba54\uc2dc\uc9c0\ub97c \ubc1b\ub294 \ub300\uc2e0 \ucd5c\uc885 \uacb0\uacfc\ub9cc \uc77c\ubc18 JSON\uc73c\ub85c \ubc1b\uc2b5\ub2c8\ub2e4."),
    (258, "With streaming disabled:", "\uc2a4\ud2b8\ub9ac\ubc0d\uc774 \ube44\ud65c\uc131\ud654\ub418\uba74:"),
    (260, "No intermediate progress messages", "\uc911\uac04 \uc9c4\ud589 \uba54\uc2dc\uc9c0 \uc5c6\uc74c"),
    (261, "No log statements during execution", "\uc2e4\ud589 \uc911 \ub85c\uadf8 \ubb38 \uc5c6\uc74c"),
    (262, "Just the final tool result", "\ucd5c\uc885 \ub3c4\uad6c \uacb0\uacfc\ub9cc \uc81c\uacf5"),
    (264, '<h2>When to Use These Flags</h2>', '<h2>\uc774 \ud50c\ub798\uadf8\ub97c \uc0ac\uc6a9\ud574\uc57c \ud560 \ub54c</h2>'),
    (265, "<strong>Use stateless HTTP when:</strong>", "<strong>stateless HTTP\ub97c \uc0ac\uc6a9\ud574\uc57c \ud560 \ub54c:</strong>"),
    (267, "You need horizontal scaling with load balancers", "\ub85c\ub4dc \ubc38\ub7f0\uc11c\ub97c \uc0ac\uc6a9\ud55c \uc218\ud3c9 \ud655\uc7a5\uc774 \ud544\uc694\ud560 \ub54c"),
    (268, "You don't need server-to-client communication", "\uc11c\ubc84\uc5d0\uc11c \ud074\ub77c\uc774\uc5b8\ud2b8\ub85c\uc758 \ud1b5\uc2e0\uc774 \ud544\uc694\ud558\uc9c0 \uc54a\uc744 \ub54c"),
    (269, "Your tools don't require AI model sampling", "\ub3c4\uad6c\uc5d0 AI \ubaa8\ub378 \uc0d8\ud50c\ub9c1\uc774 \ud544\uc694\ud558\uc9c0 \uc54a\uc744 \ub54c"),
    (270, "You want to minimize connection overhead", "\uc5f0\uacb0 \uc624\ubc84\ud5e4\ub4dc\ub97c \ucd5c\uc18c\ud654\ud558\uace0 \uc2f6\uc744 \ub54c"),
    (272, "<strong>Use JSON response when:</strong>", "<strong>JSON response\ub97c \uc0ac\uc6a9\ud574\uc57c \ud560 \ub54c:</strong>"),
    (274, "You don't need streaming responses", "\uc2a4\ud2b8\ub9ac\ubc0d \uc751\ub2f5\uc774 \ud544\uc694\ud558\uc9c0 \uc54a\uc744 \ub54c"),
    (275, "You prefer simpler, non-streaming HTTP responses", "\ub354 \uac04\ub2e8\ud55c \ube44\uc2a4\ud2b8\ub9ac\ubc0d HTTP \uc751\ub2f5\uc744 \uc120\ud638\ud560 \ub54c"),
    (276, "You're integrating with systems that expect plain JSON", "\uc77c\ubc18 JSON\uc744 \uae30\ub300\ud558\ub294 \uc2dc\uc2a4\ud15c\uacfc \ud1b5\ud569\ud560 \ub54c"),
    (278, '<h2>Development vs Production</h2>', '<h2>\uac1c\ubc1c vs \ud504\ub85c\ub355\uc158</h2>'),
    (280, "These flags fundamentally change how your MCP server operates, so choose them based on your specific scaling and functionality requirements.",
     "\uc774 \ud50c\ub798\uadf8\ub4e4\uc740 MCP \uc11c\ubc84\uc758 \uc791\ub3d9 \ubc29\uc2dd\uc744 \uadfc\ubcf8\uc801\uc73c\ub85c \ubcc0\uacbd\ud558\ubbc0\ub85c, \ud2b9\uc815 \ud655\uc7a5\uc131 \ubc0f \uae30\ub2a5 \uc694\uad6c \uc0ac\ud56d\uc5d0 \ub530\ub77c \uc120\ud0dd\ud558\uc138\uc694."),
]

for lineno, old, new in para_translations:
    idx = lineno - 1
    if idx < len(lines) and old in lines[idx]:
        lines[idx] = lines[idx].replace(old, new)
        count += 1
    else:
        print(f'Line {lineno} NOT FOUND: {old[:60]}...', file=sys.stderr)

# Special lines with smart quotes
for i in range(len(lines)):
    line = lines[i]
    if "But here's where things get complicated" in line:
        lines[i] = "<p>\ud558\uc9c0\ub9cc \uc5ec\uae30\uc11c \uc0c1\ud669\uc774 \ubcf5\uc7a1\ud574\uc9d1\ub2c8\ub2e4. MCP \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0\ub294 \ub450 \uac1c\uc758 \ubcc4\ub3c4 \uc5f0\uacb0\uc774 \ud544\uc694\ud558\ub2e4\ub294 \uac83\uc744 \uae30\uc5b5\ud558\uc138\uc694:</p>\n"
        count += 1
    if "With a load balancer, these requests might get routed" in line:
        lines[i] = "<p>\ub85c\ub4dc \ubc38\ub7f0\uc11c\ub97c \uc0ac\uc6a9\ud558\uba74 \uc774\ub7ec\ud55c \uc694\uccad\uc774 \ub2e4\ub978 \uc11c\ubc84 \uc778\uc2a4\ud134\uc2a4\ub85c \ub77c\uc6b0\ud305\ub420 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ub3c4\uad6c\uac00 Claude\ub97c \uc0ac\uc6a9\ud574\uc57c \ud558\ub294 \uacbd\uc6b0(\uc0d8\ud50c\ub9c1\uc744 \ud1b5\ud574), POST \uc694\uccad\uc744 \ucc98\ub9ac\ud558\ub294 \uc11c\ubc84\ub294 GET SSE \uc5f0\uacb0\uc744 \ucc98\ub9ac\ud558\ub294 \uc11c\ubc84\uc640 \uc870\uc815\ud574\uc57c \ud569\ub2c8\ub2e4. \uc774\ub294 \uc11c\ubc84 \uac04 \ubcf5\uc7a1\ud55c \uc870\uc815 \ubb38\uc81c\ub97c \ub9cc\ub4ed\ub2c8\ub2e4.</p>\n"
        count += 1
    if "However, there's one benefit" in line:
        lines[i] = lines[i]  # already handled above via para_translations
    if "If you're developing locally" in line:
        lines[i] = "<p>\ub85c\uceec\uc5d0\uc11c \ud45c\uc900 I/O \uc804\uc1a1\uc73c\ub85c \uac1c\ubc1c\ud558\uc9c0\ub9cc HTTP \uc804\uc1a1\uc73c\ub85c \ubc30\ud3ec\ud560 \uacc4\ud68d\uc774\ub77c\uba74, \ud504\ub85c\ub355\uc158\uc5d0\uc11c \uc0ac\uc6a9\ud560 \ub3d9\uc77c\ud55c \uc804\uc1a1\uc73c\ub85c \ud14c\uc2a4\ud2b8\ud558\uc138\uc694. stateful\uacfc stateless \ubaa8\ub4dc \uac04\uc758 \ub3d9\uc791 \ucc28\uc774\uac00 \uc0c1\ub2f9\ud560 \uc218 \uc788\uc73c\uba70, \ud504\ub85c\ub355\uc158\ubcf4\ub2e4 \uac1c\ubc1c \uc911\uc5d0 \ubb38\uc81c\ub97c \ubc1c\uacac\ud558\ub294 \uac83\uc774 \ub0ab\uc2b5\ub2c8\ub2e4.</p>\n"
        count += 1

content = '\n'.join(lines)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

korean = sum(1 for c in content if '\uac00' <= c <= '\ud7a3')
print(f'Replaced {count} segments. Korean chars: {korean}', file=sys.stderr)
