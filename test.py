from flask import *
from flask_cors import CORS
from pymongo import MongoClient
import pandas as pd
from flask import jsonify
from bson.json_util import dumps
import pulp
from pulp import LpVariable,LpProblem,LpStatus,LpMaximize
import pandas as pd
import pymongo
from pymongo import MongoClient
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import datetime
import json

@app.route('/')
def home():
    return "welcome to natwest backend"

@app.route('/home')
def home1():
    return "welcome to natwest backend"
