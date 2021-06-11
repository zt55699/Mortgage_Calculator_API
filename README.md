# Mortgage_Calculator_API
A Flask-restful backend API of a mortgage calculator<br><br>

# Requirements Installation

For local debugging, there are several components to install.<br>
For the the python packages install through pip using the command:

```bash
sudo pip3 install -r requirements.txt
```

The text file contains the necessary packages.<br><br>


# Consume the API


## **GET /payment-amount**


Get the recurring payment amount of a mortgage

```
GET http://127.0.0.1:5000/payment-amount/?amount=<Asking Price>&downPay=<Down Payment>&schedule=<Payment schedule>&period=<Amortization Period>
```

Parameters(in query string):

* Asking Price: INT

* Down Payment: INT

* Payment schedule: STR

* Amortization Period: INT

*for constrain details, please consult [schema.py](../main/schema.py)*

Example:
```
GET http://127.0.0.1:5000/payment-amount/?amount=1000000&downPay=200000&schedule=monthly&period=20
```

Return:

* Payment amount per scheduled payment in JSON format


---
## **GET /mortgage-amount**


Get the maximum mortgage amount (principal)

```
GET http://127.0.0.1:5000/payment-amount/?payment=<Payment amount>&schedule=<Payment schedule>&period=<Amortization Period>
```

Parameters(in query string):

* Payment amount: INT

* Payment schedule: STR

* Amortization Period: INT

*for constrain details, please consult [schema.py](../main/schema.py)*

Example:
```
GET http://127.0.0.1:5000/payment-amount/?payment=2000&schedule=weekly&period=10
```

Return:

* Maximum Mortgage that can be taken out in JSON format

---
## **PATCH /interest-rate**


Change the interest rate used by the application

```
PATCH http://127.0.0.1:5000/interest-rate/
```

Parameters(in request body):
* Interest Rate: FLOAT

*for constrain details, please consult [schema.py](../main/schema.py)*

``` json
{
    "interest_rate": 0.015
}
```

Return:

* message indicating the old and new interest rate in JSON format

``` json
{
    "anual interest-rate": [
        {
            "old": "2.5%"
        },
        {
            "new": "1.5%"
        }
    ]
}
```

---
Please feel free to contact me at *tong@uvic.ca* if you have any question.
