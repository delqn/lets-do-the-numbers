from sklearn import metrics

def evaluate(y_test, predicted):
    return (
        ('Logistic Regression Accuracy', metrics.accuracy_score(y_test, predicted)),
        ('Logistic Regression Precision', metrics.precision_score(y_test, predicted)),
        ('Logistic Regression Recall', metrics.recall_score(y_test, predicted)),
    )
