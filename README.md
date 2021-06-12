# Mortgage_Calculator_API
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
![Safe](https://img.shields.io/badge/Stay-Safe-red?logo=data:image/svg%2bxml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEwIDUxMCIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCA1MTAgNTEwIiB3aWR0aD0iNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnPjxnPjxwYXRoIGQ9Im0xNzQuNjEgMzAwYy0yMC41OCAwLTQwLjU2IDYuOTUtNTYuNjkgMTkuNzJsLTExMC4wOSA4NS43OTd2MTA0LjQ4M2g1My41MjlsNzYuNDcxLTY1aDEyNi44MnYtMTQ1eiIgZmlsbD0iI2ZmZGRjZSIvPjwvZz48cGF0aCBkPSJtNTAyLjE3IDI4NC43MmMwIDguOTUtMy42IDE3Ljg5LTEwLjc4IDI0LjQ2bC0xNDguNTYgMTM1LjgyaC03OC4xOHYtODVoNjguMThsMTE0LjM0LTEwMC4yMWMxMi44Mi0xMS4yMyAzMi4wNi0xMC45MiA0NC41LjczIDcgNi41NSAxMC41IDE1LjM4IDEwLjUgMjQuMnoiIGZpbGw9IiNmZmNjYmQiLz48cGF0aCBkPSJtMzMyLjgzIDM0OS42M3YxMC4zN2gtNjguMTh2LTYwaDE4LjU1YzI3LjQxIDAgNDkuNjMgMjIuMjIgNDkuNjMgNDkuNjN6IiBmaWxsPSIjZmZjY2JkIi8+PHBhdGggZD0ibTM5OS44IDc3LjN2OC4wMWMwIDIwLjY1LTguMDQgNDAuMDctMjIuNjQgNTQuNjdsLTExMi41MSAxMTIuNTF2LTIyNi42NmwzLjE4LTMuMTljMTQuNi0xNC42IDM0LjAyLTIyLjY0IDU0LjY3LTIyLjY0IDQyLjYyIDAgNzcuMyAzNC42OCA3Ny4zIDc3LjN6IiBmaWxsPSIjZDAwMDUwIi8+PHBhdGggZD0ibTI2NC42NSAyNS44M3YyMjYuNjZsLTExMi41MS0xMTIuNTFjLTE0LjYtMTQuNi0yMi42NC0zNC4wMi0yMi42NC01NC42N3YtOC4wMWMwLTQyLjYyIDM0LjY4LTc3LjMgNzcuMy03Ny4zIDIwLjY1IDAgNDAuMDYgOC4wNCA1NC42NiAyMi42NHoiIGZpbGw9IiNmZjRhNGEiLz48cGF0aCBkPSJtMjEyLjgzIDM2MC4xMnYzMGg1MS44MnYtMzB6IiBmaWxsPSIjZmZjY2JkIi8+PHBhdGggZD0ibTI2NC42NSAzNjAuMTJ2MzBoMzYuMTRsMzIuMDQtMzB6IiBmaWxsPSIjZmZiZGE5Ii8+PC9nPjwvc3ZnPg==)
![codecov.io Code Coverage](https://img.shields.io/badge/coverage-91%25-brightgreen)


A Flask-restful backend API of a mortgage calculator<br><br>

# Requirements Installation

For local debugging, there are several components to install.<br>
For the the python packages install through pip using the command:

```bash
sudo pip3 install -r requirements.txt
```

The text file contains the necessary packages.<br><br>


```bash
python3 app.py
```
Start a local server at port:5000 using the command above. <br><br>



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

``` json
{
    "payment-amount": 4239
}
```


---
## **GET /mortgage-amount**


Get the maximum mortgage amount (principal)

```
GET http://127.0.0.1:5000/mortgage-amount/?payment=<Payment amount>&schedule=<Payment schedule>&period=<Amortization Period>
```

Parameters(in query string):

* Payment amount: INT

* Payment schedule: STR

* Amortization Period: INT

*for constrain details, please consult [schema.py](../main/schema.py)*

Example:
```
GET http://127.0.0.1:5000/mortgage-amount/?payment=1550&schedule=biweekly&period=10
```

Return:

* Maximum Mortgage that can be taken out in JSON format

``` json
{
    "mortgage-amount": 357747
}
```

---
## **PATCH /interest-rate**


Change the interest rate used by the application

```
PATCH http://127.0.0.1:5000/interest-rate/
```

Parameters(json in request body):
``` json
{
    "interest_rate": 0.015
}
```
* Interest Rate: FLOAT

*for constrain details, please consult [schema.py](../main/schema.py)*

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
## **Unittesting**

change to */tests* directory, then run
```
python3 run_allTests.py
```
Coverage:

| Name               | Stmts | Miss | Cover | Missing   |
|--------------------|-------|------|-------|-----------|
|                    |       |      |       |           |
| test_basic.py      | 25    | 3    | 88%   | 11-12, 38 |
| test_calculator.py | 32    | 3    | 91%   | 12-13, 59 |
| test_getPayment.py | 44    | 3    | 93%   | 13-14, 81 |
|                    |       |      |       |           |
| TOTAL              | 101   | 9    | 91%   |           |



---
Please feel free to contact me at *tong@uvic.ca* if you have any question.
