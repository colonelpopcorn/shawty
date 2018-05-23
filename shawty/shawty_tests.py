import os
import database
import unittest
import json

from shawty import app

class ShawtyUnitTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        database.database_build()
    
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        assert b'<div id="app"></div>' in response.data

    def test_login_route(self):
        response = self.app.post('/api/login', data=json.dumps(dict(uname="bob", passwd="bobsupersecret")), content_type='application/json')
        self.assertEqual(response.get_json().get("status"), 200)
        self.assertIn("Logged in!", response.get_json().get("msg"))
    
    def test_login_route_with_nonexistent_user(self):
        response = self.app.post('/api/login', data=json.dumps(dict(uname="alice", passwd="alicesupersecret")), content_type='application/json')
        self.assertEqual(response.get_json().get("status"), 404)
    
    def test_redirect_route_with_nonexistent_url(self):
        response = self.app.get('/some_hash', follow_redirects=True)
        self.assertEqual(response.get_json().get("status"), 404)
        self.assertIn("url not found!", response.get_json().get("msg"))
    
    def test_redirect_route_with_existing_url(self):
        response = self.app.get('/some_other_hash')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "https://google.com")
    
    def test_registration_route(self):
        response = self.app.post('/api/register', data=json.dumps(dict(uname="jerry", passwd="jerrysupersecret")), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("jerry", response.get_json().get("msg"))

if __name__ == "__main__":
    unittest.main()