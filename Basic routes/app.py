from flask import Flask, render_template, request
from os import environ
from pymongo import MongoClient
import json
import fn

app = Flask(__name__)
MONGO_URL = environ.get('MONGO_URL')
client = MongoClient(MONGO_URL, tls=True, tlsAllowInvalidCertificates=True)
db = client.SoccerFantasy

numbersArray = []

# Return a template with basic elements for and if
@app.route('/')
def index():
    user = {'username': 'Oliver'}
    names = [{'name':'0liver'},{'name':'Bravo'}]
    return render_template('index.html', title='Home', user=user, names=names)

@app.route('/average', methods=['GET'])
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
    
