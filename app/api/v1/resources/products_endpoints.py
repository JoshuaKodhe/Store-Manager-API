from flask_restful import Resource
from flask import request

from app.api.v1.models.products_model import Product


class ProductEndpoint(Resource):
    def post(self):
        data = request.get_json()

        name = data['name']
        description = data['description']
        quantity = data['quantity']
        category = data['category']

        new_product = Product(name, description, quantity, category)
        added_product = new_product.save_product()

        return {"Product": added_product}, 201


class ProductListEndpoint(Resource):
    def get(self):
        all_products = Product.retrieve_products(self)
        return {"Products": all_products}
