import pytest
import json
import uuid

from flask import Response

from ... import create_app, db

@pytest.fixture
def instance():
    app = create_app(testing=True)
    return app.test_client()

def test_get_users(instance):
    response = instance.get("/api/users/")
    assert response.status_code == 501

def test_valid_uuid(instance):
    response = instance.get("/api/users/nonuuid/")
    assert response.status_code == 422

def test_retrieve_non_registered_user(instance):
    id = uuid.uuid4()
    response = instance.get("/api/users/{id}/".format(id=id))
    assert response.status_code == 404
    
def test_retrieve_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    id = json.loads(response.data)["id"]
    response = instance.get("/api/users/{id}/".format(id=id))
    assert response.status_code == 200

def test_post_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    id = json.loads(response.data)["id"]
    response = instance.post("/api/users/{id}/".format(id=id), data={"email": "test@test.com"})
    assert response.status_code == 405

def test_create_user_without_email(instance):
    response = instance.post("/api/users/")
    assert response.status_code == 400

def test_create_user_invalid_email(instance):
    response = instance.post("/api/users/", data={"email": "testtestcom"})
    assert response.status_code == 422

def test_already_registered_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    assert response.status_code == 403

def test_create_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    assert response.status_code == 201

def test_put_not_allowed_for_users_endpoint(instance):
    response = instance.put("/api/users/")
    assert response.status_code == 405

def test_update_non_existent_user(instance):
    id = uuid.uuid4()
    response = instance.put("/api/users/{id}/".format(id=id))
    assert response.status_code == 404

def test_update_user_without_email(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    id = json.loads(response.data)["id"]
    response = instance.put("/api/users/{id}/".format(id=id))
    assert response.status_code == 200

def test_update_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    id = json.loads(response.data)["id"]
    response = instance.put("/api/users/{id}/".format(id=id), data={"email": "non-test@test.com"})
    assert response.status_code == 200

def test_delete_user(instance):
    response = instance.post("/api/users/", data={"email": "test@test.com"})
    id = json.loads(response.data)["id"]
    response = instance.delete("/api/users/{id}/".format(id=id), data={"email": "test@test.com"})
    assert response.status_code == 204





