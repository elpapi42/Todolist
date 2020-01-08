import uuid

from sqlalchemy.dialects.postgresql import UUID

from ... import db

class Task(db.Model):
    """ Storage for tasks """
    __tablename__ = "tasks"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(256), default="", nullable=False)
    is_done = db.Column(db.Boolean, default=False, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))

    def __init__(self, title, user_id):
        self.id = uuid.uuid4()
        self.title = title
        self.user_id = user_id
        
    def __repr__(self):
        return "<Task: {}>".format(self.title)