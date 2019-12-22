from flask_restful import Api

from . import api_bp
from .controllers import UserController

api = Api(api_bp)

api.add_resource(UserController, "/users/", "/users/<id>/")