from gensim.models import Word2Vec

def train_word2vec(
    sentences,
    vector_size=200,
    window=5,
    min_count=25,
    workers=4,
    epochs=10
):
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=workers,
        sg=1
    )

    model.train(
        sentences,
        total_examples=len(sentences),
        epochs=epochs
    )

    return model
