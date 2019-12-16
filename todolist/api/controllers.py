from flask_restful import Resource

class ApiEntry(Resource):
    def get(self):
        return "Hello From API"