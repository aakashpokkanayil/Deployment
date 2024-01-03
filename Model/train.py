import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data=pd.read_csv('Data/diabetes.csv')

print(data.head())

X=data.drop(columns=['Outcome'])
y=data['Outcome']

xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=.3,random_state=1)

logit_reg=LogisticRegression()
logit_reg.fit(xtrain,ytrain)
y_pred=logit_reg.predict(xtest)
print(accuracy_score(y_true=ytest,y_pred=y_pred))

pickle.dump(logit_reg,open('Model/logit_model_1.pkl','wb'))


