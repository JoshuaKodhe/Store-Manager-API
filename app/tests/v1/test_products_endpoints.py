import unittest
from flask import json
from app import create_app

BASE_URL = '/api/v1/products'
SINGLE_PROD_URL = '/api/v1/products/{}'
LOGIN_URL = '/api/v1/login'


class TestProductsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.product_item = {"name": "Chair",
                             "description": "The product description here",
                             "quantity": 12,
                             "category": "Furniture",
                             "price": 2000}

        self.login_user = {"email": "testuser@gmail.com",
                           "password": "asdfg",
                           }

    def login(self):
        response = self.client().post(LOGIN_URL,
                                      data=json.dumps(self.login_user),
                                      content_type='application/json')
        access_token = json.loads(response.get_data())["access_token"]
        return access_token

    def test_post_product_method(self):
        """ Test for posting a single product """
        response = self.client().post(BASE_URL,
                                      data=json.dumps(self.product_item),
                                      headers=dict(Authorization="Bearer "+self.login()),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_products_method(self):
        """ Test for getting all products """
        get_all_products = self.client().get(BASE_URL,
                                             headers=dict(Authorization="Bearer "+self.login()),
                                             content_type='application/json')
        self.assertEqual(get_all_products.status_code, 200)

    def test_get_single_product(self):
        """ Test for getting a single product """
        response = self.client().post(BASE_URL,
                                      data=json.dumps(self.product_item),
                                      headers=dict(Authorization="Bearer "+self.login()),
                                      content_type='application/json')

        data = json.loads(response.get_data())
        print(data)
        single_product = self.client().get(SINGLE_PROD_URL.format(data['Product']['product_id']),
                                           headers=dict(Authorization="Bearer "+self.login()),
                                           content_type='application/json')
        self.assertEqual(single_product.status_code, 200)
