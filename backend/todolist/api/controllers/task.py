import uuid

from validator_collection.checkers import is_uuid
from flask import request, make_response, jsonify
from flask_restful import Resource

from ... import db
from ..models import User, Task
from . import format_response
from ..decorators import token_required, admin_required

class TaskList(Resource):
    """ Get tasks and create new task """

    method_decorators = [token_required]

    def get(self, user_id, *args, **kwargs):
        pass