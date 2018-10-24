from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from app.api.v1.models.products_model import Product
from app.validators.input_validators import InputValidator


class ProductEndpoint(Resource):
    def post(self):
        data = request.get_json()

        name = InputValidator.valid_string(data['name'].strip())
        description = InputValidator.valid_string(data['description'].strip())
        category = InputValidator.valid_string(data['category'].strip())
        quantity = InputValidator.valid_number(data['quantity'])
        unit_price = InputValidator.valid_number((data['unit price']))

        if Product.retrieve_single_products_by_name(self, name):
            return{"message": f"Product {name} exists"}, 400

        if (name) and description and category and(quantity)and(unit_price):
            new_product = Product(name, description, quantity, unit_price, category)
            added_product = new_product.save_product()
            return {"product": added_product}, 201
        return {"message": "Ensure all the fields are correctly entered"}, 400


    def get(self, productId):
        single_product = Product.retrieve_single_products(self, productId)
        if single_product:
            return {"product": single_product}, 200
        return {"message": f"Product of ID {productId} does not exist"}, 404


class ProductListEndpoint(Resource):

    def get(self):
        all_products = Product.retrieve_products(self)
        return {"Products": all_products,
                "message": "Request succeful"
                }
