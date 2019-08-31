from sklearn import metrics

def evaluate(train_test, predictors, bow_vector, classify, tokenizer):
    x_train, x_test, y_train, y_test = train_test
    pipe = classify(x_train, y_train, predictors, bow_vector, tokenizer)
    predicted = pipe.predict(x_test)
    return (
        ('Logistic Regression Accuracy', metrics.accuracy_score(y_test, predicted)),
        ('Logistic Regression Precision', metrics.precision_score(y_test, predicted)),
        ('Logistic Regression Recall', metrics.recall_score(y_test, predicted)),
    )
