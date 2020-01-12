import click

from ..auth.models import OAuthClient
from .. import db
from . import client_bp

@client_bp.cli.command("add")
@click.argument("handle")
@click.argument("id")
@click.argument("secret")
def add_oauth_client(handle, id, secret):

    oauth_client = OAuthClient.query.filter(OAuthClient.client_handle == handle).first()
    if(oauth_client):
        print("client already registered")
        return False

    oauth_client = OAuthClient(id, secret, handle)

    db.session.add(oauth_client)
    db.session.commit()

    print("{} client registered".format(handle))

    return True

@client_bp.cli.command("remove")
@click.argument("handle")
def add_oauth_client(handle):

    oauth_client = OAuthClient.query.filter(OAuthClient.client_handle == handle).first()
    if(not oauth_client):
        print("client not found")
        return False

    db.session.delete(oauth_client)
    db.session.commit()

    print("{} client removed".format(handle))

    return True