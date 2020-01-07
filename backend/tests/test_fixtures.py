import datetime
import jwt
import os
import uuid

import pytest

from todolist import create_app, db
from todolist.auth.models import OAuth
from todolist.api.models import User

@pytest.fixture
def instance():
    app = create_app(testing=True)
    return app.test_client()

@pytest.fixture
def user():
    """ Creates and user and return it id and access token """
    app = create_app(testing=True)

    id = uuid.uuid4()

    # Token testing payload
    jwt_payload = {
        "uid": str(id),
        "eml": "{}@test.com".format(id),
        "adm": False,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    # Generate token
    token = jwt.encode(jwt_payload, os.environ["SECRET_KEY"], algorithm="HS256").decode("utf-8")
    token = "Bearer {}".format(token)

    with app.app_context():
        user = User("{}@test.com".format(id))
        user.id = id
        db.session.add(user)

        github_token = {
            "access_token": "97f801e817bf4d4d3b3c22514a8608b047789823", 
            "token_type": "bearer", 
            "scope": [""]
        }

        oauth_token = OAuth("github", github_token, user.id, user)
        db.session.add(oauth_token)

        db.session.commit()

        return {
            "id": user.id,
            "token": token
        }

@pytest.fixture
def admin():
    """ Creates and user with admin permission and return its id and access token """
    app = create_app(testing=True)

    id = uuid.uuid4()

    # Token testing payload
    jwt_payload = {
        "uid": str(id),
        "eml": "{}@test.com".format(id),
        "adm": True,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    # Generate token
    token = jwt.encode(jwt_payload, os.environ["SECRET_KEY"], algorithm="HS256").decode("utf-8")
    token = "Bearer {}".format(token)

    with app.app_context():
        user = User("{}@test.com".format(id))
        user.id = id
        db.session.add(user)

        oauth_token = OAuth("local", None, user.id, user)
        db.session.add(oauth_token)

        db.session.commit()

        return {
            "id": user.id,
            "token": token
        }