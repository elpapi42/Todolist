import uuid
import datetime
import os
import jwt

import click

from . import cli_bp

@cli_bp.cli.command("generate-admin-token")
def generate_admin_token():

    jwt_payload = {
        "uid": str(uuid.uuid4()),
        "eml": "test@test.com",
        "adm": True,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    token = jwt.encode(jwt_payload, os.environ["SECRET_KEY"], algorithm="HS256").decode("utf-8")

    print("Bearer {}".format(token))