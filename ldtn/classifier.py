from sklearn.pipeline import Pipeline

def fit(x_train, y_train, predictors, bow_vector, tokenizer, classifier):
    pipe = Pipeline([
        ('cleaner', predictors()),
        ('vectorizer', bow_vector(tokenizer)),
        ('classifier', classifier),
    ])
    return pipe.fit(x_train, y_train)

