    #Fitting Logistic Regression to the training set  
    from sklearn.linear_model import LogisticRegression  
    classifier= LogisticRegression(random_state=0)  
    classifier.fit(x_train, y_train)  
