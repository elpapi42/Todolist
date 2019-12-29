from flask import redirect
from flask_restful import Resource
from flask_login import logout_user

class Logout(Resource):
    """ Logout the Current User from the Session """
    def get(self):
        logout_user()
        return redirect("/")