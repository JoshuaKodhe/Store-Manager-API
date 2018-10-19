import unittest
from flask import json
from app import create_app


BASE_URL = '/api/v1/sales'
SINGLE_PROD_URL = '/api/v1/sales/{}'


class TestSalesEndpoints(unittest.TestCase):
    """class to test the sales endpoints"""
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.sale_record = {"sale_attendant": "Kay Jay",
                            "unit_price": 2000,
                            "product_quantity": 2,
                            "category": "Furniture",
                            "total_price": 2000*2,
                            }

    def test_post_single_sale_record(self):
        """ Testing post a sale record """
        response = self.client().post(BASE_URL,
                                      data=json.dumps(self.sale_record),
                                      content_type="application/json")

        self.assertEqual(response.status_code, 201)
