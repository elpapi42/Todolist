import uuid

from flask_dance.consumer import oauth_authorized
from flask_login import login_user

from . import github_bp
from .. import login_manager
from .. import db
from ..api.models import User

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

    oauth = None
    
    # If there is not ouath entry related to the retrieved user, create a new one
    try:
        oauth = db.session.query(OAuth).filter(OAuth.user_id == user.id).first()
        oauth.provider = blueprint.name
        oauth.token = token
    except:
        oauth = OAuth(provider=blueprint.name, token=token, user_id=user.id, user=user)
        db.session.add(oauth)
   
    db.session.commit()
    login_user(user)
    flash("Successfully signed in with GitHub.")
    
    return False

@login_manager.user_loader
def user_loader(id):
    user = db.session.query(User).filter(User.id == id).first()
    return user
    