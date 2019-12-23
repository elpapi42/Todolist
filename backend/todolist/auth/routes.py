from flask_restful import Api

from . import auth_bp
from .controllers import GithubLogin

auth = Api(auth_bp)

auth.add_resource(GithubLogin, "/login/github/")