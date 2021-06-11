from db import db


DEFAULT_RATE = 0.025
INSUR_RATES = {
        '5-9.99%': 0.0315,
        '10-14.99%': 0.024,
        '15-19.99%': 0.018,
        '20%+': 0.0
        }

class InterestRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anual_rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str(self.anual_rate)


class InsuranceRate(db.Model):
    down_range = db.Column(db.String(20), primary_key=True)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str(self.rate)


def init_rates():
    interest_rate = InterestRate(id=0, anual_rate=0.025)
    db.session.add(interest_rate)
    for down, rate in INSUR_RATES.items():
        db.session.add(InsuranceRate(down_range=down, rate=rate))
    db.session.commit()


def update_interest_rate(new_rate):
    interest_rate = InterestRate.query.get(0)
    old_rate = interest_rate.anual_rate
    interest_rate.anual_rate = new_rate
    db.session.commit()
    message = {'anual interest-rate' : 
        [{'old':toStr_percent(old_rate)}, {'new':toStr_percent(new_rate)}]}
    return message

def toStr_percent(value :float) -> str:
    str_percent = str(value*100) + '%'
    return str_percent

def toNum_percent(value: str) -> float:
    float_percent = float(value.strip('%'))/100
    return float_percent

# def model_exists(model_class) -> bool:
#     import sqlalchemy as sa
#     engine = sa.create_engine('sqlite:///data.db')
#     insp = sa.inspect(engine)
#     return insp.has_table(model_class)