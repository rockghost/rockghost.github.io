import re

with open('src/Try it out (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

translations = [
    # Page titles
    ('\n   Try it out\n  ', '\n   직접 해보기\n  '),
    ('\n   Visualizing 1024D Space\n  ', '\n   1024차원 공간 시각화\n  '),

    # Article header
    ('Embeddings &amp; Similarity Search', '임베딩 &amp; 유사도 검색'),
    ('Visualizing 1024D Space', '1024차원 공간 시각화'),
    ('How multidimensional "nearness" works', '다차원 "근접성"의 작동 원리'),

    # Section: The Problem with Strings
    ('The Problem with Strings', '문자열의 문제'),
    ('Search "car" and you\'ll find every document containing the word "car." You won\'t find "automobile." Or "vehicle." Or "my Civic needs new brakes."',
     '"car"를 검색하면 "car"라는 단어가 포함된 문서만 찾아줍니다. "automobile"이나 "vehicle", 또는 "my Civic needs new brakes" 같은 표현은 찾아주지 않습니다.'),
    ('For decades, that was search, returning results based on string similarity rather than meaning. Google continuously made incremental improvements with engineering: Synonym dictionaries mapped "car" to "automobile," Stemming rules connected "running" to "run," and click-pattern mining surfaced that people who search "NYC apartments" want the same results as "Manhattan rentals." The connections between non-matching strings had to be mapped more or less by hand.',
     '수십 년 동안 검색은 의미가 아닌 문자열 유사도를 기반으로 결과를 반환했습니다. Google은 공학적 접근으로 점진적인 개선을 거듭했습니다. 동의어 사전으로 "car"를 "automobile"에 매핑하고, 어간 추출 규칙으로 "running"을 "run"에 연결하며, 클릭 패턴 분석으로 "NYC apartments"를 검색한 사람과 "Manhattan rentals"를 검색한 사람이 같은 결과를 원한다는 사실을 파악했습니다. 서로 다른 문자열 간의 연결은 사실상 수작업으로 매핑해야 했습니다.'),
    ('<strong>Embeddings</strong> challenged all of this with the idea that <strong>meaning</strong> could be a <em>place</em> . By converting text into coordinates, similar concepts end up near each other. This mapping of semantic space isn\'t manual, but rather <strong>emergent</strong> from training data.',
     '<strong>임베딩</strong>은 <strong>의미</strong>가 <em>위치</em>가 될 수 있다는 발상으로 이 모든 것에 도전했습니다. 텍스트를 좌표로 변환하면 유사한 개념들이 서로 가까운 곳에 위치하게 됩니다. 이 의미 공간의 매핑은 수작업이 아닌 학습 데이터로부터 <strong>자연스럽게 나타납니다</strong>.'),

    # Section: Encoding
    ('\n              Encoding\n             ', '\n              인코딩\n             '),
    ("Let's start with a simplified example.", '간단한 예시부터 시작해 봅시다.'),
    ('Imagine you were to score every document in a corpus of knowledge on two dimensions: how much it relates to dinosaurs, and how much it relates to roller coasters. Documents about similar topics would end up near each other.',
     '지식 말뭉치에 있는 모든 문서를 두 가지 차원으로 점수화한다고 상상해 보세요. 공룡과 얼마나 관련 있는지, 그리고 롤러코스터와 얼마나 관련 있는지입니다. 비슷한 주제의 문서들은 서로 가까운 위치에 놓이게 됩니다.'),
    ("Let's start with just three sources. Place each of these where you think they belong.",
     '세 가지 출처만으로 시작해 봅시다. 각 항목을 적절하다고 생각하는 위치에 놓아 보세요.'),
    ('How much does this relate to\n                <strong>roller coasters</strong>\n                ? \u2192',
     '이것은 <strong>롤러코스터</strong>와\n                얼마나 관련 있나요? \u2192'),
    ('How much does this relate to\n                <strong>dinosaurs</strong>\n                ? \u2192',
     '이것은 <strong>공룡</strong>과\n                얼마나 관련 있나요? \u2192'),
    ('>not at all<', '>전혀 없음<'),
    ('click to place selected item', '클릭하여 선택한 항목 배치'),
    ('\n               <p class="plot-key-label">\n                Sources\n               </p>',
     '\n               <p class="plot-key-label">\n                출처\n               </p>'),
    ('<span class="key-name">A children\'s book about dinosaurs</span>',
     '<span class="key-name">공룡에 관한 어린이 책</span>'),
    ('<span class="key-status">click to select</span>',
     '<span class="key-status">클릭하여 선택</span>'),
    ('<span class="key-name">The Velocicoaster web page</span>',
     '<span class="key-name">Velocicoaster 웹 페이지</span>'),
    ('<span class="key-name">An entire encyclopedia</span>',
     '<span class="key-name">백과사전 전체</span>'),
    ("You've just mapped meaning in 2D space, plotting our collection of items based on what they're about.",
     '방금 2차원 공간에서 의미를 매핑했습니다. 각 항목이 무엇에 관한 것인지를 기준으로 위치를 표시한 것입니다.'),

    # Section: Retrieval
    ('\n              Retrieval\n             ', '\n              검색\n             '),
    ("Now let's search this space.", '이제 이 공간을 검색해 봅시다.'),
    ('Plot a question on the same graph with the same axes. By mapping your question with the same logic you used to map sources, you can be sure that the nearest items will be the most relevant. Bonus feature: Use the slider to control how many get retrieved.',
     '같은 그래프의 같은 축에 질문을 표시해 보세요. 출처를 매핑할 때 사용한 것과 동일한 논리로 질문을 매핑하면, 가장 가까운 항목이 가장 관련성이 높다는 것을 확인할 수 있습니다. 추가 기능: 슬라이더를 사용하여 검색할 항목의 수를 조절하세요.'),
    ('Sources to retrieve (k):', '검색할 출처 수 (k):'),
    ('click to place the question', '클릭하여 질문 배치'),
    ('\n                 Question\n                ', '\n                 질문\n                '),
    ('\u2753 "What\'s the best dinosaur-themed roller coaster?"',
     '\u2753 "공룡을 테마로 한 롤러코스터 중 최고는 무엇인가요?"'),
    ('click graph to place', '그래프를 클릭하여 배치'),
    ("That's <strong>similarity search</strong> in a nutshell. We plot the question and find the nearest k items. Instead of keyword matching or synonym tables, we use multi-dimensional proximity.",
     '이것이 <strong>유사도 검색</strong>의 핵심입니다. 질문을 표시하고 가장 가까운 k개의 항목을 찾습니다. 키워드 매칭이나 동의어 테이블 대신 다차원 근접성을 사용합니다.'),
    ('Two axes is a start. But two dimensions can only capture two concepts. The real world has more than two topics, so we need more <strong>dimensions</strong> .',
     '두 개의 축은 시작에 불과합니다. 하지만 두 차원으로는 두 가지 개념만 포착할 수 있습니다. 실제 세계는 두 가지 주제보다 훨씬 많으므로 더 많은 <strong>차원</strong>이 필요합니다.'),

    # Section: More Dimensions
    ('More Dimensions', '더 많은 차원'),
    ('What if we added a third axis? Let\'s use <strong>biology</strong> .',
     '세 번째 축을 추가하면 어떨까요? <strong>생물학</strong>을 사용해 봅시다.'),
    ('The children\'s book scores high (species, habitats, diets). The encyclopedia covers some. The Velocicoaster page barely mentions it.',
     '어린이 책은 높은 점수를 받습니다(종, 서식지, 먹이). 백과사전은 일부를 다룹니다. Velocicoaster 페이지는 거의 언급하지 않습니다.'),
    ('Drag to rotate.', '드래그하여 회전하세요.'),
    ('Three dimensions, three coordinates per document. The Velocicoaster page is now <span class="coord">(0.50, 0.90, 0.05)</span> instead of <span class="coord">(0.50, 0.90)</span> .',
     '세 차원, 문서당 세 개의 좌표. Velocicoaster 페이지는 이제 <span class="coord">(0.50, 0.90)</span> 대신 <span class="coord">(0.50, 0.90, 0.05)</span>가 됩니다.'),
    ('Now try to picture a fourth axis.', '이제 네 번째 축을 상상해 보세요.'),
    ('Since I only exist in 3 dimensions, I personally can\'t \U0001f614 but that actually doesn\'t matter! Each new dimension just adds another coordinate to each point and another squared term to the distance formula. The spatial representation stops working at 4D, but the math keeps working.',
     '저는 3차원에만 존재하기 때문에 개인적으로는 상상할 수 없습니다 \U0001f614. 하지만 그건 사실 중요하지 않습니다! 새로운 차원이 추가될 때마다 각 점에 좌표 하나가 더해지고 거리 공식에 제곱 항 하나가 추가됩니다. 공간적 표현은 4D에서 작동하지 않게 되지만, 수학은 계속 작동합니다.'),
    ("We're going to have to push well past 4D, because real <strong>embedding models</strong> use around a thousand dimensions. Each document and each query becomes a point in that thousand-dimensional space. \"Find the nearest documents\" still means the same thing it meant on the 2D graph. It's just a longer distance calculation.",
     '실제 <strong>임베딩 모델</strong>은 약 천 개의 차원을 사용하기 때문에 4D를 훨씬 넘어서야 합니다. 각 문서와 각 쿼리는 그 천 차원 공간의 한 점이 됩니다. "가장 가까운 문서 찾기"는 2D 그래프에서의 의미와 동일합니다. 단지 거리 계산이 더 길어질 뿐입니다.'),

    # Section: Unlabeled Axes
    ('Unlabeled Axes', '이름 없는 축'),
    ('We chose the axes: dinosaurs, roller coasters, biology. But who determines which 1,024 topics make it into a real embedding model?',
     '우리는 축을 직접 선택했습니다: 공룡, 롤러코스터, 생물학. 하지만 실제 임베딩 모델에는 어떤 1,024개의 주제가 포함될지 누가 결정할까요?'),
    ('In point of fact, no one decides. The meaning of each axis is emergent (meaning it just shows up in training), and more of a black box. You can\'t look at dimension 847 and say "that\'s the dinosaur axis." The dimensions don\'t correspond to anything a human could name.',
     '실제로는 아무도 결정하지 않습니다. 각 축의 의미는 자연 발생적(학습 중에 자연스럽게 나타남)이며 일종의 블랙 박스입니다. 차원 847을 보고 "이게 공룡 축이다"라고 말할 수 없습니다. 차원들은 인간이 이름 붙일 수 있는 어떤 것과도 대응하지 않습니다.'),
    ("This makes the space harder to reason about. We can't interrogate dimension 847 to understand why two texts landed near each other, or why something we expected to be close ended up far away.",
     '이로 인해 공간에 대해 추론하기가 더 어려워집니다. 두 텍스트가 서로 가까운 이유나 가까울 것으로 예상했던 것이 멀리 떨어진 이유를 알아내기 위해 차원 847을 조사할 수 없습니다.'),

    # Section: Text as Coordinates
    ('Text as Coordinates', '좌표로서의 텍스트'),
    ('So who assigns the coordinates? An <strong>embedding model</strong> . Any string in, a fixed-length list of numbers out.',
     '그렇다면 좌표는 누가 할당할까요? <strong>임베딩 모델</strong>입니다. 어떤 문자열을 입력하든 고정 길이의 숫자 목록이 출력됩니다.'),
    ('<span class="step-label">Text</span>', '<span class="step-label">텍스트</span>'),
    ('<span class="step-label">Embedding</span>', '<span class="step-label">임베딩</span>'),
    ('The output is always the same length (1,024 values in our specific case, since we\'re using VoyageAI\'s embeddings model) and this is true whether the input is three words or three paragraphs. One chunk of text corresponds to one point in space. The embedding model reads the text and outputs a single <strong>vector</strong> .',
     '출력은 항상 동일한 길이입니다(저희의 경우 VoyageAI 임베딩 모델을 사용하기 때문에 1,024개의 값). 이는 입력이 세 단어이든 세 단락이든 동일합니다. 텍스트 한 청크는 공간의 한 점에 해당합니다. 임베딩 모델은 텍스트를 읽고 단일 <strong>벡터</strong>를 출력합니다.'),
    ('The math-eyed among you will recognize that "vector" and "coordinate set" aren\'t actually interchangeable, but for our purposes, it\'s appropriate to think of the vector as the address where this text lives relative to everything else.',
     '수학에 익숙한 분들은 "벡터"와 "좌표 집합"이 실제로 서로 교환 가능하지 않다는 것을 알고 있겠지만, 여기서는 벡터를 이 텍스트가 다른 모든 것을 기준으로 존재하는 주소로 이해하는 것이 적절합니다.'),

    # Section: Similarity
    ('\n              Similarity\n             ', '\n              유사도\n             '),
    ('"Nearest" on our 2D graph meant straight-line distance. In practice, similarity search uses <strong>cosine similarity</strong> instead. Cosine similarity is just another measure of how similar two pieces of text are, based on the direction their vectors point rather than how far apart they sit.',
     '2차원 그래프에서 "가장 가까운"은 직선 거리를 의미했습니다. 실제로 유사도 검색은 대신 <strong>코사인 유사도</strong>를 사용합니다. 코사인 유사도는 두 텍스트가 얼마나 유사한지를 측정하는 또 다른 방법으로, 두 점이 얼마나 떨어져 있는지가 아닌 벡터가 가리키는 방향을 기준으로 합니다.'),
    ('Try it yourself! Pick two sources to see their cosine similarity.',
     '직접 해보세요! 두 출처를 선택하여 코사인 유사도를 확인해 보세요.'),
    ('\n                 Source A\n                ', '\n                 출처 A\n                '),
    ('\n                 Source B\n                ', '\n                 출처 B\n                '),
    ('\u2753 Best dinosaur roller coaster?', '\u2753 최고의 공룡 롤러코스터는?'),
    ('\U0001f995 Children\'s dinosaur book', '\U0001f995 공룡 어린이 책'),
    ('<span class="result-label">Cosine similarity</span>',
     '<span class="result-label">코사인 유사도</span>'),
    ('<em>opposite</em>', '<em>반대</em>'),
    ('<em>unrelated</em>', '<em>무관</em>'),
    ('<em>identical</em>', '<em>동일</em>'),
    ('Try comparing the Velocicoaster page to the dinosaur book \u2014 their vectors point in very different directions. The encyclopedia lands somewhere in between everything, which fits, since it\'s a jack of all trades but a master of none.',
     'Velocicoaster 페이지와 공룡 책을 비교해 보세요. 두 벡터는 매우 다른 방향을 가리킵니다. 백과사전은 모든 것의 중간 어딘가에 위치하는데, 이는 모든 분야를 다루지만 어느 하나에 특화되지 않은 특성과 잘 맞습니다.'),

    # Header navigation
    ('>Courses<', '>강좌<'),
    ('<span>My Profile</span>', '<span>내 프로필</span>'),
    ('<span>Sign Out</span>', '<span>로그아웃</span>'),

    # Footer navigation
    ('aria-label="Previous - Knowledge"', 'aria-label="이전 - 지식"'),
    ('title="Knowledge"', 'title="지식"'),
    ('<span>Previous</span>', '<span>이전</span>'),
    ('<span class="lesson-title-label">- Knowledge</span>',
     '<span class="lesson-title-label">- 지식</span>'),
    ('<span class="lesson-title-footer sf-hidden">Try it out</span>',
     '<span class="lesson-title-footer sf-hidden">직접 해보기</span>'),
    ('<span class="lesson-title-label">Working Memory</span>',
     '<span class="lesson-title-label">작업 기억</span>'),
    ('title="Working Memory"', 'title="작업 기억"'),
    ('<span>Next</span>', '<span>다음</span>'),
    ('aria-label="Toggle fullscreen"', 'aria-label="전체 화면 전환"'),

    # h2 lesson title at top
    ('\n          Try it out\n         ', '\n          직접 해보기\n         '),

    # Header h2 (hidden)
    ('\n       Header Navigation\n      ', '\n       헤더 내비게이션\n      '),
]

# Sort by length descending to avoid partial replacement issues
translations_sorted = sorted(translations, key=lambda x: len(x[0]), reverse=True)

new_content = content
hit = 0
miss = 0
for eng, kor in translations_sorted:
    if eng in new_content:
        new_content = new_content.replace(eng, kor)
        print(f"OK: {repr(eng[:70])}")
        hit += 1
    else:
        print(f"MISS: {repr(eng[:70])}")
        miss += 1

with open('src/Try it out (1).html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nDone. {hit} replaced, {miss} missed. File written.")
