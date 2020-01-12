import uuid

from sqlalchemy.dialects.postgresql import UUID

from ... import db

class OAuthClient(db.Model):
    """ Storage for oauth clients information """
    __tablename__ = "oauth_clients"

    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    client_id = db.Column(db.String, nullable=False)
    client_secret = db.Column(db.String, nullable=False)
    client_handle = db.Column(db.String(16), nullable=False)

    def __init__(self, client_id, client_secret, client_handle):
        self.id = uuid.uuid4()
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_handle = client_handle
        
    def __repr__(self):
        return "<OAuth Client: {}>".format(self.client_handle)