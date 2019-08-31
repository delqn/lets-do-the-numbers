import pandas as pd

from sklearn.model_selection import train_test_split

def split(size_of_test, dataset_filename):
    """Returns x_train, x_test, y_train, y_test"""
    alexa_dataframes = pd.read_csv (
        'training_sets/amazon_alexa.tsv',
        sep='\t',
    )
    x_train, x_test, y_train, y_test = train_test_split(
        alexa_dataframes['verified_reviews'],
        alexa_dataframes['feedback'],
        test_size,
    )
    return x_train, x_test, y_train, y_test
