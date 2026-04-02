import sys

with open('D:/Git/rockghost.github.io/src/The Description-Discernment loop.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Attribute replacements
attr_replacements = [
    ('aria-label="Lessons"', 'aria-label="레슨 목록"'),
    ('alt="Go home"', 'alt="홈으로 이동"'),
    ('aria-label="Open menu"', 'aria-label="메뉴 열기"'),
    ('aria-label="User settings menu"', 'aria-label="사용자 설정 메뉴"'),
    ('aria-label="Previous - A closer look at Discernment"', 'aria-label="이전 - 식별력 자세히 살펴보기"'),
    ('title="A closer look at Discernment"', 'title="식별력 자세히 살펴보기"'),
    ('aria-label="Toggle fullscreen"', 'aria-label="전체 화면 전환"'),
    ('title="A closer look at Diligence"', 'title="성실성 자세히 살펴보기"'),
]

text_replacements = [
    # Title tag
    ('<title>\n  The Description-Discernment loop\n </title>', '<title>\n  묘사-식별 루프\n </title>'),
    # Header nav hidden h2
    ('Header Navigation', '헤더 내비게이션'),
    # Header links
    ('>Courses<', '>강좌<'),
    # Profile dropdown
    ('<span>My Profile</span>', '<span>내 프로필</span>'),
    ('<span>Sign Out</span>', '<span>로그아웃</span>'),
    # Estimated time
    ('<em>Estimated Time: 30 - 60 minutes</em>', '<em>예상 소요 시간: 30~60분</em>'),
    # Lesson intro
    ("By the end of this lesson, you'll be able to:", '이 레슨을 마치면 다음을 할 수 있게 됩니다:'),
    ('Apply Description and Discernment skills to a real project', '실제 프로젝트에 묘사(Description)와 식별(Discernment) 역량 적용하기'),
    ('Engage in productive Description-Discernment feedback loops', '생산적인 묘사-식별 피드백 루프 실행하기'),
    ('Create results through human-AI collaboration that exceed what either could achieve alone', '인간과 AI의 협업을 통해 각자가 단독으로 이룰 수 있는 것 이상의 결과 만들어내기'),
    # Headings
    ('>Exercises<', '>실습<'),
    ('Exercise: Project execution with description-discernment loops', '실습: 묘사-식별 루프를 활용한 프로젝트 실행'),
    ("Now it's time to put everything you've learned into practice by working on the project you planned in Lesson 5, using the Description and Discernment skills you've been developing.",
     '이제 레슨 5에서 계획한 프로젝트를 직접 실행하며, 그동안 개발해 온 묘사(Description)와 식별(Discernment) 역량을 실제로 활용해 볼 시간입니다.'),
    ('Step 1: Review your project plan', '1단계: 프로젝트 계획 검토하기'),
    ('Pull up the project plan you created in Lesson 5', '레슨 5에서 작성한 프로젝트 계획을 꺼내 보세요'),
    ('Quickly review your delegation decisions about which tasks would benefit from human expertise, AI capabilities, or collaboration',
     '인간의 전문성, AI 역량, 또는 협업이 각각 어떤 작업에 적합한지에 대한 위임 결정을 빠르게 검토하세요'),
    ("Feel free to refine your plan based on what you've learned since then", '그 이후로 배운 내용을 바탕으로 계획을 자유롭게 다듬어 보세요'),
    ('Step 2: Prepare your description approach', '2단계: 묘사 방식 준비하기'),
    ("Start a conversation with Claude and explain the project you'll be working on together. Before diving into execution, plan how you'll approach Description:",
     'Claude와 대화를 시작하고 함께 진행할 프로젝트를 설명하세요. 본격적인 실행에 앞서, 묘사(Description)를 어떻게 접근할지 계획해 보세요:'),
    ('<strong>Product Description</strong>', '<strong>결과물 묘사(Product Description)</strong>'),
    (': What specific outputs do you need from Claude for each task? What format, style, length, and level of detail are you looking for?',
     ': 각 작업에서 Claude에게 필요한 구체적인 결과물은 무엇인가요? 어떤 형식, 스타일, 분량, 세부 수준을 원하시나요?'),
    ('<strong>Process Description</strong>', '<strong>과정 묘사(Process Description)</strong>'),
    (': How should Claude approach each task? Are there specific methods, frameworks, or steps you want it to follow?',
     ': Claude가 각 작업에 어떻게 접근해야 하나요? 따르길 원하는 특정 방법, 프레임워크, 또는 단계가 있나요?'),
    ('<strong>Performance Description</strong>', '<strong>수행 방식 묘사(Performance Description)</strong>'),
    (': What kind of collaborative behavior do you want from Claude during this project? Should it be concise or detailed, challenging or supportive, focused on ideas or analysis?',
     ': 이 프로젝트에서 Claude에게 어떤 협업 방식을 원하시나요? 간결하게 또는 상세하게, 도전적으로 또는 지지적으로, 아이디어 중심 또는 분석 중심으로 진행하길 원하시나요?'),
    ('Discuss these questions with Claude to establish clear expectations for your collaboration.',
     '이 질문들을 Claude와 함께 논의하여 협업에 대한 명확한 기대치를 설정하세요.'),
    ('Step 3: Execute your project using description-discernment loops', '3단계: 묘사-식별 루프를 활용해 프로젝트 실행하기'),
    ('Now, work through your planned project tasks with Claude. For each task:', '이제 Claude와 함께 계획된 프로젝트 작업을 진행하세요. 각 작업에 대해:'),
    ('<strong>Describe</strong>', '<strong>묘사하기(Describe)</strong>'),
    ("what you need clearly, using the Description skills you've learned:", '배운 묘사 역량을 활용하여 필요한 것을 명확하게 전달하세요:'),
    ('Be specific about what you want (Product)', '원하는 것을 구체적으로 명시하세요 (결과물)'),
    ('Guide how Claude should approach or think about the task (Process)', 'Claude가 작업에 접근하거나 생각하는 방식을 안내하세요 (과정)'),
    ('Specify how you want Claude to engage with you during the process (Performance)', '과정 중 Claude가 어떻게 소통하길 원하는지 명시하세요 (수행 방식)'),
    ('<strong>Discern</strong>', '<strong>식별하기(Discern)</strong>'),
    ('the quality of what you receive:', '받은 결과물의 품질을 평가하세요:'),
    ('Evaluate the output itself (Product Discernment)', '결과물 자체를 평가하세요 (결과물 식별)'),
    ('Assess how Claude approached the task (Process Discernment)', 'Claude가 작업에 접근한 방식을 평가하세요 (과정 식별)'),
    ("Consider if Claude's behavior is most helpful for what you need (Performance Discernment)",
     'Claude의 수행 방식이 필요에 가장 적합한지 고려하세요 (수행 방식 식별)'),
    ('<strong>Refine</strong>', '<strong>다듬기(Refine)</strong>'),
    ('based on your discernment:', '식별 결과를 바탕으로:'),
    ("Provide feedback on what worked and what didn't", '잘 된 점과 그렇지 않은 점에 대한 피드백을 제공하세요'),
    ('Clarify or adjust your description as needed', '필요에 따라 묘사를 명확히 하거나 조정하세요'),
    ("Request iterations until you're satisfied with the result", '결과에 만족할 때까지 반복을 요청하세요'),
    ('<strong>Integrate</strong>', '<strong>통합하기(Integrate)</strong>'),
    ('your own expertise and judgment:', '자신의 전문성과 판단력을 발휘하세요:'),
    ('Add your unique perspective, creativity, or domain knowledge', '자신만의 시각, 창의성, 또는 도메인 지식을 더하세요'),
    ('Make the final decisions about what to keep, modify, or discard', '무엇을 유지하고, 수정하고, 버릴지 최종 결정을 내리세요'),
    ('Take responsibility for the final output', '최종 결과물에 대한 책임을 지세요'),
    ('Continue this Description-Discernment loop for each task in your project until completion.',
     '프로젝트가 완료될 때까지 각 작업에 이 묘사-식별 루프를 계속 적용하세요.'),
    ('>Reflection<', '>성찰<'),
    ('Before moving on, take a moment to consider:', '다음 단계로 넘어가기 전에 잠시 다음을 생각해 보세요:'),
    ('What patterns did you notice in the types of descriptions that led to the best outcomes?',
     '최선의 결과로 이어진 묘사 유형에서 어떤 패턴을 발견했나요?'),
    ('Which required more effort from you: Description or Discernment? Why do you think that was the case?',
     '묘사(Description)와 식별(Discernment) 중 어느 쪽에 더 많은 노력이 필요했나요? 왜 그랬다고 생각하시나요?'),
    ('How did your actual project execution compare to your initial plan from Lesson 5? What adjustments did you make along the way?',
     '레슨 5의 초기 계획과 실제 프로젝트 실행은 어떻게 달랐나요? 진행 중에 어떤 조정을 했나요?'),
    ("What's next", '다음 단계'),
    ("In the next lesson, we'll explore the final competency in the AI Fluency Framework: Diligence. While Delegation, Description, and Discernment focus primarily on effectiveness and efficiency, Diligence addresses the ethical and safety aspects of working with AI. You'll learn how to ensure your AI collaborations are responsible, transparent, and accountable.",
     'AI 유창성 프레임워크(AI Fluency Framework)의 마지막 역량인 성실성(Diligence)을 다음 레슨에서 살펴봅니다. 위임(Delegation), 묘사(Description), 식별(Discernment)이 주로 효과성과 효율성에 초점을 맞춘다면, 성실성(Diligence)은 AI와 함께하는 작업의 윤리적·안전한 측면을 다룹니다. AI 협업이 책임감 있고, 투명하며, 설명 가능한 방식으로 이루어지도록 하는 방법을 배우게 됩니다.'),
    ('Feedback on this course', '강좌 피드백'),
    ("As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your life, work, or classes and any feedback you may have.",
     '강좌를 진행하면서, 일상·업무·수업에서 강좌 개념을 어떻게 활용하고 있는지, 그리고 어떤 피드백이든 자유롭게 공유해 주시면 감사하겠습니다.'),
    ('>Share your feedback here.<', '>여기에서 피드백을 공유하세요.<'),
    ('Acknowledgments and license', '감사의 말 및 라이선스'),
    ('Copyright 2025 Rick Dakan, Joseph Feller, and Anthropic. Released under the CC BY-NC-SA 4.0 license.',
     'Copyright 2025 Rick Dakan, Joseph Feller, and Anthropic. CC BY-NC-SA 4.0 라이선스 하에 배포됩니다.'),
    ('This course is based on The AI Fluency Framework by Dakan and Feller.',
     '본 강좌는 Dakan과 Feller의 AI Fluency Framework를 기반으로 합니다.'),
    ('Supported in part by the Higher Education Authority, Ireland, through the National Forum for the Enhancement of Teaching and Learning.',
     '아일랜드 고등교육청(Higher Education Authority)과 교수학습 향상을 위한 국가 포럼(National Forum for the Enhancement of Teaching and Learning)의 부분 지원을 받았습니다.'),
    # Footer
    ('<span>Previous</span>', '<span>이전</span>'),
    ('- A closer look at Discernment', '- 식별력 자세히 살펴보기'),
    ('<span class="lesson-title-footer sf-hidden">The Description-Discernment loop</span>',
     '<span class="lesson-title-footer sf-hidden">묘사-식별 루프</span>'),
    ('<span class="lesson-title-label">A closer look at Diligence</span>',
     '<span class="lesson-title-label">성실성 자세히 살펴보기</span>'),
    ('<span>Next</span>', '<span>다음</span>'),
]

not_found = []

for old, new in attr_replacements:
    if old in content:
        content = content.replace(old, new)
    else:
        not_found.append(old)

for old, new in text_replacements:
    if old in content:
        content = content.replace(old, new)
    else:
        not_found.append(old)

if not_found:
    print('NOT FOUND:')
    for s in not_found:
        print(f'  {repr(s[:80])}')

with open('D:/Git/rockghost.github.io/src/The Description-Discernment loop.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Translation complete.')
