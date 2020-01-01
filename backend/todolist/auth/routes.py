from flask_restful import Api

from . import auth_bp
from .controllers import Logout, IssueToken

auth = Api(auth_bp)

auth.add_resource(Logout, "/logout/")
auth.add_resource(IssueToken, "/token/")