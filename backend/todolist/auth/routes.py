from flask_restful import Api

from . import auth_bp
from .controllers import GithubLogin

from ..api.models import User
from .. import db

auth = Api(auth_bp)

auth.add_resource(GithubLogin, "/github/login/")

@auth_bp.route("/github/login/callback/")
def callback():
    user = db.session.query(User).filter(User.email == "whitman-2@hotmail.com").first()
    return str(user.repr())