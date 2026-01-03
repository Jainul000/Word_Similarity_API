import os
import pandas as pd
from preprocessing.data_cleaning import clean_text
from preprocessing.data_normalization import normalize_text
from app.model import train_word2vec

DATA_PATH = "data/stack_overflow_tech_final.parquet"
MODEL_PATH = "model/word2vec.model"

def main():
    print("Loading dataset...")
    df = pd.read_parquet(DATA_PATH)

    print("Cleaning and normalizing text...")
    sentences = (
        df["answer"]
        .dropna()
        .astype(str)
        .apply(normalize_text)
        .apply(clean_text)
        .tolist()
    )

    print("Training Word2Vec model...")
    model = train_word2vec(sentences)

    os.makedirs("model", exist_ok=True)
    model.save(MODEL_PATH)

    print("Word2Vec model saved successfully.")

if __name__ == "__main__":
    main()
