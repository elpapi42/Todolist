from flask_restful import Resource

class Home(Resource):
    """ Web Home Page """

    def get(self):
        return "Home Page"