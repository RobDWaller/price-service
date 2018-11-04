[![Build Status](https://travis-ci.org/RobDWaller/price-service.svg?branch=master)](https://travis-ci.org/RobDWaller/price-service) [![codecov](https://codecov.io/gh/RobDWaller/price-service/branch/master/graph/badge.svg)](https://codecov.io/gh/RobDWaller/price-service)
# Price Service Test

This library aims to complete the price service assessment created by [behrendtio](https://github.com/behrendtio):

[https://github.com/tailsdotcom/coding-test-pricing-service](https://github.com/tailsdotcom/coding-test-pricing-service)

The library is built based on the Flask micro-framework.

## Usage
Clone the repository and install dependencies:

```
pip install -r requirements.txt
```

Setup Flask:

```
export FLASK_APP=price/main.py
flask run
```

There are two methods:

- `/` returns documentation on how to use the library.
- `/prices` main endpoint, processes product data and returns prices data.

## API Usage

Post the below data to /prices endpoint. Attach the json data to the HTTP body with a key of 'data'.

```javascript
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
```

Response will be:
```javascript
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
```

## Notes

There are some obvious flaws with this library, positives include the compliance with Pylint standards and a Radon CC A1 grade and score.

The flaws are listed below and are generally based on time constraints.

Flaws:

- No attempt is made to integrate with a third party exchange rate API / provider. The code and unit tests show the core business logic can cope with different exchange rates though.
- No validation of the input JSON input data is carried. It assumes input will always be correct.
- The library generally returns lists of dictionaries. This is not ideal a 'collection' of objects would be preferable.
- The representation of the different currencies could be better, using symbols isn't ideal.
- There is no integration with a database to acquire price data.
- Code coverage could be a lot better and further tests added.

## Author

[RobDWaller](https://twitter.com/RobDWaller)
