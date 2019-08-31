from sklearn.model_selection import train_test_split

def split(text, labels, size_of_test):
    x_train, x_test, y_train, y_test = train_test_split(
        text,
        labels,
        test_size=size_of_test if size_of_test else 0.3,
    )
    return x_train, x_test, y_train, y_test
