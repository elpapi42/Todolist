from validator_collection.checkers import is_email
from flask import request, make_response, jsonify, g
from flask_restful import Resource

from ... import db
from ..models import User
from ...auth.models import OAuth
from . import format_response
from ..decorators import token_required, admin_required, authorization_required

class UserController(Resource):
    """ Interact with Users DataBase Entries """

    method_decorators = [authorization_required, token_required]

    def get(self, *args, **kwargs):
        user = g.user

        return make_response(
            jsonify({
                "id": user.id,
                "admin": user.admin,
                "email": user.email
            }), 
            200
        )

    def put(self, *args, **kwargs):
        return format_response("PUT will be implemented when the user get some data like username or biography", 501)

        user = g.user

        # If user is admin, cant be edited by other admin, but by himslef
        if(user.is_admin and (user.id != token_data.get("id"))):
            return format_response("non authorized", 403)

        # Edit user data from here

        # Commit changes to the database
        db.session.commit()

        # Return the lasts state of the user entry
        return make_response(
            jsonify({
                "id": user.id,
                "email": user.email
            }), 
            200
        )

    def delete(self, *args, **kwargs):
        # Tries to retreive user by id
        user = g.user

        # If user is admin, cant be deleted by other admin, but by himslef
        if(user.admin and (user.id != token_data.get("id"))):
            return format_response("non authorized", 403)

        # Try to retrieve oauth_token related to the user
        oauth_token = user.oauth
        if(not oauth_token):
            return format_response("database integrity error", 500)

        db.session.delete(oauth_token)
        db.session.delete(user)
        db.session.commit()

        return make_response("user deleted", 204)
        
class UserList(Resource):
    """ Get users and create new user """

    method_decorators = [admin_required, token_required]

    def get(self):
        # Retrieve all the users. 
        # WARNING: This must implement pagination in the future!
        users = User.query.all()

        users_list = []

        for user in users:
            # Create dictionary
            user_data = {
                "id": user.id,
                "email": user.email,
                "admin": user.admin
            }

            # Append user to the output dictionary
            users_list.append(user_data)

        return make_response(
            jsonify(users_list),
            200
        )

