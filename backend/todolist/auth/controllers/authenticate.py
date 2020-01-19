import jwt
import datetime
import os
import requests

from flask import jsonify, request, make_response
from flask_restful import Resource
from sqlalchemy.orm.exc import NoResultFound

from ...api.controllers import format_response
from ..models import OAuthClient, OAuthToken
from ...api.models import User
from ... import db

class Authenticate(Resource):
    """ Validates user trough one the OAuth Providers, register, and generate access token """
    
    def post(self, handle):
        # Get provider authorization code
        auth_code = request.form.get("auth_code")
        if(not auth_code):
            return format_response("missing authorization code", 400)

        # Get request state
        auth_state = request.form.get("auth_state")
        if(not auth_state):
            return format_response("missing request state", 400)

        # Retrieve provider client data from db
        oauth_client = OAuthClient.query.filter(OAuthClient.handle == handle).first()
        if(not oauth_client):
            return format_response("client not found", 404)

        token_response = requests.post(
            "https://github.com/login/oauth/access_token",
            data = {
                "client_id": oauth_client.id,
                "client_secret": oauth_client.secret,
                "code": auth_code,
                "state": auth_state
            },
            headers = {
                "Accept": "application/json"
            }
        ).json()

        if(not token_response):
            return format_response("platform connection error", 500)

        error = token_response.get("error_description")
        if(error):
            return format_response(error, 400)

        token = token_response.get("access_token")
        schema = token_response.get("token_type")

        email_response = requests.get(
            "https://api.github.com/user/emails",
            headers={"Authorization": schema + token},
        )

        error = email_response.get("error_description")
        if(error):
            return format_response(error, 400)

        # Try to retrieve primary email from github
        try:
            email = [email.get("email") for email in email_response if email.get("primary") == True][0]
        except IndexError:
            return format_response("not email set with oauth provider", 500)
        except Exception:
            return format_response("unknow error", 500)

        # Try to recover user using the email
        try:
            user = User.query.filter(User.email == email).first()
        except NoResultFound:
            user = User(email)
            db.session.add(user)
        except Exception:
            return format_response("unknow error", 500)

        # If token found, update information, create a new one otherwise
        try:
            oauth_token = OAuthToken.query.filter(OAuthToken.user_id == user.id)
            oauth_token.provider = handle
            oauth_token.token = token
        except NoResultFound:
            oauth_token = OAuthToken(handle, token, user.id)
            db.session.add(oauth_token)
        except Exception:
            return format_response("unknow error", 500)

        db.session.commit()

        # API access Token payload
        jwt_payload = {
            "uid": str(user.id),
            "eml": user.email,
            "adm": user.admin,
            "uct": str(user.created),
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        }

        # Generate token
        jwt_token = jwt.encode(jwt_payload, os.environ["SECRET_KEY"], algorithm="HS256").decode("utf-8")
        jwt_token = "Bearer {}".format(token)

        return make_response(
            jsonify({
                "token": jwt_token
            }), 
            200
        )
        
        