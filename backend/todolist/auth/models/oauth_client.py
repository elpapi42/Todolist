import uuid

from sqlalchemy.dialects.postgresql import UUID

from ... import db

class OAuthClient(db.Model):
    """ Storage for oauth clients information """
    __tablename__ = "oauth_clients"

    identifier = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    id = db.Column(db.String, unique=True, nullable=False)
    secret = db.Column(db.String, nullable=False)
    handle = db.Column(db.String(16), nullable=False)

    def __init__(self, id, secret, handle):
        self.identifier = uuid.uuid4()
        self.id = id
        self.secret = secret
        self.handle = handle
        
    def __repr__(self):
        return "<OAuth Client: {}>".format(self.handle)