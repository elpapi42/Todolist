from flask_restful import Resource
from flask import jsonify

from ..api.models import User
from ..auth.models import OAuth

class Home(Resource):
    """ Web Home Page """
    def get(self):
        return "Home Page"