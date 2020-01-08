from flask import redirect
from flask_restful import Resource
from flask_login import logout_user, login_required

class Logout(Resource):
    """ Logout the Current User from the Session """
    method_decorators = [login_required]
    def get(self):
        logout_user()
        return redirect("/")