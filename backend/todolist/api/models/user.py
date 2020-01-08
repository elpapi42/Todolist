import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin

from ... import db

class User(UserMixin, db.Model):
    """ Define User Fields """
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    oauth = db.relationship("OAuth", backref="user", uselist=False)

    def __init__(self, email, is_admin=False):
        self.id = uuid.uuid4()
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return "<email {}>".format(self.email)

    def get_id(self):
        return str(self.id)