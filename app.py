from flask import abort, Flask, request
from flask_restful import Resource, Api
from schema import payment_schema, mortgage_schema
from calculator import *
from rates import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    init_rates()

class Welcome(Resource):
    def get(self):
        return 'Welcome to Mortgage Calculator API v0.1'

class PaymentAmount(Resource):
    def get(self):
        errors = payment_schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        param = payment_schema.dump(request.args)
        payment_amount = cal_payment_amount(
            param['amount'], param['downPay'], param['schedule'], param['period'])
        return {'payment-amount': payment_amount}


class MortgageAmount(Resource):
    def get(self):
        errors = mortgage_schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        param = mortgage_schema.dump(request.args)
        mortgage_amount = cal_mortgage_amount(
            param['amount'], param['schedule'], param['period'])
        return {'mortgage-amount': mortgage_amount}


class InterestRate(Resource):
    def patch(self, parameters):
        param = request.json
        message = {'interest-rates' : 
                    [{'old':old_rate}, 
                    {'new':new_rate}]}
        return message
    

api.add_resource(Welcome, '/')
api.add_resource(PaymentAmount, '/payment-amount/')
api.add_resource(MortgageAmount, '/mortgage-amount/')
api.add_resource(InterestRate, '/interest-rate/')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)


# source .venv/bin/activate
# export FLASK_APP=app.py
# export FLASK_ENV=development
# pip3 freeze > requirements.txt
# http://127.0.0.1:5000/payment-amount/?amount=1000000&downPay=200000&schedule=monthly&period=20