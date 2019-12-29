import uuid

from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import login_user
from sqlalchemy.orm.exc import NoResultFound

from . import github_bp
from .. import login_manager
from .. import db
from ..api.models import User

@oauth_authorized.connect_via(github_bp)
def github_logged_in(blueprint, token):
    if not token:
        return False

    resp = blueprint.session.get("/user")
    if not resp.ok:
        return False

    github_info = resp.json()

    query = db.session.query(User).filter(User.email == github_info["email"])

    # If user does not exists, create record using email
    try:
        user = query.one()
    except NoResultFound:
        user = User(github_info["email"])
        db.session.add(user)
        db.session.commit()
        
    login_user(user)

@login_manager.user_loader
def user_loader(id):
    return db.session.query(User).filter(User.id == id).first()

@oauth_error.connect
def error(error):
    raise Exception()
    return error
    