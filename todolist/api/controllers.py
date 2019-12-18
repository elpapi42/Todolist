import uuid

from validator_collection.checkers import is_uuid

from flask import make_response, jsonify, request
from flask_restful import Resource

from .models import db, Task, User

class UserController(Resource):
    """ Interact with Users DataBase Entries """

    def get(self, id=None):
        if(not id):
            return make_response(
                jsonify({"error": "not implemented"}),
                501
            )
        
        # Check if supplied id complains with UUID standards
        if(not is_uuid(id)):
            return make_response(
                jsonify({"error": "invalid id"}),
                422
            )


        # Tries to retreive user by id
        user = db.session.query(User).filter(User.id == id).first()

        if(not user):
            return make_response(
                jsonify({"error": "not found"}),
                404
            )  

        return make_response(
            jsonify({
                "id": user.id,
                "email": user.email
            }), 
            200
        )

    def post(self, id=None):
        if(id):
            return make_response(
                jsonify({"error": "post not allowed, use put instead"}),
                400
            )

        # Retrieve email from request body
        email = request.form.get("email")

        # Checks if email is already registered by another user on the Database
        db_user = db.session.query(User).filter(User.email == email).first()
        if(db_user):
            return make_response(
                jsonify({"error": "email already registered"}),
                403
            )
        
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

class TaskController(Resource):
    """ Interact with Task DataBase Entries """

    def get(self, taskname, id):
        tasks = db.session.query(Task).filter(Task.title == taskname).all()
        tasks_list = list()

        for task in tasks:
            task_dict = {
                "id": task.id,
                "title": task.title,
                "description": task.description
            }
            tasks_list.append(task_dict)

        return jsonify(tasks_list)

    def post(self, taskname):
        task = Task(taskname, request.form["description"])

        db.session.add(task)
        db.session.commit()

        task_dict = {
            "id": task.id,
            "title": task.title,
            "description": task.description
        }

        return jsonify(task_dict)

    def put(self, taskname, id):
        tasks = db.session.query(Task).filter(Task.title == taskname).all()


        return "Update Task"

