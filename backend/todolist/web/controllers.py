from flask_restful import Resource
from flask import jsonify

class Home(Resource):
    """ Web Home Page """
    def get(self):
        return "Home Page"