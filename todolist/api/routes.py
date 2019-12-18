from . import api
from .controllers import TaskController, UserController

api.add_resource(UserController, "/users/", "/users/<id>/")