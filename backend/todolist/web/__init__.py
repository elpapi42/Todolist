from flask import Blueprint
from flask_restful import Api

web_bp = Blueprint("web_bp", __name__)
web = Api(web_bp)

from . import routes