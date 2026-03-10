#!/usr/bin/env python3
"""Translate all MCP Advanced Topics HTML files from English to Korean."""
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))

# Common UI/nav translations
COMMON = {
    'Header Navigation': '헤더 내비게이션',
    'Anthropic Academy': 'Anthropic 아카데미',
    '>Courses<': '>강좌<',
    'My Profile': '내 프로필',
    'Sign Out': '로그아웃',
    'Open in Claude': 'Claude에서 열기',
    'Ask questions about this course': '이 강좌에 대해 질문하기',
    'Copy notes': '노트 복사',
    'Copy full course notes for LLMs': 'LLM용 전체 강좌 노트 복사',
    '>Previous<': '>이전<',
    '>Downloads<': '>다운로드<',
    'Model Context Protocol: Advanced Topics': 'Model Context Protocol: 고급 주제',
    'Course Overview': '강좌 개요',
    '>Introduction<': '>소개<',
    ">Let's get started!<": '>시작해 봅시다!<',
    '>Core MCP features<': '>핵심 MCP 기능<',
    '>Sampling<': '>샘플링<',
    '>Sampling walkthrough<': '>샘플링 실습<',
    '>Log and progress notifications<': '>로그 및 진행 알림<',
    '>Notifications walkthrough<': '>알림 실습<',
    '>Roots<': '>루트<',
    '>Roots walkthrough<': '>루트 실습<',
    '>Survey<': '>설문조사<',
    'Course satisfaction survey': '강좌 만족도 설문조사',
    '>Transports and communication<': '>전송 및 통신<',
    '>JSON message types<': '>JSON 메시지 유형<',
    '>The STDIO transport<': '>STDIO 전송<',
    '>The StreamableHTTP transport<': '>StreamableHTTP 전송<',
    '>StreamableHTTP in depth<': '>StreamableHTTP 심화<',
    '>State and the StreamableHTTP transport<': '>상태와 StreamableHTTP 전송<',
    '>Assessment and next steps<': '>평가 및 다음 단계<',
    '>Assessment on MCP concepts<': '>MCP 개념 평가<',
    '>Wrapping up<': '>마무리<',
    'Hands-on with MCP servers': 'MCP 서버 실습',
    'Connecting with MCP clients': 'MCP 클라이언트 연결하기',
    'Assessment and wrap Up': '평가 및 마무리',
    'Sampling walkthrough': '샘플링 실습',
    'Notifications walkthrough': '알림 실습',
    'Roots walkthrough': '루트 실습',
}

FILES = {
    'Sampling': {
        'title=Sampling>': 'title=샘플링>',
        "Sampling allows a server to access a language model like Claude through a connected MCP client. Instead of the server directly calling Claude, it asks the client to make the call on its behalf. This s":
            "샘플링은 서버가 연결된 MCP 클라이언트를 통해 Claude와 같은 언어 모델에 접근할 수 있게 합니다. 서버가 직접 Claude를 호출하는 대신 클라이언트에게 대신 호출해 달라고 요청합니다.",
        'The Problem Sampling Solves': '샘플링이 해결하는 문제',
        "Imagine you have an MCP server with a research tool that fetches information from Wikipedia. After gathering all that data, you need to summarize it into a coherent report. You have two options:":
            "Wikipedia에서 정보를 가져오는 연구 도구가 있는 MCP 서버가 있다고 상상해 보세요. 모든 데이터를 수집한 후 일관된 보고서로 요약해야 합니다. 두 가지 옵션이 있습니다:",
        "Give the MCP server direct access to Claude. The server would need its own API key, handle authentication, manage costs, and implement all the Claude integration code. This works but adds significant ":
            "MCP 서버에 Claude 직접 접근 권한을 부여합니다. 서버는 자체 API 키가 필요하고, 인증을 처리하고, 비용을 관리하고, 모든 Claude 통합 코드를 구현해야 합니다. 작동하지만 상당한 복잡성이 추가됩니다.",
        "Use sampling. The server generates a prompt and asks the client \"Could you call Claude for me?\" The client, which already has a connection to Claude, makes the call and returns the results.":
            "샘플링을 사용합니다. 서버가 프롬프트를 생성하고 클라이언트에게 \"Claude를 대신 호출해 주실 수 있나요?\"라고 요청합니다. 이미 Claude와 연결이 있는 클라이언트가 호출하고 결과를 반환합니다.",
        'The flow is straightforward:': '흐름은 간단합니다:',
        'Server completes its work (like fetching Wikipedia articles)': '서버가 작업을 완료합니다 (예: Wikipedia 기사 가져오기)',
        'Server creates a prompt asking for text generation': '서버가 텍스트 생성을 요청하는 프롬프트를 만듭니다',
        'Server sends a sampling request to the client': '서버가 클라이언트에게 샘플링 요청을 보냅니다',
        'Client calls Claude with the provided prompt': '클라이언트가 제공된 프롬프트로 Claude를 호출합니다',
        'Client returns the generated text to the server': '클라이언트가 생성된 텍스트를 서버에 반환합니다',
        'Server uses the generated text in its response': '서버가 응답에 생성된 텍스트를 사용합니다',
        'Reduces server complexity:': '서버 복잡성 감소:',
        "The server doesn't need to integrate with language models directly": '서버가 언어 모델과 직접 통합할 필요가 없습니다',
        "The client pays for token usage, not the server": '클라이언트가 토큰 사용량을 지불하며, 서버가 아닙니다',
        "The server doesn't need credentials for Claude": '서버에 Claude 자격 증명이 필요 없습니다',
        'Perfect for public servers:': '공개 서버에 완벽:',
        "You don't want a public server racking up AI costs for every user": '공개 서버가 모든 사용자에 대해 AI 비용을 누적하는 것을 원하지 않습니다',
        'Setting up sampling requires code on both sides:': '샘플링 설정에는 양쪽 코드가 필요합니다:',
        'function to request text generation:': '함수를 사용하여 텍스트 생성을 요청합니다:',
        'Create a sampling callback that handles the server\'s requests:': '서버의 요청을 처리하는 샘플링 콜백을 만듭니다:',
        'Then pass this callback when initializing your client session:': '그런 다음 클라이언트 세션을 초기화할 때 이 콜백을 전달합니다:',
        "Sampling is most valuable when building publicly accessible MCP servers. You don't want random users generating unlimited text at your expense. By using sampling, each client pays for their own AI usa":
            "샘플링은 공개적으로 접근 가능한 MCP 서버를 구축할 때 가장 유용합니다. 무작위 사용자가 비용 부담 없이 무제한으로 텍스트를 생성하는 것을 원하지 않습니다. 샘플링을 사용하면 각 클라이언트가 자체 AI 사용량을 지불합니다.",
        'The technique essentially moves the AI integration complexity from your server to the client, which often already has the necessary connections and credentials in place.':
            '이 기술은 본질적으로 AI 통합 복잡성을 서버에서 클라이언트로 옮기며, 클라이언트에는 이미 필요한 연결과 자격 증명이 갖추어져 있는 경우가 많습니다.',
    },
    'Log and progress notifications': {
        'title="Log and progress notifications"': 'title="로그 및 진행 알림"',
        "Logging and progress notifications are simple to implement but make a huge difference in user experience when working with MCP servers. They help users understand what's happening during long-running ":
            "로깅 및 진행 알림은 구현이 간단하지만 MCP 서버 작업 시 사용자 경험에 큰 차이를 만듭니다. 장시간 실행되는 작업 중에 무슨 일이 일어나고 있는지 사용자가 이해할 수 있도록 도와줍니다.",
        "When Claude calls a tool that takes time to complete - like researching a topic or processing data - users typically see nothing until the operation finishes. This can be frustrating because they don'":
            "Claude가 완료하는 데 시간이 걸리는 도구를 호출할 때 - 주제를 조사하거나 데이터를 처리하는 것처럼 - 사용자는 일반적으로 작업이 완료될 때까지 아무것도 볼 수 없습니다. 무슨 일이 일어나고 있는지 모르기 때문에 답답할 수 있습니다.",
        "With logging and progress notifications enabled, users get real-time feedback showing exactly what's happening behind the scenes. They can see progress bars, status messages, and detailed logs as the ":
            "로깅 및 진행 알림이 활성화되면 사용자는 백그라운드에서 정확히 무슨 일이 일어나고 있는지 보여주는 실시간 피드백을 받습니다. 작업이 실행되는 동안 진행 표시줄, 상태 메시지, 상세 로그를 볼 수 있습니다.",
        "In the Python MCP SDK, logging and progress notifications work through the Context argument that's automatically provided to your tool functions. This context object gives you methods to communicate b":
            "Python MCP SDK에서 로깅 및 진행 알림은 도구 함수에 자동으로 제공되는 Context 인수를 통해 작동합니다. 이 컨텍스트 객체는 작업 중 클라이언트와 통신할 수 있는 메서드를 제공합니다.",
        "The key methods you'll use are:": '사용할 주요 메서드는 다음과 같습니다:',
        '- Send log messages to the client': '- 클라이언트에 로그 메시지 전송',
        '- Update progress with current and total values': '- 현재 값과 총 값으로 진행 상황 업데이트',
        'Client-Side Implementation': '클라이언트 측 구현',
        "On the client side, you need to set up callback functions to handle these notifications. The server emits these messages, but it's up to your client application to decide how to present them to users.":
            "클라이언트 측에서는 이러한 알림을 처리하기 위한 콜백 함수를 설정해야 합니다. 서버가 이러한 메시지를 보내지만, 사용자에게 어떻게 표시할지는 클라이언트 애플리케이션이 결정합니다.",
        'You provide the logging callback when creating the client session, and the progress callback when making individual tool calls. This gives you flexibility to handle different types of notifications ap':
            '클라이언트 세션을 만들 때 로깅 콜백을, 개별 도구 호출 시 진행 콜백을 제공합니다. 이를 통해 다양한 유형의 알림을 적절하게 처리할 수 있는 유연성을 갖습니다.',
        'How you present these notifications depends on your application type:': '이러한 알림을 표시하는 방법은 애플리케이션 유형에 따라 다릅니다:',
        '- Simply print messages and progress to the terminal': '- 터미널에 메시지와 진행 상황을 간단히 출력',
        '- Use WebSockets, server-sent events, or polling to push updates to the browser': '- WebSocket, 서버 전송 이벤트 또는 폴링을 사용하여 브라우저에 업데이트 푸시',
        '- Update progress bars and status displays in your UI': '- UI에서 진행 표시줄 및 상태 표시 업데이트',
        "Remember that implementing these notifications is entirely optional. You can choose to ignore them completely, show only certain types, or present them however makes sense for your application. They'r":
            "이러한 알림 구현은 전적으로 선택 사항임을 기억하세요. 완전히 무시하거나, 특정 유형만 표시하거나, 애플리케이션에 맞는 방식으로 표시할 수 있습니다.",
    },
    'Roots': {
        'title=Roots>': 'title=루트>',
        'Roots are a way to grant MCP servers access to specific files and folders on your local machine. Think of them as a permission system that says "Hey, MCP server, you can access these files" - but they':
            '루트는 MCP 서버에 로컬 머신의 특정 파일과 폴더에 대한 접근 권한을 부여하는 방법입니다. "MCP 서버야, 이 파일들에 접근할 수 있어"라고 말하는 권한 시스템이라고 생각하면 됩니다.',
        'The Problem Roots Solve': '루트가 해결하는 문제',
        "Without roots, you'd run into a common issue. Imagine you have an MCP server with a video conversion tool that takes a file path and converts an MP4 to MOV format.":
            "루트가 없으면 흔한 문제에 부딪히게 됩니다. 파일 경로를 받아 MP4를 MOV 형식으로 변환하는 비디오 변환 도구가 있는 MCP 서버가 있다고 상상해 보세요.",
        'When a user asks Claude to "convert biking.mp4 to mov format", Claude would call the tool with just the filename. But here\'s the problem - Claude has no way to search through your entire file system t':
            '사용자가 Claude에게 "biking.mp4를 mov 형식으로 변환해 줘"라고 요청하면, Claude는 파일명만으로 도구를 호출합니다. 하지만 문제는 - Claude가 전체 파일 시스템을 검색할 방법이 없다는 것입니다.',
        "Your file system might be complex with files scattered across different directories. The user knows the biking.mp4 file is in their Movies folder, but Claude doesn't have that context.":
            "파일 시스템은 여러 디렉토리에 파일이 흩어져 있어 복잡할 수 있습니다. 사용자는 biking.mp4 파일이 Movies 폴더에 있다는 것을 알지만, Claude는 그 컨텍스트가 없습니다.",
        "You could solve this by requiring users to always provide full paths, but that's not very user-friendly. Nobody wants to type out complete file paths every time.":
            "사용자에게 항상 전체 경로를 제공하도록 요구하여 이 문제를 해결할 수 있지만, 그다지 사용자 친화적이지 않습니다. 매번 전체 파일 경로를 입력하고 싶은 사람은 없습니다.",
        "Here's how the workflow changes with roots:": '루트를 사용하면 워크플로우가 다음과 같이 변경됩니다:',
        'User asks to convert a video file': '사용자가 비디오 파일 변환을 요청합니다',
        'to see what directories it can access': '접근 가능한 디렉토리를 확인합니다',
        'on accessible directories to find the file': '접근 가능한 디렉토리에서 파일을 찾습니다',
        'Once found, Claude calls the conversion tool with the full path': '파일을 찾으면 Claude가 전체 경로로 변환 도구를 호출합니다',
        'This happens automatically - users can still just say "convert biking.mp4" without providing full paths.':
            '이 과정은 자동으로 이루어집니다 - 사용자는 전체 경로를 제공하지 않고도 "biking.mp4 변환해 줘"라고만 말하면 됩니다.',
        'Security and Boundaries': '보안 및 경계',
        "Roots also provide security by limiting access. If you only grant access to your Desktop folder, the MCP server cannot access files in other locations like Documents or Downloads.":
            "루트는 접근을 제한하여 보안도 제공합니다. Desktop 폴더에만 접근 권한을 부여하면 MCP 서버는 Documents나 Downloads 같은 다른 위치의 파일에 접근할 수 없습니다.",
        "When Claude tries to access a file outside the approved roots, it gets an error and can inform the user that the file isn't accessible from the current server configuration.":
            "Claude가 승인된 루트 외부의 파일에 접근하려고 하면 오류가 발생하고, 현재 서버 구성에서 해당 파일에 접근할 수 없다고 사용자에게 알릴 수 있습니다.",
        'Implementation Details': '구현 세부 사항',
        "The MCP SDK doesn't automatically enforce root restrictions - you need to implement this yourself. A typical pattern is to create a helper function like":
            "MCP SDK는 루트 제한을 자동으로 적용하지 않습니다 - 직접 구현해야 합니다. 일반적인 패턴은 다음과 같은 헬퍼 함수를 만드는 것입니다:",
        'Takes a requested file path': '요청된 파일 경로를 받습니다',
        'Gets the list of approved roots': '승인된 루트 목록을 가져옵니다',
        'Checks if the requested path falls within one of those roots': '요청된 경로가 승인된 루트 중 하나에 해당하는지 확인합니다',
        'Returns true/false for access permission': '접근 권한에 대해 true/false를 반환합니다',
        'You then call this function in any tool that accesses files or directories before performing the actual file operation.':
            '그런 다음 실제 파일 작업을 수행하기 전에 파일이나 디렉토리에 접근하는 모든 도구에서 이 함수를 호출합니다.',
        "- Users don't need to provide full file paths": '- 사용자가 전체 파일 경로를 제공할 필요 없음',
        '- Claude only looks in approved directories, making file discovery faster': '- Claude가 승인된 디렉토리에서만 검색하여 파일 발견이 더 빠름',
        '- Prevents accidental access to sensitive files outside approved areas': '- 승인된 영역 밖의 민감한 파일에 대한 실수로 인한 접근 방지',
        '- You can provide roots through tools or inject them directly into prompts': '- 도구를 통해 루트를 제공하거나 프롬프트에 직접 주입 가능',
        'Roots make MCP servers both more powerful and more secure by giving Claude the context it needs to find files while maintaining clear boundaries around what it can access.':
            '루트는 Claude가 파일을 찾는 데 필요한 컨텍스트를 제공하면서 접근 가능한 범위에 대한 명확한 경계를 유지하여 MCP 서버를 더 강력하고 안전하게 만듭니다.',
    },
    'JSON message types': {
        'title="JSON message types"': 'title="JSON 메시지 유형"',
        "MCP (Model Context Protocol) uses JSON messages to handle communication between clients and servers. Understanding these message types is crucial for working with MCP, especially when dealing with dif":
            "MCP(Model Context Protocol)는 JSON 메시지를 사용하여 클라이언트와 서버 간의 통신을 처리합니다. 이러한 메시지 유형을 이해하는 것은 MCP 작업에 중요하며, 특히 다른 전송 방법을 다룰 때 그렇습니다.",
        "All MCP communication happens through JSON messages. Each message type serves a specific purpose - whether it's calling a tool, listing available resources, or sending notifications about system event":
            "모든 MCP 통신은 JSON 메시지를 통해 이루어집니다. 각 메시지 유형은 특정 목적을 수행합니다 - 도구 호출, 사용 가능한 리소스 나열, 시스템 이벤트에 대한 알림 전송 등입니다.",
        'Here\'s a typical example: when Claude needs to call a tool provided by an MCP server, the client sends a "Call Tool Request" message. The server processes this request, runs the tool, and responds wit':
            '일반적인 예시: Claude가 MCP 서버에서 제공하는 도구를 호출해야 할 때, 클라이언트는 "Call Tool Request" 메시지를 보냅니다. 서버가 이 요청을 처리하고, 도구를 실행하고, 응답합니다.',
        "The complete list of message types is defined in the official MCP specification repository on GitHub. This specification is separate from the various SDK repositories (like Python or TypeScript SDKs) ":
            "메시지 유형의 전체 목록은 GitHub의 공식 MCP 사양 저장소에 정의되어 있습니다. 이 사양은 다양한 SDK 저장소(Python 또는 TypeScript SDK 등)와 별개입니다.",
        "The message types are written in TypeScript for convenience - not because they're executed as TypeScript code, but because TypeScript provides a clear way to describe data structures and types.":
            "메시지 유형은 편의상 TypeScript로 작성되어 있습니다 - TypeScript 코드로 실행되기 때문이 아니라, TypeScript가 데이터 구조와 타입을 명확하게 설명하는 방법을 제공하기 때문입니다.",
        'MCP messages fall into two main categories:': 'MCP 메시지는 두 가지 주요 범주로 나뉩니다:',
        'Request-Result Messages': '요청-결과 메시지',
        'These messages always come in pairs. You send a request and expect to get a result back:': '이 메시지는 항상 쌍으로 옵니다. 요청을 보내면 결과를 돌려받을 것으로 기대합니다:',
        'List Prompts Request → List Prompts Result': '프롬프트 목록 요청 → 프롬프트 목록 결과',
        'Read Resource Request → Read Resource Result': '리소스 읽기 요청 → 리소스 읽기 결과',
        'Initialize Request → Initialize Result': '초기화 요청 → 초기화 결과',
        'Notification Messages': '알림 메시지',
        "These are one-way messages that inform about events but don't require a response:": '이것은 이벤트에 대해 알리지만 응답이 필요 없는 단방향 메시지입니다:',
        'Progress Notification': '진행 알림',
        '- Updates on long-running operations': '- 장시간 실행 작업에 대한 업데이트',
        'Logging Message Notification': '로깅 메시지 알림',
        '- System log messages': '- 시스템 로그 메시지',
        'Tool List Changed Notification': '도구 목록 변경 알림',
        '- When available tools change': '- 사용 가능한 도구가 변경될 때',
        'Resource Updated Notification': '리소스 업데이트 알림',
        '- When resources are modified': '- 리소스가 수정될 때',
        'Client vs Server Messages': '클라이언트 대 서버 메시지',
        'The MCP specification organizes messages by who sends them:': 'MCP 사양은 메시지를 보내는 주체별로 구성합니다:',
        'include requests that clients send to servers (like tool calls) and notifications that clients might send.': '클라이언트가 서버에 보내는 요청(도구 호출 등)과 클라이언트가 보낼 수 있는 알림을 포함합니다.',
        'include requests that servers send to clients and notifications that servers broadcast.': '서버가 클라이언트에 보내는 요청과 서버가 브로드캐스트하는 알림을 포함합니다.',
        "Understanding that servers can send messages to clients is particularly important when working with different transport methods. Some transports, like the streamable HTTP transport, have limitations o":
            "서버가 클라이언트에 메시지를 보낼 수 있다는 것을 이해하는 것은 다양한 전송 방법으로 작업할 때 특히 중요합니다. streamable HTTP 전송과 같은 일부 전송에는 제한이 있습니다.",
        "The key insight is that MCP is designed as a bidirectional protocol - both clients and servers can initiate communication. This becomes crucial when you need to choose the right transport method for y":
            "핵심 인사이트는 MCP가 양방향 프로토콜로 설계되었다는 것입니다 - 클라이언트와 서버 모두 통신을 시작할 수 있습니다. 이는 사용 사례에 적합한 전송 방법을 선택해야 할 때 중요해집니다.",
    },
    'The STDIO transport': {
        'title="The STDIO transport"': 'title="STDIO 전송"',
        "MCP clients and servers communicate by exchanging JSON messages, but how do these messages actually get transmitted? The communication channel used is called a":
            "MCP 클라이언트와 서버는 JSON 메시지를 교환하여 통신하지만, 이 메시지는 실제로 어떻게 전송될까요? 사용되는 통신 채널을",
        ", and there are several ways to implement this - from HTTP requests to WebSockets to even writing JSON on a postcard (though that last one isn't recommended for production use).":
            "이라고 하며, HTTP 요청부터 WebSocket, 심지어 엽서에 JSON을 쓰는 것까지(마지막 방법은 프로덕션 사용에는 권장하지 않지만) 여러 구현 방법이 있습니다.",
        "When you're first developing an MCP server or client, the most commonly used transport is the":
            "MCP 서버나 클라이언트를 처음 개발할 때, 가장 일반적으로 사용되는 전송은",
        ". This approach is straightforward: the client launches the MCP server as a subprocess and communicates through standard input and output streams.":
            "입니다. 이 접근 방식은 간단합니다: 클라이언트가 MCP 서버를 서브프로세스로 실행하고 표준 입출력 스트림을 통해 통신합니다.",
        "Client sends messages to the server using the server's": "클라이언트는 서버의",
        'Server responds by writing to': '서버는 다음에 작성하여 응답합니다:',
        'Either the server or client can send a message at any time': '서버나 클라이언트 모두 언제든지 메시지를 보낼 수 있습니다',
        'Only works when client and server run on the same machine': '클라이언트와 서버가 같은 머신에서 실행될 때만 작동합니다',
        'Seeing Stdio in Action': 'Stdio 동작 확인',
        "You can actually test an MCP server directly from your terminal without writing a separate client. When you run a server with":
            "별도의 클라이언트를 작성하지 않고 터미널에서 직접 MCP 서버를 테스트할 수 있습니다. 서버를 다음으로 실행하면",
        ", it listens to stdin and writes responses to stdout. This means you can paste JSON messages directly into your terminal and see the server's responses immediately.":
            ", stdin을 수신하고 stdout에 응답을 작성합니다. 이는 JSON 메시지를 터미널에 직접 붙여넣고 서버의 응답을 즉시 볼 수 있다는 의미입니다.",
        'The terminal output shows the complete message exchange, including example messages for initialization and tool calls.':
            '터미널 출력은 초기화 및 도구 호출을 위한 예시 메시지를 포함한 전체 메시지 교환을 보여줍니다.',
        'MCP Connection Sequence': 'MCP 연결 시퀀스',
        'Every MCP connection must start with a specific three-message handshake:': '모든 MCP 연결은 특정 세 가지 메시지 핸드셰이크로 시작해야 합니다:',
        '- Client sends this first': '- 클라이언트가 먼저 전송',
        '- Server responds with capabilities': '- 서버가 기능으로 응답',
        'Initialized Notification': '초기화 완료 알림',
        '- Client confirms (no response expected)': '- 클라이언트가 확인 (응답 불필요)',
        'Only after this handshake can you send other requests like tool calls or prompt listings.':
            '이 핸드셰이크 이후에만 도구 호출이나 프롬프트 목록과 같은 다른 요청을 보낼 수 있습니다.',
        'Message Types and Flow': '메시지 유형 및 흐름',
        'MCP supports various message types that flow in both directions:': 'MCP는 양방향으로 흐르는 다양한 메시지 유형을 지원합니다:',
        "The key insight is that some messages require responses (requests → results) while others don't (notifications). Both client and server can initiate communication at any time.":
            "핵심 인사이트는 일부 메시지는 응답이 필요하고(요청 → 결과) 다른 메시지는 필요 없다는 것입니다(알림). 클라이언트와 서버 모두 언제든지 통신을 시작할 수 있습니다.",
        'Four Communication Scenarios': '네 가지 통신 시나리오',
        'With any transport, you need to handle four different communication patterns:': '어떤 전송이든 네 가지 다른 통신 패턴을 처리해야 합니다:',
        'Client → Server request': '클라이언트 → 서버 요청',
        ': Client writes to stdin': ': 클라이언트가 stdin에 작성',
        'Server → Client response': '서버 → 클라이언트 응답',
        ': Server writes to stdout': ': 서버가 stdout에 작성',
        'Server → Client request': '서버 → 클라이언트 요청',
        'Client → Server response': '클라이언트 → 서버 응답',
        "The beauty of stdio transport is its simplicity - either party can initiate communication at any time using these two channels.":
            "stdio 전송의 장점은 단순함입니다 - 어느 쪽이든 이 두 채널을 사용하여 언제든지 통신을 시작할 수 있습니다.",
        "Understanding stdio transport is crucial because it represents the \"ideal\" case where bidirectional communication is seamless. When we move to other transports like HTTP, we'll encounter limitations w":
            "stdio 전송을 이해하는 것이 중요한 이유는 양방향 통신이 원활한 \"이상적인\" 사례를 나타내기 때문입니다. HTTP와 같은 다른 전송으로 넘어가면 제한 사항이 발생합니다.",
        "For development and testing, stdio transport is perfect. For production deployments where client and server need to run on different machines, you'll need to consider other transport options with thei":
            "개발 및 테스트에는 stdio 전송이 완벽합니다. 클라이언트와 서버가 다른 머신에서 실행되어야 하는 프로덕션 배포에는 각각의 트레이드오프가 있는 다른 전송 옵션을 고려해야 합니다.",
    },
    'The StreamableHTTP transport': {
        'title="The StreamableHTTP transport"': 'title="StreamableHTTP 전송"',
        "The streamable HTTP transport enables MCP clients to connect to remotely hosted servers over HTTP connections. Unlike the standard I/O transport that requires both client and server on the same machin":
            "streamable HTTP 전송은 MCP 클라이언트가 HTTP 연결을 통해 원격 호스팅된 서버에 연결할 수 있게 합니다. 클라이언트와 서버가 같은 머신에 있어야 하는 표준 I/O 전송과 달리,",
        "However, there's an important caveat: some configuration settings can significantly limit your MCP server's functionality. If your application works perfectly with standard I/O transport locally but b":
            "그러나 중요한 주의점이 있습니다: 일부 구성 설정이 MCP 서버의 기능을 크게 제한할 수 있습니다. 애플리케이션이 로컬에서 표준 I/O 전송으로 완벽하게 작동하지만",
        'Configuration Settings That Matter': '중요한 구성 설정',
        'Two key settings control how the streamable HTTP transport behaves:': 'streamable HTTP 전송의 동작을 제어하는 두 가지 핵심 설정이 있습니다:',
        '- Controls connection state management': '- 연결 상태 관리를 제어',
        '- Controls response format handling': '- 응답 형식 처리를 제어',
        'The HTTP Communication Challenge': 'HTTP 통신 과제',
        'To understand why these limitations exist, we need to review how HTTP communication works. In standard HTTP:':
            '이러한 제한이 존재하는 이유를 이해하려면 HTTP 통신 작동 방식을 검토해야 합니다. 표준 HTTP에서:',
        'Clients can easily initiate requests to servers (the server has a known URL)': '클라이언트는 서버에 쉽게 요청을 시작할 수 있습니다 (서버에 알려진 URL이 있으므로)',
        'Servers can easily respond to these requests': '서버는 이러한 요청에 쉽게 응답할 수 있습니다',
        "Servers cannot easily initiate requests to clients (clients don't have known URLs)": '서버는 클라이언트에 쉽게 요청을 시작할 수 없습니다 (클라이언트에 알려진 URL이 없으므로)',
        'Response patterns from client back to server become problematic': '클라이언트에서 서버로의 응답 패턴이 문제가 됩니다',
        'MCP Message Types Affected': '영향 받는 MCP 메시지 유형',
        'This HTTP limitation impacts specific MCP communication patterns. The following message types become difficult to implement with plain HTTP:':
            '이 HTTP 제한은 특정 MCP 통신 패턴에 영향을 미칩니다. 다음 메시지 유형은 일반 HTTP로 구현하기 어려워집니다:',
        'Server-initiated requests:': '서버에서 시작하는 요청:',
        'Create Message requests, List Roots requests': '메시지 생성 요청, 루트 목록 요청',
        'Progress notifications, Logging notifications, Initialized notifications, Cancelled notifications':
            '진행 알림, 로깅 알림, 초기화 알림, 취소 알림',
        "These are exactly the features that break when you enable the restrictive HTTP settings. Progress bars disappear, logging stops working, and server-initiated sampling requests fail.":
            "이것들이 바로 제한적인 HTTP 설정을 활성화할 때 깨지는 기능들입니다. 진행 표시줄이 사라지고, 로깅이 작동을 멈추고, 서버에서 시작하는 샘플링 요청이 실패합니다.",
        'The Streamable HTTP Solution': 'Streamable HTTP 솔루션',
        "The streamable HTTP transport does provide a clever solution to work around HTTP's limitations, but it comes with trade-offs. When you're forced to use":
            "streamable HTTP 전송은 HTTP의 제한을 해결하기 위한 영리한 솔루션을 제공하지만 트레이드오프가 있습니다.",
        "Understanding these limitations helps you make informed decisions about:": '이러한 제한을 이해하면 다음에 대해 정보에 입각한 결정을 내리는 데 도움이 됩니다:',
        'Which transport to use for different deployment scenarios': '다른 배포 시나리오에 어떤 전송을 사용할지',
        'How to design your MCP server to gracefully handle HTTP constraints': 'HTTP 제약 조건을 우아하게 처리하도록 MCP 서버를 설계하는 방법',
        'When to accept reduced functionality for the benefits of remote hosting': '원격 호스팅의 이점을 위해 감소된 기능을 수용할 시기',
        "The key is knowing that these restrictions exist and planning your MCP server architecture accordingly. If your application heavily relies on server-initiated requests or real-time notifications, you ":
            "핵심은 이러한 제한이 존재한다는 것을 알고 그에 따라 MCP 서버 아키텍처를 계획하는 것입니다. 애플리케이션이 서버에서 시작하는 요청이나 실시간 알림에 크게 의존하는 경우,",
    },
    'StreamableHTTP in depth': {
        'title="StreamableHTTP in depth"': 'title="StreamableHTTP 심화"',
        "StreamableHTTP is MCP's solution to a fundamental problem: some MCP functionality requires the server to make requests to the client, but HTTP makes this challenging. Let's explore how StreamableHTTP ":
            "StreamableHTTP은 근본적인 문제에 대한 MCP의 솔루션입니다: 일부 MCP 기능은 서버가 클라이언트에 요청해야 하지만 HTTP는 이를 어렵게 만듭니다. StreamableHTTP이 어떻게 작동하는지 살펴봅시다.",
        "Some MCP features like sampling, notifications, and logging rely on the server initiating requests to the client. However, HTTP is designed for clients to make requests to servers, not the other way a":
            "샘플링, 알림, 로깅과 같은 일부 MCP 기능은 서버가 클라이언트에 요청을 시작하는 것에 의존합니다. 그러나 HTTP는 클라이언트가 서버에 요청하도록 설계되어 있으며, 그 반대가 아닙니다.",
        'How StreamableHTTP Works': 'StreamableHTTP 작동 방식',
        'The magic happens through a multi-step process that establishes persistent connections between client and server.':
            '마법은 클라이언트와 서버 간에 영구 연결을 설정하는 다단계 프로세스를 통해 발생합니다.',
        'Initial Connection Setup': '초기 연결 설정',
        'The process starts like any MCP connection:': '프로세스는 모든 MCP 연결과 마찬가지로 시작됩니다:',
        'This session ID is crucial - it uniquely identifies the client and must be included in all future requests.':
            '이 세션 ID는 중요합니다 - 클라이언트를 고유하게 식별하며 향후 모든 요청에 포함되어야 합니다.',
        "After initialization, the client can make a GET request to establish a Server-Sent Events connection. This creates a long-lived HTTP response that the server can use to stream messages back to the cli":
            "초기화 후 클라이언트는 GET 요청을 하여 Server-Sent Events 연결을 설정할 수 있습니다. 이는 서버가 클라이언트에 메시지를 스트리밍하는 데 사용할 수 있는 장기 HTTP 응답을 생성합니다.",
        'This SSE connection is the key to allowing server-to-client communication. The server can now send requests, notifications, and other messages through this persistent channel.':
            '이 SSE 연결은 서버에서 클라이언트로의 통신을 가능하게 하는 핵심입니다. 서버는 이제 이 영구 채널을 통해 요청, 알림 및 기타 메시지를 보낼 수 있습니다.',
        'Tool Calls and Dual SSE Connections': '도구 호출 및 이중 SSE 연결',
        'When the client makes a tool call, things get more complex. The system creates two separate SSE connections:':
            '클라이언트가 도구를 호출하면 상황이 더 복잡해집니다. 시스템은 두 개의 별도 SSE 연결을 생성합니다:',
        'Primary SSE Connection:': '기본 SSE 연결:',
        'Used for server-initiated requests and stays open indefinitely': '서버에서 시작하는 요청에 사용되며 무기한 열려 있음',
        'Tool-Specific SSE Connection:': '도구별 SSE 연결:',
        'Created for each tool call and closes automatically when the tool result is sent': '각 도구 호출에 대해 생성되며 도구 결과가 전송되면 자동으로 닫힘',
        'Different types of messages get routed through different connections:': '다른 유형의 메시지는 다른 연결을 통해 라우팅됩니다:',
        'Progress notifications:': '진행 알림:',
        'Sent through the primary SSE connection': '기본 SSE 연결을 통해 전송',
        'Logging messages and tool results:': '로깅 메시지 및 도구 결과:',
        'Sent through the tool-specific SSE connection': '도구별 SSE 연결을 통해 전송',
        'Configuration Flags That Break the Workaround': '우회 방법을 깨뜨리는 구성 플래그',
        "StreamableHTTP includes two important configuration options:": 'StreamableHTTP에는 두 가지 중요한 구성 옵션이 있습니다:',
        "can break the SSE workaround mechanism. You might want to enable these flags in certain scenarios, but doing so limits the full MCP functionality that depends on server-to-client communication.":
            "이 SSE 우회 메커니즘을 깨뜨릴 수 있습니다. 특정 시나리오에서 이 플래그를 활성화하고 싶을 수 있지만, 그렇게 하면 서버에서 클라이언트로의 통신에 의존하는 전체 MCP 기능이 제한됩니다.",
        "StreamableHTTP is more complex than other MCP transports because it has to work around HTTP's limitations. The SSE-based workaround enables full MCP functionality over HTTP, but understanding the dual":
            "StreamableHTTP은 HTTP의 제한을 해결해야 하기 때문에 다른 MCP 전송보다 더 복잡합니다. SSE 기반 우회는 HTTP를 통한 전체 MCP 기능을 가능하게 하지만, 이중 연결을 이해하는 것이 중요합니다.",
        'When building MCP applications with StreamableHTTP, remember that session IDs are required for all requests after initialization, and the system automatically manages multiple SSE connections to handl':
            'StreamableHTTP으로 MCP 애플리케이션을 구축할 때, 초기화 후 모든 요청에 세션 ID가 필요하며, 시스템이 자동으로 여러 SSE 연결을 관리한다는 것을 기억하세요.',
    },
    'State and the StreamableHTTP transport': {
        'title="State and the StreamableHTTP transport"': 'title="상태와 StreamableHTTP 전송"',
        "flags in MCP servers control fundamental aspects of how your server behaves. Understanding when and why to use them is crucial, especially if you're planning to scale your server or deploy it in produ":
            "MCP 서버의 플래그는 서버 동작의 근본적인 측면을 제어합니다. 언제, 왜 사용하는지 이해하는 것이 중요하며, 특히 서버를 확장하거나 프로덕션에 배포하려는 경우 그렇습니다.",
        'When You Need Stateless HTTP': '무상태 HTTP가 필요한 경우',
        "Imagine you build an MCP server that becomes popular. Initially, you might have just a few clients connecting to a single server instance:":
            "인기 있는 MCP 서버를 구축한다고 상상해 보세요. 처음에는 단일 서버 인스턴스에 연결하는 클라이언트가 몇 개뿐일 수 있습니다:",
        "As your server grows, you might have thousands of clients trying to connect. Running a single server instance won't scale to handle all that traffic:":
            "서버가 성장하면 수천 개의 클라이언트가 연결하려고 할 수 있습니다. 단일 서버 인스턴스로는 그 모든 트래픽을 처리할 수 없습니다:",
        'The typical solution is horizontal scaling - running multiple server instances behind a load balancer:':
            '일반적인 해결책은 수평 확장입니다 - 로드 밸런서 뒤에서 여러 서버 인스턴스를 실행합니다:',
        "But here's where things get complicated. Remember that MCP clients need two separate connections:":
            "하지만 여기서 상황이 복잡해집니다. MCP 클라이언트에는 두 개의 별도 연결이 필요하다는 것을 기억하세요:",
        'A GET SSE connection for receiving server-to-client requests': '서버에서 클라이언트로의 요청을 받기 위한 GET SSE 연결',
        'POST requests for calling tools and receiving responses': '도구 호출 및 응답 수신을 위한 POST 요청',
        "With a load balancer, these requests might get routed to different server instances. If your tool needs to use Claude (through sampling), the server handling the POST request would need to coordinate ":
            "로드 밸런서를 사용하면 이러한 요청이 다른 서버 인스턴스로 라우팅될 수 있습니다. 도구가 Claude를 사용해야 하는 경우(샘플링을 통해), POST 요청을 처리하는 서버가 조율해야 합니다.",
        'How Stateless HTTP Solves This': '무상태 HTTP가 이를 해결하는 방법',
        'eliminates this coordination problem, but with significant trade-offs:': '이 조율 문제를 제거하지만, 상당한 트레이드오프가 있습니다:',
        'When stateless HTTP is enabled:': '무상태 HTTP가 활성화되면:',
        "Clients don't get session IDs": '클라이언트는 세션 ID를 받지 않습니다',
        "- the server can't track individual clients": '- 서버가 개별 클라이언트를 추적할 수 없음',
        'No server-to-client requests': '서버에서 클라이언트로의 요청 없음',
        '- the GET SSE pathway becomes unavailable': '- GET SSE 경로가 사용 불가능해짐',
        "- can't use Claude or other AI models": '- Claude 또는 다른 AI 모델을 사용할 수 없음',
        "- can't send progress updates during long operations": '- 장시간 작업 중 진행 업데이트를 보낼 수 없음',
        "- can't notify clients about resource updates": '- 리소스 업데이트에 대해 클라이언트에 알릴 수 없음',
        "However, there's one benefit:": '그러나 한 가지 이점이 있습니다:',
        'client initialization is no longer required': '클라이언트 초기화가 더 이상 필요하지 않음',
        '. Clients can make requests directly without the initial handshake process.': '. 클라이언트는 초기 핸드셰이크 프로세스 없이 직접 요청할 수 있습니다.',
        'Understanding JSON Response': 'JSON 응답 이해',
        'flag is simpler - it just disables streaming for POST request responses. Instead of getting multiple SSE messages as a tool executes, you get only the final result as plain JSON.':
            '플래그는 더 간단합니다 - POST 요청 응답에 대한 스트리밍을 비활성화합니다. 도구가 실행되는 동안 여러 SSE 메시지를 받는 대신 최종 결과만 일반 JSON으로 받습니다.',
        'With streaming disabled:': '스트리밍이 비활성화되면:',
        'No intermediate progress messages': '중간 진행 메시지 없음',
        'No log statements during execution': '실행 중 로그 문 없음',
        'Just the final tool result': '최종 도구 결과만',
        'When to Use These Flags': '이러한 플래그를 사용할 시기',
        'Use stateless HTTP when:': '다음의 경우 무상태 HTTP를 사용하세요:',
        'You need horizontal scaling with load balancers': '로드 밸런서를 사용한 수평 확장이 필요한 경우',
        "You don't need server-to-client communication": '서버에서 클라이언트로의 통신이 필요 없는 경우',
        "Your tools don't require AI model sampling": '도구가 AI 모델 샘플링을 필요로 하지 않는 경우',
        'You want to minimize connection overhead': '연결 오버헤드를 최소화하려는 경우',
        'Use JSON response when:': '다음의 경우 JSON 응답을 사용하세요:',
        "You don't need streaming responses": '스트리밍 응답이 필요 없는 경우',
        'You prefer simpler, non-streaming HTTP responses': '더 간단한 비스트리밍 HTTP 응답을 선호하는 경우',
        "You're integrating with systems that expect plain JSON": '일반 JSON을 기대하는 시스템과 통합하는 경우',
        'Development vs Production': '개발 대 프로덕션',
        "If you're developing locally with standard I/O transport but planning to deploy with HTTP transport, test with the same transport you'll use in production. The behavior differences between stateful an":
            "표준 I/O 전송으로 로컬에서 개발하지만 HTTP 전송으로 배포할 계획이라면, 프로덕션에서 사용할 동일한 전송으로 테스트하세요. 상태 유지와 무상태 간의 동작 차이는",
        'These flags fundamentally change how your MCP server operates, so choose them based on your specific scaling and functionality requirements.':
            '이러한 플래그는 MCP 서버의 작동 방식을 근본적으로 변경하므로, 특정 확장 및 기능 요구 사항에 따라 선택하세요.',
    },
}

def translate_file(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    all_trans = {**COMMON, **translations}
    sorted_items = sorted(all_trans.items(), key=lambda x: len(x[0]), reverse=True)

    for eng, kor in sorted_items:
        if eng in content:
            content = content.replace(eng, kor)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return content != original

# Process files
for lesson_name, translations in FILES.items():
    matches = [f for f in os.listdir(FOLDER)
               if f.startswith(lesson_name) and f.endswith('.html') and f != 'index.html']
    if not matches:
        print(f'  [SKIP] No file found for: {lesson_name}')
        continue

    fpath = os.path.join(FOLDER, matches[0])
    changed = translate_file(fpath, translations)
    status = 'TRANSLATED' if changed else 'NO CHANGE'
    print(f'  [{status}] {matches[0]}')

print('\nTranslation complete!')
