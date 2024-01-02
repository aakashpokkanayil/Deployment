import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df=pd.read_csv('Data/placement.csv')
X=df[['cgpa']]
y=df[['package']]
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=.3,random_state=1)
Linearreg_model=LinearRegression()
Linearreg_model.fit(xtrain,ytrain)
y_pred=Linearreg_model.predict(xtest)
print(r2_score(y_true=ytest,y_pred=y_pred))