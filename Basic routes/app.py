from flask import Flask, render_template, request
import logging
from functools import wraps
from os import environ
from pymongo import MongoClient
from functools import wraps
import json
import fn

app = Flask(__name__)
MONGO_URL = environ.get('MONGO_URL')
client = MongoClient(MONGO_URL, tls=True, tlsAllowInvalidCertificates=True)
db = client.SoccerFantasy

numbersArray = []

# A decorator that checks mehtod type and executes a specific function
def check_get(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # if get us used log 'get used'  
        getCalled = False 
        if request.method == 'GET':
            print('get called', flush=True)
            getCalled = True         
        # finally call f. f() now haves access to getCalled
        return f(*args, **kwargs)
    return wrap

# Return a template with basic elements for and if
@app.route('/')
def index():
    user = {'username': 'Oliver'}
    names = [{'name':'0liver'},{'name':'Bravo'}]
    return render_template('index.html', title='Home', user=user, names=names)

@app.route('/average', methods=['GET'])
#Call check_get decorator
@check_get
def average():
    numbers = request.args.get('numbers')
    formatedNumbers = numbers.split(',')
    return str(fn.average(formatedNumbers))

@app.route('/newNumber', methods=['POST'])
def newNumber():
    number = request.form.get('number')
    numbersArray.append(number)
    return 'Success'

@app.route('/getUsers', methods=['GET'])
def getUsers():
    allUsers = []
    users = list(db.Users.find({},{'password':0}))
    return json.dumps(users, default=str)
    

