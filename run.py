#!/usr/bin/env python3

import pandas

from ldtn import split, evaluate, predict, train

DATASET_FILENAME = 'training_sets/product_reviews.tsv'

if __name__ == '__main__':
    train_test_data = pandas.read_csv(DATASET_FILENAME, sep='\t')
    text= train_test_data['verified_reviews']
    labels = train_test_data['feedback']
    x_train, x_test, y_train, y_test = split(text, labels, size_of_test=0.3)
    model = train(x_train, y_train)
    prediction = predict(model, x_test)
    stats = evaluate(y_test, prediction)

    for label, value in stats:
        print(f'{label}: \t{value}')
