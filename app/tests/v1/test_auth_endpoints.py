import unittest
from flask import json
from app import create_app

REGISTER_URL = '/api/v1/register'
LOGIN_URL = 'api/v1/login'


class TestAuthEndPoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.register_user = {"email": "testuser@gmail.com",
                              "password": "asdfg",
                              }
        self.login_user = {"email": "testuser@gmail.com",
                           "password": "asdfg",
                           }

    def test_registration(self):
        response = self.client.post(REGISTER_URL,
                                    data=json.dumps(self.register_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.client.post(LOGIN_URL,
                                    data=json.dumps(self.login_user),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertTrue(data["access_token"])
        self.assertLessEqual(response.status_code, 200)
