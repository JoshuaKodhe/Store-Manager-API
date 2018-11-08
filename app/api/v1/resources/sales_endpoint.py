from flask_restful import Resource
from flask import request

from app.api.v1.models.sales_models import SaleRecordModel


class SalesRecordEndpoint(Resource):
    def post(self):
        """ Post a sale_record """
        data = request.get_json()

        attendant = data["sale_attendant"]
        name = data["product_name"]
        price = data["unit_price"]
        quantity = data["product_quantity"]
        category = data["category"]

        new_sale_record = SaleRecordModel(attendant,
                                          name,
                                          price,
                                          quantity,
                                          category)
        added_sale_record = new_sale_record.save_record()

        return {"sale record": added_sale_record}, 201

    def get(self):
        pass


class SalesRecordsListEndpoint(Resource):
    def get(self):
        pass
