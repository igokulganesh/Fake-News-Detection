import numpy as np
from flask import Flask, request, jsonify, render_template
#from flask_cors import CORS
import os
#from sklearn.externals import joblib
import pickle
import newspaper
from newspaper import Article
import urllib
import nltk

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('main.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    title=request.get_data(as_text=True)
    url=request.get_data(as_text=True)[5:]
    url=urllib.parse.unquote(url)
    article=Article(str(url))
    
    article.download()
    while article.download_state==0:
        time.sleep(1)
    article.parse()
    article.nlp()

    news = article.summary
    head = article.title
    pred=model.predict([head, news])
    

    return render_template('main.html', prediction_text='The news is :{}'.format(pred[0]))

if __name__ == '__main__':
	app.debug = True
	app.run(debug = True)