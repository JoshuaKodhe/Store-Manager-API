""" Register Blueprints and our routes """
from flask import Blueprint
from flask_restful import Api


from app.api.v1.resources.products_endpoints import (ProductEndpoint,
                                                     ProductListEndpoint)

from app.api.v1.resources.sales_endpoint import SalesRecordEndpoint

VERSION_1 = Blueprint('API', __name__, url_prefix="/api/v1")
API = Api(VERSION_1)

API.add_resource(ProductListEndpoint, '/products')
API.add_resource(ProductEndpoint, '/products', '/products/<int:productId>')

API.add_resource(SalesRecordEndpoint, '/sales', '/sales/<int:saleId>')
