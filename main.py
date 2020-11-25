import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from sklearn.externals import joblib
import pickle

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('main.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='CO2 Emission of the vehicle is :{}'.format(output))

if __name__ == '__main__':
	app.debug = True
	app.run(debug = True)