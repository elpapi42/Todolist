import uuid
import datetime
import os
import jwt

import click
from validator_collection import is_email

from . import cli_bp
from .. import db
from ..api.models import User
from ..auth.models import OAuthClient

@cli_bp.cli.command("admin")
@click.argument("email")
def make_user_admin(email):

    admins = User.query.filter(User.admin == True).all()
    if(len(admins) > 0):
        print("Admins Already Registered, Contact Them for Get Admin Permissions")
        return False

    if(not is_email(email)):
        print("Invalid Email")
        return False

    user = User.query.filter(User.email == email).first()
    if(not user):
        print("Email Not Registered")
        return False

    user.admin = True
    db.session.commit()
    print("Now {} has Admin Access".format(email))

    return True

@cli_bp.cli.command("client")
def add_oauth_client():

    client_handle = input("Client Handle: ")
    oauth_client = OAuthClient.query.filter(OAuthClient.client_handle == client_handle).first()
    if(oauth_client):
        print("OAuth Provider already registered")
        return False

    client_id = input("Client ID: ")
    if(client_id == ""):
        print("Invalid ID")
        return False

    client_secret = input("Client Secret: ")
    if(client_secret == ""):
        print("Invalid Secret")
        return False

    oauth_client = OAuthClient(client_id, client_secret, client_handle)

    db.session.add(oauth_client)
    db.session.commit()

    return True
    
    