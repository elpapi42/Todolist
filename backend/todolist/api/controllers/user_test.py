import pytest
import json
import uuid
import datetime
import jwt
import os

from flask import Response

from ... import create_app, db
from ..models import User
from ...auth.models import OAuth

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

def test_get_users(instance, token):
    response = instance.get(
        "/api/users/",
        headers={"Authorization": token}
    )
    assert response.status_code == 501

def test_valid_uuid(instance, token):
    response = instance.get(
        "/api/users/nonuuid/",
        headers={"Authorization": token}
    )
    assert response.status_code == 422

def test_retrieve_non_registered_user(instance, token):
    id = uuid.uuid4()
    response = instance.get(
        "/api/users/{id}/".format(id=id),
        headers={"Authorization": token}
    )
    assert response.status_code == 404
    
def test_retrieve_user(instance, user_id, token):
    response = instance.get(
        "/api/users/{id}/".format(id=user_id),
        headers={"Authorization": token}
    )
    assert response.status_code == 200

def test_post_user(instance, user_id, token):
    response = instance.post(
        "/api/users/{id}/".format(id=user_id), 
        data={"email": "test@test.com"},
        headers={"Authorization": token}
    )
    assert response.status_code == 405

def test_put_not_allowed_for_users_endpoint(instance, token):
    response = instance.put(
        "/api/users/",
        headers={"Authorization": token}
    )
    assert response.status_code == 405

def test_update_non_existent_user(instance, token):
    id = uuid.uuid4()
    response = instance.put(
        "/api/users/{id}/".format(id=id),
        data={"email": "test@test.com"},
        headers={"Authorization": token}
    )
    assert response.status_code == 404

def test_update_user_without_email(instance, user_id, token):
    response = instance.put(
        "/api/users/{id}/".format(id=user_id),
        headers={"Authorization": token}
    )
    assert response.status_code == 400

def test_update_user(instance, user_id, token):
    response = instance.put(
        "/api/users/{id}/".format(id=user_id), 
        data={"email": "non-test@test.com"},
        headers={"Authorization": token}
    )
    assert response.status_code == 200

def test_delete_user(instance, user_id, token):
    response = instance.delete(
        "/api/users/{id}/".format(id=user_id), 
        headers={"Authorization": token}
    )
    assert response.status_code == 204





