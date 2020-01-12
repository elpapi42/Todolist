import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin

from ... import db

class User(UserMixin, db.Model):
    """ Define User Fields """
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    oauth = db.relationship("OAuth", backref="user", uselist=False)
    tasks = db.relationship("Task", backref="user")

    def __init__(self, email):
        self.id = uuid.uuid4()
        self.email = email

    def __repr__(self):
        return "<User: {}>".format(self.email)

    def get_id(self):
        return str(self.id)