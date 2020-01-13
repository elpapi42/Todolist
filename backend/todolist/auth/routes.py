from flask_restful import Api

from . import auth_bp
from .controllers import Authenticate

auth = Api(auth_bp)

auth.add_resource(Authenticate, "/<handle>/")