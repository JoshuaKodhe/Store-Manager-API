from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from app.api.v1.models.products_model import Product


class ProductEndpoint(Resource):
    @jwt_required
    def post(self):
        data = request.get_json()

        name = data['name']
        description = data['description']
        quantity = data['quantity']
        category = data['category']

        new_product = Product(name, description, quantity, category)
        added_product = new_product.save_product()

        return {"Product": added_product}, 201

    @jwt_required
    def get(self, productId):
        single_product = Product.retrieve_single_products(self, productId)
        return single_product


class ProductListEndpoint(Resource):
    @jwt_required
    def get(self):
        all_products = Product.retrieve_products(self)
        return {"Products": all_products}
