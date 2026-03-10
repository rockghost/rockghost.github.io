#!/usr/bin/env python3
"""Translate all MCP course HTML files from English to Korean."""
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
    'Introduction to Model Context Protocol': 'Model Context Protocol 입문',
    'Course Overview': '강좌 개요',
    '>Introduction<': '>소개<',
    '>Welcome to the course<': '>강좌에 오신 것을 환영합니다<',
    '>Introducing MCP<': '>MCP 소개<',
    '>MCP clients<': '>MCP 클라이언트<',
    'Hands-on with MCP servers': 'MCP 서버 실습',
    '>Project setup<': '>프로젝트 설정<',
    '>Defining tools with MCP<': '>MCP로 도구 정의하기<',
    '>The server inspector<': '>서버 인스펙터<',
    'Course satisfaction survey': '강좌 만족도 설문조사',
    'Connecting with MCP clients': 'MCP 클라이언트 연결하기',
    '>Implementing a client<': '>클라이언트 구현하기<',
    '>Defining resources<': '>리소스 정의하기<',
    '>Accessing resources<': '>리소스 접근하기<',
    '>Defining prompts<': '>프롬프트 정의하기<',
    '>Prompts in the client<': '>클라이언트의 프롬프트<',
    'Assessment and wrap Up': '평가 및 마무리',
    'Final assessment on MCP': 'MCP 최종 평가',
    '>MCP review<': '>MCP 복습<',
}

# Per-file content translations
FILES = {
    'Welcome to the course': {
        'title="Welcome to the course"': 'title="강좌에 오신 것을 환영합니다"',
        'Direct link to the UV install guide:': 'UV 설치 가이드 직접 링크:',
        'Model Context Protocol introduction:': 'Model Context Protocol 소개:',
    },
    'Introducing MCP': {
        'title="Introducing MCP"': 'title="MCP 소개"',
        "Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.":
            "Model Context Protocol(MCP)은 번거로운 통합 코드를 작성하지 않고도 Claude에게 컨텍스트와 도구를 제공하는 통신 계층입니다. 도구 정의와 실행의 부담을 서버에서 전문 MCP 서버로 옮기는 방법이라고 생각하면 됩니다.",
        "When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to some outside service.":
            "MCP를 처음 접하면 기본 아키텍처를 보여주는 다이어그램을 볼 수 있습니다: MCP 클라이언트(서버)가 도구, 프롬프트, 리소스를 포함하는 MCP 서버에 연결됩니다. 각 MCP 서버는 외부 서비스에 대한 인터페이스 역할을 합니다.",
        'The Problem MCP Solves': 'MCP가 해결하는 문제',
        "Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask \"What open pull requests are there across all my repositories?\" To handle this, Claude needs tools to access GitHub's API.":
            "사용자가 GitHub 데이터에 대해 Claude에게 질문할 수 있는 채팅 인터페이스를 구축한다고 가정해 봅시다. 사용자가 \"내 모든 저장소에 열린 풀 리퀘스트가 있나요?\"라고 물을 수 있습니다. 이를 처리하려면 Claude에게 GitHub API에 접근할 수 있는 도구가 필요합니다.",
        "GitHub has massive functionality - repositories, pull requests, issues, projects, and tons more. Without MCP, you'd need to create an incredible number of tool schemas and functions to handle all of GitHub's features.":
            "GitHub은 저장소, 풀 리퀘스트, 이슈, 프로젝트 등 방대한 기능을 가지고 있습니다. MCP 없이는 GitHub의 모든 기능을 처리하기 위해 엄청난 수의 도구 스키마와 함수를 만들어야 합니다.",
        "This means writing, testing, and maintaining all that integration code yourself. That's a lot of effort and ongoing maintenance burden.":
            "이는 모든 통합 코드를 직접 작성하고, 테스트하고, 유지보수해야 한다는 의미입니다. 많은 노력과 지속적인 유지보수 부담이 됩니다.",
        'How MCP Works': 'MCP 작동 방식',
        "MCP shifts this burden by moving tool definitions and execution from your server to dedicated MCP servers. Instead of you authoring all those GitHub tools, an MCP Server for GitHub handles it.":
            "MCP는 도구 정의와 실행을 서버에서 전용 MCP 서버로 옮겨 이 부담을 해소합니다. GitHub 도구를 직접 작성하는 대신 GitHub용 MCP 서버가 이를 처리합니다.",
        "The MCP Server wraps up tons of functionality around GitHub and exposes it as a standardized set of tools. Your application connects to this MCP server instead of implementing everything from scratch.":
            "MCP 서버는 GitHub 관련 많은 기능을 래핑하고 표준화된 도구 세트로 노출합니다. 애플리케이션은 모든 것을 처음부터 구현하는 대신 이 MCP 서버에 연결합니다.",
        'MCP Servers Explained': 'MCP 서버 설명',
        "MCP Servers provide access to data or functionality implemented by outside services. They act as specialized interfaces that expose tools, prompts, and resources in a standardized way.":
            "MCP 서버는 외부 서비스에서 구현된 데이터나 기능에 대한 접근을 제공합니다. 도구, 프롬프트, 리소스를 표준화된 방식으로 노출하는 전문 인터페이스 역할을 합니다.",
        "In our GitHub example, the MCP Server for GitHub contains tools like":
            "GitHub 예시에서 GitHub용 MCP 서버는 다음과 같은 도구를 포함합니다:",
        "and connects directly to GitHub's API. Your server communicates with the MCP server, which handles all the GitHub-specific implementation details.":
            "그리고 GitHub API에 직접 연결합니다. 서버는 MCP 서버와 통신하며, MCP 서버가 모든 GitHub 관련 구현 세부 사항을 처리합니다.",
        'Common Questions': '자주 묻는 질문',
        'Who authors MCP Servers?': 'MCP 서버를 누가 만드나요?',
        "Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tools for their various services.":
            "누구나 MCP 서버 구현을 만들 수 있습니다. 종종 서비스 제공업체가 자체 공식 MCP 구현을 만들기도 합니다. 예를 들어, AWS가 다양한 서비스용 도구가 포함된 공식 MCP 서버를 출시할 수 있습니다.",
        "How is this different from calling APIs directly?": "API를 직접 호출하는 것과 어떻게 다른가요?",
        "MCP servers provide tool schemas and functions already defined for you. If you want to call an API directly, you'll be authoring those tool definitions on your own. MCP saves you that implementation work.":
            "MCP 서버는 이미 정의된 도구 스키마와 함수를 제공합니다. API를 직접 호출하려면 도구 정의를 직접 작성해야 합니다. MCP는 그 구현 작업을 절약해 줍니다.",
        "Isn't MCP just the same as tool use?": "MCP는 도구 사용과 같은 것 아닌가요?",
        "This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP servers provide tool schemas and functions already defined for you, while tool use is about how Claude actually calls those tools. The key difference is who does the work - with MCP, someone else has already implemented the tools for you.":
            "이것은 흔한 오해입니다. MCP 서버와 도구 사용은 상호 보완적이지만 다른 개념입니다. MCP 서버는 이미 정의된 도구 스키마와 함수를 제공하고, 도구 사용은 Claude가 실제로 도구를 호출하는 방법에 관한 것입니다. 핵심 차이점은 누가 작업을 하느냐입니다 - MCP를 사용하면 다른 누군가가 이미 도구를 구현해 놓았습니다.",
        "The benefit is clear: instead of maintaining a complex set of integrations yourself, you can leverage MCP servers that handle the heavy lifting of connecting to external services.":
            "이점은 명확합니다: 복잡한 통합 세트를 직접 유지보수하는 대신, 외부 서비스 연결의 무거운 작업을 처리하는 MCP 서버를 활용할 수 있습니다.",
    },
    'MCP clients': {
        'title="MCP clients"': 'title="MCP 클라이언트"',
        "The MCP client serves as the communication bridge between your server and MCP servers. It's your access point to all the tools that an MCP server provides, handling the message exchange and protocol details so your application doesn't have to.":
            "MCP 클라이언트는 서버와 MCP 서버 사이의 통신 다리 역할을 합니다. MCP 서버가 제공하는 모든 도구에 대한 접근점이며, 메시지 교환과 프로토콜 세부 사항을 처리하여 애플리케이션이 이를 신경 쓸 필요가 없게 합니다.",
        'Transport Agnostic Communication': '전송 방식에 독립적인 통신',
        "One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can communicate over different protocols depending on your setup.":
            "MCP의 주요 강점 중 하나는 전송 방식에 독립적이라는 것입니다 - 설정에 따라 클라이언트와 서버가 다른 프로토콜로 통신할 수 있다는 의미입니다.",
        "The most common setup runs both the MCP client and server on the same machine, communicating through standard input/output. But you can also connect them over:":
            "가장 일반적인 설정은 MCP 클라이언트와 서버를 같은 머신에서 실행하고 표준 입출력을 통해 통신하는 것입니다. 하지만 다음을 통해서도 연결할 수 있습니다:",
        'WebSockets': 'WebSocket',
        'Various other network protocols': '기타 다양한 네트워크 프로토콜',
        'MCP Message Types': 'MCP 메시지 유형',
        'Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you\'ll work with are:':
            '연결되면 클라이언트와 서버는 MCP 사양에 정의된 특정 메시지 유형을 교환합니다. 주로 다루게 될 메시지는 다음과 같습니다:',
        'The client asks the server "what tools do you provide?" and gets back a list of available tools.':
            '클라이언트가 서버에 "어떤 도구를 제공하나요?"라고 묻고 사용 가능한 도구 목록을 받습니다.',
        'The client asks the server to run a specific tool with given arguments, then receives the results.':
            '클라이언트가 서버에 주어진 인수로 특정 도구를 실행하도록 요청한 다음 결과를 받습니다.',
        'How It All Works Together': '모든 것이 함께 작동하는 방식',
        "Here's a complete example showing how a user query flows through the entire system - from your server, through the MCP client, to external services like GitHub, and back to Claude.":
            "사용자 쿼리가 전체 시스템을 통해 어떻게 흐르는지 보여주는 완전한 예시입니다 - 서버에서 MCP 클라이언트를 거쳐 GitHub 같은 외부 서비스로, 그리고 다시 Claude로 돌아옵니다.",
        'Let\'s say a user asks "What repositories do I have?" Here\'s the step-by-step flow:':
            '사용자가 "내 저장소가 뭐가 있나요?"라고 질문한다고 가정해 봅시다. 단계별 흐름은 다음과 같습니다:',
        'User Query:': '사용자 쿼리:',
        'The user submits their question to your server': '사용자가 서버에 질문을 제출합니다',
        'Tool Discovery:': '도구 발견:',
        'Your server needs to know what tools are available to send to Claude': '서버는 Claude에게 보낼 수 있는 도구가 무엇인지 알아야 합니다',
        'List Tools Exchange:': '도구 목록 교환:',
        'Your server asks the MCP client for available tools': '서버가 MCP 클라이언트에게 사용 가능한 도구를 요청합니다',
        'MCP Communication:': 'MCP 통신:',
        'Claude Request:': 'Claude 요청:',
        "Your server sends the user's query plus the available tools to Claude": '서버가 사용자의 쿼리와 사용 가능한 도구를 Claude에게 보냅니다',
        'Tool Use Decision:': '도구 사용 결정:',
        'Claude decides it needs to call a tool to answer the question': 'Claude가 질문에 답하기 위해 도구를 호출해야 한다고 결정합니다',
        'Tool Execution Request:': '도구 실행 요청:',
        'Your server asks the MCP client to run the tool Claude specified': '서버가 MCP 클라이언트에게 Claude가 지정한 도구를 실행하도록 요청합니다',
        'External API Call:': '외부 API 호출:',
        'to the MCP server, which makes the actual GitHub API call': 'MCP 서버로 전달되어 실제 GitHub API 호출을 수행합니다',
        'Results Flow Back:': '결과 반환:',
        'GitHub responds with repository data, which flows back through the MCP server as a':
            'GitHub이 저장소 데이터로 응답하고, 이는 MCP 서버를 통해',
        'Tool Result to Claude:': '도구 결과를 Claude에게:',
        'Your server sends the tool results back to Claude': '서버가 도구 결과를 Claude에게 다시 보냅니다',
        'Final Response:': '최종 응답:',
        'Claude formulates a final answer using the repository data': 'Claude가 저장소 데이터를 사용하여 최종 답변을 작성합니다',
        'User Gets Answer:': '사용자가 답변을 받음:',
        "Your server delivers Claude's response back to the user": '서버가 Claude의 응답을 사용자에게 전달합니다',
        "Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on your application logic while still getting access to powerful external tools and data sources.":
            "네, 이 흐름은 많은 단계를 포함하지만 각 구성 요소에는 명확한 책임이 있습니다. MCP 클라이언트는 서버 통신의 복잡성을 추상화하여, 강력한 외부 도구와 데이터 소스에 접근하면서도 애플리케이션 로직에 집중할 수 있게 해줍니다.",
        "Understanding this flow is crucial because you'll see all these pieces when building your own MCP clients and servers in the upcoming sections.":
            "이 흐름을 이해하는 것이 중요합니다. 앞으로의 섹션에서 자신만의 MCP 클라이언트와 서버를 구축할 때 이 모든 구성 요소를 보게 될 것이기 때문입니다.",
    },
    'Project setup': {
        'title="Project setup"': 'title="프로젝트 설정"',
    },
    'Defining tools with MCP': {
        'title="Defining tools with MCP"': 'title="MCP로 도구 정의하기"',
        "Building an MCP server becomes much simpler when you use the official Python SDK. Instead of writing complex JSON schemas by hand, you can define tools with decorators and let the SDK handle the heavy lifting.":
            "공식 Python SDK를 사용하면 MCP 서버를 훨씬 간단하게 구축할 수 있습니다. 복잡한 JSON 스키마를 직접 작성하는 대신, 데코레이터로 도구를 정의하고 SDK가 무거운 작업을 처리하도록 할 수 있습니다.",
        "In this example, we're creating a document management server with two core tools: one to read documents and another to update them. All documents exist in memory as a simple dictionary where keys are document IDs and values are the content.":
            "이 예시에서는 두 가지 핵심 도구가 있는 문서 관리 서버를 만듭니다: 문서를 읽는 도구와 업데이트하는 도구입니다. 모든 문서는 키가 문서 ID이고 값이 내용인 간단한 딕셔너리로 메모리에 존재합니다.",
        'Setting Up the MCP Server': 'MCP 서버 설정',
        'The Python MCP SDK makes server creation straightforward. You can initialize a server with just one line:':
            'Python MCP SDK는 서버 생성을 간단하게 만듭니다. 한 줄로 서버를 초기화할 수 있습니다:',
        'Your documents can be stored in a simple dictionary structure:': '문서는 간단한 딕셔너리 구조에 저장할 수 있습니다:',
        'Tool Definition with Decorators': '데코레이터를 사용한 도구 정의',
        'The SDK uses decorators to define tools. Instead of writing JSON schemas manually, you can use Python type hints and field descriptions. The SDK automatically generates the proper schema that Claude can understand.':
            'SDK는 데코레이터를 사용하여 도구를 정의합니다. JSON 스키마를 수동으로 작성하는 대신, Python 타입 힌트와 필드 설명을 사용할 수 있습니다. SDK가 Claude가 이해할 수 있는 적절한 스키마를 자동으로 생성합니다.',
        'Creating a Document Reader Tool': '문서 읽기 도구 만들기',
        "The first tool reads document contents by ID. Here's the complete implementation:":
            '첫 번째 도구는 ID로 문서 내용을 읽습니다. 전체 구현은 다음과 같습니다:',
        'The decorator specifies the tool name and description, while the function parameters define the required arguments. The':
            '데코레이터는 도구 이름과 설명을 지정하고, 함수 매개변수는 필수 인수를 정의합니다.',
        'class from Pydantic provides argument descriptions that help Claude understand what each parameter expects.':
            'Pydantic의 클래스는 각 매개변수가 무엇을 기대하는지 Claude가 이해할 수 있도록 인수 설명을 제공합니다.',
        'Building a Document Editor Tool': '문서 편집 도구 만들기',
        'The second tool performs simple find-and-replace operations on documents:': '두 번째 도구는 문서에서 간단한 찾기-바꾸기 작업을 수행합니다:',
        'This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation includes error handling for missing documents and performs a straightforward string replacement.':
            '이 도구는 세 가지 매개변수를 받습니다: 문서 ID, 찾을 텍스트, 대체 텍스트. 구현에는 누락된 문서에 대한 오류 처리가 포함되어 있으며 간단한 문자열 대체를 수행합니다.',
        'Key Benefits of the SDK Approach': 'SDK 접근 방식의 핵심 이점',
        'No manual JSON schema writing required': '수동 JSON 스키마 작성 불필요',
        'Type hints provide automatic validation': '타입 힌트가 자동 유효성 검사 제공',
        'Clear parameter descriptions help Claude understand tool usage': '명확한 매개변수 설명이 Claude의 도구 사용 이해를 도움',
        'Error handling integrates naturally with Python exceptions': '오류 처리가 Python 예외와 자연스럽게 통합',
        'Tool registration happens automatically through decorators': '도구 등록이 데코레이터를 통해 자동으로 수행',
        'The MCP Python SDK transforms tool creation from a complex schema-writing exercise into simple Python function definitions. This approach makes it much easier to build and maintain MCP servers while ensuring Claude receives properly formatted tool specifications.':
            'MCP Python SDK는 도구 생성을 복잡한 스키마 작성 작업에서 간단한 Python 함수 정의로 변환합니다. 이 접근 방식은 Claude가 올바른 형식의 도구 사양을 받도록 보장하면서 MCP 서버를 훨씬 쉽게 구축하고 유지보수할 수 있게 합니다.',
    },
    'The server inspector': {
        'title="The server inspector"': 'title="서버 인스펙터"',
        'When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.':
            'MCP 서버를 구축할 때, 전체 애플리케이션에 연결하지 않고 기능을 테스트할 방법이 필요합니다. Python MCP SDK에는 서버를 실시간으로 디버그하고 테스트할 수 있는 내장 브라우저 기반 인스펙터가 포함되어 있습니다.',
        'Starting the Inspector': '인스펙터 시작하기',
        "First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:":
            '먼저 Python 환경이 활성화되어 있는지 확인하세요(정확한 명령은 프로젝트의 README를 참조). 그런 다음 인스펙터를 실행합니다:',
        'This starts a development server and gives you a local URL, typically something like':
            '이것은 개발 서버를 시작하고 로컬 URL을 제공합니다. 일반적으로 다음과 같은 형태입니다:',
        '. Open this URL in your browser to access the MCP Inspector.': '. 브라우저에서 이 URL을 열어 MCP 인스펙터에 접근하세요.',
        'Using the Inspector Interface': '인스펙터 인터페이스 사용하기',
        'The inspector interface is actively being developed, so it may look different when you use it. However, the core functionality remains consistent. Look for these key elements:':
            '인스펙터 인터페이스는 활발히 개발 중이므로 사용할 때 모양이 다를 수 있습니다. 하지만 핵심 기능은 일관됩니다. 다음 핵심 요소를 찾으세요:',
        'button to start your MCP server': '버튼을 클릭하여 MCP 서버를 시작',
        'Navigation tabs for': '다음에 대한 내비게이션 탭:',
        ', and other features': ', 그리고 기타 기능',
        'A tools listing and testing panel': '도구 목록 및 테스트 패널',
        'Click the Connect button first to initialize your server. You\'ll see the connection status change from "Disconnected" to "Connected".':
            'Connect 버튼을 먼저 클릭하여 서버를 초기화하세요. 연결 상태가 "Disconnected"에서 "Connected"로 변경되는 것을 볼 수 있습니다.',
        'Testing Your Tools': '도구 테스트하기',
        'Navigate to the Tools section and click "List Tools" to see all available tools from your server. When you select a tool, the right panel shows its details and input fields.':
            'Tools 섹션으로 이동하고 "List Tools"를 클릭하여 서버의 모든 사용 가능한 도구를 확인하세요. 도구를 선택하면 오른쪽 패널에 세부 정보와 입력 필드가 표시됩니다.',
        'For example, to test a document reading tool:': '예를 들어, 문서 읽기 도구를 테스트하려면:',
        'Enter a document ID (like "deposition.md")': '문서 ID를 입력합니다 (예: "deposition.md")',
        'Click "Run Tool"': '"Run Tool"을 클릭합니다',
        'Check the results for success and expected output': '성공 여부와 예상 출력을 확인합니다',
        'The inspector shows both the success status and the actual returned data, making it easy to verify your tool works correctly.':
            '인스펙터는 성공 상태와 실제 반환 데이터를 모두 보여주므로 도구가 올바르게 작동하는지 쉽게 확인할 수 있습니다.',
        'Testing Tool Interactions': '도구 상호작용 테스트',
        'You can test multiple tools in sequence to verify complex workflows. For instance, after using an edit tool to modify a document, immediately test the read tool to confirm the changes were applied correctly.':
            '복잡한 워크플로우를 검증하기 위해 여러 도구를 순서대로 테스트할 수 있습니다. 예를 들어, 편집 도구로 문서를 수정한 후 즉시 읽기 도구로 변경 사항이 올바르게 적용되었는지 확인할 수 있습니다.',
        'The inspector maintains your server state between tool calls, so edits persist and you can verify the complete functionality of your MCP server.':
            '인스펙터는 도구 호출 간에 서버 상태를 유지하므로 편집이 지속되며 MCP 서버의 전체 기능을 검증할 수 있습니다.',
        'Development Workflow': '개발 워크플로우',
        'The MCP Inspector becomes an essential part of your development process. Instead of writing separate test scripts or connecting to full applications, you can:':
            'MCP 인스펙터는 개발 프로세스의 필수적인 부분이 됩니다. 별도의 테스트 스크립트를 작성하거나 전체 애플리케이션에 연결하는 대신:',
        'Quickly iterate on tool implementations': '도구 구현을 빠르게 반복',
        'Test edge cases and error conditions': '엣지 케이스와 오류 조건 테스트',
        'Verify tool interactions and state management': '도구 상호작용과 상태 관리 검증',
        'Debug issues in real-time': '실시간으로 문제 디버그',
        'This immediate feedback loop makes MCP server development much more efficient and helps catch issues early in the development process.':
            '이 즉각적인 피드백 루프는 MCP 서버 개발을 훨씬 더 효율적으로 만들고 개발 프로세스 초기에 문제를 발견하는 데 도움이 됩니다.',
    },
    'Implementing a client': {
        'title="Implementing a client"': 'title="클라이언트 구현하기"',
        "Now that we have our MCP server working, it's time to build the client side. The client is what allows our application code to communicate with the MCP server and access its functionality.":
            "이제 MCP 서버가 작동하므로 클라이언트 측을 구축할 차례입니다. 클라이언트는 애플리케이션 코드가 MCP 서버와 통신하고 그 기능에 접근할 수 있게 해주는 것입니다.",
        'Understanding the Client Architecture': '클라이언트 아키텍처 이해',
        "In most real-world projects, you'll either implement an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.":
            "대부분의 실제 프로젝트에서는 MCP 클라이언트 또는 MCP 서버 중 하나만 구현합니다 - 둘 다 구현하지는 않습니다. 이 프로젝트에서는 어떻게 함께 작동하는지 볼 수 있도록 둘 다 구축합니다.",
        'The MCP client consists of two main components:': 'MCP 클라이언트는 두 가지 주요 구성 요소로 이루어져 있습니다:',
        '- A custom class we create to make using the session easier': '- 세션 사용을 더 쉽게 하기 위해 만드는 커스텀 클래스',
        '- The actual connection to the server (part of the MCP Python SDK)': '- 서버에 대한 실제 연결 (MCP Python SDK의 일부)',
        "The client session requires careful resource management - we need to properly clean up connections when we're done. That's why we wrap it in our own class that handles all the cleanup automatically.":
            "클라이언트 세션은 신중한 리소스 관리가 필요합니다 - 작업이 끝나면 연결을 올바르게 정리해야 합니다. 그래서 모든 정리를 자동으로 처리하는 자체 클래스로 래핑합니다.",
        'How the Client Fits Into Our Application': '클라이언트가 애플리케이션에 어떻게 맞는지',
        'Remember our application flow diagram? The client is what enables our code to interact with the MCP server at two key points:':
            '애플리케이션 흐름 다이어그램을 기억하시나요? 클라이언트는 코드가 두 가지 핵심 지점에서 MCP 서버와 상호작용할 수 있게 해줍니다:',
        'Our CLI code uses the client to:': 'CLI 코드는 클라이언트를 사용하여:',
        'Get a list of available tools to send to Claude': 'Claude에게 보낼 사용 가능한 도구 목록 가져오기',
        'Execute tools when Claude requests them': 'Claude가 요청할 때 도구 실행하기',
        'Implementing Core Client Functions': '핵심 클라이언트 함수 구현',
        'We need to implement two essential functions:': '두 가지 필수 함수를 구현해야 합니다:',
        'List Tools Function': '도구 목록 함수',
        'This function gets all available tools from the MCP server:': '이 함수는 MCP 서버에서 사용 가능한 모든 도구를 가져옵니다:',
        "It's straightforward - we access our session (the connection to the server), call the built-in":
            '간단합니다 - 세션(서버와의 연결)에 접근하고, 내장된',
        'method, and return the tools from the result.': '메서드를 호출하고, 결과에서 도구를 반환합니다.',
        'Call Tool Function': '도구 호출 함수',
        'This function executes a specific tool on the server:': '이 함수는 서버에서 특정 도구를 실행합니다:',
        'We pass the tool name and input parameters (provided by Claude) to the server and return the result.':
            '도구 이름과 입력 매개변수(Claude가 제공)를 서버에 전달하고 결과를 반환합니다.',
        'Testing the Client': '클라이언트 테스트',
        'The client file includes a simple test harness at the bottom. You can run it directly to verify everything works:':
            '클라이언트 파일 하단에 간단한 테스트 하네스가 포함되어 있습니다. 직접 실행하여 모든 것이 작동하는지 확인할 수 있습니다:',
        'This will connect to your MCP server and print out the available tools. You should see output showing your tool definitions, including descriptions and input schemas.':
            '이것은 MCP 서버에 연결하고 사용 가능한 도구를 출력합니다. 설명과 입력 스키마를 포함한 도구 정의를 보여주는 출력을 볼 수 있습니다.',
        'Putting It All Together': '모든 것을 합치기',
        'Once the client functions are implemented, you can test the complete flow by running your main application:':
            '클라이언트 함수가 구현되면 메인 애플리케이션을 실행하여 전체 흐름을 테스트할 수 있습니다:',
        'Try asking: "What is the contents of the report.pdf document?"': '"report.pdf 문서의 내용이 뭐예요?"라고 질문해 보세요.',
        "Here's what happens behind the scenes:": '뒤에서 일어나는 일은 다음과 같습니다:',
        'Your application uses the client to get available tools': '애플리케이션이 클라이언트를 사용하여 사용 가능한 도구를 가져옵니다',
        'These tools are sent to Claude along with your question': '이 도구들이 질문과 함께 Claude에게 전송됩니다',
        'Claude decides to use the read_doc_contents tool': 'Claude가 read_doc_contents 도구를 사용하기로 결정합니다',
        'Your application uses the client to execute that tool': '애플리케이션이 클라이언트를 사용하여 해당 도구를 실행합니다',
        'The result is returned to Claude, who then responds to you': '결과가 Claude에게 반환되고, Claude가 응답합니다',
        'The client acts as the bridge between your application logic and the MCP server\'s functionality, making it easy to integrate powerful tools into your AI workflows.':
            '클라이언트는 애플리케이션 로직과 MCP 서버의 기능 사이의 다리 역할을 하여, 강력한 도구를 AI 워크플로우에 쉽게 통합할 수 있게 합니다.',
    },
    'Defining resources': {
        'title="Defining resources"': 'title="리소스 정의하기"',
        "Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.":
            "MCP 서버의 리소스를 사용하면 일반적인 HTTP 서버의 GET 요청 핸들러와 유사하게 클라이언트에 데이터를 노출할 수 있습니다. 작업을 수행하는 것이 아니라 정보를 가져와야 하는 시나리오에 적합합니다.",
        'Understanding Resources Through an Example': '예시를 통한 리소스 이해',
        'Getting a list of all available documents (for autocomplete)': '사용 가능한 모든 문서 목록 가져오기 (자동완성용)',
        'Fetching the contents of a specific document (when mentioned)': '특정 문서의 내용 가져오기 (언급 시)',
        "When a user mentions a document, your system automatically injects the document's contents into the prompt sent to Claude, eliminating the need for Claude to use tools to fetch the information.":
            "사용자가 문서를 언급하면, 시스템이 자동으로 문서의 내용을 Claude에게 보내는 프롬프트에 주입하여, Claude가 정보를 가져오기 위해 도구를 사용할 필요가 없게 합니다.",
        'How Resources Work': '리소스 작동 방식',
        'Resources follow a request-response pattern.': '리소스는 요청-응답 패턴을 따릅니다.',
        'The flow looks like this: your code requests a resource from the MCP client, which forwards the request to the MCP server. The server processes the URI, runs the appropriate function, and returns the result.':
            '흐름은 다음과 같습니다: 코드가 MCP 클라이언트에서 리소스를 요청하고, 클라이언트가 요청을 MCP 서버로 전달합니다. 서버가 URI를 처리하고, 적절한 함수를 실행하고, 결과를 반환합니다.',
        'Types of Resources': '리소스 유형',
        'There are two types of resources:': '리소스에는 두 가지 유형이 있습니다:',
        'Direct Resources': '직접 리소스',
        "Direct resources have static URIs that never change. They're perfect for operations that don't need parameters.":
            "직접 리소스는 변경되지 않는 정적 URI를 가집니다. 매개변수가 필요 없는 작업에 적합합니다.",
        'Templated Resources': '템플릿 리소스',
        'Templated resources include parameters in their URIs. The Python SDK automatically parses these parameters and passes them as keyword arguments to your function.':
            '템플릿 리소스는 URI에 매개변수를 포함합니다. Python SDK가 이러한 매개변수를 자동으로 파싱하여 함수의 키워드 인수로 전달합니다.',
        'Implementation Details': '구현 세부 사항',
        'for structured data': '구조화된 데이터용',
        'for plain text': '일반 텍스트용',
        'for binary files': '바이너리 파일용',
        "The MCP Python SDK automatically serializes your return values. You don't need to manually convert objects to JSON strings - just return the data structure and let the SDK handle serialization.":
            "MCP Python SDK는 반환 값을 자동으로 직렬화합니다. 객체를 JSON 문자열로 수동 변환할 필요 없이 - 데이터 구조를 반환하면 SDK가 직렬화를 처리합니다.",
        'Testing Your Resources': '리소스 테스트하기',
        'You can test resources using the MCP Inspector. Start your server with:': 'MCP 인스펙터를 사용하여 리소스를 테스트할 수 있습니다. 서버를 다음으로 시작하세요:',
        "Then connect to the inspector in your browser. You'll see two sections:": '그런 다음 브라우저에서 인스펙터에 연결하세요. 두 가지 섹션을 볼 수 있습니다:',
        '- Lists your direct/static resources': '- 직접/정적 리소스 목록',
        '- Lists your templated resources': '- 템플릿 리소스 목록',
        "Click on any resource to test it. For templated resources, you'll need to provide values for the parameters. The inspector shows you the exact response structure your client will receive, including the MIME type and serialized data.":
            "리소스를 클릭하여 테스트하세요. 템플릿 리소스의 경우 매개변수 값을 제공해야 합니다. 인스펙터는 MIME 타입과 직렬화된 데이터를 포함하여 클라이언트가 받을 정확한 응답 구조를 보여줍니다.",
        'Resources provide a clean way to expose read-only data from your MCP server, making it easy for clients to fetch information without the complexity of tool calls.':
            '리소스는 MCP 서버에서 읽기 전용 데이터를 노출하는 깔끔한 방법을 제공하여, 클라이언트가 도구 호출의 복잡성 없이 쉽게 정보를 가져올 수 있게 합니다.',
    },
    'Defining prompts': {
        'title="Defining prompts"': 'title="프롬프트 정의하기"',
        "Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that give better results than what users might come up with on their own.":
            "MCP 서버의 프롬프트를 사용하면 클라이언트가 처음부터 프롬프트를 작성하는 대신 사용할 수 있는 사전 구축된 고품질 지시사항을 정의할 수 있습니다. 사용자가 직접 만들 수 있는 것보다 더 나은 결과를 제공하는 정교하게 제작된 템플릿이라고 생각하면 됩니다.",
        'Why Use Prompts?': '왜 프롬프트를 사용하나요?',
        "Here's the key insight: users can already ask Claude to do most tasks directly. For example, a user could type \"reformat the report.pdf in markdown\" and get decent results. But they'll get much better results if you provide a thoroughly tested, specialized prompt that handles edge cases and follows best practices.":
            "핵심 인사이트는 다음과 같습니다: 사용자는 이미 대부분의 작업을 Claude에게 직접 요청할 수 있습니다. 예를 들어, 사용자가 \"report.pdf를 마크다운으로 변환해 줘\"라고 입력하면 괜찮은 결과를 얻을 수 있습니다. 하지만 엣지 케이스를 처리하고 모범 사례를 따르는 철저히 테스트된 전문 프롬프트를 제공하면 훨씬 더 나은 결과를 얻을 수 있습니다.",
        "As the MCP server author, you can spend time crafting, testing, and evaluating prompts that work consistently across different scenarios. Users benefit from this expertise without having to become prompt engineering experts themselves.":
            "MCP 서버 작성자로서, 다양한 시나리오에서 일관되게 작동하는 프롬프트를 제작, 테스트, 평가하는 데 시간을 투자할 수 있습니다. 사용자는 직접 프롬프트 엔지니어링 전문가가 되지 않고도 이 전문 지식의 혜택을 받을 수 있습니다.",
        'Building a Format Command': '포맷 명령 만들기',
        "Let's implement a practical example: a format command that converts documents to markdown.":
            "실용적인 예시를 구현해 봅시다: 문서를 마크다운으로 변환하는 포맷 명령입니다.",
        'The workflow looks like this:': '워크플로우는 다음과 같습니다:',
        'to see available commands': '사용 가능한 명령 보기',
        'and specify a document ID': '문서 ID 지정',
        'Claude uses your pre-built prompt to read and reformat the document': 'Claude가 사전 구축된 프롬프트를 사용하여 문서를 읽고 다시 포맷합니다',
        'The result is clean markdown with proper headers, lists, and formatting': '결과는 적절한 헤더, 목록, 서식이 갖춰진 깔끔한 마크다운입니다',
        'Defining Prompts': '프롬프트 정의하기',
        'Prompts use a similar decorator pattern to tools and resources:': '프롬프트는 도구 및 리소스와 유사한 데코레이터 패턴을 사용합니다:',
        'The function returns a list of messages that get sent directly to Claude. You can include multiple user and assistant messages to create more complex conversation flows.':
            '함수는 Claude에게 직접 전송되는 메시지 목록을 반환합니다. 여러 사용자 및 어시스턴트 메시지를 포함하여 더 복잡한 대화 흐름을 만들 수 있습니다.',
        'Testing Your Prompts': '프롬프트 테스트하기',
        'Use the MCP Inspector to test your prompts before deploying them:': 'MCP 인스펙터를 사용하여 배포 전에 프롬프트를 테스트하세요:',
        'The inspector shows you exactly what messages will be sent to Claude, including how variables get interpolated into your prompt template. This lets you verify the prompt looks correct before users start relying on it.':
            '인스펙터는 변수가 프롬프트 템플릿에 어떻게 삽입되는지를 포함하여 Claude에게 전송될 정확한 메시지를 보여줍니다. 이를 통해 사용자가 의존하기 전에 프롬프트가 올바른지 확인할 수 있습니다.',
        'Key Benefits': '핵심 이점',
        'Consistency': '일관성',
        '- Users get reliable results every time': '- 사용자가 매번 안정적인 결과를 얻음',
        'Expertise': '전문 지식',
        '- You can encode domain knowledge into prompts': '- 도메인 지식을 프롬프트에 인코딩 가능',
        'Reusability': '재사용성',
        '- Multiple client applications can use the same prompts': '- 여러 클라이언트 애플리케이션이 같은 프롬프트를 사용 가능',
        'Maintenance': '유지보수',
        '- Update prompts in one place to improve all clients': '- 한 곳에서 프롬프트를 업데이트하여 모든 클라이언트 개선',
        "Prompts work best when they're specialized for your MCP server's domain.":
            "프롬프트는 MCP 서버의 도메인에 특화되었을 때 가장 잘 작동합니다.",
        'The goal is to provide prompts that are so well-crafted and tested that users prefer them over writing their own instructions from scratch.':
            '목표는 사용자가 직접 지시사항을 작성하는 것보다 선호할 만큼 잘 제작되고 테스트된 프롬프트를 제공하는 것입니다.',
    },
    'Prompts in the client': {
        'title="Prompts in the client"': 'title="클라이언트의 프롬프트"',
        'The final step in building our MCP client is implementing prompt functionality. This allows us to list all available prompts from the server and retrieve specific prompts with variables filled in.':
            'MCP 클라이언트 구축의 마지막 단계는 프롬프트 기능을 구현하는 것입니다. 이를 통해 서버에서 사용 가능한 모든 프롬프트를 나열하고 변수가 채워진 특정 프롬프트를 가져올 수 있습니다.',
        'Implementing List Prompts': '프롬프트 목록 구현',
        'Getting Individual Prompts': '개별 프롬프트 가져오기',
        'Testing Prompts in Action': '프롬프트 실제 테스트',
        'How Prompts Work': '프롬프트 작동 방식',
        'Prompts define a set of user and assistant messages that clients can use.': '프롬프트는 클라이언트가 사용할 수 있는 사용자 및 어시스턴트 메시지 세트를 정의합니다.',
        "They should be high-quality, well-tested, and relevant to your MCP server's purpose. The workflow is:":
            "고품질이고, 잘 테스트되었으며, MCP 서버의 목적에 관련이 있어야 합니다. 워크플로우는 다음과 같습니다:",
        "Write and evaluate a prompt relevant to your server's functionality": '서버 기능과 관련된 프롬프트를 작성하고 평가합니다',
        'Define the prompt in your MCP server using the': '다음을 사용하여 MCP 서버에서 프롬프트를 정의합니다',
        'Clients can request the prompt at any time': '클라이언트는 언제든지 프롬프트를 요청할 수 있습니다',
        'Arguments provided by the client become keyword arguments in your prompt function': '클라이언트가 제공한 인수는 프롬프트 함수의 키워드 인수가 됩니다',
        'The function returns formatted messages ready for the AI model': '함수는 AI 모델에 사용할 수 있는 포맷된 메시지를 반환합니다',
        "This system creates reusable, parameterized prompts that maintain consistency while allowing customization through variables. It's particularly useful for complex workflows where you want to ensure the AI receives properly structured instructions every time.":
            "이 시스템은 변수를 통한 커스터마이징을 허용하면서 일관성을 유지하는 재사용 가능한 매개변수화된 프롬프트를 생성합니다. AI가 매번 올바르게 구조화된 지시사항을 받도록 보장하려는 복잡한 워크플로우에 특히 유용합니다.",
    },
    'MCP review': {
        'title="MCP review"': 'title="MCP 복습"',
        "Now that we've built our MCP server, let's review the three core server primitives and understand when to use each one. The key insight is that each primitive is controlled by a different part of your application stack.":
            "MCP 서버를 구축했으니, 세 가지 핵심 서버 프리미티브를 복습하고 각각을 언제 사용해야 하는지 이해해 봅시다. 핵심 인사이트는 각 프리미티브가 애플리케이션 스택의 다른 부분에 의해 제어된다는 것입니다.",
        'Tools: Model-Controlled': '도구: 모델 제어',
        'Tools are controlled entirely by Claude. The AI model decides when to call these functions, and the results are used directly by Claude to accomplish tasks.':
            '도구는 전적으로 Claude에 의해 제어됩니다. AI 모델이 이 함수들을 언제 호출할지 결정하고, 결과는 Claude가 작업을 수행하는 데 직접 사용됩니다.',
        'Tools are perfect for giving Claude additional capabilities it can use autonomously.':
            '도구는 Claude가 자율적으로 사용할 수 있는 추가 기능을 제공하는 데 완벽합니다.',
        'Resources: App-Controlled': '리소스: 앱 제어',
        'Resources are controlled by your application code. Your app decides when to fetch resource data and how to use it - typically for UI elements or to add context to conversations.':
            '리소스는 애플리케이션 코드에 의해 제어됩니다. 앱이 리소스 데이터를 언제 가져오고 어떻게 사용할지 결정합니다 - 일반적으로 UI 요소나 대화에 컨텍스트를 추가하기 위해서입니다.',
        'In our project, we used resources in two ways:': '프로젝트에서 리소스를 두 가지 방식으로 사용했습니다:',
        'Fetching data to populate autocomplete options in the UI': 'UI의 자동완성 옵션을 채우기 위한 데이터 가져오기',
        'Retrieving content to augment prompts with additional context': '추가 컨텍스트로 프롬프트를 보강하기 위한 콘텐츠 가져오기',
        'Prompts: User-Controlled': '프롬프트: 사용자 제어',
        'Prompts are triggered by user actions. Users decide when to run these predefined workflows through UI interactions like button clicks, menu selections, or slash commands.':
            '프롬프트는 사용자 액션에 의해 트리거됩니다. 사용자가 버튼 클릭, 메뉴 선택, 슬래시 명령 등의 UI 상호작용을 통해 이러한 사전 정의된 워크플로우를 언제 실행할지 결정합니다.',
        'Prompts are ideal for implementing workflows that users can trigger on demand.':
            '프롬프트는 사용자가 필요에 따라 트리거할 수 있는 워크플로우를 구현하는 데 이상적입니다.',
        'Choosing the Right Primitive': '올바른 프리미티브 선택',
        "Here's a quick decision guide:": '빠른 결정 가이드입니다:',
        'Need to give Claude new capabilities?': 'Claude에게 새로운 기능을 부여해야 하나요?',
        'Use tools': '도구를 사용하세요',
        'Need to get data into your app for UI or context?': '앱의 UI나 컨텍스트를 위해 데이터를 가져와야 하나요?',
        'Use resources': '리소스를 사용하세요',
        'Want to create predefined workflows for users?': '사용자를 위한 사전 정의된 워크플로우를 만들고 싶나요?',
        'Use prompts': '프롬프트를 사용하세요',
        'These are high-level guidelines to help you choose the right primitive for your specific use case. Each serves a different part of your application stack - tools serve the model, resources serve your app, and prompts serve your users.':
            '이것은 특정 사용 사례에 적합한 프리미티브를 선택하는 데 도움이 되는 상위 수준의 가이드라인입니다. 각각은 애플리케이션 스택의 다른 부분을 담당합니다 - 도구는 모델을, 리소스는 앱을, 프롬프트는 사용자를 담당합니다.',
    },
}

def translate_file(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Apply common translations
    all_trans = {**COMMON, **translations}

    # Sort by length (longest first) to avoid partial replacements
    sorted_items = sorted(all_trans.items(), key=lambda x: len(x[0]), reverse=True)

    for eng, kor in sorted_items:
        if eng in content:
            content = content.replace(eng, kor)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    changed = content != original
    return changed

# Process files
for lesson_name, translations in FILES.items():
    # Find matching file
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
