#!/usr/bin/env python3
"""Batch translate all untranslated HTML files in src/ to Korean.
Uses string replacement to preserve HTML structure. All I/O is UTF-8."""

import os
import re

SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')

# Common UI translations shared across all files
COMMON = {
    '>Header Navigation<': '>헤더 내비게이션<',
    '\nAnthropic Academy\n': '\nAnthropic 아카데미\n',
    '\nCourses\n': '\n과정\n',
    '>My Profile<': '>내 프로필<',
    '>Sign Out<': '>로그아웃<',
    '<span>Open in Claude</span>': '<span>Claude에서 열기</span>',
    '\nOpen in Claude\n': '\nClaude에서 열기\n',
    '>Ask questions about this course<': '>이 과정에 대해 질문하기<',
    '>Copy notes<': '>노트 복사<',
    '>Copy full course notes for LLMs<': '>LLM용 전체 과정 노트 복사<',
    '<span>Previous</span>': '<span>이전</span>',
    '<span>Next</span>': '<span>다음</span>',
}

# Per-file translations: {filename: {english: korean}}
TRANSLATIONS = {
    "Defining prompts.html": {
        "<title>Defining prompts</title>": "<title>프롬프트 정의하기</title>",
        "<h2>Defining prompts</h2>": "<h2>프롬프트 정의하기</h2>",
        ">Defining prompts<": ">프롬프트 정의하기<",
        "<p>Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that ": "<p>MCP 서버의 프롬프트를 사용하면 클라이언트가 처음부터 직접 프롬프트를 작성하는 대신 사용할 수 있는 사전 구축된 고품질 지침을 정의할 수 있습니다. 이를 다양한 상황에서 일관된 결과를 보장하는 세심하게 작성된 템플릿이라고 생각하면 됩니다. ",
        "<h2>Why Use Prompts?</h2>": "<h2>왜 프롬프트를 사용할까요?</h2>",
        "<p>Here's the key insight: users can already ask Claude to do most tasks directly. For example, a user could type \"reformat the report.pdf in markdown\" and get decent results. But they'll get much bet": "<p>핵심 통찰은 이것입니다: 사용자는 이미 대부분의 작업을 Claude에게 직접 요청할 수 있습니다. 예를 들어, 사용자가 \"report.pdf를 마크다운으로 다시 포맷해줘\"라고 입력하면 괜찮은 결과를 얻을 수 있습니다. 하지만 훨씬 더 나은 결과를 얻을 수 있습니다. ",
        "<p>As the MCP server author, you can spend time crafting, testing, and evaluating prompts that work consistently across different scenarios. Users benefit from this expertise without having to become ": "<p>MCP 서버 작성자로서, 다양한 시나리오에서 일관되게 작동하는 프롬프트를 작성하고, 테스트하고, 평가하는 데 시간을 투자할 수 있습니다. 사용자는 직접 프롬프트 엔지니어링 전문가가 되지 않아도 이러한 전문 지식의 혜택을 누릴 수 있습니다. ",
        "<h2>Building a Format Command</h2>": "<h2>포맷 명령어 만들기</h2>",
        "<p>Let's implement a practical example: a format command that converts documents to markdown. Users will type <code>/format doc_id</code> and get back a professionally formatted markdown version of th": "<p>실용적인 예제를 구현해 봅시다: 문서를 마크다운으로 변환하는 포맷 명령어입니다. 사용자가 <code>/format doc_id</code>를 입력하면 전문적으로 포맷된 마크다운 버전의 문서를 받을 수 있습니다. ",
        "<p>The workflow looks like this:</p>": "<p>워크플로우는 다음과 같습니다:</p>",
        "<li>User types <code>/</code> to see available commands</li>": "<li>사용자가 <code>/</code>를 입력하여 사용 가능한 명령어를 확인합니다</li>",
        "<li>They select <code>format</code> and specify a document ID</li>": "<li><code>format</code>을 선택하고 문서 ID를 지정합니다</li>",
        "<li>Claude uses your pre-built prompt to read and reformat the document</li>": "<li>Claude가 사전 구축된 프롬프트를 사용하여 문서를 읽고 다시 포맷합니다</li>",
        "<li>The result is clean markdown with proper headers, lists, and formatting</li>": "<li>결과는 적절한 헤더, 목록, 서식을 갖춘 깔끔한 마크다운입니다</li>",
        "<h2>Defining Prompts</h2>": "<h2>프롬프트 정의하기</h2>",
        "<p>Prompts use a similar decorator pattern to tools and resources:</p>": "<p>프롬프트는 도구 및 리소스와 유사한 데코레이터 패턴을 사용합니다:</p>",
        "<p>The function returns a list of messages that get sent directly to Claude. You can include multiple user and assistant messages to create more complex conversation flows.</p>": "<p>이 함수는 Claude에게 직접 전송되는 메시지 목록을 반환합니다. 여러 사용자 및 어시스턴트 메시지를 포함하여 더 복잡한 대화 흐름을 만들 수 있습니다.</p>",
        "<h2>Testing Your Prompts</h2>": "<h2>프롬프트 테스트하기</h2>",
        "<p>Use the MCP Inspector to test your prompts before deploying them:</p>": "<p>프롬프트를 배포하기 전에 MCP Inspector를 사용하여 테스트하세요:</p>",
        "<p>The inspector shows you exactly what messages will be sent to Claude, including how variables get interpolated into your prompt template. This lets you verify the prompt looks correct before users ": "<p>인스펙터는 변수가 프롬프트 템플릿에 어떻게 보간되는지를 포함하여 Claude에게 전송될 메시지를 정확하게 보여줍니다. 이를 통해 사용자가 사용하기 전에 프롬프트가 올바른지 확인할 수 있습니다. ",
        "<h2>Key Benefits</h2>": "<h2>주요 이점</h2>",
        "<li><strong>Consistency</strong> - Users get reliable results every time</li>": "<li><strong>일관성</strong> - 사용자가 매번 신뢰할 수 있는 결과를 얻습니다</li>",
        "<li><strong>Expertise</strong> - You can encode domain knowledge into prompts</li>": "<li><strong>전문성</strong> - 도메인 지식을 프롬프트에 인코딩할 수 있습니다</li>",
        "<li><strong>Reusability</strong> - Multiple client applications can use the same prompts</li>": "<li><strong>재사용성</strong> - 여러 클라이언트 애플리케이션이 동일한 프롬프트를 사용할 수 있습니다</li>",
        "<li><strong>Maintenance</strong> - Update prompts in one place to improve all clients</li>": "<li><strong>유지보수</strong> - 한 곳에서 프롬프트를 업데이트하여 모든 클라이언트를 개선할 수 있습니다</li>",
        "<p>Prompts work best when they're specialized for your MCP server's domain. A document management server might have prompts for formatting, summarizing, or analyzing documents. A data analysis server ": "<p>프롬프트는 MCP 서버의 도메인에 특화되었을 때 가장 잘 작동합니다. 문서 관리 서버에는 문서 포맷팅, 요약 또는 분석을 위한 프롬프트가 있을 수 있습니다. 데이터 분석 서버에는 ",
        "<p>The goal is to provide prompts that are so well-crafted and tested that users prefer them over writing their own instructions from scratch.</p>": "<p>목표는 사용자가 처음부터 직접 지침을 작성하는 것보다 선호할 만큼 잘 만들어지고 테스트된 프롬프트를 제공하는 것입니다.</p>",
        "- Accessing resources": "- 리소스 접근하기",
        "Prompts in the client": "클라이언트에서의 프롬프트",
    },
    "Defining resources.html": {
        "<title>Defining resources</title>": "<title>리소스 정의하기</title>",
        "<h2>Defining resources</h2>": "<h2>리소스 정의하기</h2>",
        ">Defining resources<": ">리소스 정의하기<",
        "<p>Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than": "<p>MCP 서버의 리소스를 사용하면 일반적인 HTTP 서버의 GET 요청 핸들러와 유사하게 클라이언트에 데이터를 노출할 수 있습니다. 작업을 수행하는 것이 아니라 정보를 가져와야 하는 시나리오에 적합합니다.",
        "<h2>Understanding Resources Through an Example</h2>": "<h2>예제를 통한 리소스 이해</h2>",
        "<p>Let's say you want to build a document mention feature where users can type <code>@document_name</code> to reference files. This requires two operations:</p>": "<p>사용자가 <code>@document_name</code>을 입력하여 파일을 참조할 수 있는 문서 멘션 기능을 만들고 싶다고 가정해 봅시다. 이를 위해 두 가지 작업이 필요합니다:</p>",
        "<li>Getting a list of all available documents (for autocomplete)</li>": "<li>사용 가능한 모든 문서 목록 가져오기 (자동완성용)</li>",
        "<li>Fetching the contents of a specific document (when mentioned)</li>": "<li>특정 문서의 내용 가져오기 (멘션될 때)</li>",
        "<p>When a user mentions a document, your system automatically injects the document's contents into the prompt sent to Claude, eliminating the need for Claude to use tools to fetch the information.</p>": "<p>사용자가 문서를 멘션하면 시스템이 자동으로 문서의 내용을 Claude에게 보내는 프롬프트에 주입하여, Claude가 정보를 가져오기 위해 도구를 사용할 필요가 없어집니다.</p>",
        "<h2>How Resources Work</h2>": "<h2>리소스 작동 방식</h2>",
        "<p>Resources follow a request-response pattern. When your client needs data, it sends a <code>ReadResourceRequest</code> with a URI to identify which resource it wants. The MCP server processes this r": "<p>리소스는 요청-응답 패턴을 따릅니다. 클라이언트가 데이터를 필요로 할 때, 원하는 리소스를 식별하기 위해 URI와 함께 <code>ReadResourceRequest</code>를 보냅니다. MCP 서버가 이 요청을 처리합니다.",
        "<p>The flow looks like this: your code requests a resource from the MCP client, which forwards the request to the MCP server. The server processes the URI, runs the appropriate function, and returns t": "<p>흐름은 다음과 같습니다: 코드가 MCP 클라이언트에게 리소스를 요청하면, 클라이언트가 MCP 서버로 요청을 전달합니다. 서버는 URI를 처리하고, 적절한 함수를 실행하며, 결과를 반환합니다.",
        "<h2>Types of Resources</h2>": "<h2>리소스 유형</h2>",
        "<p>There are two types of resources:</p>": "<p>리소스에는 두 가지 유형이 있습니다:</p>",
        "<h3>Direct Resources</h3>": "<h3>직접 리소스</h3>",
        "<p>Direct resources have static URIs that never change. They're perfect for operations that don't need parameters.</p>": "<p>직접 리소스는 변경되지 않는 정적 URI를 가집니다. 매개변수가 필요 없는 작업에 적합합니다.</p>",
        "<h3>Templated Resources</h3>": "<h3>템플릿 리소스</h3>",
        "<p>Templated resources include parameters in their URIs. The Python SDK automatically parses these parameters and passes them as keyword arguments to your function.</p>": "<p>템플릿 리소스는 URI에 매개변수를 포함합니다. Python SDK가 자동으로 이러한 매개변수를 파싱하여 함수에 키워드 인자로 전달합니다.</p>",
        "<h2>Implementation Details</h2>": "<h2>구현 세부사항</h2>",
        "<p>Resources can return any type of data - strings, JSON, binary data, etc. Use the <code>mime_type</code> parameter to give clients a hint about what kind of data you're returning:</p>": "<p>리소스는 문자열, JSON, 바이너리 데이터 등 모든 유형의 데이터를 반환할 수 있습니다. <code>mime_type</code> 매개변수를 사용하여 반환하는 데이터의 종류에 대한 힌트를 클라이언트에게 제공하세요:</p>",
        "<li><code>\"application/json\"</code> for structured data</li>": "<li><code>\"application/json\"</code> 구조화된 데이터용</li>",
        "<li><code>\"text/plain\"</code> for plain text</li>": "<li><code>\"text/plain\"</code> 일반 텍스트용</li>",
        "<li><code>\"application/pdf\"</code> for binary files</li>": "<li><code>\"application/pdf\"</code> 바이너리 파일용</li>",
        "<p>The MCP Python SDK automatically serializes your return values. You don't need to manually convert objects to JSON strings - just return the data structure and let the SDK handle serialization.</p>": "<p>MCP Python SDK는 반환 값을 자동으로 직렬화합니다. 객체를 JSON 문자열로 수동 변환할 필요 없이, 데이터 구조를 반환하면 SDK가 직렬화를 처리합니다.</p>",
        "<h2>Testing Your Resources</h2>": "<h2>리소스 테스트하기</h2>",
        "<p>You can test resources using the MCP Inspector. Start your server with:</p>": "<p>MCP Inspector를 사용하여 리소스를 테스트할 수 있습니다. 다음 명령어로 서버를 시작하세요:</p>",
        "<p>Then connect to the inspector in your browser. You'll see two sections:</p>": "<p>그런 다음 브라우저에서 인스펙터에 연결합니다. 두 개의 섹션이 보일 것입니다:</p>",
        "<li><strong>Resources</strong> - Lists your direct/static resources</li>": "<li><strong>Resources</strong> - 직접/정적 리소스 목록</li>",
        "<li><strong>Resource Templates</strong> - Lists your templated resources</li>": "<li><strong>Resource Templates</strong> - 템플릿 리소스 목록</li>",
        "<p>Click on any resource to test it. For templated resources, you'll need to provide values for the parameters. The inspector shows you the exact response structure your client will receive, including": "<p>리소스를 클릭하여 테스트합니다. 템플릿 리소스의 경우 매개변수 값을 제공해야 합니다. 인스펙터는 MIME 유형과 콘텐츠를 포함하여 클라이언트가 받을 정확한 응답 구조를 보여줍니다.",
        "<p>Resources provide a clean way to expose read-only data from your MCP server, making it easy for clients to fetch information without the complexity of tool calls.</p>": "<p>리소스는 MCP 서버에서 읽기 전용 데이터를 노출하는 깔끔한 방법을 제공하여, 도구 호출의 복잡성 없이 클라이언트가 쉽게 정보를 가져올 수 있게 합니다.</p>",
        "- Implementing a client": "- 클라이언트 구현하기",
        "Accessing resources": "리소스 접근하기",
    },
    "Defining tools with MCP.html": {
        "<title>Defining tools with MCP</title>": "<title>MCP로 도구 정의하기</title>",
        "<h2>Defining tools with MCP</h2>": "<h2>MCP로 도구 정의하기</h2>",
        ">Defining tools with MCP<": ">MCP로 도구 정의하기<",
        "<p>Building an MCP server becomes much simpler when you use the official Python SDK. Instead of writing complex JSON schemas by hand, you can define tools with decorators and let the SDK handle the he": "<p>공식 Python SDK를 사용하면 MCP 서버 구축이 훨씬 간단해집니다. 복잡한 JSON 스키마를 직접 작성하는 대신, 데코레이터로 도구를 정의하고 SDK가 무거운 작업을 처리하도록 할 수 있습니다.",
        "<p>In this example, we're creating a document management server with two core tools: one to read documents and another to update them. All documents exist in memory as a simple dictionary where keys a": "<p>이 예제에서는 문서 읽기와 업데이트를 위한 두 가지 핵심 도구를 갖춘 문서 관리 서버를 만들고 있습니다. 모든 문서는 키가 파일명이고 값이 내용인 간단한 딕셔너리로 메모리에 존재합니다.",
        "<h2>Setting Up the MCP Server</h2>": "<h2>MCP 서버 설정하기</h2>",
        "<p>The Python MCP SDK makes server creation straightforward. You can initialize a server with just one line:</p>": "<p>Python MCP SDK로 서버 생성이 간단합니다. 단 한 줄로 서버를 초기화할 수 있습니다:</p>",
        "<p>Your documents can be stored in a simple dictionary structure:</p>": "<p>문서는 간단한 딕셔너리 구조에 저장할 수 있습니다:</p>",
        "<h2>Tool Definition with Decorators</h2>": "<h2>데코레이터를 사용한 도구 정의</h2>",
        "<p>The SDK uses decorators to define tools. Instead of writing JSON schemas manually, you can use Python type hints and field descriptions. The SDK automatically generates the proper schema that Claud": "<p>SDK는 데코레이터를 사용하여 도구를 정의합니다. JSON 스키마를 수동으로 작성하는 대신, Python 타입 힌트와 필드 설명을 사용할 수 있습니다. SDK가 Claude가 이해하는 적절한 스키마를 자동으로 생성합니다.",
        "<h2>Creating a Document Reader Tool</h2>": "<h2>문서 읽기 도구 만들기</h2>",
        "<p>The first tool reads document contents by ID. Here's the complete implementation:</p>": "<p>첫 번째 도구는 ID로 문서 내용을 읽습니다. 전체 구현은 다음과 같습니다:</p>",
        "<p>The decorator specifies the tool name and description, while the function parameters define the required arguments. The <code>Field</code> class from Pydantic provides argument descriptions that he": "<p>데코레이터는 도구 이름과 설명을 지정하고, 함수 매개변수는 필수 인자를 정의합니다. Pydantic의 <code>Field</code> 클래스는 Claude가 각 매개변수의 용도를 이해하는 데 도움이 되는 인자 설명을 제공합니다.",
        "<h2>Building a Document Editor Tool</h2>": "<h2>문서 편집 도구 만들기</h2>",
        "<p>The second tool performs simple find-and-replace operations on documents:</p>": "<p>두 번째 도구는 문서에서 간단한 찾기-바꾸기 작업을 수행합니다:</p>",
        "<p>This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation includes error handling for missing documents and performs a straightforward string": "<p>이 도구는 세 가지 매개변수를 받습니다: 문서 ID, 찾을 텍스트, 대체 텍스트입니다. 구현에는 문서 누락에 대한 오류 처리가 포함되어 있으며, 간단한 문자열 대체를 수행합니다.",
        "<h2>Key Benefits of the SDK Approach</h2>": "<h2>SDK 접근 방식의 주요 이점</h2>",
        "<li>No manual JSON schema writing required</li>": "<li>수동 JSON 스키마 작성이 필요 없음</li>",
        "<li>Type hints provide automatic validation</li>": "<li>타입 힌트가 자동 유효성 검사를 제공</li>",
        "<li>Clear parameter descriptions help Claude understand tool usage</li>": "<li>명확한 매개변수 설명이 Claude의 도구 사용 이해를 도움</li>",
        "<li>Error handling integrates naturally with Python exceptions</li>": "<li>오류 처리가 Python 예외와 자연스럽게 통합</li>",
        "<li>Tool registration happens automatically through decorators</li>": "<li>데코레이터를 통해 도구 등록이 자동으로 수행</li>",
        "<p>The MCP Python SDK transforms tool creation from a complex schema-writing exercise into simple Python function definitions. This approach makes it much easier to build and maintain MCP servers whil": "<p>MCP Python SDK는 도구 생성을 복잡한 스키마 작성 작업에서 간단한 Python 함수 정의로 변환합니다. 이 접근 방식은 Claude와의 완전한 호환성을 유지하면서 MCP 서버를 훨씬 쉽게 구축하고 유지할 수 있게 합니다.",
        "- Project setup": "- 프로젝트 설정",
        "The server inspector": "서버 인스펙터",
    },
    "Implementing a client.html": {
        "<title>Implementing a client</title>": "<title>클라이언트 구현하기</title>",
        "<h2>Implementing a client</h2>": "<h2>클라이언트 구현하기</h2>",
        ">Implementing a client<": ">클라이언트 구현하기<",
        "<p>Now that we have our MCP server working, it's time to build the client side. The client is what allows our application code to communicate with the MCP server and access its functionality.</p>": "<p>MCP 서버가 작동하고 있으니, 이제 클라이언트 측을 구축할 차례입니다. 클라이언트는 애플리케이션 코드가 MCP 서버와 통신하고 그 기능에 접근할 수 있게 해주는 것입니다.</p>",
        "<h2>Understanding the Client Architecture</h2>": "<h2>클라이언트 아키텍처 이해하기</h2>",
        "<p>In most real-world projects, you'll either implement an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.</p>": "<p>대부분의 실제 프로젝트에서는 MCP 클라이언트 또는 MCP 서버 중 하나만 구현합니다. 이 프로젝트에서는 둘 다 구축하여 함께 작동하는 방식을 볼 수 있도록 합니다.</p>",
        "<p>The MCP client consists of two main components:</p>": "<p>MCP 클라이언트는 두 가지 주요 구성 요소로 이루어져 있습니다:</p>",
        "<li><strong>MCP Client</strong> - A custom class we create to make using the session easier</li>": "<li><strong>MCP Client</strong> - 세션 사용을 더 쉽게 하기 위해 만든 커스텀 클래스</li>",
        "<li><strong>Client Session</strong> - The actual connection to the server (part of the MCP Python SDK)</li>": "<li><strong>Client Session</strong> - 서버와의 실제 연결 (MCP Python SDK의 일부)</li>",
        "<p>The client session requires careful resource management - we need to properly clean up connections when we're done. That's why we wrap it in our own class that handles all the cleanup automatically": "<p>클라이언트 세션은 신중한 리소스 관리가 필요합니다 - 작업이 끝나면 연결을 적절하게 정리해야 합니다. 그래서 모든 정리를 자동으로 처리하는 자체 클래스로 감쌉니다.",
        "<h2>How the Client Fits Into Our Application</h2>": "<h2>클라이언트가 애플리케이션에 어떻게 들어맞는가</h2>",
        "<p>Remember our application flow diagram? The client is what enables our code to interact with the MCP server at two key points:</p>": "<p>애플리케이션 흐름도를 기억하시나요? 클라이언트는 두 가지 핵심 지점에서 코드가 MCP 서버와 상호작용할 수 있게 해줍니다:</p>",
        "<p>Our CLI code uses the client to:</p>": "<p>CLI 코드는 클라이언트를 사용하여:</p>",
        "<li>Get a list of available tools to send to Claude</li>": "<li>Claude에게 보낼 사용 가능한 도구 목록 가져오기</li>",
        "<li>Execute tools when Claude requests them</li>": "<li>Claude가 요청할 때 도구 실행하기</li>",
        "<h2>Implementing Core Client Functions</h2>": "<h2>핵심 클라이언트 함수 구현하기</h2>",
        "<p>We need to implement two essential functions: <code>list_tools()</code> and <code>call_tool()</code>.</p>": "<p>두 가지 필수 함수를 구현해야 합니다: <code>list_tools()</code>와 <code>call_tool()</code>.</p>",
        "<h3>List Tools Function</h3>": "<h3>도구 목록 함수</h3>",
        "<p>This function gets all available tools from the MCP server:</p>": "<p>이 함수는 MCP 서버에서 사용 가능한 모든 도구를 가져옵니다:</p>",
        "<p>It's straightforward - we access our session (the connection to the server), call the built-in <code>list_tools()</code> method, and return the tools from the result.</p>": "<p>간단합니다 - 세션(서버와의 연결)에 접근하고, 내장된 <code>list_tools()</code> 메서드를 호출하며, 결과에서 도구를 반환합니다.</p>",
        "<h3>Call Tool Function</h3>": "<h3>도구 호출 함수</h3>",
        "<p>This function executes a specific tool on the server:</p>": "<p>이 함수는 서버에서 특정 도구를 실행합니다:</p>",
        "<p>We pass the tool name and input parameters (provided by Claude) to the server and return the result.</p>": "<p>도구 이름과 입력 매개변수(Claude가 제공)를 서버에 전달하고 결과를 반환합니다.</p>",
        "<h2>Testing the Client</h2>": "<h2>클라이언트 테스트하기</h2>",
        "<p>The client file includes a simple test harness at the bottom. You can run it directly to verify everything works:</p>": "<p>클라이언트 파일 하단에 간단한 테스트 하니스가 포함되어 있습니다. 직접 실행하여 모든 것이 작동하는지 확인할 수 있습니다:</p>",
        "<p>This will connect to your MCP server and print out the available tools. You should see output showing your tool definitions, including descriptions and input schemas.</p>": "<p>MCP 서버에 연결하고 사용 가능한 도구를 출력합니다. 설명과 입력 스키마를 포함한 도구 정의가 출력되는 것을 볼 수 있습니다.</p>",
        "<h2>Putting It All Together</h2>": "<h2>모두 합쳐보기</h2>",
        "<p>Once the client functions are implemented, you can test the complete flow by running your main application:</p>": "<p>클라이언트 함수가 구현되면, 메인 애플리케이션을 실행하여 전체 흐름을 테스트할 수 있습니다:</p>",
        "<p>Try asking: \"What is the contents of the report.pdf document?\"</p>": "<p>이렇게 물어보세요: \"report.pdf 문서의 내용이 무엇인가요?\"</p>",
        "<p>Here's what happens behind the scenes:</p>": "<p>내부적으로 다음과 같은 일이 일어납니다:</p>",
        "<li>Your application uses the client to get available tools</li>": "<li>애플리케이션이 클라이언트를 사용하여 사용 가능한 도구를 가져옵니다</li>",
        "<li>These tools are sent to Claude along with your question</li>": "<li>이 도구들이 질문과 함께 Claude에게 전송됩니다</li>",
        "<li>Claude decides to use the read_doc_contents tool</li>": "<li>Claude가 read_doc_contents 도구를 사용하기로 결정합니다</li>",
        "<li>Your application uses the client to execute that tool</li>": "<li>애플리케이션이 클라이언트를 사용하여 해당 도구를 실행합니다</li>",
        "<li>The result is returned to Claude, who then responds to you</li>": "<li>결과가 Claude에게 반환되고, Claude가 응답합니다</li>",
        "<p>The client acts as the bridge between your application logic and the MCP server's functionality, making it easy to integrate powerful tools into your AI workflows.</p>": "<p>클라이언트는 애플리케이션 로직과 MCP 서버의 기능 사이의 다리 역할을 하여, 강력한 도구를 AI 워크플로우에 쉽게 통합할 수 있게 합니다.</p>",
        "- Course satisfaction survey": "- 과정 만족도 설문",
        "Defining resources": "리소스 정의하기",
    },
    "Introducing MCP.html": {
        "<title>Introducing MCP</title>": "<title>MCP 소개</title>",
        "<h2>Introducing MCP</h2>": "<h2>MCP 소개</h2>",
        ">Introducing MCP<": ">MCP 소개<",
        "<p>Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift t": "<p>Model Context Protocol (MCP)은 지루한 통합 코드를 많이 작성할 필요 없이 Claude에게 컨텍스트와 도구를 제공하는 통신 계층입니다. 도구 관리의 부담을 자신의 서버에서 전문화된 MCP 서버로 옮기는 방법이라고 생각하세요.",
        "<p>When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP Server a": "<p>MCP를 처음 접하면 기본 아키텍처를 보여주는 다이어그램을 볼 수 있습니다: 도구, 프롬프트, 리소스를 포함하는 MCP 서버에 연결하는 MCP 클라이언트(여러분의 서버). 각 MCP 서버는 특정 서비스의 전문 래퍼 역할을 합니다.",
        "<h2>The Problem MCP Solves</h2>": "<h2>MCP가 해결하는 문제</h2>",
        "<p>Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask \"What open pull requests are there across all my repositories?\" To handle this, Claud": "<p>사용자가 GitHub 데이터에 대해 Claude에게 질문할 수 있는 채팅 인터페이스를 구축한다고 가정해 봅시다. 사용자가 \"내 모든 리포지토리에 열려 있는 풀 리퀘스트는 무엇인가요?\"라고 물을 수 있습니다. 이를 처리하려면 Claude가 GitHub의 API와 상호작용해야 합니다.",
        "<p>GitHub has massive functionality - repositories, pull requests, issues, projects, and tons more. Without MCP, you'd need to create an incredible number of tool schemas and functions to handle all o": "<p>GitHub에는 리포지토리, 풀 리퀘스트, 이슈, 프로젝트 등 방대한 기능이 있습니다. MCP 없이는 이 모든 기능을 처리하기 위해 엄청난 수의 도구 스키마와 함수를 만들어야 합니다.",
        "<p>This means writing, testing, and maintaining all that integration code yourself. That's a lot of effort and ongoing maintenance burden.</p>": "<p>이는 모든 통합 코드를 직접 작성하고, 테스트하고, 유지해야 한다는 의미입니다. 많은 노력과 지속적인 유지보수 부담이 됩니다.</p>",
        "<h2>How MCP Works</h2>": "<h2>MCP 작동 방식</h2>",
        "<p>MCP shifts this burden by moving tool definitions and execution from your server to dedicated MCP servers. Instead of you authoring all those GitHub tools, an MCP Server for GitHub handles it.</p>": "<p>MCP는 도구 정의와 실행을 여러분의 서버에서 전용 MCP 서버로 이동시켜 이 부담을 줄입니다. 여러분이 모든 GitHub 도구를 작성하는 대신, GitHub용 MCP 서버가 이를 처리합니다.</p>",
        "<p>The MCP Server wraps up tons of functionality around GitHub and exposes it as a standardized set of tools. Your application connects to this MCP server instead of implementing everything from scrat": "<p>MCP 서버는 GitHub 관련 수많은 기능을 래핑하고 표준화된 도구 세트로 노출합니다. 애플리케이션은 처음부터 모든 것을 구현하는 대신 이 MCP 서버에 연결합니다.",
        "<h2>MCP Servers Explained</h2>": "<h2>MCP 서버 설명</h2>",
        "<p>MCP Servers provide access to data or functionality implemented by outside services. They act as specialized interfaces that expose tools, prompts, and resources in a standardized way.</p>": "<p>MCP 서버는 외부 서비스가 구현한 데이터나 기능에 대한 접근을 제공합니다. 표준화된 방식으로 도구, 프롬프트, 리소스를 노출하는 전문화된 인터페이스 역할을 합니다.</p>",
        "<p>In our GitHub example, the MCP Server for GitHub contains tools like <code>get_repos()</code> and connects directly to GitHub's API. Your server communicates with the MCP server, which handles all ": "<p>GitHub 예제에서, GitHub용 MCP 서버는 <code>get_repos()</code>와 같은 도구를 포함하고 GitHub의 API에 직접 연결합니다. 여러분의 서버는 MCP 서버와 통신하며, MCP 서버가 모든 API 상호작용을 처리합니다.",
        "<h2>Common Questions</h2>": "<h2>자주 묻는 질문</h2>",
        "<h3>Who authors MCP Servers?</h3>": "<h3>MCP 서버는 누가 만드나요?</h3>",
        "<p>Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tool": "<p>누구나 MCP 서버 구현을 만들 수 있습니다. 종종 서비스 제공자들이 직접 공식 MCP 구현을 만들기도 합니다. 예를 들어, AWS가 AWS 서비스와 상호작용하기 위한 도구가 포함된 공식 MCP 서버를 출시할 수 있습니다.",
        "<h3>How is this different from calling APIs directly?</h3>": "<h3>API를 직접 호출하는 것과 어떻게 다른가요?</h3>",
        "<p>MCP servers provide tool schemas and functions already defined for you. If you want to call an API directly, you'll be authoring those tool definitions on your own. MCP saves you that implementatio": "<p>MCP 서버는 이미 정의된 도구 스키마와 함수를 제공합니다. API를 직접 호출하려면 도구 정의를 직접 작성해야 합니다. MCP는 그 구현 작업을 줄여줍니다.",
        "<h3>Isn't MCP just the same as tool use?</h3>": "<h3>MCP는 도구 사용과 같은 것 아닌가요?</h3>",
        "<p>This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP servers provide tool schemas and functions already defined for you, while tool use is about ho": "<p>이것은 흔한 오해입니다. MCP 서버와 도구 사용은 상호 보완적이지만 다른 개념입니다. MCP 서버는 이미 정의된 도구 스키마와 함수를 제공하고, 도구 사용은 Claude가 이러한 도구를 어떻게 활용하는지에 대한 것입니다.",
        "<p>The benefit is clear: instead of maintaining a complex set of integrations yourself, you can leverage MCP servers that handle the heavy lifting of connecting to external services.</p>": "<p>이점은 명확합니다: 복잡한 통합 세트를 직접 유지하는 대신, 외부 서비스 연결의 무거운 작업을 처리하는 MCP 서버를 활용할 수 있습니다.</p>",
        "- Welcome to the course": "- 과정에 오신 것을 환영합니다",
        ">MCP clients<": ">MCP 클라이언트<",
    },
    "MCP clients.html": {
        "<title>MCP clients</title>": "<title>MCP 클라이언트</title>",
        "<h2>MCP clients</h2>": "<h2>MCP 클라이언트</h2>",
        ">MCP clients<": ">MCP 클라이언트<",
        "<p>The MCP client serves as the communication bridge between your server and MCP servers. It's your access point to all the tools that an MCP server provides, handling the message exchange and protoco": "<p>MCP 클라이언트는 여러분의 서버와 MCP 서버 사이의 통신 다리 역할을 합니다. MCP 서버가 제공하는 모든 도구에 대한 접근 지점으로, 메시지 교환과 프로토콜 세부사항을 처리합니다.",
        "<h2>Transport Agnostic Communication</h2>": "<h2>전송 방식에 구애받지 않는 통신</h2>",
        "<p>One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can communicate over different protocols depending on your setup.</p>": "<p>MCP의 핵심 강점 중 하나는 전송 방식에 구애받지 않는다는 것입니다 - 설정에 따라 클라이언트와 서버가 다양한 프로토콜로 통신할 수 있다는 멋진 표현입니다.</p>",
        "<p>The most common setup runs both the MCP client and server on the same machine, communicating through standard input/output. But you can also connect them over:</p>": "<p>가장 일반적인 설정은 MCP 클라이언트와 서버를 동일한 머신에서 실행하여 표준 입출력으로 통신하는 것입니다. 하지만 다음을 통해서도 연결할 수 있습니다:</p>",
        "<li>Various other network protocols</li>": "<li>기타 다양한 네트워크 프로토콜</li>",
        "<h2>MCP Message Types</h2>": "<h2>MCP 메시지 유형</h2>",
        "<p>Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:</p>": "<p>연결되면, 클라이언트와 서버는 MCP 사양에 정의된 특정 메시지 유형을 교환합니다. 주로 다루게 될 것들은:</p>",
        "<p><strong>ListToolsRequest/ListToolsResult:</strong> The client asks the server \"what tools do you provide?\" and gets back a list of available tools.</p>": "<p><strong>ListToolsRequest/ListToolsResult:</strong> 클라이언트가 서버에게 \"어떤 도구를 제공하나요?\"라고 묻고 사용 가능한 도구 목록을 받습니다.</p>",
        "<p><strong>CallToolRequest/CallToolResult:</strong> The client asks the server to run a specific tool with given arguments, then receives the results.</p>": "<p><strong>CallToolRequest/CallToolResult:</strong> 클라이언트가 서버에게 주어진 인자로 특정 도구를 실행하도록 요청하고, 결과를 받습니다.</p>",
        "<h2>How It All Works Together</h2>": "<h2>모든 것이 어떻게 함께 작동하는가</h2>",
        "<p>Here's a complete example showing how a user query flows through the entire system - from your server, through the MCP client, to external services like GitHub, and back to Claude.</p>": "<p>사용자 쿼리가 전체 시스템을 통해 어떻게 흐르는지 보여주는 완전한 예제입니다 - 여러분의 서버에서 MCP 클라이언트를 거쳐, GitHub과 같은 외부 서비스로, 그리고 다시 Claude로 돌아옵니다.</p>",
        "<p>Let's say a user asks \"What repositories do I have?\" Here's the step-by-step flow:</p>": "<p>사용자가 \"내 리포지토리는 뭐가 있나요?\"라고 물었다고 가정합시다. 단계별 흐름은 다음과 같습니다:</p>",
        "<li><strong>User Query:</strong> The user submits their question to your server</li>": "<li><strong>사용자 쿼리:</strong> 사용자가 서버에 질문을 제출합니다</li>",
        "<li><strong>Tool Discovery:</strong> Your server needs to know what tools are available to send to Claude</li>": "<li><strong>도구 발견:</strong> 서버가 Claude에게 보낼 수 있는 도구가 무엇인지 알아야 합니다</li>",
        "<li><strong>List Tools Exchange:</strong> Your server asks the MCP client for available tools</li>": "<li><strong>도구 목록 교환:</strong> 서버가 MCP 클라이언트에게 사용 가능한 도구를 요청합니다</li>",
        "<li><strong>MCP Communication:</strong> The MCP client sends a <code>ListToolsRequest</code> to the MCP server and receives a <code>ListToolsResult</code></li>": "<li><strong>MCP 통신:</strong> MCP 클라이언트가 MCP 서버에 <code>ListToolsRequest</code>를 보내고 <code>ListToolsResult</code>를 받습니다</li>",
        "<li><strong>Claude Request:</strong> Your server sends the user's query plus the available tools to Claude</li>": "<li><strong>Claude 요청:</strong> 서버가 사용자의 쿼리와 사용 가능한 도구를 Claude에게 전송합니다</li>",
        "<li><strong>Tool Use Decision:</strong> Claude decides it needs to call a tool to answer the question</li>": "<li><strong>도구 사용 결정:</strong> Claude가 질문에 답하기 위해 도구를 호출해야 한다고 결정합니다</li>",
        "<li><strong>Tool Execution Request:</strong> Your server asks the MCP client to run the tool Claude specified</li>": "<li><strong>도구 실행 요청:</strong> 서버가 MCP 클라이언트에게 Claude가 지정한 도구를 실행하도록 요청합니다</li>",
        "<li><strong>External API Call:</strong> The MCP client sends a <code>CallToolRequest</code> to the MCP server, which makes the actual GitHub API call</li>": "<li><strong>외부 API 호출:</strong> MCP 클라이언트가 MCP 서버에 <code>CallToolRequest</code>를 보내고, MCP 서버가 실제 GitHub API를 호출합니다</li>",
        "<li><strong>Results Flow Back:</strong> GitHub responds with repository data, which flows back through the MCP server as a <code>CallToolResult</code></li>": "<li><strong>결과 반환:</strong> GitHub이 리포지토리 데이터로 응답하고, 이는 MCP 서버를 통해 <code>CallToolResult</code>로 반환됩니다</li>",
        "<li><strong>Tool Result to Claude:</strong> Your server sends the tool results back to Claude</li>": "<li><strong>도구 결과를 Claude에게:</strong> 서버가 도구 결과를 Claude에게 다시 전송합니다</li>",
        "<li><strong>Final Response:</strong> Claude formulates a final answer using the repository data</li>": "<li><strong>최종 응답:</strong> Claude가 리포지토리 데이터를 사용하여 최종 답변을 작성합니다</li>",
        "<li><strong>User Gets Answer:</strong> Your server delivers Claude's response back to the user</li>": "<li><strong>사용자가 답변을 받음:</strong> 서버가 Claude의 응답을 사용자에게 전달합니다</li>",
        "<p>Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on your application logic ": "<p>네, 이 흐름은 많은 단계를 포함하지만 각 구성 요소에는 명확한 책임이 있습니다. MCP 클라이언트는 서버 통신의 복잡성을 추상화하여 애플리케이션 로직에 집중할 수 있게 합니다. ",
        "<p>Understanding this flow is crucial because you'll see all these pieces when building your own MCP clients and servers in the upcoming sections.</p>": "<p>이 흐름을 이해하는 것은 중요합니다. 다음 섹션에서 자신만의 MCP 클라이언트와 서버를 구축할 때 이 모든 요소들을 보게 될 것이기 때문입니다.</p>",
        "- Introducing MCP": "- MCP 소개",
        "Project setup": "프로젝트 설정",
    },
    "MCP review.html": {
        "<title>MCP review</title>": "<title>MCP 복습</title>",
        "<h2>MCP review</h2>": "<h2>MCP 복습</h2>",
        ">MCP review<": ">MCP 복습<",
        "<p>Now that we've built our MCP server, let's review the three core server primitives and understand when to use each one. The key insight is that each primitive is controlled by a different part of y": "<p>MCP 서버를 구축했으니, 세 가지 핵심 서버 프리미티브를 복습하고 각각을 언제 사용해야 하는지 이해해 봅시다. 핵심 통찰은 각 프리미티브가 시스템의 다른 부분에 의해 제어된다는 것입니다.",
        "<h2>Tools: Model-Controlled</h2>": "<h2>도구: 모델 제어</h2>",
        "<p>Tools are controlled entirely by Claude. The AI model decides when to call these functions, and the results are used directly by Claude to accomplish tasks.</p>": "<p>도구는 전적으로 Claude에 의해 제어됩니다. AI 모델이 이러한 함수를 언제 호출할지 결정하며, 결과는 Claude가 작업을 수행하는 데 직접 사용됩니다.</p>",
        "<p>Tools are perfect for giving Claude additional capabilities it can use autonomously. When you ask Claude to \"calculate the square root of 3 using JavaScript,\" it's Claude that decides to use a Java": "<p>도구는 Claude가 자율적으로 사용할 수 있는 추가 기능을 제공하는 데 적합합니다. Claude에게 \"JavaScript를 사용하여 3의 제곱근을 계산해줘\"라고 요청하면, JavaScript 실행 도구를 사용하기로 결정하는 것은 Claude입니다.",
        "<h2>Resources: App-Controlled</h2>": "<h2>리소스: 앱 제어</h2>",
        "<p>Resources are controlled by your application code. Your app decides when to fetch resource data and how to use it - typically for UI elements or to add context to conversations.</p>": "<p>리소스는 애플리케이션 코드에 의해 제어됩니다. 앱이 리소스 데이터를 언제 가져올지, 어떻게 사용할지를 결정합니다 - 일반적으로 UI 요소나 대화에 컨텍스트를 추가하기 위해 사용됩니다.</p>",
        "<p>In our project, we used resources in two ways:</p>": "<p>우리 프로젝트에서는 리소스를 두 가지 방식으로 사용했습니다:</p>",
        "<li>Fetching data to populate autocomplete options in the UI</li>": "<li>UI에서 자동완성 옵션을 채우기 위한 데이터 가져오기</li>",
        "<li>Retrieving content to augment prompts with additional context</li>": "<li>추가 컨텍스트로 프롬프트를 보강하기 위한 콘텐츠 가져오기</li>",
        "<p>Think of the \"Add from Google Drive\" feature in Claude's interface - the application code determines which documents to show and handles injecting their content into the chat context.</p>": "<p>Claude 인터페이스의 \"Google Drive에서 추가\" 기능을 생각해 보세요 - 애플리케이션 코드가 어떤 문서를 표시할지 결정하고 그 내용을 채팅 컨텍스트에 주입하는 것을 처리합니다.</p>",
        "<h2>Prompts: User-Controlled</h2>": "<h2>프롬프트: 사용자 제어</h2>",
        "<p>Prompts are triggered by user actions. Users decide when to run these predefined workflows through UI interactions like button clicks, menu selections, or slash commands.</p>": "<p>프롬프트는 사용자 행동에 의해 트리거됩니다. 사용자가 버튼 클릭, 메뉴 선택 또는 슬래시 명령어와 같은 UI 상호작용을 통해 이러한 사전 정의된 워크플로우를 언제 실행할지 결정합니다.</p>",
        "<p>Prompts are ideal for implementing workflows that users can trigger on demand. In Claude's interface, those workflow buttons below the chat input are examples of prompts - predefined, optimized wor": "<p>프롬프트는 사용자가 필요에 따라 트리거할 수 있는 워크플로우를 구현하는 데 이상적입니다. Claude 인터페이스에서 채팅 입력란 아래의 워크플로우 버튼들이 프롬프트의 예입니다 - 사전 정의되고 최적화된 워크플로우입니다.",
        "<h2>Choosing the Right Primitive</h2>": "<h2>올바른 프리미티브 선택하기</h2>",
        "<p>Here's a quick decision guide:</p>": "<p>빠른 결정 가이드입니다:</p>",
        "<li><strong>Need to give Claude new capabilities?</strong> Use tools</li>": "<li><strong>Claude에게 새로운 기능을 부여해야 하나요?</strong> 도구를 사용하세요</li>",
        "<li><strong>Need to get data into your app for UI or context?</strong> Use resources</li>": "<li><strong>UI나 컨텍스트를 위해 앱에 데이터를 가져와야 하나요?</strong> 리소스를 사용하세요</li>",
        "<li><strong>Want to create predefined workflows for users?</strong> Use prompts</li>": "<li><strong>사용자를 위한 사전 정의된 워크플로우를 만들고 싶나요?</strong> 프롬프트를 사용하세요</li>",
        "<p>You can see all three primitives in action in Claude's official interface. The workflow buttons demonstrate prompts, the Google Drive integration shows resources in action, and when Claude executes": "<p>Claude의 공식 인터페이스에서 세 가지 프리미티브 모두를 볼 수 있습니다. 워크플로우 버튼은 프롬프트를, Google Drive 통합은 리소스를, Claude가 코드를 실행할 때는 도구를 보여줍니다.",
        "<p>These are high-level guidelines to help you choose the right primitive for your specific use case. Each serves a different part of your application stack - tools serve the model, resources serve yo": "<p>이것들은 특정 사용 사례에 맞는 올바른 프리미티브를 선택하는 데 도움이 되는 높은 수준의 가이드라인입니다. 각각은 애플리케이션 스택의 다른 부분을 담당합니다 - 도구는 모델을, 리소스는 앱을, 프롬프트는 사용자를 위해 작동합니다.",
        "- Final assessment on MCP": "- MCP 최종 평가",
    },
    "Prompts in the client.html": {
        "<title>Prompts in the client</title>": "<title>클라이언트에서의 프롬프트</title>",
        "<h2>Prompts in the client</h2>": "<h2>클라이언트에서의 프롬프트</h2>",
        ">Prompts in the client<": ">클라이언트에서의 프롬프트<",
        "<p>The final step in building our MCP client is implementing prompt functionality. This allows us to list all available prompts from the server and retrieve specific prompts with variables filled in.<": "<p>MCP 클라이언트 구축의 마지막 단계는 프롬프트 기능을 구현하는 것입니다. 이를 통해 서버에서 사용 가능한 모든 프롬프트를 나열하고 변수가 채워진 특정 프롬프트를 가져올 수 있습니다.<",
        "<h2>Implementing List Prompts</h2>": "<h2>프롬프트 목록 구현하기</h2>",
        "<p>The <code>list_prompts</code> method is straightforward. It calls the session's list prompts function and returns the prompts:</p>": "<p><code>list_prompts</code> 메서드는 간단합니다. 세션의 프롬프트 목록 함수를 호출하고 프롬프트를 반환합니다:</p>",
        "<h2>Getting Individual Prompts</h2>": "<h2>개별 프롬프트 가져오기</h2>",
        "<p>The <code>get_prompt</code> method is more interesting because it handles variable interpolation. When you request a prompt, you provide arguments that get passed to the prompt function as keyword ": "<p><code>get_prompt</code> 메서드는 변수 보간을 처리하기 때문에 더 흥미롭습니다. 프롬프트를 요청할 때 프롬프트 함수에 키워드 인자로 전달되는 인자를 제공합니다. ",
        "<p>For example, if your server has a <code>format_document</code> prompt that expects a <code>doc_id</code> parameter, the arguments dictionary would contain <code>{\"doc_id\": \"plan.md\"}</code>. This v": "<p>예를 들어, 서버에 <code>doc_id</code> 매개변수를 기대하는 <code>format_document</code> 프롬프트가 있다면, 인자 딕셔너리에는 <code>{\"doc_id\": \"plan.md\"}</code>가 포함됩니다. 이 값이 프롬프트 템플릿에 보간됩니다.",
        "<h2>Testing Prompts in Action</h2>": "<h2>프롬프트 실제 테스트</h2>",
        "<p>Once implemented, you can test prompts through the CLI. When you type a slash (<code>/</code>), available prompts appear as commands. Selecting a prompt like \"format\" will prompt you to choose from": "<p>구현이 완료되면 CLI를 통해 프롬프트를 테스트할 수 있습니다. 슬래시(<code>/</code>)를 입력하면 사용 가능한 프롬프트가 명령어로 나타납니다. \"format\"과 같은 프롬프트를 선택하면 사용 가능한 문서 중에서 선택하라는 메시지가 표시됩니다.",
        "<p>After selecting a document, the system sends the complete prompt to Claude. The AI receives both the formatting instructions and the document ID, then uses available tools to fetch and process the ": "<p>문서를 선택하면 시스템이 완전한 프롬프트를 Claude에게 보냅니다. AI는 서식 지침과 문서 ID를 모두 받은 다음, 사용 가능한 도구를 사용하여 문서를 가져오고 처리합니다. ",
        "<h2>How Prompts Work</h2>": "<h2>프롬프트 작동 방식</h2>",
        "<p>Prompts define a set of user and assistant messages that clients can use. They should be high-quality, well-tested, and relevant to your MCP server's purpose. The workflow is:</p>": "<p>프롬프트는 클라이언트가 사용할 수 있는 사용자 및 어시스턴트 메시지 세트를 정의합니다. 고품질이고 잘 테스트되어야 하며 MCP 서버의 목적에 관련되어야 합니다. 워크플로우는 다음과 같습니다:</p>",
        "<li>Write and evaluate a prompt relevant to your server's functionality</li>": "<li>서버 기능에 관련된 프롬프트를 작성하고 평가합니다</li>",
        "<li>Define the prompt in your MCP server using the <code>@mcp.prompt</code> decorator</li>": "<li><code>@mcp.prompt</code> 데코레이터를 사용하여 MCP 서버에서 프롬프트를 정의합니다</li>",
        "<li>Clients can request the prompt at any time</li>": "<li>클라이언트가 언제든지 프롬프트를 요청할 수 있습니다</li>",
        "<li>Arguments provided by the client become keyword arguments in your prompt function</li>": "<li>클라이언트가 제공한 인자가 프롬프트 함수의 키워드 인자가 됩니다</li>",
        "<li>The function returns formatted messages ready for the AI model</li>": "<li>함수가 AI 모델을 위한 포맷된 메시지를 반환합니다</li>",
        "<p>This system creates reusable, parameterized prompts that maintain consistency while allowing customization through variables. It's particularly useful for complex workflows where you want to ensure": "<p>이 시스템은 변수를 통한 커스터마이징을 허용하면서 일관성을 유지하는 재사용 가능한 매개변수화된 프롬프트를 만듭니다. 사용자에게 최적의 결과를 보장하고 싶은 복잡한 워크플로우에 특히 유용합니다.",
        "- Defining prompts": "- 프롬프트 정의하기",
        "Final assessment on MCP": "MCP 최종 평가",
    },
    "The server inspector.html": {
        "<title>The server inspector</title>": "<title>서버 인스펙터</title>",
        "<h2>The server inspector</h2>": "<h2>서버 인스펙터</h2>",
        ">The server inspector<": ">서버 인스펙터<",
        "<p>When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and": "<p>MCP 서버를 구축할 때, 전체 애플리케이션에 연결하지 않고도 기능을 테스트할 방법이 필요합니다. Python MCP SDK에는 도구를 디버그하고 테스트할 수 있는 내장 브라우저 기반 인스펙터가 포함되어 있습니다.",
        "<h2>Starting the Inspector</h2>": "<h2>인스펙터 시작하기</h2>",
        "<p>First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:</p>": "<p>먼저 Python 환경이 활성화되어 있는지 확인하세요 (정확한 명령어는 프로젝트의 README를 확인하세요). 그런 다음 인스펙터를 실행합니다:</p>",
        "<p>This starts a development server and gives you a local URL, typically something like <code>http://127.0.0.1:6274</code>. Open this URL in your browser to access the MCP Inspector.</p>": "<p>이렇게 하면 개발 서버가 시작되고 로컬 URL이 제공됩니다. 일반적으로 <code>http://127.0.0.1:6274</code>와 같습니다. 브라우저에서 이 URL을 열어 MCP Inspector에 접근하세요.</p>",
        "<h2>Using the Inspector Interface</h2>": "<h2>인스펙터 인터페이스 사용하기</h2>",
        "<p>The inspector interface is actively being developed, so it may look different when you use it. However, the core functionality remains consistent. Look for these key elements:</p>": "<p>인스펙터 인터페이스는 활발히 개발 중이므로, 사용할 때 다르게 보일 수 있습니다. 하지만 핵심 기능은 일관됩니다. 다음 핵심 요소들을 찾으세요:</p>",
        "<li>A <strong>Connect</strong> button to start your MCP server</li>": "<li>MCP 서버를 시작하는 <strong>Connect</strong> 버튼</li>",
        "<li>Navigation tabs for <strong>Resources</strong>, <strong>Tools</strong>, <strong>Prompts</strong>, and other features</li>": "<li><strong>Resources</strong>, <strong>Tools</strong>, <strong>Prompts</strong> 및 기타 기능을 위한 내비게이션 탭</li>",
        "<li>A tools listing and testing panel</li>": "<li>도구 목록 및 테스트 패널</li>",
        "<p>Click the Connect button first to initialize your server. You'll see the connection status change from \"Disconnected\" to \"Connected\".</p>": "<p>먼저 Connect 버튼을 클릭하여 서버를 초기화하세요. 연결 상태가 \"Disconnected\"에서 \"Connected\"로 변경되는 것을 볼 수 있습니다.</p>",
        "<h2>Testing Your Tools</h2>": "<h2>도구 테스트하기</h2>",
        "<p>Navigate to the Tools section and click \"List Tools\" to see all available tools from your server. When you select a tool, the right panel shows its details and input fields.</p>": "<p>Tools 섹션으로 이동하여 \"List Tools\"를 클릭하면 서버의 모든 사용 가능한 도구를 볼 수 있습니다. 도구를 선택하면 오른쪽 패널에 세부 정보와 입력 필드가 표시됩니다.</p>",
        "<p>For example, to test a document reading tool:</p>": "<p>예를 들어, 문서 읽기 도구를 테스트하려면:</p>",
        "<li>Select the <code>read_doc_contents</code> tool</li>": "<li><code>read_doc_contents</code> 도구를 선택합니다</li>",
        "<li>Enter a document ID (like \"deposition.md\")</li>": "<li>문서 ID를 입력합니다 (예: \"deposition.md\")</li>",
        "<li>Click \"Run Tool\"</li>": "<li>\"Run Tool\"을 클릭합니다</li>",
        "<li>Check the results for success and expected output</li>": "<li>성공 여부와 예상 출력을 확인합니다</li>",
        "<p>The inspector shows both the success status and the actual returned data, making it easy to verify your tool works correctly.</p>": "<p>인스펙터는 성공 상태와 실제 반환된 데이터를 모두 보여주어, 도구가 올바르게 작동하는지 쉽게 확인할 수 있습니다.</p>",
        "<h2>Testing Tool Interactions</h2>": "<h2>도구 상호작용 테스트</h2>",
        "<p>You can test multiple tools in sequence to verify complex workflows. For instance, after using an edit tool to modify a document, immediately test the read tool to confirm the changes were applied ": "<p>복잡한 워크플로우를 검증하기 위해 여러 도구를 순서대로 테스트할 수 있습니다. 예를 들어, 편집 도구를 사용하여 문서를 수정한 후, 읽기 도구로 바로 테스트하여 변경 사항이 적용되었는지 확인할 수 있습니다. ",
        "<p>The inspector maintains your server state between tool calls, so edits persist and you can verify the complete functionality of your MCP server.</p>": "<p>인스펙터는 도구 호출 사이에 서버 상태를 유지하므로, 편집이 지속되며 MCP 서버의 전체 기능을 검증할 수 있습니다.</p>",
        "<h2>Development Workflow</h2>": "<h2>개발 워크플로우</h2>",
        "<p>The MCP Inspector becomes an essential part of your development process. Instead of writing separate test scripts or connecting to full applications, you can:</p>": "<p>MCP Inspector는 개발 프로세스의 필수 부분이 됩니다. 별도의 테스트 스크립트를 작성하거나 전체 애플리케이션에 연결하는 대신:</p>",
        "<li>Quickly iterate on tool implementations</li>": "<li>도구 구현을 빠르게 반복할 수 있습니다</li>",
        "<li>Test edge cases and error conditions</li>": "<li>엣지 케이스와 오류 조건을 테스트할 수 있습니다</li>",
        "<li>Verify tool interactions and state management</li>": "<li>도구 상호작용과 상태 관리를 검증할 수 있습니다</li>",
        "<li>Debug issues in real-time</li>": "<li>실시간으로 이슈를 디버그할 수 있습니다</li>",
        "<p>This immediate feedback loop makes MCP server development much more efficient and helps catch issues early in the development process.</p>": "<p>이러한 즉각적인 피드백 루프는 MCP 서버 개발을 훨씬 효율적으로 만들고, 개발 프로세스 초기에 문제를 발견하는 데 도움을 줍니다.</p>",
        "- Defining tools with MCP": "- MCP로 도구 정의하기",
        "Course satisfaction survey": "과정 만족도 설문",
    },
}


def translate_file(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    count = 0

    # Apply common translations
    for eng, kor in COMMON.items():
        if eng in content:
            content = content.replace(eng, kor)
            count += 1

    # Apply file-specific translations
    for eng, kor in translations.items():
        if eng in content:
            content = content.replace(eng, kor)
            count += 1

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        # Verify
        with open(filepath, 'r', encoding='utf-8') as f:
            verify = f.read(500)

        korean_count = len(re.findall(r'[\uac00-\ud7af]', content))
        print(f'  [OK] {os.path.basename(filepath)}: {count} replacements, {korean_count} Korean chars')
    else:
        print(f'  [SKIP] {os.path.basename(filepath)}: no matches found')


def main():
    print('Batch translating HTML files to Korean...\n')

    for filename, translations in TRANSLATIONS.items():
        filepath = os.path.join(SRC_DIR, filename)
        if not os.path.exists(filepath):
            print(f'  [MISSING] {filename}')
            continue
        translate_file(filepath, translations)

    print('\nDone.')


if __name__ == '__main__':
    main()
