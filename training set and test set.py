    # Splitting the dataset into training and test set.
    # Splitting the dataset into test set.
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)
