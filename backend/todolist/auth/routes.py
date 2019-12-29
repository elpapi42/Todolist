from flask_restful import Api

from . import auth_bp

auth = Api(auth_bp)