from flask_restful import Api
from flask_dance.contrib.github import github

from . import auth_bp

from ..api.models import User
from .. import db

auth = Api(auth_bp)

from flask import redirect, url_for
@auth_bp.route("/provider/github/authorized/")
def callback():
    return redirect(url_for("web_bp.home"))
