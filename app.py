import numpy as np
from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from translator import translation

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/predict',methods=['POST'])
def predict():
	text = request.form['content']
	trans = translation(text)
	result = trans.translate_word()
    #print(result)
    #print(type(result))
    #return {"Result": str(result)}
	return render_template('index.html', prediction_text='{}'.format(result))
	
if __name__== "main":
	app.run()
