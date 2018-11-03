from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/prices', methods=['POST'])
def prices_read():
    return request.form['data']
