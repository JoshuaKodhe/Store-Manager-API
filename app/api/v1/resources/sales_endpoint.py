from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from app.api.v1.models.sales_models import SaleRecordModel


class SalesRecordEndpoint(Resource):
    @jwt_required
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

    @jwt_required
    def get(self, saleId):
        """ Get a single sale_record"""
        sale_record = SaleRecordModel.retrieve_single_records(self, saleId)
        return sale_record


class SalesRecordsListEndpoint(Resource):
    @jwt_required
    def get(self):
        sale_records = SaleRecordModel.retrieve_records(self)
        return {"sale_records": sale_records}
