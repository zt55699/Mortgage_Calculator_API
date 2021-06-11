import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

try:
    import unittest
    from app import app
    

except Exception as e:
    print("Modules are Missing {} ".format(e))


class test_basic(unittest.TestCase):

    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        code = response.status_code
        self.assertEqual(code, 200)

    # Check if return type is application/json
    def test_type(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "application/json")

    # Check response content corectness 
    def test_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b"Welcome to Mortgage Calculator API v0.1" in response.data)


if __name__ == "__main__":
    unittest.main()