from gensim.models import Word2Vec

MODEL_PATH = "model/word2vec.model"

# Curated test words grouped by category
TEST_WORDS = {
    "Core Programming": [
        "function", "class", "object", "method", "variable",
        "loop", "array", "list", "dictionary", "string"
    ],
    "Python Specific": [
        "python", "pip", "package", "module", "import",
        "decorator", "generator", "iterator", "lambda"
    ],
    "Errors & Debugging": [
        "error", "exception", "traceback", "bug",
        "debug", "fail", "warning"
    ],
    "CS Concepts": [
        "algorithm", "performance", "complexity",
        "memory", "thread", "process"
    ],
    "StackOverflow Meta": [
        "answer", "question", "comment", "accepted"
    ],
    "Common / Weak Words": [
        "get", "set", "use", "make", "possible"
    ]
}


def main():
    print("Loading Word2Vec model...")
    model = Word2Vec.load(MODEL_PATH)

    print("\n===== WORD SIMILARITY TEST RESULTS =====\n")

    for category, words in TEST_WORDS.items():
        print(f"\n🔹 {category}")
        print("-" * (len(category) + 4))

        for word in words:
            if word not in model.wv:
                print(f"{word:15s} → ❌ Not in vocabulary")
                continue

            similar_words = model.wv.most_similar(word, topn=5)

            formatted = ", ".join(
                f"{w} ({score:.2f})" for w, score in similar_words
            )

            print(f"{word:15s} → {formatted}")


if __name__ == "__main__":
    main()
