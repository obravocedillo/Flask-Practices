from flask import Flask, request
import json

app = Flask(__name__)

currentNumber = 0
videogames = []

@app.route('/')
def index():
    return 'hello world'

@app.route('/number', methods=['GET', 'POST'])
def numberRoutes():
    global currentNumber
    if request.method == 'GET':
        return str(currentNumber)
    elif request.method == 'POST':
        requestNumber = request.form.get('number')
        currentNumber += int(requestNumber)
        return str(currentNumber)

@app.route('/videogames', methods=['GET','POST'])
def videoGamesRoutes():
    global videogames
    if request.method == 'GET':
        return json.dumps(videogames, default=str)
    elif request.method == 'POST':  
        requestVideogame = request.form.get('videogame')
        videogames.append(requestVideogame)
        return json.dumps(videogames, default=str)