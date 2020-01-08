from flask_restful import Api

from . import api_bp
from .controllers import UserController, UserList, TaskList, TaskController

api = Api(api_bp)

api.add_resource(UserList, "/users/")
api.add_resource(UserController, "/users/<u_id>/")
api.add_resource(TaskList, "/users/<u_id>/tasks/")
api.add_resource(TaskController, "/users/<u_id>/tasks/<t_id>/")