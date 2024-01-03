import pickle
import numpy as np
import pandas as pd

model=pickle.load(open('Deploy/logit_model_1.pkl','rb'))
xtest=pd.DataFrame([[3,4,5,6,7,3,7,4]])
print(type(xtest),xtest)
print(model.predict(xtest))
