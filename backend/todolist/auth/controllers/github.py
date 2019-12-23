from flask import request, make_response, jsonify
from flask_restful import Resource

from ... import db

class GithubLogin(Resource):
    """ Login Controller """

    def get(self):
        return "github login"