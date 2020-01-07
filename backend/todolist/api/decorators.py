import functools
import jwt
import os

from flask import request

from .controllers import format_response

def token_required(func):
    @functools.wraps(func)
    def wrapper_token_required(*args, **kwargs):
        # Retrieves token and checks integrity
        scheme, token = request.headers.get("Authorization").split(sep=" ")
        if(not token):
            return format_response("missing token", 401)
        if(scheme != "Bearer"):
            return format_response("unsupported auth scheme", 400)

        # Try to Decode token
        try:
            payload = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return format_response("token expired", 403)
        except jwt.DecodeError:
            return format_response("invalid token", 401)

        token_data = {
            "id": payload.get("uid"),
            "is_admin": payload.get("adm")
        }

        value = func(token_data=token_data, *args, **kwargs)
        return value
    return wrapper_token_required

def admin_required(func):
    @functools.wraps(func)
    def wrapper_admin_required(*args, **kwargs):
        # Retrieves token and checks integrity
        scheme, token = request.headers.get("Authorization").split(sep=" ")
        if(not token):
            return format_response("missing token", 401)
        if(scheme != "Bearer"):
            return format_response("unsupported auth scheme", 400)

        # Try to Decode token
        try:
            payload = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return format_response("token expired", 403)
        except jwt.DecodeError:
            return format_response("invalid token", 401)
        
        # Check for admin permissions, if required but not present, return error
        if(payload.get("adm") == False):
            return format_response("unathorized token", 401)

        value = func(*args, **kwargs)
        return value
    return wrapper_admin_required