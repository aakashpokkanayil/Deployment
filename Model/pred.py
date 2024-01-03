import pickle

model=pickle.load(open('Model/logit_model_1.pkl','rb'))
print(model.predict([3,4,5,6,7,3,7,4]))
