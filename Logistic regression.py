# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import dataset
dataset=pd.read_csv(r"C:\Users\Rajendra\NIT Note\Machine Learning\logit classification.csv")

x=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)
print(ac)

bias=classifier.score(x_train,y_train)
print(bias)

variance=classifier.score(x_test,y_test)
print(variance)

dataset1=pd.read_csv(r"C:\Users\Rajendra\NIT Note\Machine Learning\logit\2.LOGISTIC REGRESSION CODE\final1.csv")
d2=dataset1.copy()

dataset1=dataset1.iloc[:,[3,4]].values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
M=sc.fit_transform(dataset1)

y_pred1=pd.DataFrame()

d2['y_pred1']=classifier.predict(M)

d2.to_csv('prediction_model.csv')

import os
os.getcwd()


