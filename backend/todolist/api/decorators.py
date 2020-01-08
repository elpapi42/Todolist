import functools
import jwt
import os

from validator_collection.checkers import is_uuid
from flask import request, g

from .controllers import format_response

def token_required(func):
    """ Check if the client has the required token for access the api """
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

        g.token_data = token_data

        value = func(*args, **kwargs)
        return value
    return wrapper_token_required

def admin_required(func):
    """ Check if the client has the required admin token for access the api """
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

        token_data = {
            "id": payload.get("uid"),
            "is_admin": payload.get("adm")
        }

        g.token_data = token_data

        value = func(*args, **kwargs)
        return value
    return wrapper_admin_required

def authorization_required(func):
    """ Check if the user has authorization for perform the requested action """
    @functools.wraps(func)
    def wrapper_authorization_required(*args, **kwargs):
        # Retrieves id and checks integrity
        id = request.view_args.get("u_id")

        # If there is no id, but "current" at the url, 
        # set id to the id of the user associated with the auth token provided to the api call
        if(id == "current"):
            id = g.token_data.get("id")

        # Check if supplied id complains with UUID standards, or "current" url self-identifier
        if(not is_uuid(id)):
            return format_response("invalid id", 422)

        # If the token is not owned by an admin, and the url id dont match with the id of the supplied token owner
        # Cancel the operation because a user can only make ops on his data
        if((id != g.token_data.get("id")) and (not g.token_data.get("is_admin"))):
            return format_response("non authorized", 403)

        value = func(user_id=id, *args, **kwargs)
        return value
    return wrapper_authorization_required

def task_data_required(func):
    """ Check if the request has the required data for create or edit a task """
    @functools.wraps(func)
    def wrapper_task_data_required(*args, **kwargs):
        # Retrieves data from body
        title = request.form.get("title")
        description = request.form.get("description")
        is_done = request.form.get("is_done") in ["True", "true", "1"]

        task_data = {
            "title": title,
            "description": description,
            "is_done": is_done
        }

        value = func(task_data=task_data, *args, **kwargs)
        return value
    return wrapper_task_data_required




