import uuid

from flask import Response

from test_fixtures import instance, user_id, token

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





