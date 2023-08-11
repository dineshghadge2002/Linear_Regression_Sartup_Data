def Linear_regration():

    #importing libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import metrics
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split

    #load Dataset
    dataset=pd.read_csv("50_Startups.csv")
    print(dataset.head())


    print(dataset.info())
    print(dataset.columns)

    #feature selection
    x=dataset[[
        'R&D Spend',
        'Administration',
        'Marketing Spend'
    ]]
    print(x.head())

    #working with catogorical variable and create dummmies
    state= dataset['State'] 
    final_state=pd.get_dummies(state,drop_first=True)


    #selecting dependent variable
    y=dataset[["Profit"]]
    print(y.ndim)

    #applying Model
    model = LinearRegression()


    #split train and test data
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=5)
    model.fit(x_train,y_train)
    #model.predict(x_test)
    y_pred=model.predict(x_test)
    

    #applying error Martix
    metrics.mean_absolute_error(y_test,y_pred)


    #printing co-efficient and intercept
    print(model.coef_)
    print(model.intercept_)

Linear_regration()
