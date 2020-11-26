import numpy as np
from flask import Flask, request,render_template
from flask_cors import CORS
import os
#from sklearn.externals import joblib
import sklearn
import pickle
import flask
import os
import newspaper
from newspaper import Article
import urllib
import nltk
nltk.download('punkt')

#Loading Flask and assigning the model variable
app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

with open('model.pickle', 'rb') as handle:
    model = pickle.load(handle)

#default page of our web-app
@app.route('/')
def home():
    return render_template('main.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['GET','POST'])
def predict():
    title=request.get_data(as_text=True)
    url=request.get_data(as_text=True)[5:]
    url=urllib.parse.unquote(url)
    article=Article(str(url))
    article.download()
    article.parse()
    article.nlp()

    news = article.summary
    head = article.title
    pred = model.predict([[head, news]])

    return render_template('main.html', prediction_text='The news is :{}'.format(pred[0]))

if __name__ == '__main__':
	app.debug = True
	app.run(debug = True)