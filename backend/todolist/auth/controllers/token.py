import jwt
import datetime
import os
import pytz

from flask import jsonify
from flask_restful import Resource
from flask_login import login_required, current_user

class IssueToken(Resource):
    """ Return a token that grants access tothe API """
    
    def get(self):
        pass
        
        