import pytest
import json
import uuid

from flask import Response

from todolist import create_app, db

@pytest.fixture
def instance():
    app = create_app(mode="test")
    return app.test_client()

def test_get_users(instance):
    response = instance.get("/api/users/")
    assert response.status_code == 501

def test_valid_uuid(instance):
    response = instance.get("/api/users/nonuuid/")
    assert response.status_code == 422

def test_create_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    assert response.status_code == 201

def test_already_registered_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    assert response.status_code == 403

def test_retrieve_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    id = json.loads(response.data)["id"]
    response = instance.get("/api/users/{id}/".format(id=id))
    assert response.status_code == 200

def test_retrieve_non_registered_user(instance):
    id = uuid.uuid4()
    response = instance.get("/api/users/{id}/".format(id=id))
    assert response.status_code == 404