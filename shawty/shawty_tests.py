import os
import unittest
import json

from shawty import app

class FlaskrUnitTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'<div id="app"></div>' in response.data

    def test_login_route(self):
        response = self.app.post('/api/login', data=json.dumps(dict(uname="bob", passwd="bobsupersecret")), content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()