from flask import request, make_response, jsonify
from flask_restful import Resource

from ... import db
from ..models import Task
from . import format_response
from ..decorators import token_required, authorization_required, task_id_required

class TaskController(Resource):
    """ Get, Edit or Delete Task """

    method_decorators = [task_id_required, authorization_required, token_required]

    def get(self, task_id, *args, **kwargs):
        # Retrieve task
        task = Task.query.filter(Task.id == task_id).first()
        if(not task):
            return format_response("task not found", 404)

        return make_response(
            jsonify({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "done": task.done
            }),
            200
        )

    def put(self, task_id, *args, **kwargs):
        # Retrieve task
        task = Task.query.filter(Task.id == task_id).first()
        if(not task):
            return format_response("task not found", 404)

        # Update title
        title = request.form.get("title")
        if(title):
            task.title = title

        # Update description
        description = request.form.get("description")
        if(description):
            task.description = description

        # Update is_done
        done = (request.form.get("done") in ["True", "true", "1"]) if request.form.get("done") else None
        if(done != None):
            task.done = done

        db.session.commit()

        return make_response(
            jsonify({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "done": task.done
            }),
            200
        )

    def delete(self, task_id, *args, **kwargs):
        # Retrieve task
        task = Task.query.filter(Task.id == task_id).delete()
        if(not task):
            return format_response("task not found", 404)

        db.session.commit()
        
        return format_response("task deleted", 204)

class TaskList(Resource):
    """ Get tasks and create new task """

    method_decorators = [authorization_required, token_required]

    def get(self, user_id, *args, **kwargs):
        # Check if the client want to get the task with done=True
        # If true, return all the completed tasks
        # If false, return all the uncomplete tasks
        # If None, return all the tasks
        return_done = (request.args.get("done") in ["True", "true", "1"]) if request.args.get("done") else None

        if(return_done == None):
            tasks = Task.query.filter(Task.user_id == user_id).all()
        else:
            tasks = Task.query.filter(Task.user_id == user_id, Task.done == return_done).all()

        tasks_list = []

        for task in tasks:
            # Create dictionary
            task_data = {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "done": task.done
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
                "done": task.done
            }),
            201
        )