# app.py allows us to send data from frontend to backend

from flask import Flask, request, render_template
import csv
from implementation import convert_to_data_array  
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
app = Flask(__name__)
CORS(app)

# Configure upload file path of messages.csv in flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'smartiesharters'

@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
      # upload file flask
        print("/ endpoint hit")
        f = request.files.get('file')
        data_filename = "messages.csv"
 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],
                            data_filename))
 
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],
                     data_filename)
        print("render_template")
        return render_template('bubble_page.html')
    # return
    #     return render_template('bubble_page.html')
    return render_template("upload-page.html")

if __name__ == '__main__':
    app.run(debug=True)
