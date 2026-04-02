#!/usr/bin/env python3
import sys

filepath = 'src/StreamableHTTP in depth.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<title>StreamableHTTP in depth</title>', '<title>StreamableHTTP \uc2ec\uce35 \ubd84\uc11d</title>'),
    ('<h2 id=header-links-navigation class="hide sf-hidden">Header Navigation</h2>',
     '<h2 id=header-links-navigation class="hide sf-hidden">\ud5e4\ub354 \ub0b4\ube44\uac8c\uc774\uc158</h2>'),
    ('Anthropic Academy', 'Anthropic \uc544\uce74\ub370\ubbf8'),
    ('\nCourses\n', '\n\uac15\uc88c\n'),
    ('aria-label=Lessons', 'aria-label=\uac15\uc758\ubaa9\ub85d'),
    ('alt="Go home"', 'alt="\ud648\uc73c\ub85c \uc774\ub3d9"'),
    ('aria-label="Open menu"', 'aria-label="\uba54\ub274 \uc5f4\uae30"'),
    ('aria-label="User settings menu"', 'aria-label="\uc0ac\uc6a9\uc790 \uc124\uc815 \uba54\ub274"'),
    ('<span>My Profile</span>', '<span>\ub0b4 \ud504\ub85c\ud544</span>'),
    ('Sign Out', '\ub85c\uadf8\uc544\uc6c3'),
    ('<h2>StreamableHTTP in depth</h2>', '<h2>StreamableHTTP \uc2ec\uce35 \ubd84\uc11d</h2>'),
    ('<span>Open in Claude</span>', '<span>Claude\uc5d0\uc11c \uc5f4\uae30</span>'),
    ('\nOpen in Claude\n', '\nClaude\uc5d0\uc11c \uc5f4\uae30\n'),
    ('Ask questions about this course', '\uc774 \uac15\uc88c\uc5d0 \ub300\ud574 \uc9c8\ubb38\ud558\uae30'),
    ('Copy notes', '\ub178\ud2b8 \ubcf5\uc0ac'),
    ('Copy full course notes for LLMs', 'LLM\uc6a9 \uc804\uccb4 \uac15\uc88c \ub178\ud2b8 \ubcf5\uc0ac'),
    # Main content
    ("StreamableHTTP is MCP's solution to a fundamental problem: some MCP functionality requires the server to make requests to the client, but HTTP makes this challenging. Let's explore how StreamableHTTP works around this limitation and when you might need to consider it.",
     "StreamableHTTP\ub294 \uadfc\ubcf8\uc801\uc778 \ubb38\uc81c\uc5d0 \ub300\ud55c MCP\uc758 \ud574\uacb0\ucc45\uc785\ub2c8\ub2e4: \uc77c\ubd80 MCP \uae30\ub2a5\uc740 \uc11c\ubc84\uac00 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uc694\uccad\uc744 \ubcf4\ub0b4\uc57c \ud558\uc9c0\ub9cc, HTTP\ub294 \uc774\ub97c \uc5b4\ub835\uac8c \ub9cc\ub4ed\ub2c8\ub2e4. StreamableHTTP\uac00 \uc774 \uc81c\ud55c\uc744 \uc5b4\ub5bb\uac8c \ud574\uacb0\ud558\ub294\uc9c0, \uadf8\ub9ac\uace0 \uc5b8\uc81c \uace0\ub824\ud574\uc57c \ud558\ub294\uc9c0 \uc0b4\ud3b4\ubcf4\uaca0\uc2b5\ub2c8\ub2e4."),
    ('<h2>The Core Problem</h2>', '<h2>\ud575\uc2ec \ubb38\uc81c</h2>'),
    ("Some MCP features like sampling, notifications, and logging rely on the server initiating requests to the client. However, HTTP is designed for clients to make requests to servers, not the other way around. StreamableHTTP solves this with a clever workaround using Server-Sent Events (SSE).",
     "\uc0d8\ud50c\ub9c1, \uc54c\ub9bc, \ub85c\uae45\uacfc \uac19\uc740 \uc77c\ubd80 MCP \uae30\ub2a5\uc740 \uc11c\ubc84\uac00 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uc694\uccad\uc744 \uc2dc\uc791\ud558\ub294 \uac83\uc5d0 \uc758\uc874\ud569\ub2c8\ub2e4. \uadf8\ub7ec\ub098 HTTP\ub294 \ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uc11c\ubc84\uc5d0 \uc694\uccad\uc744 \ubcf4\ub0b4\ub3c4\ub85d \uc124\uacc4\ub418\uc5c8\uc9c0, \uadf8 \ubc18\ub300\ub294 \uc544\ub2d9\ub2c8\ub2e4. StreamableHTTP\ub294 Server-Sent Events(SSE)\ub97c \uc0ac\uc6a9\ud55c \ub611\ub611\ud55c \uc6b0\ud68c \ubc29\ubc95\uc73c\ub85c \uc774\ub97c \ud574\uacb0\ud569\ub2c8\ub2e4."),
    ('<h2>How StreamableHTTP Works</h2>', '<h2>StreamableHTTP \uc791\ub3d9 \ubc29\uc2dd</h2>'),
    ('The magic happens through a multi-step process that establishes persistent connections between client and server.',
     '\ud074\ub77c\uc774\uc5b8\ud2b8\uc640 \uc11c\ubc84 \uac04\uc5d0 \uc601\uad6c \uc5f0\uacb0\uc744 \uc124\uc815\ud558\ub294 \ub2e4\ub2e8\uacc4 \ud504\ub85c\uc138\uc2a4\ub97c \ud1b5\ud574 \uc791\ub3d9\ud569\ub2c8\ub2e4.'),
    ('<h3>Initial Connection Setup</h3>', '<h3>\ucd08\uae30 \uc5f0\uacb0 \uc124\uc815</h3>'),
    ('The process starts like any MCP connection:', '\ud504\ub85c\uc138\uc2a4\ub294 \uc77c\ubc18\uc801\uc778 MCP \uc5f0\uacb0\uacfc \uac19\uc774 \uc2dc\uc791\ub429\ub2c8\ub2e4:'),
    ('Client sends an <code>Initialize Request</code> to the server',
     '\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uc11c\ubc84\uc5d0 <code>Initialize Request</code>\ub97c \ubcf4\ub0c5\ub2c8\ub2e4'),
    ('Server responds with an <code>Initialize Result</code> that includes a special <code>mcp-session-id</code> header',
     '\uc11c\ubc84\uac00 \ud2b9\ubcc4\ud55c <code>mcp-session-id</code> \ud5e4\ub354\ub97c \ud3ec\ud568\ud55c <code>Initialize Result</code>\ub85c \uc751\ub2f5\ud569\ub2c8\ub2e4'),
    ('Client sends an <code>Initialized Notification</code> with the session ID',
     '\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \uc138\uc158 ID\uc640 \ud568\uaed8 <code>Initialized Notification</code>\uc744 \ubcf4\ub0c5\ub2c8\ub2e4'),
    ('This session ID is crucial - it uniquely identifies the client and must be included in all future requests.',
     '\uc774 \uc138\uc158 ID\ub294 \ub9e4\uc6b0 \uc911\uc694\ud569\ub2c8\ub2e4 - \ud074\ub77c\uc774\uc5b8\ud2b8\ub97c \uace0\uc720\ud558\uac8c \uc2dd\ubcc4\ud558\uba70 \ubaa8\ub4e0 \ud5a5\ud6c4 \uc694\uccad\uc5d0 \ud3ec\ud568\ub418\uc5b4\uc57c \ud569\ub2c8\ub2e4.'),
    ('<h3>The SSE Workaround</h3>', '<h3>SSE \uc6b0\ud68c \ubc29\ubc95</h3>'),
    ('After initialization, the client can make a GET request to establish a Server-Sent Events connection. This creates a long-lived HTTP response that the server can use to stream messages back to the client at any time.',
     '\ucd08\uae30\ud654 \ud6c4, \ud074\ub77c\uc774\uc5b8\ud2b8\ub294 GET \uc694\uccad\uc744 \ud1b5\ud574 Server-Sent Events \uc5f0\uacb0\uc744 \uc124\uc815\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uc774\ub294 \uc11c\ubc84\uac00 \uc5b8\uc81c\ub4e0\uc9c0 \ud074\ub77c\uc774\uc5b8\ud2b8\uc5d0 \uba54\uc2dc\uc9c0\ub97c \uc2a4\ud2b8\ub9ac\ubc0d\ud560 \uc218 \uc788\ub294 \uc7a5\uae30 HTTP \uc751\ub2f5\uc744 \uc0dd\uc131\ud569\ub2c8\ub2e4.'),
    ('This SSE connection is the key to allowing server-to-client communication. The server can now send requests, notifications, and other messages through this persistent channel.',
     '\uc774 SSE \uc5f0\uacb0\uc740 \uc11c\ubc84\uc5d0\uc11c \ud074\ub77c\uc774\uc5b8\ud2b8\ub85c\uc758 \ud1b5\uc2e0\uc744 \uac00\ub2a5\ud558\uac8c \ud558\ub294 \ud575\uc2ec\uc785\ub2c8\ub2e4. \uc11c\ubc84\ub294 \uc774\uc81c \uc774 \uc601\uad6c \ucc44\ub110\uc744 \ud1b5\ud574 \uc694\uccad, \uc54c\ub9bc \ubc0f \uae30\ud0c0 \uba54\uc2dc\uc9c0\ub97c \ubcf4\ub0bc \uc218 \uc788\uc2b5\ub2c8\ub2e4.'),
    ('<h2>Tool Calls and Dual SSE Connections</h2>', '<h2>\ub3c4\uad6c \ud638\ucd9c\uacfc \uc774\uc911 SSE \uc5f0\uacb0</h2>'),
    ('When the client makes a tool call, things get more complex. The system creates two separate SSE connections:',
     '\ud074\ub77c\uc774\uc5b8\ud2b8\uac00 \ub3c4\uad6c\ub97c \ud638\ucd9c\ud558\uba74 \uc0c1\ud669\uc774 \ub354 \ubcf5\uc7a1\ud574\uc9d1\ub2c8\ub2e4. \uc2dc\uc2a4\ud15c\uc740 \ub450 \uac1c\uc758 \ubcc4\ub3c4 SSE \uc5f0\uacb0\uc744 \uc0dd\uc131\ud569\ub2c8\ub2e4:'),
    ('<li><strong>Primary SSE Connection:</strong> Used for server-initiated requests and stays open indefinitely</li>',
     '<li><strong>\uae30\ubcf8 SSE \uc5f0\uacb0:</strong> \uc11c\ubc84 \uc2dc\uc791 \uc694\uccad\uc5d0 \uc0ac\uc6a9\ub418\uba70 \ubb34\uae30\ud55c \uc5f4\ub9b0 \uc0c1\ud0dc\ub85c \uc720\uc9c0\ub429\ub2c8\ub2e4</li>'),
    ('<li><strong>Tool-Specific SSE Connection:</strong> Created for each tool call and closes automatically when the tool result is sent</li>',
     '<li><strong>\ub3c4\uad6c \uc804\uc6a9 SSE \uc5f0\uacb0:</strong> \uac01 \ub3c4\uad6c \ud638\ucd9c\ub9c8\ub2e4 \uc0dd\uc131\ub418\uba70 \ub3c4\uad6c \uacb0\uacfc\uac00 \uc804\uc1a1\ub418\uba74 \uc790\ub3d9\uc73c\ub85c \ub2eb\ud799\ub2c8\ub2e4</li>'),
    ('<h3>Message Routing</h3>', '<h3>\uba54\uc2dc\uc9c0 \ub77c\uc6b0\ud305</h3>'),
    ('Different types of messages get routed through different connections:',
     '\ub2e4\ub978 \uc720\ud615\uc758 \uba54\uc2dc\uc9c0\ub294 \ub2e4\ub978 \uc5f0\uacb0\uc744 \ud1b5\ud574 \ub77c\uc6b0\ud305\ub429\ub2c8\ub2e4:'),
    ('<li><strong>Progress notifications:</strong> Sent through the primary SSE connection</li>',
     '<li><strong>\uc9c4\ud589 \uc0c1\ud669 \uc54c\ub9bc:</strong> \uae30\ubcf8 SSE \uc5f0\uacb0\uc744 \ud1b5\ud574 \uc804\uc1a1</li>'),
    ('<li><strong>Logging messages and tool results:</strong> Sent through the tool-specific SSE connection</li>',
     '<li><strong>\ub85c\uae45 \uba54\uc2dc\uc9c0 \ubc0f \ub3c4\uad6c \uacb0\uacfc:</strong> \ub3c4\uad6c \uc804\uc6a9 SSE \uc5f0\uacb0\uc744 \ud1b5\ud574 \uc804\uc1a1</li>'),
    ('<h2>Configuration Flags That Break the Workaround</h2>', '<h2>\uc6b0\ud68c \ubc29\ubc95\uc744 \ubb34\ud6a8\ud654\ud558\ub294 \uc124\uc815 \ud50c\ub798\uadf8</h2>'),
    ('StreamableHTTP includes two important configuration options:',
     'StreamableHTTP\uc5d0\ub294 \ub450 \uac00\uc9c0 \uc911\uc694\ud55c \uc124\uc815 \uc635\uc158\uc774 \uc788\uc2b5\ub2c8\ub2e4:'),
    ('Setting these to <code>True</code> can break the SSE workaround mechanism. You might want to enable these flags in certain scenarios, but doing so limits the full MCP functionality that depends on server-to-client communication.',
     '\uc774\ub4e4\uc744 <code>True</code>\ub85c \uc124\uc815\ud558\uba74 SSE \uc6b0\ud68c \uba54\ucee4\ub2c8\uc998\uc774 \ub9dd\uac00\uc9c8 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ud2b9\uc815 \uc2dc\ub098\ub9ac\uc624\uc5d0\uc11c \uc774 \ud50c\ub798\uadf8\ub97c \ud65c\uc131\ud654\ud560 \uc218 \uc788\uc9c0\ub9cc, \uc11c\ubc84\uc5d0\uc11c \ud074\ub77c\uc774\uc5b8\ud2b8\ub85c\uc758 \ud1b5\uc2e0\uc5d0 \uc758\uc874\ud558\ub294 \uc804\uccb4 MCP \uae30\ub2a5\uc774 \uc81c\ud55c\ub429\ub2c8\ub2e4.'),
    ('<h2>Key Takeaways</h2>', '<h2>\ud575\uc2ec \uc694\uc57d</h2>'),
    ("StreamableHTTP is more complex than other MCP transports because it has to work around HTTP's limitations. The SSE-based workaround enables full MCP functionality over HTTP, but understanding the dual-connection model is crucial for debugging and building robust applications.",
     "StreamableHTTP\ub294 HTTP\uc758 \uc81c\ud55c\uc744 \uc6b0\ud68c\ud574\uc57c \ud558\uae30 \ub54c\ubb38\uc5d0 \ub2e4\ub978 MCP \uc804\uc1a1 \ubc29\uc2dd\ubcf4\ub2e4 \ubcf5\uc7a1\ud569\ub2c8\ub2e4. SSE \uae30\ubc18 \uc6b0\ud68c \ubc29\ubc95\uc740 HTTP\ub97c \ud1b5\ud55c \uc804\uccb4 MCP \uae30\ub2a5\uc744 \uac00\ub2a5\ud558\uac8c \ud558\uc9c0\ub9cc, \ub514\ubc84\uae45\uacfc \uacac\uace0\ud55c \uc560\ud50c\ub9ac\ucf00\uc774\uc158 \uad6c\ucd95\uc744 \uc704\ud574 \uc774\uc911 \uc5f0\uacb0 \ubaa8\ub378\uc744 \uc774\ud574\ud558\ub294 \uac83\uc774 \uc911\uc694\ud569\ub2c8\ub2e4."),
    ('When building MCP applications with StreamableHTTP, remember that session IDs are required for all requests after initialization, and the system automatically manages multiple SSE connections to handle different types of server-to-client communication.',
     'StreamableHTTP\ub85c MCP \uc560\ud50c\ub9ac\ucf00\uc774\uc158\uc744 \uad6c\ucd95\ud560 \ub54c, \ucd08\uae30\ud654 \ud6c4 \ubaa8\ub4e0 \uc694\uccad\uc5d0 \uc138\uc158 ID\uac00 \ud544\uc694\ud558\uba70, \uc2dc\uc2a4\ud15c\uc774 \ub2e4\uc591\ud55c \uc720\ud615\uc758 \uc11c\ubc84-\ud074\ub77c\uc774\uc5b8\ud2b8 \ud1b5\uc2e0\uc744 \ucc98\ub9ac\ud558\uae30 \uc704\ud574 \uc5ec\ub7ec SSE \uc5f0\uacb0\uc744 \uc790\ub3d9\uc73c\ub85c \uad00\ub9ac\ud55c\ub2e4\ub294 \uc810\uc744 \uae30\uc5b5\ud558\uc138\uc694.'),
    # Footer
    ('<span>Previous</span>', '<span>\uc774\uc804</span>'),
    ('<span>Next</span>', '<span>\ub2e4\uc74c</span>'),
    ('aria-label="Toggle fullscreen"', 'aria-label="\uc804\uccb4\ud654\uba74 \uc804\ud658"'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
    else:
        print(f'NOT FOUND: {old[:70]}...', file=sys.stderr)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

korean = sum(1 for c in content if '\uac00' <= c <= '\ud7a3')
print(f'Replaced {count}/{len(replacements)} segments. Korean chars: {korean}', file=sys.stderr)
