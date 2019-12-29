import uuid

from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import login_user
from sqlalchemy.orm.exc import NoResultFound

from . import github_bp
from .. import login_manager
from .. import db
from ..api.models import User
from .models import OAuth

@oauth_authorized.connect_via(github_bp)
def github_logged_in(blueprint, token):
    if not token:
        return False

    resp = blueprint.session.get("/user")
    if not resp.ok:
        return False

    github_info = resp.json()

    # If user does not exists, create record using email
    try:
        user = db.session.query(User).filter(User.email == github_info["email"]).one()
    except NoResultFound:
        user = User(github_info["email"])
        db.session.add(user)

    # If oauth token does not exist, create a new one, and attach it to the recently created user
    try:
        oauth_token = db.session.query(OAuth).filter(OAuth.user_id == user.id).one()
    except NoResultFound:
        oauth_token = OAuth(blueprint.name, token, user.id, user)
        db.session.add(oauth_token)

    db.session.commit()
    login_user(user)
    return False

@login_manager.user_loader
def user_loader(id):
    return db.session.query(User).filter(User.id == id).first()
    