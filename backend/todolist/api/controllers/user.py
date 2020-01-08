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

    def get(self, user_id, *args, **kwargs):
        # Tries to retreive user by id
        user = User.query.filter(User.id == user_id).first()
        if(not user):
            return format_response("not found", 404)

        return make_response(
            jsonify({
                "id": user.id,
                "email": user.email
            }), 
            200
        )

    def put(self, user_id, *args, **kwargs):
        return format_response("PUT will be implemented when the user get some data like username or biography", 501)

        # Tries to retreive user by id
        user = db.session.query(User).filter(User.id == user_id).first()
        if(not user):
            return format_response("not found", 404)

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

    def delete(self, user_id, *args, **kwargs):
        # Tries to retreive user by id
        user = db.session.query(User).filter(User.id == user_id).first()
        if(not user):
            return format_response("not found", 404)

        # If user is admin, cant be deleted by other admin, but by himslef
        if(user.is_admin and (user.id != token_data.get("id"))):
            return format_response("non authorized", 403)

        # Try to retrieve oauth_token related to the user
        oauth_token = OAuth.query.filter(OAuth.user_id == user_id).first()
        if(not oauth_token):
            return format_response("database integrity error", 500)

        db.session.delete(oauth_token)
        db.session.delete(user)
        db.session.commit()

        return make_response("user deleted", 204)
        
class UserList(Resource):
    """ Get users and create new user """

    method_decorators = [admin_required]

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
                "is_admin": user.is_admin
            }

            # Append user to the output dictionary
            users_list.append(user_data)

        return make_response(
            jsonify(users_list),
            200
        )

    def post(self):
        # Retrieve email from request body
        email = request.form.get("email")
        if(not email):
            return format_response("email not supplied", 400)

        # Check email is valid
        if(not is_email(email)):
            return format_response("invalid email", 422)

        # Checks if email is already registered by another user on the Database
        db_user = User.query.filter(User.email == email).first()
        if(db_user):
            return format_response("email already registered", 403)
        
        # Register new user
        user = User(email)
        db.session.add(user)
        db.session.commit()

        return make_response(
            jsonify({
                "id": user.id,
                "email": user.email
            }), 
            201
        )

