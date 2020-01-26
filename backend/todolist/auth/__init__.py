from flask import Blueprint

from .. import db

auth_bp = Blueprint("auth_bp", __name__)

from . import routes