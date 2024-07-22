#!/usr/bin/env python
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify
from waitress import serve

from ctrl import SolidColor, TwoColorAlter, off

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/', methods=['GET', 'POST'])
# ‘/’ URL is bound with hello_world() function.
def index():
    return render_template('index.html')

@app.route('/ctrl', methods=['POST'])
def ctrl():
    data = request.get_json()
    if data['cmd'] == 'clear':
        off()
    elif data['cmd'] == '1color':
        SolidColor('solidtmp')
    elif data['cmd'] == '2color':
        TwoColorAlter('tmp')
    return jsonify({'status': 'success'})

# main driver function
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
    