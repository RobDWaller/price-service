'''
Main routes module for price service application
'''
from flask import Flask
from flask import request
from flask import jsonify
import json
from price.src.controller import Controller

app = Flask(__name__)

@app.route('/prices', methods=['POST'])
def prices_read():
    '''
    Prices endpoint, consumes json data representing a list of products and
    the quantity required. Calls the controller read method.
    '''
    result = Controller.read(json.loads(request.form['data']))

    return jsonify(result)

@app.route('/')
def documentation():
    '''
    Base application endpoint, explains how to use service and confirm flask
    application is working.
    '''

    return '''
    <h1>Prices Service</h1>
    <p>Post the below data to /prices endpoint.</p>
    <p>Attach the json data to the HTTP body with a key of 'data'.</p>
    <pre>
    {
        "order": {
            "id": 12345,
            "customer": {
                "id": 1,
                "name": "Rob"
            },
            "items": [{
                "product_id": 1,
                    "quantity": 1
                },
                {
                    "product_id": 2,
                    "quantity": 5
                },
                {
                    "product_id": 3,
                    "quantity": 1
                }
            ]
        }
    }
    </pre>
    <p>Response will be:</p>
    <pre>
    {
        "prices": [
            {
                "currency": "£",
                "price": 2.5,
                "price_currency": "£2.50",
                "total_price": 3,
                "total_price_currency": "£3.00",
                "vat": 20,
                "vat_amount": 0.5
            },
            {
                "currency": "£",
                "price": 3.5,
                "price_currency": "£3.50",
                "total_price": 4.2,
                "total_price_currency": "£4.20",
                "vat": 20,
                "vat_amount": 0.7
            },
            {
                "currency": "£",
                "price": 3.5,
                "price_currency": "£3.50",
                "total_price": 4.2,
                "total_price_currency": "£4.20",
                "vat": 20,
                "vat_amount": 0.7
            },
            {
                "currency": "£",
                "price": 3.5,
                "price_currency": "£3.50",
                "total_price": 4.2,
                "total_price_currency": "£4.20",
                "vat": 20,
                "vat_amount": 0.7
            },
            {
                "currency": "£",
                "price": 3.5,
                "price_currency": "£3.50",
                "total_price": 4.2,
                "total_price_currency": "£4.20",
                "vat": 20,
                "vat_amount": 0.7
            },
            {
                "currency": "£",
                "price": 3.5,
                "price_currency": "£3.50",
                "total_price": 4.2,
                "total_price_currency": "£4.20",
                "vat": 20,
                "vat_amount": 0.7
            },
            {
                "currency": "£",
                "price": 4.5,
                "price_currency": "£4.50",
                "total_price": 5.4,
                "total_price_currency": "£5.40",
                "vat": 20,
                "vat_amount": 0.9
            }
        ],
        "total": {
            "total_price": 24.5,
            "total_price_currency": "£24.50",
            "total_price_vat": 29.4,
            "total_price_vat_currency": "£29.40",
            "vat": 20
        }
    }
    </pre>
    '''
