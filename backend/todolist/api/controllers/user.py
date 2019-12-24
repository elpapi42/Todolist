import uuid

from validator_collection.checkers import is_uuid, is_email
from flask import request, make_response, jsonify
from flask_restful import Resource

from ... import db
from ..models import User
from . import format_response

class UserController(Resource):
    """ Interact with Users DataBase Entries """

    def get(self, id=None):
        if(not id):
            return format_response("not implemented", 501)
        
        # Check if supplied id complains with UUID standards
        if(not is_uuid(id)):
            return format_response("invalid id", 422)

        # Tries to retreive user by id
        user = db.session.query(User).filter(User.id == id).first()
        if(not user):
            return format_response("not found", 404)

        return make_response(
            jsonify({
                "id": user.id,
                "email": user.email
            }), 
            200
        )

    def post(self, id=None):
        if(id):
            return format_response("post not allowed", 405) 

        # Retrieve email from request body
        email = request.form.get("email")
        if(not email):
            return format_response("email not supplied", 400)

        # Check email is valid
        if(not is_email(email)):
            return format_response("invalid email", 422)

        # Checks if email is already registered by another user on the Database
        db_user = db.session.query(User).filter(User.email == email).first()
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

    def put(self, id=None):
        if(not id):
            return format_response("put not allowed", 405)

        # Check if supplied id complains with UUID standards
        if(not is_uuid(id)):
            return format_response("invalid id", 422)

        # Tries to retreive user by id
        user = db.session.query(User).filter(User.id == id).first()
        if(not user):
            return format_response("not found", 404)

        # Retrieve email from request body
        email = request.form.get("email")

        # Check email in body
        if(email):
            # Check email is valid
            if(not is_email(email)):
                return format_response("invalid email", 422)

            # Checks if email is already registered by another user on the Database
            db_user = db.session.query(User).filter(User.email == email).first()
            if(db_user):
                return format_response("email already registered", 403)
            
            # Updates the email
            user.email = email

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

    def delete(self, id=None):
        if(not id):
            return format_response("delete not allowed", 405)

        # Check if supplied id complains with UUID standards
        if(not is_uuid(id)):
            return format_response("invalid id", 422)

        # Tries to retreive user by id
        user = db.session.query(User).filter(User.id == id).first()
        if(not user):
            return format_response("not found", 404)

        db.session.delete(user)
        db.session.commit()

        return make_response(code=204)

        

        
