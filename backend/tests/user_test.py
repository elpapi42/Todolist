import uuid

from flask import Response

from .test_fixtures import instance, user, admin

def test_get_users_as_user(instance, user):
    response = instance.get(
        "/api/users/",
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 403

def test_get_users_as_admin(instance, admin):
    response = instance.get(
        "/api/users/",
        headers={"Authorization": admin.get("token")}
    )
    assert response.status_code == 200

def test_valid_uuid(instance, user):
    response = instance.get(
        "/api/users/nonuuid/",
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 422

def test_retrieve_non_registered_user(instance, admin):
    id = uuid.uuid4()
    response = instance.get(
        "/api/users/{id}/".format(id=id),
        headers={"Authorization": admin.get("token")}
    )
    assert response.status_code == 404

def test_retrieve_other_user(instance, user, admin):
    response = instance.get(
        "/api/users/{id}/".format(id=admin.get("id")),
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 403
    
def test_retrieve_user(instance, user):
    response = instance.get(
        "/api/users/{id}/".format(id=user.get("id")),
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 200

def test_retrieve_current_user(instance, user):
    response = instance.get(
        "/api/users/current/",
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 200

def test_post_user(instance, user):
    response = instance.post(
        "/api/users/current/",
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 405

def test_delete_other_user(instance, user, admin):
    response = instance.delete(
        "/api/users/{id}/".format(id=admin.get("id")),
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 403

def test_delete_user(instance, user):
    response = instance.delete(
        "/api/users/current/",
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 204





