import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from ... import db

class OAuth(OAuthConsumerMixin, db.Model):
    """ Storage for oauth tokens """
    __tablename__ = "oauth_tokens"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="oauth", uselist=False)

    def __init__(self, provider, token, user_id, user):
        self.id = uuid.uuid4()
        self.provider = provider
        self.token = token
        self.user_id = user_id
        self.user = user
        
    def __repr__(self):
        return "<user {}>".format(self.user.email)