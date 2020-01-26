import uuid

from sqlalchemy.dialects.postgresql import UUID

from ... import db

class OAuthToken(db.Model):
    """ Storage for oauth tokens """
    __tablename__ = "oauth_tokens"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    provider = db.Column(db.String(16), nullable=False)
    token = db.Column(db.String, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)

    def __init__(self, provider, token, user_id):
        self.id = uuid.uuid4()
        self.provider = provider
        self.token = token
        self.user_id = user_id
        
    def __repr__(self):
        return "<OAuth Token: {}>".format(self.provider)