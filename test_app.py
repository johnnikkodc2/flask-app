# File: tests/test_app.py
from app import app
import unittest

class FlaskTest(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
