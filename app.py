import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
# model = pickle.load("model.pkl", "rb")

@app.route('/')
def home():
    return render_template('web.html',
                           data = [{'gender' : 'Gender'}, {'gender' : 'male'}, {'gender' : 'female'}],
                           data1 = [{'married' : 'Marital status'}, {'married' : 'yes'}, {'married' : 'no'}],
                           data2 = [{'dependents' : 'Dependency'}, {'dependents' : '0'}, {'dependents' : '1'}, {'dependents' : '2'}, {'dependents' : '3'}, {'dependents' : '4'}],
                           data3 = [{'education' : 'Education'}, {'education' : 'graduated'}, {'education' : 'not-graduated'}],
                           data4 = [{'self_employed' : 'Employment'}, {'self-employed' : 'yes'}, {'self-employed' : 'no'}],
                           data5 = [{'credit' : 'Credit score'}, {'credit' : 'yes'}, {'credit' : 'no'}],
                           data6 = [{'area' : 'Area'}, {'area' : 'urban'}, {'area' : 'semi-urban'}, {'area' : 'rural'}])

@app.route('/predict', methods = ['GET','POST'])
def predict():
    input_data = list(request.form.values())
    for i in input_data:
        print(input_data[i])
    gender = request.form.get('gender')
    married = request.form.get('married')
    dependents = request.form.get('dependents')
    education = request.form.get('education')
    self_employed = request.form.get('self_employed')
    income = request.form.get('income')
    co_applicant = request.form.get('co_applicant')
    amount = request.form.get('amount')
    amount_term = request.form.get('amount_term')
    credit = request.form.get('credit')
    area = request.form.get('area')
    return render_template('web.html',prediction_text = f"This is working {gender}, {married}, {dependents}, {education}, {self_employed}, {income}, {co_applicant}, {amount}, {amount_term}, {credit}, {area}")

if __name__ == "__main__":
    app.run(debug = True)