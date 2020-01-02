import datetime
import jwt
import os

import pytest

from todolist import create_app, db
from todolist.auth.models import OAuth
from todolist.api.models import User

@pytest.fixture
def instance():
    app = create_app(testing=True)
    return app.test_client()

@pytest.fixture
def token():
    jwt_payload = {
        "uid": "c82753c6-0775-46c4-b050-af8eee8b9c93",
        "eml": "test@test.com",
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    token = jwt.encode(jwt_payload, os.environ["SECRET_KEY"], algorithm="HS256").decode("utf-8")

    return "Bearer {}".format(token)

@pytest.fixture
def user_id():
    app = create_app(testing=True)

    with app.app_context():
        user = User("test@test.com")
        user.id = "c82753c6-0775-46c4-b050-af8eee8b9c93"
        db.session.add(user)

        github_token = {
            "access_token": "97f801e817bf4d4d3b3c22514a8608b047789823", 
            "token_type": "bearer", 
            "scope": [""]
        }

        oauth_token = OAuth("github", github_token, user.id, user)
        db.session.add(oauth_token)

        db.session.commit()

        return user.id