import uuid
import datetime
import os
import click
from validator_collection import is_email

from . import cli_bp
from .. import db
from ..api.models import User

@cli_bp.cli.command("admin")
@click.argument("email")
def make_user_admin(email):

    admins = User.query.filter(User.admin == True).all()
    if(len(admins) > 0):
        print("admins already registered, contact one for request admin permissions")
        return False

    if(not is_email(email)):
        print("invalid email")
        return False

    user = User.query.filter(User.email == email).first()
    if(not user):
        print("email not registered")
        return False

    user.admin = True
    db.session.commit()
    print("now {} has admin permissions".format(email))

    return True


    
    