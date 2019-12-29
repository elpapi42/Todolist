from flask_restful import Api

from . import auth_bp

from ..api.models import User
from .. import db

auth = Api(auth_bp)