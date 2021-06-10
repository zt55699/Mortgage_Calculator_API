from rates import InterestRate, InsuranceRate
import math


def cal_payment_amount(amount:int, down_pay:int, schedule:str, period:int) -> int:
    # for price over 1m and downpay less than 20% already been filtered out by schema
    down_percent = down_pay*1.0/amount
    loan = amount - down_pay
    insurance_rate = get_insurance_rate(down_percent)
    insurance = loan * insurance_rate

    P = loan + insurance
    r = cal_interest_rate(schedule, get_anual_rate())
    n = cal_num_payments(schedule, period)
    payment = P*(r*((1+r)**n))/((1+r)**n-1)
    return round(payment)

def cal_mortgage_amount(amount, schedule, period):
    pass







def cal_interest_rate(schedule: str, anual_rate: float) -> float:
    r = 0
    if schedule == "weekly":
        r = anual_rate /365*7
    elif schedule == "biweekly":
        r = anual_rate /365*14
    elif schedule == "monthly":
        r = anual_rate /12
    return r


def cal_num_payments(schedule: str, period: int) -> int:
    n = 0
    if schedule == "weekly":
        n = math.ceil(period*365/7)
    elif schedule == "biweekly":
        n = math.ceil(period*365/14)
    elif schedule == "monthly":
        n = period*12
    return n

def get_anual_rate() -> float:
    return InterestRate.query.filter_by(id=0).first().anual_rate

def get_insurance_rate(down_percent: float) -> float:
    rate = 0.0
    if down_percent>=0.05 and down_percent<0.1:
        rate = InsuranceRate.query.filter_by(down_range='5-9.99%').first().rate
    elif down_percent>=0.1 and down_percent<0.15:
        rate = InsuranceRate.query.filter_by(down_range='10-14.99%').first().rate
    elif down_percent>=0.15 and down_percent<0.2:
        rate = InsuranceRate.query.filter_by(down_range='15-19.99%').first().rate
    elif down_percent>=0.2:
        rate = InsuranceRate.query.filter_by(down_range='20%+').first().rate
    return rate