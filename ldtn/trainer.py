from sklearn.linear_model import LogisticRegression

from .predictors import Predictors
from .vectorize import bow_vector
from .tokenizer import tokenizer
from .classifier import fit

def train(x_train, y_train):
    classifier = LogisticRegression()
    model = fit(x_train, y_train, Predictors, bow_vector, tokenizer, classifier)
    return model