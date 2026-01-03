from fastapi import FastAPI, HTTPException
from gensim.models import Word2Vec

MODEL_PATH = "model/word2vec.model"

app = FastAPI(title="Word Similarity API")

try:
    model = Word2Vec.load(MODEL_PATH)
except Exception:
    model = None


@app.get("/similar-words")
def get_similar_words(word: str):
    if not word:
        raise HTTPException(status_code=400, detail="Input word cannot be empty")

    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    word = word.lower()

    if word not in model.wv:
        raise HTTPException(status_code=404, detail=f"Word '{word}' not found in vocabulary")

    similar_words = model.wv.most_similar(word, topn=5)

    return {
        "word": word,
        "similar_words": [
            {"word": w, "score": float(score)}
            for w, score in similar_words
        ]
    }


