import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

try:
    import unittest
    from app import app
    from calculator import *

except Exception as e:
    print("Modules are Missing {} ".format(e))


class test_calculator(unittest.TestCase):

    # Dont worry about invalid inputs, which will be filtered out by schema
    def test_get_insurance_rate(self):
        downPay_and_rates = {
            0.05: 0.0315,
            0.1: 0.024,
            0.15: 0.018,
            0.2: 0.0,
            0.5: 0.0
        }
        for downPay, rate in downPay_and_rates.items():
            self.assertEqual(get_insurance_rate(downPay), rate)

    def test_get_anual_rate(self):
        interest_rate = get_anual_rate()
        self.assertEqual(interest_rate, 0.025)

    def test_cal_num_payments(self):
        # {(schedule, period): num_of_payment}
        test_cases = {
            ("weekly", 5): 261,
            ("biweekly", 10): 261,
            ("monthly", 20): 240
        }
        for params, num_pays in test_cases.items():
            self.assertEqual(cal_num_payments(params[0], params[1]), num_pays)

    def test_cal_interest_rate(self):
        test_cases = {
            "weekly": (0.025/365*7),
            "biweekly": (0.025/365*14),
            "monthly": (0.025/12)
        }
        for schedule, rate in test_cases.items():
            self.assertEqual(cal_interest_rate(schedule, 0.025), rate)


if __name__ == "__main__":
    from db import db
    app.app_context().push()
    db.init_app(app)
    unittest.main()