from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from app.api.v1.models.products_model import Product


parser = reqparse.RequestParser()
parser.add_argument('name', help='Enter product name', required=True, type=str)
parser.add_argument('description', help='Enter product description', required=True, type=str)
parser.add_argument('quantity', help='Enter product quantity as a number', required=True, type=int)
parser.add_argument('unit price', help='Enter product price as a number', required=True, type=int)
parser.add_argument('category', help='Enter product Category', required=True, type=str)


class ProductEndpoint(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()

        name = data['name'].strip()
        description = data['description'].strip()
        quantity = int(data['quantity'])
        unit_price = int(data['unit price'])
        category = data['category'].strip()

        if (name) and description and category and(quantity >= 1)and(unit_price >= 1):
            new_product = Product(name, description, quantity, unit_price, category)
            added_product = new_product.save_product()
            return {"product": added_product}, 201
        return {"message": "Ensure all the fields are correctly entered"}, 400

    @jwt_required
    def get(self, productId):
        single_product = Product.retrieve_single_products(self, productId)
        return single_product


class ProductListEndpoint(Resource):
    @jwt_required
    def get(self):
        all_products = Product.retrieve_products(self)
        return {"Products": all_products}, 200
