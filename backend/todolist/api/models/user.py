import uuid
from datetime import datetime
import pytz

from sqlalchemy.dialects.postgresql import UUID

from ... import db

class User(db.Model):
    """ Define User Fields """
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow().replace(tzinfo=pytz.utc), nullable=False)

    oauth = db.relationship("OAuth", backref="user", uselist=False)
    tasks = db.relationship("Task", backref="user")

    def __init__(self, email):
        self.id = uuid.uuid4()
        self.email = email

    def __repr__(self):
        return "<User: {}>".format(self.email)

    def get_id(self):
        return str(self.id)