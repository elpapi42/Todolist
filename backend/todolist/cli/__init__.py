from flask import Blueprint

cli_bp = Blueprint("cli_bp", __name__, cli_group=None)
client_bp = Blueprint("client_bp", __name__, cli_group="client")

from . import commands, client