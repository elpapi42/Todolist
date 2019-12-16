from api import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String())

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "<id {}>".format(self.id)