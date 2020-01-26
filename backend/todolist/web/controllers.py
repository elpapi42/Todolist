from flask_restful import Resource
from flask import jsonify

from ..auth.models import OAuthClient, OAuthToken

class Home(Resource):
    """ Web Home Page """
    def get(self):

        

        return {
            "data": "void"
        }