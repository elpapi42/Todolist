from flask_restful import Api
from flask_dance.contrib.github import github

from . import auth_bp
from .controllers import GithubLogin

from ..api.models import User
from .. import db

auth = Api(auth_bp)

auth.add_resource(GithubLogin, "/github/")