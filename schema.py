from marshmallow import Schema, fields, validate, validates_schema, ValidationError
import math


class PaymentAmountSchema(Schema):
    amount = fields.Integer(required=True, validate=validate.Range(min=0))
    downPay = fields.Integer(required=True)
    schedule = fields.String(required=True, validate=validate.OneOf(
        ['weekly', 'biweekly', 'monthly']))
    period = fields.Integer(required=True, validate=validate.Range(min=5, max=25))

    @validates_schema
    def validate_downPay(self, data, **kwargs):
        if data['downPay'] < 0 or data['amount'] <= data['downPay']:
            raise ValidationError('invalid down payment')
        elif data['amount'] >= 1000000 and (data['downPay']*1.0/data['amount']) < 0.2:
            raise ValidationError(f'20% down payments minimum is required for mortgages > $1 million')
        else:
            min_downPay = math.ceil(
                0.05* min(data['amount'], 500000) + max(0.1*(data['amount']-500000), 0))
            if data['downPay'] < min_downPay:
                raise ValidationError(f'down payment needs at least {min_downPay}')


class MortgageAmountSchema(Schema):
    payment = fields.Integer(required=True, validate=validate.Range(min=0))
    schedule = fields.String(required=True, validate=validate.OneOf(
        ['weekly', 'biweekly', 'monthly']))
    period = fields.Integer(required=True, validate=validate.Range(min=5, max=25))


class InterestRateSchema(Schema):
    interest_rate = fields.Float(required=True, validate=validate.Range(min=0.00, max=1.00))


payment_schema = PaymentAmountSchema()
mortgage_schema = MortgageAmountSchema()
interest_schema = InterestRateSchema()