import uuid
import datetime
import os
import jwt

import click

from . import cli_bp

@cli_bp.cli.command("blank-command")
def generate_admin_token():
    print("This does nothing")