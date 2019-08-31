from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def fit(x_train, y_train, predictors, bow_vector, tokenizer):
    classifier = LogisticRegression()
    pipe = Pipeline([
        ('cleaner', predictors()),
        ('vectorizer', bow_vector(tokenizer)),
        ('classifier', classifier),
    ])
    pipe.fit(x_train, y_train)
    return pipe
