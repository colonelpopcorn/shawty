import os
import unittest

from shawty import app

class FlaskrUnitTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'<div id="app"></div>' in response.data

if __name__ == "__main__":
    unittest.main()