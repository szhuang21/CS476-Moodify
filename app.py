# app.py allows us to send data from frontend to backend

from flask import Flask, request, render_template
import csv
from implementation import create_data_json  
from flask_cors import CORS
from distutils.log import debug
from fileinput import filename
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename
 
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
ALLOWED_EXTENSIONS = {'csv'}

# Starts Flask connection
app = Flask(__name__, '/static')
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Configure upload file path of messages.csv in flask
app.secret_key = 'smartiesharters'

@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        print("/ endpoint hit")
        f = request.files.get('file')
        print("line 28")
        data_filename = "messages.csv"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],
                            data_filename))
        print("line 32")
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],
                     data_filename)
        print("line 35")
        create_data_json()
        return render_template('bubble_page.html')
    return render_template("upload_page.html")

if __name__ == '__main__':
    app.run(debug=True)
