from flask import make_response, jsonify

def format_response(message, status, message_type="message"):
    """ 
    Format error responses from the API 

    Useful for seek api responses uniformity and saves boilerplate writing the controllers

    """
    return make_response(
        jsonify({message_type: message}),
        status
    )

from .user import UserController, UserList


    