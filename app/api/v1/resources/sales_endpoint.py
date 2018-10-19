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

    def get(self, saleId):
        """ Get a single sale_record"""
        sale_record = SaleRecordModel.retrieve_single_records(self, saleId)
        return sale_record


class SalesRecordsListEndpoint(Resource):
    def get(self):
        pass
