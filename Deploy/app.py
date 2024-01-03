import pickle
import numpy as np
import pandas as pd
from flask import Flask,render_template,request


app=Flask(__name__)


@app.route('/')
def base():
    return render_template('index.html')

@app.route('/gallery')
def galary():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/predict',methods = ['POST'])
def Predict():
    no_of_pregnensies=request.form.get('Pregnancies')
    Glucose_lvl=request.form.get('Glucose')
    BloodPressure=request.form.get('BloodPressure')
    SkinThickness=request.form.get('SkinThickness')
    Insulin=request.form.get('Insulin')
    BMI=request.form.get('BMI')
    DiabetesPedigreeFunction=request.form.get('DiabetesPedigreeFunction')
    Age=request.form.get('Age')
    
    with open('Deploy/logit_model_1.pkl','rb') as obj:
        model=pickle.load(obj)
    
    test_data_dict={
        "Pregnancies":[no_of_pregnensies],
        "Glucose":[Glucose_lvl],
        "BloodPressure":[BloodPressure],
        "SkinThickness":[SkinThickness],
        "Insulin":[Insulin],
        "BMI":[BMI],
        "DiabetesPedigreeFunction":[DiabetesPedigreeFunction],
        "Age":Age
    }
    test_data_df=pd.DataFrame(test_data_dict)
    print('testdata:',test_data_df)
    
    y_pred=model.predict(test_data_df)
    print(y_pred[0])
    
    if y_pred[0]==1:
        result="You Have Diabetes, Please Consult A Doctor!!"
    else:
        result="Hurray!!! You are perfectly fine."

    return render_template('index.html',result=result)

if __name__=="__main__":
    app.run(debug=True)
