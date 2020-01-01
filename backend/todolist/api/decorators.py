import functools
import jwt
import os

from flask import request

from .controllers import format_response

def auth_token_required(func):
    @functools.wraps(func)
    def wrapper_auth_token_required(*args, **kwargs):
        # Retrieves token and checks integrity
        token = request.headers.get("Authorization")
        if(not token):
            return format_response("missing token", 400)

        # Try to Decode token
        try:
            payload = jwt.decode(token, os.environ["SECRET_KEY"])
        except jwt.ExpiredSignatureError:
            return format_response("token expired", 403)
        except jwt.DecodeError:
            return format_response("invalid token", 400)

        value = func(*args, **kwargs)
        return value
    return wrapper_auth_token_required