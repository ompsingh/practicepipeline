from flask import *
import pandas as pd
from flask import jsonify
import json

@app.route('/')
def home():
    return "welcome to natwest backend"

@app.route('/home')
def home1():
    return "welcome to natwest backend"
