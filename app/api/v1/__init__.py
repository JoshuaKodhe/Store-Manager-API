""" Register Blueprints and our routes """
from flask import Blueprint
from flask_restful import Api


VERSION_1 = Blueprint('API', __name__, url_prefix="/api/v1")
API = Api(VERSION_1)
