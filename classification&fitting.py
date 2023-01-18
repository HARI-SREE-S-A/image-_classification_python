classifier = SVC()
parameters = [{'gamma':[0.01,0.001,0.0001],'C':[1,10,100,1000]}]

grid_search = GridSearchCV(classifier,parameters)
grid_search.fit(x_train,y_train)
