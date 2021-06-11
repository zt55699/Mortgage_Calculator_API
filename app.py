import os
from flask import abort, Flask, request
from flask_restful import Resource, Api
from schema import payment_schema, mortgage_schema, interest_schema
from calculator import *
from rates import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)


@app.before_first_request
def create_tables():
    if not os.path.isfile('./data.db'):
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
            param['payment'], param['schedule'], param['period'])
        return {'mortgage-amount': mortgage_amount}


class InterestRate(Resource):
    def get(self):
        return {"usage": "PATCH /interest-rate"}

    def patch(self):
        param = request.get_json()
        errors =  interest_schema.validate(param)
        if errors:
            abort(400, str(errors))
        new_rate = interest_schema.dump(param)['interest_rate']
        message = update_interest_rate(new_rate)
        return message
    

api.add_resource(Welcome, '/')
api.add_resource(PaymentAmount, '/payment-amount/')
api.add_resource(MortgageAmount, '/mortgage-amount/')
api.add_resource(InterestRate, '/interest-rate/')

if __name__ == '__main__':
    from db import db

    create_tables
    db.init_app(app)
    app.run(debug=True)

