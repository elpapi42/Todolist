from flask import Blueprint, url_for
from flask_dance.contrib.github import make_github_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized

from .models import OAuth
from ..api.models import User
from .. import db

auth_bp = Blueprint("auth_bp", __name__)
github_bp = make_github_blueprint(redirect_url="/login/github/callback/", storage=SQLAlchemyStorage(OAuth, db.session))

@oauth_authorized.connect_via(github_bp)
def github_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with GitHub.", category="error")
        return False

    resp = blueprint.session.get("/user")
    if not resp.ok:
        msg = "Failed to fetch user info from GitHub."
        flash(msg, category="error")
        return False

    github_info = resp.json()

    user = db.session.query(User).filter(User.email == github_info["email"]).first()

    # If user does not exists, create record using email
    if(not user):
        user = User(github_info["email"])
        db.session.add(user)
        db.session.commit()

    oauth = db.session.query(OAuth).filter(OAuth.user_id == user.id).first()

    # If there is not ouath entry related to the retrieved user, create a new one
    if(not oauth):
        oauth = OAuth(provider=blueprint.name, token=token, user_id=user.id, user=user)
        db.session.add(oauth)
        db.session.commit()
    # If exists, update provider and token
    else:
        oauth.provider = blueprint.name
        oauth.token = token
        db.session.commit()
    
    return False

from . import routes