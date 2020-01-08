import uuid

from validator_collection.checkers import is_uuid
from flask import request, make_response, jsonify
from flask_restful import Resource

from ... import db
from ..models import User, Task
from . import format_response
from ..decorators import token_required, admin_required, authorization_required, task_data_required

class TaskList(Resource):
    """ Get tasks and create new task """

    method_decorators = {
        "get": [authorization_required, token_required],
        "post": [authorization_required, token_required]
    }

    def get(self, user_id, *args, **kwargs):
        tasks = Task.query.filter(Task.user_id == user_id).all()

        tasks_list = []

        for task in tasks:
            # Create dictionary
            task_data = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "is_done": task.is_done
            }

            # Append user to the output dictionary
            tasks_list.append(task_data)

        return make_response(
            jsonify(tasks_list),
            200
        )

    def post(self, user_id, *args, **kwargs):
        # Retrieves data from body
        title = request.form.get("title")
        description = request.form.get("description")

        # Check for title in the body, its mandatory
        if(not title):
            return make_response("missing title", 400)

        # Create task and associate it with the user
        task = Task(title, user_id)

        # Set description, if there is one in the request body
        task.description = description if description else ""

        db.session.add(task)
        db.session.commit()

        return make_response(
            jsonify({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "is_done": task.is_done
            }),
            201
        )