import unittest
from flask import json
from app import create_app

BASE_URL = '/api/v1/products'


class TestProductsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.product_item = {"name": "Chair",
                             "description": "The product description here",
                             "quantity": 12,
                             "category": "Furniture",
                             "price": 2000}

    def test_post_product_method(self):
        response = self.client().post(BASE_URL,
                                      data=json.dumps(self.product_item),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_products_method(self):
        get_all_products = self.client().get(BASE_URL)
        self.assertEqual(get_all_products.status_code, 200)
