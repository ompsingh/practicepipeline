from flask import *
import pandas as pd
from flask import jsonify
import json
from flask_cors import CORS
app.secret_key='om2020@!'
cors = CORS(app)
authenticated = False

@app.route('/')
def home():
    return "welcome to Home"

@app.route('/home')
def home1():
    return "welcome to Home1"
