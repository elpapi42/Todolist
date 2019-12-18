from . import api
from .controllers import UserController

api.add_resource(UserController, "/users/", "/users/<id>/")