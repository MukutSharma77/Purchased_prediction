from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = float(request.form['age'])
        estimatedsalary=float(request.form['estimatedsalary'])

        gender=request.form['gender']
        if(gender=='male'):
                gender=0

        else:
            gender=1

        prediction=model.predict([[gender, age,	estimatedsalary]])

        if prediction==0:
            return render_template('index.html',prediction_text="Not purchased")
        else:
            return render_template('index.html',prediction_text="Purchased")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)