#!/usr/bin/env python3
# Translation script for 4 HTML files - English to Korean
import re
import os

# Common navigation translations (shared across all files)
NAV_TRANSLATIONS = {
    'Anthropic Academy': 'Anthropic 아카데미',
    'Courses': '강좌',
    'My Profile': '내 프로필',
    'Sign Out': '로그아웃',
    'Claude Code in Action': 'Claude Code 실전 활용',
    'Course Overview': '강좌 개요',
    'What is Claude Code?': 'Claude Code란?',
    'Introduction': '소개',
    'What is a coding assistant?': '코딩 어시스턴트란?',
    'Claude Code in action': 'Claude Code 실전 활용',
    'Getting hands on': '직접 해보기',
    'Claude Code setup': 'Claude Code 설정',
    'Project setup': '프로젝트 설정',
    'Adding context': '컨텍스트 추가',
    'Making changes': '변경 사항 만들기',
    'Course satisfaction survey': '강좌 만족도 설문조사',
    'Controlling context': '컨텍스트 제어',
    'Custom commands': '커스텀 명령어',
    'MCP servers with Claude Code': 'Claude Code와 MCP 서버',
    'Github integration': 'Github 통합',
    'Hooks and the SDK': '훅과 SDK',
    'Introducing hooks': '훅 소개',
    'Defining hooks': '훅 정의하기',
    'Implementing a hook': '훅 구현하기',
    'Gotchas around hooks': '훅 관련 주의사항',
    'Useful hooks!': '유용한 훅!',
    'Another useful hook': '또 다른 유용한 훅',
    'The Claude Code SDK': 'Claude Code SDK',
    'Wrapping up': '마무리',
    'Quiz on Claude Code': 'Claude Code 퀴즈',
    'Summary and next steps': '요약 및 다음 단계',
    'Open in Claude': 'Claude에서 열기',
    'Ask questions about this course': '이 강좌에 대해 질문하기',
    'Copy notes': '노트 복사',
    'Copy full course notes for LLMs': 'LLM용 전체 강좌 노트 복사',
    'Previous': '이전',
    'Next': '다음',
    'Header Navigation': '헤더 내비게이션',
}

# File-specific translations
FILE_TRANSLATIONS = {
    'MCP servers with Claude Code (2026. 3. 9. 오후 9：37：53).html': {
        'MCP servers with Claude Code': 'Claude Code와 MCP 서버',
        "You can extend Claude Code's capabilities by adding MCP (Model Context Protocol) servers. These servers run either remotely or locally on your machine and provide Claude with new tools and abilities it wouldn't normally have.":
            "MCP(Model Context Protocol) 서버를 추가하여 Claude Code의 기능을 확장할 수 있습니다. 이 서버들은 원격 또는 로컬 머신에서 실행되며, Claude에게 기본적으로는 없는 새로운 도구와 기능을 제공합니다.",
        'One of the most popular MCP servers is Playwright, which gives Claude the ability to control a web browser. This opens up powerful possibilities for web development workflows.':
            '가장 인기 있는 MCP 서버 중 하나는 Playwright로, Claude에게 웹 브라우저를 제어하는 능력을 부여합니다. 이를 통해 웹 개발 워크플로우에서 강력한 가능성이 열립니다.',
        'Installing the Playwright MCP Server': 'Playwright MCP 서버 설치',
        'To add the Playwright server to Claude Code, run this command in your terminal (not inside Claude Code):':
            'Playwright 서버를 Claude Code에 추가하려면, 터미널에서 다음 명령을 실행하세요(Claude Code 내부가 아닌 외부 터미널에서):',
        'This command does two things:': '이 명령은 두 가지 작업을 수행합니다:',
        'Names the MCP server "playwright"': 'MCP 서버 이름을 "playwright"로 지정합니다',
        'Provides the command that starts the server locally on your machine': '로컬 머신에서 서버를 시작하는 명령을 제공합니다',
        'Managing Permissions': '권한 관리',
        'When you first use MCP server tools, Claude will ask for permission each time. If you get tired of these permission prompts, you can pre-approve the server by editing your settings.':
            'MCP 서버 도구를 처음 사용할 때, Claude는 매번 권한을 요청합니다. 이러한 권한 프롬프트가 번거로우시면, 설정을 편집하여 서버를 미리 승인할 수 있습니다.',
        'Open the': '다음 파일을 열고',
        'file and add the server to the allow array:': '파일에서 allow 배열에 서버를 추가하세요:',
        'Note the double underscores in': '다음에서 이중 밑줄에 주의하세요:',
        '. This allows Claude to use the Playwright tools without asking for permission every time.':
            '. 이렇게 하면 Claude가 매번 권한을 요청하지 않고 Playwright 도구를 사용할 수 있습니다.',
        'Practical Example: Improving Component Generation': '실용적인 예시: 컴포넌트 생성 개선',
        "Here's a real-world example of how the Playwright MCP server can improve your development workflow. Instead of manually testing and tweaking prompts, you can have Claude:":
            'Playwright MCP 서버가 개발 워크플로우를 개선하는 실제 예시입니다. 프롬프트를 수동으로 테스트하고 조정하는 대신, Claude에게 다음을 수행하도록 할 수 있습니다:',
        'Open a browser and navigate to your application': '브라우저를 열고 애플리케이션으로 이동',
        'Generate a test component': '테스트 컴포넌트 생성',
        'Analyze the visual styling and code quality': '시각적 스타일링과 코드 품질 분석',
        'Update the generation prompt based on what it observes': '관찰한 내용을 바탕으로 생성 프롬프트 업데이트',
        'Test the improved prompt with a new component': '새 컴포넌트로 개선된 프롬프트 테스트',
        'For instance, you might ask Claude to:': '예를 들어, Claude에게 다음을 요청할 수 있습니다:',
        '"Navigate to localhost:3000, generate a basic component, review the styling, and update the generation prompt at @src/lib/prompts/generation.tsx to produce better components going forward."':
            '"localhost:3000으로 이동하여 기본 컴포넌트를 생성하고, 스타일링을 검토한 다음, @src/lib/prompts/generation.tsx의 생성 프롬프트를 업데이트하여 앞으로 더 나은 컴포넌트를 생성하도록 하세요."',
        'Claude will use the browser tools to interact with your app, examine the generated output, and then modify your prompt file to encourage more original and creative designs.':
            'Claude는 브라우저 도구를 사용하여 앱과 상호작용하고, 생성된 출력을 검토한 다음, 더 독창적이고 창의적인 디자인을 장려하도록 프롬프트 파일을 수정합니다.',
        'Results and Benefits': '결과와 이점',
        'In practice, this approach can lead to significantly better results. Instead of generic purple-to-blue gradients and standard Tailwind patterns, Claude might update prompts to encourage:':
            '실제로 이 접근 방식은 훨씬 더 나은 결과를 가져올 수 있습니다. 일반적인 보라색-파란색 그라디언트와 표준 Tailwind 패턴 대신, Claude는 다음을 장려하도록 프롬프트를 업데이트할 수 있습니다:',
        'Warm sunset gradients (orange-to-pink-to-purple)': '따뜻한 일몰 그라디언트 (주황색-분홍색-보라색)',
        'Ocean depth themes (teal-to-emerald-to-cyan)': '바다 깊이 테마 (청록색-에메랄드-시안)',
        'Asymmetric designs and overlapping elements': '비대칭 디자인과 겹치는 요소',
        'Creative spacing and unconventional layouts': '창의적인 간격과 색다른 레이아웃',
        'The key advantage is that Claude can see the actual visual output, not just the code, which allows it to make much more informed decisions about styling improvements.':
            '핵심 장점은 Claude가 코드만이 아닌 실제 시각적 출력을 볼 수 있어, 스타일링 개선에 대해 훨씬 더 정보에 기반한 결정을 내릴 수 있다는 것입니다.',
        'Exploring Other MCP Servers': '다른 MCP 서버 탐색',
        "Playwright is just one example of what's possible with MCP servers. The ecosystem includes servers for:":
            'Playwright는 MCP 서버로 가능한 것의 한 예에 불과합니다. 에코시스템에는 다음을 위한 서버가 포함되어 있습니다:',
        'Database interactions': '데이터베이스 상호작용',
        'API testing and monitoring': 'API 테스트 및 모니터링',
        'File system operations': '파일 시스템 작업',
        'Cloud service integrations': '클라우드 서비스 통합',
        'Development tool automation': '개발 도구 자동화',
        'Consider exploring MCP servers that align with your specific development needs. They can transform Claude from a code assistant into a comprehensive development partner that can interact with your entire toolchain.':
            '특정 개발 요구 사항에 맞는 MCP 서버를 탐색해 보세요. MCP 서버는 Claude를 단순한 코드 어시스턴트에서 전체 도구 체인과 상호작용할 수 있는 종합적인 개발 파트너로 변환시킬 수 있습니다.',
        '- Custom commands': '- 커스텀 명령어',
    },
    'Github integration (2026. 3. 9. 오후 9：38：09).html': {
        'Github integration': 'Github 통합',
        'Claude Code offers an official GitHub integration that lets Claude run inside GitHub Actions. This integration provides two main workflows: mention support for issues and pull requests, and automatic pull request reviews.':
            'Claude Code는 GitHub Actions 내에서 Claude를 실행할 수 있는 공식 GitHub 통합을 제공합니다. 이 통합은 두 가지 주요 워크플로우를 제공합니다: 이슈 및 풀 리퀘스트에 대한 멘션 지원, 그리고 자동 풀 리퀘스트 리뷰.',
        'Setting Up the Integration': '통합 설정',
        'To get started, run': '시작하려면',
        'in Claude. This command walks you through the setup process:': '를 Claude에서 실행하세요. 이 명령은 설정 과정을 안내합니다:',
        'Install the Claude Code app on GitHub': 'GitHub에 Claude Code 앱 설치',
        'Add your API key': 'API 키 추가',
        'Automatically generate a pull request with the workflow files': '워크플로우 파일이 포함된 풀 리퀘스트 자동 생성',
        "The generated pull request adds two GitHub Actions to your repository. Once merged, you'll have the workflow files in your":
            '생성된 풀 리퀘스트는 리포지토리에 두 개의 GitHub Actions를 추가합니다. 병합되면',
        'directory.': '디렉토리에 워크플로우 파일이 생성됩니다.',
        'Default GitHub Actions': '기본 GitHub Actions',
        'The integration provides two main workflows:': '통합은 두 가지 주요 워크플로우를 제공합니다:',
        'Mention Action': '멘션 액션',
        'You can mention Claude in any issue or pull request using': '다음을 사용하여 모든 이슈 또는 풀 리퀘스트에서 Claude를 멘션할 수 있습니다:',
        '. When mentioned, Claude will:': '. 멘션되면, Claude는 다음을 수행합니다:',
        'Analyze the request and create a task plan': '요청을 분석하고 작업 계획 생성',
        'Execute the task with full access to your codebase': '코드베이스에 완전히 접근하여 작업 실행',
        'Respond with results directly in the issue or PR': '이슈 또는 PR에 직접 결과 응답',
        'Pull Request Action': '풀 리퀘스트 액션',
        'Whenever you create a pull request, Claude automatically:': '풀 리퀘스트를 생성할 때마다, Claude는 자동으로:',
        'Reviews the proposed changes': '제안된 변경 사항 검토',
        'Analyzes the impact of modifications': '수정 사항의 영향 분석',
        'Posts a detailed report on the pull request': '풀 리퀘스트에 상세 보고서 게시',
        'Customizing the Workflows': '워크플로우 커스터마이징',
        "After merging the initial pull request, you can customize the workflow files to fit your project's needs. Here's how to enhance the mention workflow:":
            '초기 풀 리퀘스트를 병합한 후, 프로젝트 요구 사항에 맞게 워크플로우 파일을 커스터마이징할 수 있습니다. 멘션 워크플로우를 개선하는 방법은 다음과 같습니다:',
        'Adding Project Setup': '프로젝트 설정 추가',
        'Before Claude runs, you can add steps to prepare your environment:': 'Claude가 실행되기 전에 환경을 준비하는 단계를 추가할 수 있습니다:',
        'Custom Instructions': '커스텀 지시사항',
        'Provide Claude with context about your project setup:': '프로젝트 설정에 대한 컨텍스트를 Claude에게 제공하세요:',
        'MCP Server Configuration': 'MCP 서버 구성',
        'You can configure MCP servers to give Claude additional capabilities:': 'Claude에게 추가 기능을 제공하도록 MCP 서버를 구성할 수 있습니다:',
        'Tool Permissions': '도구 권한',
        'When running Claude in GitHub Actions, you must explicitly list all allowed tools. This is especially important when using MCP servers.':
            'GitHub Actions에서 Claude를 실행할 때, 허용된 모든 도구를 명시적으로 나열해야 합니다. 이는 MCP 서버를 사용할 때 특히 중요합니다.',
        "Unlike local development, there's no shortcut for permissions in GitHub Actions. Each tool from each MCP server must be individually listed.":
            '로컬 개발과 달리, GitHub Actions에서는 권한에 대한 단축키가 없습니다. 각 MCP 서버의 각 도구를 개별적으로 나열해야 합니다.',
        'Best Practices': '모범 사례',
        "When setting up Claude's GitHub integration:": 'Claude의 GitHub 통합을 설정할 때:',
        'Start with the default workflows and customize gradually': '기본 워크플로우로 시작하여 점진적으로 커스터마이징',
        'Use custom instructions to provide project-specific context': '커스텀 지시사항을 사용하여 프로젝트별 컨텍스트 제공',
        'Be explicit about tool permissions when using MCP servers': 'MCP 서버 사용 시 도구 권한을 명시적으로 지정',
        'Test your workflows with simple tasks before complex ones': '복잡한 작업 전에 간단한 작업으로 워크플로우 테스트',
        "Consider your project's specific needs when configuring additional steps": '추가 단계를 구성할 때 프로젝트의 특정 요구 사항 고려',
        'The GitHub integration transforms Claude from a development assistant into an automated team member that can handle tasks, review code, and provide insights directly within your GitHub workflow.':
            'GitHub 통합은 Claude를 개발 어시스턴트에서 GitHub 워크플로우 내에서 직접 작업을 처리하고, 코드를 검토하며, 인사이트를 제공할 수 있는 자동화된 팀원으로 변환합니다.',
        '- MCP servers with Claude Code': '- Claude Code와 MCP 서버',
    },
    'Introducing hooks (2026. 3. 9. 오후 9：38：26).html': {
        'Introducing hooks': '훅 소개',
        "Hooks allow you to run commands before or after Claude attempts to run a tool. They're incredibly useful for implementing automated workflows like running code formatters after file edits, executing tests when files change, or blocking access to specific files.":
            '훅을 사용하면 Claude가 도구를 실행하기 전이나 후에 명령을 실행할 수 있습니다. 파일 편집 후 코드 포맷터 실행, 파일 변경 시 테스트 실행, 특정 파일에 대한 접근 차단 등 자동화된 워크플로우를 구현하는 데 매우 유용합니다.',
        'How Hooks Work': '훅의 작동 방식',
        "To understand hooks, let's first review the normal flow when you interact with Claude Code. When you ask Claude something, your query gets sent to the Claude model along with tool definitions. Claude might decide to use a tool by providing a formatted response, and then Claude Code executes that tool and returns the result.":
            '훅을 이해하려면, 먼저 Claude Code와 상호작용할 때의 일반적인 흐름을 살펴보겠습니다. Claude에게 무언가를 요청하면, 쿼리가 도구 정의와 함께 Claude 모델로 전송됩니다. Claude는 형식화된 응답을 제공하여 도구 사용을 결정할 수 있고, 그런 다음 Claude Code가 해당 도구를 실행하고 결과를 반환합니다.',
        'Hooks insert themselves into this process, allowing you to execute code just before or just after the tool execution happens.':
            '훅은 이 과정에 개입하여, 도구 실행 직전 또는 직후에 코드를 실행할 수 있게 해줍니다.',
        'There are two types of hooks:': '훅에는 두 가지 유형이 있습니다:',
        'PreToolUse hooks': 'PreToolUse 훅',
        '- Run before a tool is called': '- 도구가 호출되기 전에 실행',
        'PostToolUse hooks': 'PostToolUse 훅',
        '- Run after a tool is called': '- 도구가 호출된 후에 실행',
        'Hook Configuration': '훅 구성',
        'Hooks are defined in Claude settings files. You can add them to:': '훅은 Claude 설정 파일에 정의됩니다. 다음에 추가할 수 있습니다:',
        'Global': '전역',
        '-': '-',
        '(affects all projects)': '(모든 프로젝트에 영향)',
        'Project': '프로젝트',
        '(shared with team)': '(팀과 공유)',
        'Project (not committed)': '프로젝트 (커밋되지 않음)',
        '(personal settings)': '(개인 설정)',
        'You can write hooks by hand in these files or use the': '이 파일에 직접 훅을 작성하거나',
        'command inside Claude Code.': '명령을 Claude Code 내에서 사용할 수 있습니다.',
        'The configuration structure includes two main sections:': '구성 구조는 두 가지 주요 섹션을 포함합니다:',
        'PreToolUse Hooks': 'PreToolUse 훅',
        'PreToolUse hooks run before a tool is executed. They include a matcher that specifies which tool types to target:':
            'PreToolUse 훅은 도구가 실행되기 전에 실행됩니다. 어떤 도구 유형을 대상으로 할지 지정하는 매처(matcher)를 포함합니다:',
        "Before the 'Read' tool is executed, this configuration runs the specified command. Your command receives details about the tool call Claude wants to make, and you can:":
            "'Read' 도구가 실행되기 전에, 이 구성은 지정된 명령을 실행합니다. 명령은 Claude가 실행하려는 도구 호출에 대한 세부 정보를 수신하며, 다음을 수행할 수 있습니다:",
        'Allow the operation to proceed normally': '작업이 정상적으로 진행되도록 허용',
        'Block the tool call and send an error message back to Claude': '도구 호출을 차단하고 Claude에게 오류 메시지 반환',
        'PostToolUse Hooks': 'PostToolUse 훅',
        "PostToolUse hooks run after a tool has been executed. Here's an example that triggers after write, edit, or multi-edit operations:":
            'PostToolUse 훅은 도구가 실행된 후에 실행됩니다. 다음은 쓰기, 편집, 또는 다중 편집 작업 후에 트리거되는 예시입니다:',
        "Since the tool call has already occurred, PostToolUse hooks can't block the operation. However, they can:":
            '도구 호출이 이미 발생했으므로, PostToolUse 훅은 작업을 차단할 수 없습니다. 하지만 다음을 수행할 수 있습니다:',
        'Run follow-up operations (like formatting a file that was just edited)': '후속 작업 실행 (방금 편집된 파일 포맷팅 등)',
        'Provide additional feedback to Claude about the tool use': '도구 사용에 대한 추가 피드백을 Claude에게 제공',
        'Practical Applications': '실용적인 활용',
        'Here are some common ways to use hooks:': '훅을 사용하는 일반적인 방법들입니다:',
        'Code formatting': '코드 포맷팅',
        '- Automatically format files after Claude edits them': '- Claude가 파일을 편집한 후 자동으로 포맷팅',
        'Testing': '테스트',
        '- Run tests automatically when files are changed': '- 파일이 변경될 때 자동으로 테스트 실행',
        'Access control': '접근 제어',
        '- Block Claude from reading or editing specific files': '- 특정 파일에 대한 Claude의 읽기 또는 편집 차단',
        'Code quality': '코드 품질',
        '- Run linters or type checkers and provide feedback to Claude': '- 린터 또는 타입 검사기를 실행하고 Claude에게 피드백 제공',
        'Logging': '로깅',
        '- Track what files Claude accesses or modifies': '- Claude가 접근하거나 수정하는 파일 추적',
        'Validation': '유효성 검사',
        '- Check naming conventions or coding standards': '- 명명 규칙 또는 코딩 표준 확인',
        "The key insight is that hooks let you extend Claude Code's capabilities by integrating your own tools and processes into the workflow. PreToolUse hooks give you control over what Claude can do, while PostToolUse hooks let you enhance what Claude has done.":
            '핵심 인사이트는 훅을 통해 자신의 도구와 프로세스를 워크플로우에 통합하여 Claude Code의 기능을 확장할 수 있다는 것입니다. PreToolUse 훅은 Claude가 할 수 있는 것을 제어하고, PostToolUse 훅은 Claude가 한 것을 향상시킬 수 있게 해줍니다.',
        '- Github integration': '- Github 통합',
    },
    'Defining hooks (2026. 3. 9. 오후 9：38：48).html': {
        'Defining hooks': '훅 정의하기',
        'Hooks in Claude Code allow you to intercept and control tool calls before or after they execute. This gives you fine-grained control over what Claude can and cannot do in your development environment.':
            'Claude Code의 훅을 사용하면 도구 호출이 실행되기 전이나 후에 가로채어 제어할 수 있습니다. 이를 통해 개발 환경에서 Claude가 할 수 있는 것과 할 수 없는 것을 세밀하게 제어할 수 있습니다.',
        'Building a Hook': '훅 만들기',
        'Creating a hook involves four main steps:': '훅을 만드는 데는 네 가지 주요 단계가 있습니다:',
        'Decide on a PreToolUse or PostToolUse hook': 'PreToolUse 또는 PostToolUse 훅 결정',
        '- PreToolUse hooks can prevent tool calls from executing, while PostToolUse hooks run after the tool has already been used':
            '- PreToolUse 훅은 도구 호출 실행을 방지할 수 있고, PostToolUse 훅은 도구가 이미 사용된 후에 실행됩니다',
        'Determine which type of tool calls you want to watch for': '감시하려는 도구 호출 유형 결정',
        '- You need to specify exactly which tools should trigger your hook': '- 어떤 도구가 훅을 트리거해야 하는지 정확히 지정해야 합니다',
        'Write a command that will receive the tool call': '도구 호출을 수신할 명령 작성',
        '- This command gets JSON data about the proposed tool call via standard input': '- 이 명령은 표준 입력을 통해 제안된 도구 호출에 대한 JSON 데이터를 받습니다',
        'If needed, command should provide feedback to Claude': '필요한 경우, 명령은 Claude에게 피드백을 제공해야 합니다',
        "- Your command's exit code tells Claude whether to allow or block the operation":
            '- 명령의 종료 코드는 Claude에게 작업을 허용하거나 차단할지를 알려줍니다',
        'Available Tools': '사용 가능한 도구',
        'Claude Code provides several built-in tools that you can monitor with hooks:': 'Claude Code는 훅으로 모니터링할 수 있는 여러 내장 도구를 제공합니다:',
        'To see exactly which tools are available in your current setup, you can ask Claude directly for a list. This is especially useful since the available tools can change when you add custom MCP servers.':
            '현재 설정에서 어떤 도구를 사용할 수 있는지 확인하려면 Claude에게 직접 목록을 요청할 수 있습니다. 커스텀 MCP 서버를 추가할 때 사용 가능한 도구가 변경될 수 있으므로 이는 특히 유용합니다.',
        'Tool Call Data Structure': '도구 호출 데이터 구조',
        'When your hook command executes, Claude sends JSON data through standard input containing details about the proposed tool call:':
            '훅 명령이 실행될 때, Claude는 제안된 도구 호출에 대한 세부 정보가 담긴 JSON 데이터를 표준 입력을 통해 전송합니다:',
        'Your command reads this JSON from standard input, parses it, and then decides whether to allow or block the operation based on the tool name and input parameters.':
            '명령은 표준 입력에서 이 JSON을 읽고, 파싱한 다음, 도구 이름과 입력 매개변수를 기반으로 작업을 허용하거나 차단할지 결정합니다.',
        'Exit Codes and Control Flow': '종료 코드와 제어 흐름',
        'Your hook command communicates back to Claude through exit codes:': '훅 명령은 종료 코드를 통해 Claude와 통신합니다:',
        'Exit Code 0': '종료 코드 0',
        '- Everything is fine, allow the tool call to proceed': '- 모든 것이 정상, 도구 호출 진행 허용',
        'Exit Code 2': '종료 코드 2',
        '- Block the tool call (PreToolUse hooks only)': '- 도구 호출 차단 (PreToolUse 훅 전용)',
        'When you exit with code 2 in a PreToolUse hook, any error messages you write to standard error will be sent to Claude as feedback, explaining why the operation was blocked.':
            'PreToolUse 훅에서 코드 2로 종료하면, 표준 오류에 작성한 오류 메시지가 Claude에게 피드백으로 전송되어 왜 작업이 차단되었는지 설명합니다.',
        'Example Use Case': '사용 사례 예시',
        'A common use case is preventing Claude from reading sensitive files like': '일반적인 사용 사례는 Claude가 다음과 같은 민감한 파일을 읽지 못하도록 방지하는 것입니다:',
        'files. Since both the': '파일. 두 가지 모두',
        'and': '와',
        "tools can access file contents, you'd want to monitor both tool types and check if they're trying to access restricted file paths.":
            '도구가 파일 내용에 접근할 수 있으므로, 두 도구 유형 모두 모니터링하여 제한된 파일 경로에 접근하려는지 확인해야 합니다.',
        "This approach gives you complete control over Claude's file system access while providing clear feedback about why certain operations are restricted.":
            '이 접근 방식은 특정 작업이 제한된 이유에 대한 명확한 피드백을 제공하면서 Claude의 파일 시스템 접근을 완전히 제어할 수 있게 해줍니다.',
        'Downloads': '다운로드',
        '- Introducing hooks': '- 훅 소개',
    },
}

def translate_html_file(filepath, specific_translations):
    """Apply translations to an HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Combine nav + file-specific translations
    all_translations = {**NAV_TRANSLATIONS, **specific_translations}

    # Sort by length (longest first) to avoid partial replacements
    sorted_items = sorted(all_translations.items(), key=lambda x: len(x[0]), reverse=True)

    for english, korean in sorted_items:
        if english in content:
            content = content.replace(english, korean)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    changed = content != original_content
    return changed

# Process all files
files_to_translate = [
    ('C:/Git/ClaudeCourse/MCP servers with Claude Code (2026. 3. 9. 오후 9：37：53).html',
     FILE_TRANSLATIONS['MCP servers with Claude Code (2026. 3. 9. 오후 9：37：53).html']),
    ('C:/Git/ClaudeCourse/Github integration (2026. 3. 9. 오후 9：38：09).html',
     FILE_TRANSLATIONS['Github integration (2026. 3. 9. 오후 9：38：09).html']),
    ('C:/Git/ClaudeCourse/Introducing hooks (2026. 3. 9. 오후 9：38：26).html',
     FILE_TRANSLATIONS['Introducing hooks (2026. 3. 9. 오후 9：38：26).html']),
    ('C:/Git/ClaudeCourse/Defining hooks (2026. 3. 9. 오후 9：38：48).html',
     FILE_TRANSLATIONS['Defining hooks (2026. 3. 9. 오후 9：38：48).html']),
]

for filepath, translations in files_to_translate:
    changed = translate_html_file(filepath, translations)
    print(f"{'CHANGED' if changed else 'NO CHANGE'}: {os.path.basename(filepath)}")

print("\nTranslation complete.")
