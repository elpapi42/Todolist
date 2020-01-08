from flask_restful import Resource
from flask import jsonify

from ..api.models import User
from ..auth.models import OAuth

class Home(Resource):
    """ Web Home Page """
    def get(self):
        users = User.query.all()
        oauth_tokens = OAuth.query.all()
        return jsonify({
            "data": oauth_tokens[0].user.email
        })