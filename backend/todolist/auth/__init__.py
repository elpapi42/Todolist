from flask import Blueprint

from .models import OAuth
from .. import db

auth_bp = Blueprint("auth_bp", __name__)

from . import routes