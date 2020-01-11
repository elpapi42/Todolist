import uuid
import datetime
import os
import jwt

import click
from validator_collection import is_email

from . import cli_bp
from .. import db
from ..api.models import User

@cli_bp.cli.command("admin")
@click.argument("email")
def make_user_admin(email):

    if(not is_email(email)):
        print("Invalid Email")
        return False

    user = User.query.filter(User.email == email).first()
    if(not user):
        print("Email Not Registered")
        return False

    user.is_admin = True
    db.session.commit()
    print("Now {} has Admin Access".format(email))
    
    return True
    
    