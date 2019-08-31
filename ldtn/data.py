import pandas as pd

from sklearn.model_selection import train_test_split

def split(size_of_test, dataset_filename):
    """Returns x_train, x_test, y_train, y_test"""
    # Loading TSV file
    alexa_dataframes = pd.read_csv (
        dataset_filename,
        sep='\t',
    )

    return train_test_split(
        alexa_dataframes['verified_reviews'],
        alexa_dataframes['feedback'],
        test_size=size_of_test if size_of_test else 0.3,
    )
