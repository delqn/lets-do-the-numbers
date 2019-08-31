from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer,
)

def bow_vector(tokenizer):
    return CountVectorizer(
        tokenizer=tokenizer,
        ngram_range=(1,1),
    )

def tfidf_vector(tokenizer):
    return TfidfVectorizer(
        tokenizer=tokenizer,
    )
