from flask import make_response, jsonify

from .. import db
from ..models import User

def format_response(message, status, message_type="error"):
    """ 
    Format error responses from the API 

    Useful for seek api responses uniformity and saves boilerplate writing the controllers

    """
    return make_response(
        jsonify({message_type: message}),
        status
    )

from .user import UserController


    