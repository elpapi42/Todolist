import jwt
import datetime
import os
import pytz

from flask import jsonify
from flask_restful import Resource

class IssueToken(Resource):
    """ Return a token that grants access tothe API """
    
    def get(self):
        pass
        
        