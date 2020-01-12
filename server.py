import os
from flask import Flask, render_template, send_from_directory, url_for, request

app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page>')
def route_page(page=None):
    return render_template(page)

@app.route('/submit_form', methods=['POST', 'GET'])
def subit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	print(data)
    	return 'form submitted'
    else:
    	return 'somehting went wrong. try again.'