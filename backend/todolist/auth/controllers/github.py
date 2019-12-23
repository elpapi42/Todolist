from flask import request, make_response, jsonify
from flask_restful import Resource

from ... import db
from ..models import User

class GithubLogin(db.Model):
    """ Login Controller """

    def get(self):
        return "github login"