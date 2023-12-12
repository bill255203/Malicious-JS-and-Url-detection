#!/usr/bin/env python

import subprocess

### Import missing Python packages
def install_missing_package(package):
	subprocess.call(['pip', 'install', package]) 

### Import package and handle package error
#def import_the_packages():

# tensorflow
try:                            
	import tensorflow as tf
except ImportError:
	print("Error: Missing required package'tensorflow'")
	install_missing_package('tensorflow')
	import tensorflow as tf

# fasttext
try:
	import fasttext
except ImportError:
	print("Error: Missing required package'fasttext'")
	install_missing_package('fasttext')
	import fasttext

# flask
try:
	from flask import Flask, request, jsonify
except ImportError:
	print("Error: Missing required package'flask'")
	install_missing_package('flask')
	from flask import Flask, request, jsonify
    
# flask_cors
try:
	from flask_cors import CORS
except ImportError:
	print("Error: Missing required package'flask_cors'")
	install_missing_package('flask_cors')
	from flask_cors import CORS

# numpy
try:
	import numpy as np
except ImportError:
	print("Error: Missing required package 'numpy'")
	install_missing_package('numpy')
	import numpy as np

# transformers
try:
	from transformers import TFBertForSequenceClassification, BertTokenizer
except ImportError:
	print("Error: Missing required package 'transformers'")
	install_missing_package('transformers')
	from transformers import TFBertForSequenceClassification, BertTokenizer

### Loading pre-trained model for malicious Javascript detection
vector_model = fasttext.load_model('./pre-trained/w2v_model.bin')
lstm_model = tf.keras.models.load_model('./pre-trained/lstm.h5')

### Loading pre-trained model for phishing detection
model = TFBertForSequenceClassification.from_pretrained('./phishing_test')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

#import_the_packages()
app = Flask(__name__)
CORS(app)

### DFS function to convert AST to syntactic unit
def AST2sequence(ast):
	count = 0
	if ast != None:
		for node in ast:
			count += 1
			if node != 'type' and type(ast[node]) == list:
				for k in ast[node]:
					AST2sequence(k)
			if node != 'type' and type(ast[node]) == dict:
				AST2sequence(ast[node])
		if 'type' in ast:
			seq.append(ast['type'])

### URL for detecting malicious Javascript code
@app.route('/process', methods=['POST'])
def processData():
	global seq
	seq = []
	malicious = False
	code_data = request.json
	data = code_data["data"]
	AST2sequence(data)
	vectors = [vector_model.get_word_vector(unit) for unit in seq]
	vectors = np.asarray(vectors)
	x = np.expand_dims(vectors, axis=0)
	r_x = tf.ragged.constant(x)
	pred = lstm_model.predict(r_x)
	print(pred)
	if pred[0][0] > 0.5:
		malicious = True

	if (malicious):
		result = {'message': 'malicious website'}
	else:
		result = {'message': 'benign website'}

	return jsonify(result)

### URL for detecting phishing website by url
@app.route('/url_test', methods=['POST'])
def urlDetection():
	url_data = request.json
	url_to_predict = url_data["data"]
	print(url_to_predict)
	inputs = tokenizer(url_to_predict, truncation=True, padding=True, return_tensors='tf')

	input_ids = inputs["input_ids"]
	token_type_ids = inputs["token_type_ids"]
	attention_mask = inputs["attention_mask"]

	predictions = model.predict({"input_ids": input_ids, "token_type_ids": token_type_ids, "attention_mask": attention_mask})
	probabilities = tf.nn.softmax(predictions.logits, axis=1)
	label = tf.argmax(probabilities, axis=1).numpy()[0]

	if label == 1:
		result = {'message': 'Phishing Alert'}
	else:
		result = {'message': 'No Alert'}

	return jsonify(result)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)

