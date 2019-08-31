from sklearn import metrics

def stats(train_test, predictors, bow_vector, classifier, classify, tokenizer):
    x_train, x_test, y_train, y_test = train_test
    pipe = classify(x_train, y_train, predictors, bow_vector, classifier, tokenizer)
    predicted = pipe.predict(x_test)
    print("Logistic Regression Accuracy:",metrics.accuracy_score(y_test, predicted))
    print("Logistic Regression Precision:",metrics.precision_score(y_test, predicted))
    print("Logistic Regression Recall:",metrics.recall_score(y_test, predicted))
