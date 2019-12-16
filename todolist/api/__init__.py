from flask import Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api_bp = Blueprint("api_bp", __name__)
api = Api(api_bp)

from . import routes