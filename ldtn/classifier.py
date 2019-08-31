import pickle

from sklearn.pipeline import Pipeline

def fit(x_train, y_train, predictors, bow_vector, tokenizer, classifier):
    pipe = Pipeline([
        ('cleaner', predictors()),
        ('vectorizer', bow_vector(tokenizer)),
        ('classifier', classifier),
    ])
    return pipe.fit(x_train, y_train)

def save_model(model, file_name):
    with open(file_name, 'w') as f:
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)