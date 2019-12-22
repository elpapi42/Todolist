from flask import Blueprint

from .. import db

api_bp = Blueprint("api_bp", __name__)

from . import routes