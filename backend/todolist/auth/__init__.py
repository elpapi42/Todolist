from flask import Blueprint
from flask_dance.contrib.github import make_github_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_login import current_user

from .models import OAuth
from .. import db

auth_bp = Blueprint("auth_bp", __name__)
github_bp = make_github_blueprint(redirect_url="/login/github/callback/", storage=SQLAlchemyStorage(OAuth, db.session, user=current_user))

from . import routes