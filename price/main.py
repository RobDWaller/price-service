from flask import Flask
from flask import request
import json
from price.src.controller import Controller

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/prices', methods=['POST'])
def prices_read():
    result = Controller.read(json.loads(request.form['data']))

    return json.dumps(result)
