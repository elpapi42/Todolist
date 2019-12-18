from flask import Blueprint, current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

api_bp = Blueprint("api_bp", __name__)
api = Api(api_bp)

db = SQLAlchemy()

from . import routes