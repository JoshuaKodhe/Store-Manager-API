import unittest
from flask import json
from app import create_app

BASE_URL = '/api/v1/products'


class TestProductsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_post_product_method(self):
        product_item = {"name": "Chair",
                        "description": "The product description here",
                        "quantity": 12,
                        "category": "Furniture",
                        "price": 2000}

        response = self.client().post(BASE_URL,
                                      data=json.dumps(product_item),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
