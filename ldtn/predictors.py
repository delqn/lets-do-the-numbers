from sklearn.base import TransformerMixin

class Predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

def clean_text(text):
    return text.strip().lower()
