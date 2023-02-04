    #Visualizing the training set result  
    from matplotlib.colors import ListedColormap  
    x_set, y_set = x_train, y_train  
    x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
    nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
    mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
    alpha = 0.75, cmap = ListedColormap(('purple','green' )))  
    mtp.xlim(x1.min(), x1.max())  
    mtp.ylim(x2.min(), x2.max())  
    for i, j in enumerate(nm.unique(y_set)):  
        mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
            c = ListedColormap(('purple', 'green'))(i), label = j)  
    mtp.title('Logistic Regression (Training set)')  
    mtp.xlabel('Age')  
    mtp.ylabel('Estimated Salary')  
    mtp.legend()  
    mtp.show()  
