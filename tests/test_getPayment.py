import os, sys
from flask import json, jsonify
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

try:
    import unittest
    from app import app
    from db import db
    

except Exception as e:
    print("Modules are Missing {} ".format(e))


class test_getPayment(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)
        db.init_app(app)

    # Check for missing parameters
    def test_missingParamemters(self):
        bad_queries = ['/payment-amount/',
            '/payment-amount/?downPay=200000&schedule=monthly&period=20',
            '/payment-amount/?amount&downPay=200000&schedule=monthly&period=20',
            '/payment-amount/?1000000&downPay=200000&schedule=monthly&period=20',
            '/payment-amount/?amount=&downPay=200000&schedule=monthly&period=20']

        for q in bad_queries:
            response = self.tester.get(q)
            code = response.status_code
            self.assertEqual(code, 400)

    # Check for invalid parameters
    def test_invalidParamemters(self):
        bad_queries = ['/payment-amount/?amount=-1&downPay=200000&schedule=monthly&period=20',
            '/payment-amount/?amount=1000000&downPay=200000&schedule=month&period=20',
            '/payment-amount/?amount=1000000&downPay=200000&schedule=weekly&period=30',
            '/payment-amount/?amount=1000000&downPay=200000&schedule=weekly&period=3',
            '/payment-amount/?amount=1000000&downPay=200000&schedule=weekly&period=8.5']

        for q in bad_queries:
            response = self.tester.get(q)
            code = response.status_code
            self.assertEqual(code, 400)

    # Check for insufficient down payment
    def test_insufficientDownPay(self):
        bad_queries = ['/payment-amount/?amount=400000&downPay=19000&schedule=monthly&period=20',
            '/payment-amount/?amount=800000&downPay=41000&schedule=monthly&period=20',
            '/payment-amount/?amount=1000000&downPay=199999&schedule=monthly&period=20']

        for q in bad_queries:
            response = self.tester.get(q)
            code = response.status_code
            self.assertEqual(code, 400)
    
    # Check if return results are correct
    def test_getPayment(self):
        expectations = [('/payment-amount/?amount=1000000&downPay=200000&schedule=monthly&period=20', 4239),
            ('/payment-amount/?amount=500000&downPay=100000&schedule=monthly&period=20', 2120),
            ('/payment-amount/?amount=500000&downPay=50000&schedule=monthly&period=20', 2442),
            ('/payment-amount/?amount=500000&downPay=50000&schedule=biweekly&period=20', 1122),
            ('/payment-amount/?amount=500000&downPay=50000&schedule=biweekly&period=10', 1996),
            ('/payment-amount/?amount=500000&downPay=50000&schedule=weekly&period=5', 1879)]

        for pair in expectations:
            response = self.tester.get(pair[0])
            data = json.loads(response.data)#["payment-amount"]
            self.assertEqual(data["payment-amount"], pair[1])

    # Check if return type is application/json
    def test_type(self):
         response = self.tester.get('/payment-amount/?amount=1000000&downPay=200000&schedule=monthly&period=20')
         self.assertEqual(response.content_type, "application/json")


if __name__ == "__main__":
    unittest.main()