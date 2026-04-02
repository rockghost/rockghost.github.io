FILE_PATH = r"D:\Git\rockghost.github.io\src\Try it out 2.html"

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

translations = [
    # Page title (in <title> tags)
    ("Visualizing 1024D Space", "1024\ucc28\uc6d0 \uacf5\uac04 \uc2dc\uac01\ud654"),

    # Navigation
    ("Header Navigation", "\ud5e4\ub354 \ub0b4\ube44\uac8c\uc774\uc158"),
    ("Anthropic Academy", "Anthropic \uc544\uce74\ub370\ubbf8"),
    ("Courses", "\uac15\uc758"),
    ("My Profile", "\ub0b4 \ud504\ub85c\ud544"),
    ("Sign Out", "\ub85c\uadf8\uc544\uc6c3"),

    # Article header
    ("Embeddings &amp; Similarity Search", "\uc784\ubca0\ub529 &amp; \uc720\uc0ac\ub3c4 \uac80\uc0c9"),
    ("How multidimensional \u201cnearness\u201d works", "\ub2e4\ucc28\uc6d0 \u201c\uadfc\uc811\uc131\u201d\uc758 \uc791\ub3d9 \uc6d0\ub9ac"),

    # Section: The Problem with Strings
    ("The Problem with Strings", "\ubb38\uc790\uc5f4\uc758 \ud55c\uacc4"),
    (
        "Search \u201ccar\u201d and you\u2019ll find every document containing the word \u201ccar.\u201d You won\u2019t find \u201cautomobile.\u201d Or \u201cvehicle.\u201d Or \u201cmy Civic needs new brakes.\u201d",
        "\u201ccar\u201d\ub97c \uac80\uc0c9\ud558\uba74 \u201ccar\u201d\ub77c\ub294 \ub2e8\uc5b4\uac00 \ud3ec\ud568\ub41c \ubaa8\ub4e0 \ubb38\uc11c\ub97c \ucc3e\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ud558\uc9c0\ub9cc \u201cautomobile\u201d\uc740 \ucc3e\uc9c0 \ubabb\ud569\ub2c8\ub2e4. \u201cvehicle\u201d\ub3c4, \u201c\ub0b4 \uc2dc\ube55 \ube0c\ub808\uc774\ud06c \uad50\uccb4\u201d\ub3c4 \ucc3e\uc9c0 \ubabb\ud569\ub2c8\ub2e4."
    ),
    (
        "For decades, that was search, returning results based on string similarity rather than meaning. Google continuously made incremental improvements with engineering: Synonym dictionaries mapped \u201ccar\u201d to \u201cautomobile,\u201d Stemming rules connected \u201cunning\u201d to \u201crun,\u201d and click-pattern mining surfaced that people who search \u201cNYC apartments\u201d want the same results as \u201cManhattan rentals.\u201d The connections between non-matching strings had to be mapped more or less by hand.",
        "\uc218\uc2ed \ub144 \ub3d9\uc548 \uac80\uc0c9\uc774\ub780 \uc758\ubbf8\uac00 \uc544\ub2cc \ubb38\uc790\uc5f4 \uc720\uc0ac\ub3c4\ub97c \uae30\ubc18\uc73c\ub85c \uacb0\uacfc\ub97c \ubc18\ud658\ud558\ub294 \uac83\uc774\uc5c8\uc2b5\ub2c8\ub2e4. Google\uc740 \uc5d4\uc9c0\ub2c8\uc5b4\ub9c1\uc73c\ub85c \uaf3e\uc900\ud788 \uac1c\uc120\ud574\uc654\uc2b5\ub2c8\ub2e4. \ub3d9\uc758\uc5b4 \uc0ac\uc804\uc740 \u201ccar\u201d\ub97c \u201cautomobile\u201d\uc5d0 \ub9e4\ud551\ud558\uace0, \uc5b4\uac04 \uaddc\uce59\uc740 \u201cunning\u201d\uc744 \u201crun\u201d\uc5d0 \uc5f0\uacb0\ud558\uba70, \ud074\ub9ad \ud328\ud134 \ubd84\uc11d\uc740 \u201cNYC apartments\u201d\ub97c \uac80\uc0c9\ud558\ub294 \uc0ac\ub78c\ub4e4\uc774 \u201cManhattan rentals\u201d\uc640 \ub3d9\uc77c\ud55c \uacb0\uacfc\ub97c \uc6d0\ud55c\ub2e4\ub294 \uac83\uc744 \ubc1c\uacac\ud588\uc2b5\ub2c8\ub2e4. \uc77c\uce58\ud558\uc9c0 \uc54a\ub294 \ubb38\uc790\uc5f4 \uac04\uc758 \uc5f0\uacb0\uc740 \uc0ac\uc2e4\uc0c1 \uc218\uc791\uc5c5\uc73c\ub85c \ub9e4\ud551\ud574\uc57c \ud588\uc2b5\ub2c8\ub2e4."
    ),
    (
        "challenged all of this with the idea that",
        "\uc740 \uc774 \ubaa8\ub4e0 \uac83\uc5d0 \ub3c4\uc804\ud588\uc2b5\ub2c8\ub2e4. \ubc14\ub85c"
    ),
    ("could be a", "\uc774 \ud558\ub098\uc758"),
    (
        ". By converting text into coordinates, similar concepts end up near each other. This mapping of semantic space isn\u2019t manual, but rather",
        "\uac00 \ub420 \uc218 \uc788\ub2e4\ub294 \uc544\uc774\ub514\uc5b4\ub85c. \ud14d\uc2a4\ud2b8\ub97c \uc88c\ud45c\ub85c \ubcc0\ud658\ud568\uc73c\ub85c\uc368 \uc720\uc0ac\ud55c \uac1c\ub150\ub4e4\uc774 \uc11c\ub85c \uac00\uae4c\uc774 \uc704\uce58\ud558\uac8c \ub429\ub2c8\ub2e4. \uc774 \uc758\ubbf8 \uacf5\uac04\uc758 \ub9e4\ud551\uc740 \uc218\ub3d9\uc774 \uc544\ub2c8\ub77c"
    ),
    ("from training data.", "\ud559\uc2b5 \ub370\uc774\ud130\uc5d0\uc11c \uc790\uc5f0\uc2a4\ub7fd\uac8c \ub098\ud0c0\ub0a9\ub2c8\ub2e4."),

    # Section: Encoding
    ("Encoding", "\uc778\ucf54\ub529"),
    ("Let\u2019s start with a simplified example.", "\uac04\ub2e8\ud55c \uc608\uc2dc\ubd80\ud130 \uc2dc\uc791\ud574 \ubcf4\uaca0\uc2b5\ub2c8\ub2e4."),
    (
        "Imagine you were to score every document in a corpus of knowledge on two dimensions: how much it relates to dinosaurs, and how much it relates to roller coasters. Documents about similar topics would end up near each other.",
        "\uc9c0\uc2dd \ucf54\ud37c\uc2a4\uc758 \ubaa8\ub4e0 \ubb38\uc11c\ub97c \ub450 \uac00\uc9c0 \ucc28\uc6d0\uc73c\ub85c \uc810\uc218\ub97c \ub9e4\uae34\ub2e4\uace0 \uc0c1\uc0c1\ud574 \ubcf4\uc138\uc694. \uacf5\ub97c\uacfc \uc5bc\ub9c8\ub098 \uad00\ub828\uc774 \uc788\ub294\uc9c0, \uadf8\ub9ac\uace0 \ub864\ub7ec\ucf54\uc2a4\ud130\uc640 \uc5bc\ub9c8\ub098 \uad00\ub828\uc774 \uc788\ub294\uc9c0. \ube44\uc2b7\ud55c \uc8fc\uc81c\uc758 \ubb38\uc11c\ub4e4\uc740 \uc11c\ub85c \uac00\uae4c\uc774 \ubaa8\uc774\uac8c \ub429\ub2c8\ub2e4."
    ),
    (
        "Let\u2019s start with just three sources. Place each of these where you think they belong.",
        "\uc138 \uac1c\uc758 \ucd9c\ucc98\ub85c \uc2dc\uc791\ud574 \ubcf4\uaca0\uc2b5\ub2c8\ub2e4. \uac01\uac01\uc774 \uc18d\ud55c\ub2e4\uace0 \uc0dd\uac01\ud558\ub294 \uc704\uce58\uc5d0 \ub193\uc544\ubcf4\uc138\uc694."
    ),
    ("How much does this relate to", "\uc774\uac83\uc740"),
    ("roller coasters", "\ub864\ub7ec\ucf54\uc2a4\ud130"),
    ("? \u2192", "\uc640 \uc5bc\ub9c8\ub098 \uad00\ub828\uc774 \uc788\ub098\uc694? \u2192"),
    ("not at all", "\uc804\ud600 \uc544\ub2d8"),
    ("click to place selected item", "\ud074\ub9ad\ud558\uc5ec \uc120\ud0dd\ud55c \ud56d\ubaa9\uc744 \ubc30\uce58\ud558\uc138\uc694"),
    ("dinosaurs", "\uacf5\ub97c"),
    ("Sources", "\ucd9c\ucc98"),
    ("A children\u2019s book about dinosaurs", "\uacf5\ub97c\uc5d0 \uad00\ud55c \uc5b4\ub9b0\uc774 \ucc45"),
    ("click to select", "\ud074\ub9ad\ud558\uc5ec \uc120\ud0dd"),
    ("The Velocicoaster web page", "Velocicoaster \uc6f9 \ud398\uc774\uc9c0"),
    ("An entire encyclopedia", "\ubc31\uacfc\uc0ac\uc804 \uc804\uccb4"),
    (
        "You\u2019ve just mapped meaning in 2D space, plotting our collection of items based on what they\u2019re about.",
        "\ubc29\uae08 2D \uacf5\uac04\uc5d0\uc11c \uc758\ubbf8\ub97c \ub9e4\ud551\ud588\uc2b5\ub2c8\ub2e4. \uac01 \ud56d\ubaa9\uc774 \ubb34\uc5c7\uc5d0 \uad00\ud55c \uac83\uc778\uc9c0 \uae30\uc900\uc73c\ub85c \ucf7c\ub809\uc158\uc744 \ud45c\uc2dc\ud55c \uac83\uc785\ub2c8\ub2e4."
    ),

    # Section: Retrieval
    ("Retrieval", "\uac80\uc0c9"),
    ("Now let\u2019s search this space.", "\uc774\uc81c \uc774 \uacf5\uac04\uc744 \uac80\uc0c9\ud574 \ubcf4\uaca0\uc2b5\ub2c8\ub2e4."),
    (
        "Plot a question on the same graph with the same axes. By mapping your question with the same logic you used to map sources, you can be sure that the nearest items will be the most relevant. Bonus feature: Use the slider to control how many get retrieved.",
        "\ub3d9\uc77c\ud55c \ucd95\uc744 \uac00\uc9c4 \ub3d9\uc77c\ud55c \uadf8\ub798\ud504\uc5d0 \uc9c8\ubb38\uc744 \ud45c\uc2dc\ud574 \ubcf4\uc138\uc694. \ucd9c\ucc98\ub97c \ub9e4\ud551\ud560 \ub54c\uc640 \uac19\uc740 \ub17c\ub9ac\ub85c \uc9c8\ubb38\uc744 \ub9e4\ud551\ud558\uba74, \uac00\uc7a5 \uac00\uae4c\uc6b4 \ud56d\ubaa9\uc774 \uac00\uc7a5 \uad00\ub828\uc131\uc774 \ub192\ub2e4\ub294 \uac83\uc744 \ud655\uc778\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ubcf4\ub108\uc2a4 \uae30\ub2a5: \uc2ac\ub77c\uc774\ub354\ub97c \uc0ac\uc6a9\ud558\uc5ec \uac80\uc0c9\ud560 \ud56d\ubaa9 \uc218\ub97c \uc870\uc808\ud558\uc138\uc694."
    ),
    ("Sources to retrieve (k):", "\uac80\uc0c9\ud560 \ucd9c\ucc98 \uc218 (k):"),
    ("click to place the question", "\ud074\ub9ad\ud558\uc5ec \uc9c8\ubb38\uc744 \ubc30\uce58\ud558\uc138\uc694"),
    ("Question", "\uc9c8\ubb38"),
    (
        "\u2753 \u201cWhat\u2019s the best dinosaur-themed roller coaster?\u201d",
        "\u2753 \u201c\uac00\uc7a5 \uc88b\uc740 \uacf5\ub97c \ud14c\ub9c8 \ub864\ub7ec\ucf54\uc2a4\ud130\ub294 \ubb34\uc5c7\uc778\uac00\uc694?\u201d"
    ),
    ("click graph to place", "\uadf8\ub798\ud504\ub97c \ud074\ub9ad\ud558\uc5ec \ubc30\uce58"),
    (
        "in a nutshell. We plot the question and find the nearest k items. Instead of keyword matching or synonym tables, we use multi-dimensional proximity.",
        "\ub97c \ud55c\ub9c8\ub514\ub85c \uc815\ub9ac\ud558\uba74 \uc774\ub807\uc2b5\ub2c8\ub2e4. \uc9c8\ubb38\uc744 \ud45c\uc2dc\ud558\uace0 \uac00\uc7a5 \uac00\uae4c\uc6b4 k\uac1c\uc758 \ud56d\ubaa9\uc744 \ucc3e\uc2b5\ub2c8\ub2e4. \ud0a4\uc6cc\ub4dc \ub9e4\uce6d\uc774\ub098 \ub3d9\uc758\uc5b4 \ud14c\uc774\ube14 \ub300\uc2e0 \ub2e4\ucc28\uc6d0 \uadfc\uc811\uc131\uc744 \uc0ac\uc6a9\ud569\ub2c8\ub2e4."
    ),
    (
        "Two axes is a start. But two dimensions can only capture two concepts. The real world has more than two topics, so we need more",
        "\ub450 \uac1c\uc758 \ucd95\uc740 \uc2dc\uc791\uc5d0 \ubd88\uacfc\ud569\ub2c8\ub2e4. \ud558\uc9c0\ub9cc \ub450 \ucc28\uc6d0\uc740 \ub450 \uac00\uc9c0 \uac1c\ub150\ub9cc \ud3ec\uc798\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uc2e4\uc81c \uc138\uacc4\ub294 \ub450 \uac00\uc9c0 \uc774\uc0c1\uc758 \uc8fc\uc81c\ub97c \uac00\uc9c0\uace0 \uc788\uc73c\ubbc0\ub85c \ub354 \ub9ce\uc740"
    ),

    # Section: More Dimensions
    ("More Dimensions", "\ub354 \ub9ce\uc740 \ucc28\uc6d0"),
    ("What if we added a third axis? Let\u2019s use", "\uc138 \ubc88\uc9f8 \ucd95\uc744 \ucd94\uac00\ud55c\ub2e4\uba74 \uc5b4\ub5a8\uae4c\uc694?"),
    (
        "The children\u2019s book scores high (species, habitats, diets). The encyclopedia covers some. The Velocicoaster page barely mentions it.",
        "\uc5b4\ub9b0\uc774 \ucc45\uc740 \ub192\uc740 \uc810\uc218\ub97c \ubc1b\uc2b5\ub2c8\ub2e4 (\uc885, \uc11c\uc2dd\uc9c0, \uc2dd\uc131). \ubc31\uacfc\uc0ac\uc804\uc740 \uc77c\ubd80\ub97c \ub2e4\ub985\ub2c8\ub2e4. Velocicoaster \ud398\uc774\uc9c0\ub294 \uac70\uc758 \uc5b8\uae09\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4."
    ),
    ("Drag to rotate.", "\ub4dc\ub798\uadf8\ud558\uc5ec \ud68c\uc804\ud558\uc138\uc694."),
    (
        "Three dimensions, three coordinates per document. The Velocicoaster page is now",
        "\uc138 \ucc28\uc6d0, \ubb38\uc11c\ub2f9 \uc138 \uac1c\uc758 \uc88c\ud45c. Velocicoaster \ud398\uc774\uc9c0\ub294 \uc774\uc81c"
    ),
    ("instead of", "\ub300\uc2e0"),
    ("Now try to picture a fourth axis.", "\uc774\uc81c \ub124 \ubc88\uc9f8 \ucd95\uc744 \uc0c1\uc0c1\ud574 \ubcf4\uc138\uc694."),
    (
        "Since I only exist in 3 dimensions, I personally can\u2019t \U0001f614 but that actually doesn\u2019t matter! Each new dimension just adds another coordinate to each point and another squared term to the distance formula. The spatial representation stops working at 4D, but the math keeps working.",
        "\uc800\ub294 3\ucc28\uc6d0\uc5d0\ub9cc \uc874\uc7ac\ud558\uae30 \ub54c\ubb38\uc5d0 \uac1c\uc778\uc801\uc73c\ub85c \uc0c1\uc0c1\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4 \U0001f614 \ud558\uc9c0\ub9cc \uc2e4\uc81c\ub85c \uadf8\uac74 \uc911\uc694\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4! \uc0c8\ub85c\uc6b4 \ucc28\uc6d0\ub9c8\ub2e4 \uac01 \uc810\uc5d0 \uc88c\ud45c \ud558\ub098\uc640 \uac70\ub9ac \uacf5\uc2dd\uc5d0 \uc81c\uacf1 \ud56d \ud558\ub098\uac00 \ucd94\uac00\ub420 \ubfd0\uc785\ub2c8\ub2e4. \uacf5\uac04\uc801 \ud45c\ud604\uc740 4D\uc5d0\uc11c \uc791\ub3d9\ud558\uc9c0 \uc54a\uc9c0\ub9cc, \uc218\ud559\uc740 \uacc4\uc18d \uc791\ub3d9\ud569\ub2c8\ub2e4."
    ),
    (
        "use around a thousand dimensions. Each document and each query becomes a point in that thousand-dimensional space. \u201cFind the nearest documents\u201d still means the same thing it meant on the 2D graph. It\u2019s just a longer distance calculation.",
        "\uc57d \ucc9c \uac1c\uc758 \ucc28\uc6d0\uc744 \uc0ac\uc6a9\ud569\ub2c8\ub2e4. \uac01 \ubb38\uc11c\uc640 \uac01 \ucffc\ub9ac\ub294 \uadf8 \ucc9c \ucc28\uc6d0 \uacf5\uac04\uc758 \ud55c \uc810\uc774 \ub429\ub2c8\ub2e4. \u201c\uac00\uc7a5 \uac00\uae4c\uc6b4 \ubb38\uc11c \ucc3e\uae30\u201d\ub294 2D \uadf8\ub798\ud504\uc5d0\uc11c \uc758\ubbf8\ud588\ub358 \uac83\uacfc \uc5ec\uc804\ud788 \ub3d9\uc77c\ud569\ub2c8\ub2e4. \ub2e8\uc9c0 \ub354 \uae34 \uac70\ub9ac \uacc4\uc0b0\uc77c \ubfd0\uc785\ub2c8\ub2e4."
    ),

    # Section: Unlabeled Axes
    ("Unlabeled Axes", "\ub808\uc774\ube14 \uc5c6\ub294 \ucd95"),
    (
        "We chose the axes: dinosaurs, roller coasters, biology. But who determines which 1,024 topics make it into a real embedding model?",
        "\uc6b0\ub9ac\ub294 \ucd95\uc744 \uc120\ud0dd\ud588\uc2b5\ub2c8\ub2e4: \uacf5\ub97c, \ub864\ub7ec\ucf54\uc2a4\ud130, \uc0dd\ubb3c\ud559. \ud558\uc9c0\ub9cc \uc2e4\uc81c \uc784\ubca0\ub529 \ubaa8\ub378\uc5d0 \ud3ec\ud568\ub420 1,024\uac1c\uc758 \uc8fc\uc81c\ub294 \ub204\uac00 \uacb0\uc815\ud560\uae4c\uc694?"
    ),
    (
        "In point of fact, no one decides. The meaning of each axis is emergent (meaning it just shows up in training), and more of a black box. You can\u2019t look at dimension 847 and say \u201cthat\u2019s the dinosaur axis.\u201d The dimensions don\u2019t correspond to anything a human could name.",
        "\uc0ac\uc2e4 \uc544\ubb34\ub3c4 \uacb0\uc815\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4. \uac01 \ucd95\uc758 \uc758\ubbf8\ub294 \uc790\uc5f0\ubc1c\uc0dd\uc801\uc73c\ub85c \ub098\ud0c0\ub0a9\ub2c8\ub2e4 (\uc989, \ud559\uc2b5 \uacfc\uc815\uc5d0\uc11c \uadf8\ub0e5 \ub098\ud0c0\ub0a9\ub2c8\ub2e4). \ub354 \ube14\ub799\ubc15\uc2a4\uc5d0 \uac00\uae5d\uc2b5\ub2c8\ub2e4. 847\ubc88 \ucc28\uc6d0\uc744 \ubcf4\uace0 \u201c\uc774\uac8c \uacf5\ub97c \ucd95\uc774\ub2e4\u201d\ub77c\uace0 \ub9d0\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4. \ucc28\uc6d0\ub4e4\uc740 \uc778\uac04\uc774 \uc774\ub984 \ubd99\uc77c \uc218 \uc788\ub294 \uc5b4\ub5a4 \uac83\uc5d0\ub3c4 \ub300\uc751\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4."
    ),
    (
        "This makes the space harder to reason about. We can\u2019t interrogate dimension 847 to understand why two texts landed near each other, or why something we expected to be close ended up far away.",
        "\uc774\uac83\uc740 \uacf5\uac04\uc5d0 \ub300\ud55c \ucd94\ub860\uc744 \ub354 \uc5b4\ub835\uac8c \ub9cc\ub4ed\ub2c8\ub2e4. \ub450 \ud14d\uc2a4\ud2b8\uac00 \uc655 \uc11c\ub85c \uac00\uae4c\uc774 \uc704\uce58\ud588\ub294\uc9c0, \ub610\ub294 \uac00\uae4c\uc6b8 \uac83\uc73c\ub85c \uc608\uc0c1\ud588\ub358 \uac83\uc774 \uc65c \uba40\ub9ac \ub5a8\uc5b4\uc84c\ub294\uc9c0 \uc774\ud574\ud558\uae30 \uc704\ud574 847\ubc88 \ucc28\uc6d0\uc744 \uc870\uc0ac\ud560 \uc218 \uc5c6\uc2b5\ub2c8\ub2e4."
    ),

    # Section: Text as Coordinates
    ("Text as Coordinates", "\uc88c\ud45c\ub85c\uc11c\uc758 \ud14d\uc2a4\ud2b8"),
    ("So who assigns the coordinates? An", "\uadf8\ub807\ub2e4\uba74 \ub204\uac00 \uc88c\ud45c\ub97c \ud560\ub2f9\ud560\uae4c\uc694?"),
    (
        ". Any string in, a fixed-length list of numbers out.",
        "\uc774 \ud569\ub2c8\ub2e4. \uc5b4\ub5a4 \ubb38\uc790\uc5f4\uc774\ub4e0 \uc785\ub825\ud558\uba74 \uace0\uc815 \uae38\uc774\uc758 \uc22b\uc790 \ubaa9\ub85d\uc774 \ucd9c\ub825\ub429\ub2c8\ub2e4."
    ),
    (
        "The output is always the same length (1,024 values in our specific case, since we\u2019re using VoyageAI\u2019s embeddings model) and this is true whether the input is three words or three paragraphs. One chunk of text corresponds to one point in space. The embedding model reads the text and outputs a single",
        "\ucd9c\ub825\uc740 \ud56d\uc0c1 \ub3d9\uc77c\ud55c \uae38\uc774\uc785\ub2c8\ub2e4 (\uc800\ud76c\uc758 \uacbd\uc6b0 VoyageAI \uc784\ubca0\ub529 \ubaa8\ub378\uc744 \uc0ac\uc6a9\ud558\ubbc0\ub85c 1,024\uac1c\uc758 \uac12). \uc785\ub825\uc774 \uc138 \ub2e8\uc5b4\uc774\ub4e0 \uc138 \ub2e8\ub77d\uc774\ub4e0 \ub9c8\ucc2c\uac00\uc9c0\uc785\ub2c8\ub2e4. \ud14d\uc2a4\ud2b8 \ud55c \uccad\ud06c\ub294 \uacf5\uac04\uc758 \ud55c \uc810\uc5d0 \ud574\ub2f9\ud569\ub2c8\ub2e4. \uc784\ubca0\ub529 \ubaa8\ub378\uc740 \ud14d\uc2a4\ud2b8\ub97c \uc77d\uace0 \ud558\ub098\uc758"
    ),
    (
        "The math-eyed among you will recognize that \u201cvector\u201d and \u201ccoordinate set\u201d aren\u2019t actually interchangeable, but for our purposes, it\u2019s appropriate to think of the vector as the address where this text lives relative to everything else.",
        "\uc218\ud559\uc801\uc73c\ub85c \uc608\ub9ac\ud55c \ubd84\ub4e4\uc740 \u201c\ubca1\ud130\u201d\uc640 \u201c\uc88c\ud45c \uc9d1\ud569\u201d\uc774 \uc2e4\uc81c\ub85c \uad50\ud658 \uac00\ub2a5\ud558\uc9c0 \uc54a\ub2e4\ub294 \uac83\uc744 \uc54c\uc544\ucc28\ub9b4 \uac83\uc785\ub2c8\ub2e4. \ud558\uc9c0\ub9cc \uc6b0\ub9ac\uc758 \ubaa9\uc801\uc0c1 \ubca1\ud130\ub97c \uc774 \ud14d\uc2a4\ud2b8\uac00 \ub2e4\ub978 \ubaa8\ub4e0 \uac83\uc5d0 \uc0c1\ub300\uc801\uc73c\ub85c \uc704\uce58\ud558\ub294 \uc8fc\uc18c\ub85c \uc0dd\uac01\ud558\ub294 \uac83\uc774 \uc801\uc808\ud569\ub2c8\ub2e4."
    ),

    # Section: Similarity
    ("Similarity", "\uc720\uc0ac\ub3c4"),
    (
        "\u201cNearest\u201d on our 2D graph meant straight-line distance. In practice, similarity search uses",
        "2D \uadf8\ub798\ud504\uc5d0\uc11c \u201c\uac00\uc7a5 \uac00\uae4c\uc6b4\u201d\uc774\ub780 \uc9c1\uc120 \uac70\ub9ac\ub97c \uc758\ubbf8\ud588\uc2b5\ub2c8\ub2e4. \uc2e4\uc81c\ub85c \uc720\uc0ac\ub3c4 \uac80\uc0c9\uc740"
    ),
    (
        "instead. Cosine similarity is just another measure of how similar two pieces of text are, based on the direction their vectors point rather than how far apart they sit.",
        "\ub97c \ub300\uc2e0 \uc0ac\uc6a9\ud569\ub2c8\ub2e4. \ucf54\uc0ac\uc778 \uc720\uc0ac\ub3c4\ub294 \ub450 \ud14d\uc2a4\ud2b8\uac00 \uc5bc\ub9c8\ub098 \uc720\uc0ac\ud55c\uc9c0\ub97c \uce21\uc815\ud558\ub294 \ub610 \ub2e4\ub978 \ubc29\ubc95\uc73c\ub85c, \ubca1\ud130\uac00 \uac00\ub9ac\ud0a4\ub294 \ubc29\ud5a5\uc744 \uae30\ubc18\uc73c\ub85c \ud558\uba70 \uc5bc\ub9c8\ub098 \uba40\ub9ac \ub5a8\uc5b4\uc838 \uc788\ub294\uc9c0\uc640\ub294 \ubb34\uad00\ud569\ub2c8\ub2e4."
    ),
    (
        "Try it yourself! Pick two sources to see their cosine similarity.",
        "\uc9c1\uc811 \ud574\ubcf4\uc138\uc694! \ub450 \ucd9c\ucc98\ub97c \uc120\ud0dd\ud558\uc5ec \ucf54\uc0ac\uc778 \uc720\uc0ac\ub3c4\ub97c \ud655\uc778\ud558\uc138\uc694."
    ),
    ("Source A", "\ucd9c\ucc98 A"),
    ("Source B", "\ucd9c\ucc98 B"),
    ("\u2753 Best dinosaur roller coaster?", "\u2753 \uac00\uc7a5 \uc88b\uc740 \uacf5\ub97c \ub864\ub7ec\ucf54\uc2a4\ud130\ub294?"),
    ("\U0001f995 Children\u2019s dinosaur book", "\U0001f995 \uc5b4\ub9b0\uc774 \uacf5\ub97c \ucc45"),
    ("opposite", "\ubc18\ub300"),
    ("unrelated", "\ubb34\uad00"),
    ("identical", "\ub3d9\uc77c"),
    (
        "Try comparing the Velocicoaster page to the dinosaur book \u2014 their vectors point in very different directions. The encyclopedia",
        "Velocicoaster \ud398\uc774\uc9c0\uc640 \uacf5\ub97c \ucc45\uc744 \ube44\uad50\ud574 \ubcf4\uc138\uc694 \u2014 \ubca1\ud130\uac00 \ub9e4\uc6b0 \ub2e4\ub978 \ubc29\ud5a5\uc744 \uac00\ub9ac\ud0b5\ub2c8\ub2e4. \ubc31\uacfc\uc0ac\uc804"
    ),

    # Navigation
    ("Previous", "\uc774\uc804"),
    ("Working Memory", "\uc791\uc5c5 \uae30\uc5b5"),
    ("Next", "\ub2e4\uc74c"),
    ("- Knowledge", "- \uc9c0\uc2dd"),

    # Inline fragments (after longer strings)
    ("Embeddings", "\uc784\ubca0\ub529"),
    ("meaning", "\uc758\ubbf8"),
    ("place", "\uc7a5\uc18c"),
    ("emergent", "\uc790\uc5f0\ubc1c\uc0dd\uc801"),
    ("similarity search", "\uc720\uc0ac\ub3c4 \uac80\uc0c9"),
    ("dimensions", "\ucc28\uc6d0"),
    ("embedding models", "\uc784\ubca0\ub529 \ubaa8\ub378"),
    ("embedding model", "\uc784\ubca0\ub529 \ubaa8\ub378"),
    ("vector", "\ubca1\ud130"),
    ("cosine similarity", "\ucf54\uc0ac\uc778 \uc720\uc0ac\ub3c4"),
    ("biology", "\uc0dd\ubb3c\ud559"),
    ("That\u2019s", "\uc774\uac83\uc774"),
    ("very", "\ub9e4\uc6b0"),
    ("Text", "\ud14d\uc2a4\ud2b8"),
    ("Embedding", "\uc784\ubca0\ub529"),
    ("1,024 values", "1,024\uac1c\uc758 \uac12"),
    ("Cosine similarity", "\ucf54\uc0ac\uc778 \uc720\uc0ac\ub3c4"),
    (
        "We\u2019re going to have to push well past 4D, because real",
        "\uc2e4\uc81c"
    ),
    ("Try it out", "\uc9c1\uc811 \ud574\ubcf4\uae30"),
]

# Sort by length descending to avoid partial replacements
translations_sorted = sorted(translations, key=lambda x: len(x[0]), reverse=True)

count_ok = 0
count_miss = 0
for eng, kor in translations_sorted:
    if eng in content:
        content = content.replace(eng, kor)
        count_ok += 1
        print(f"OK  : {repr(eng[:70])}")
    else:
        count_miss += 1
        print(f"MISS: {repr(eng[:70])}")

print(f"\nReplaced {count_ok}, Missed {count_miss}")

with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved.")
