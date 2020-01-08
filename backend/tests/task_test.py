import uuid

from flask import Response

from .test_fixtures import instance, user, admin

def test_create_task(instance, user):
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 201
    assert response.is_json == True
    assert response.json.get("description") == "this is a test task"