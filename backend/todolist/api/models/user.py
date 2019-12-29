import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin

from ... import db

class User(UserMixin, db.Model):
    """ Define User Fields """
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email
        self.id = uuid.uuid4()

    def __repr__(self):
        return "<email {}>".format(self.email)

    def get_id(self):
        return str(self.id)