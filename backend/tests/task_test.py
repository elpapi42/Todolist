import uuid

from flask import Response

from .test_fixtures import instance, user, admin

def test_create_task(instance, user):
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 201
    assert response.is_json == True
    assert response.json.get("description") == "this is a test task"

def test_create_task_without_description(instance, user):
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 02",
        },
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 201
    assert response.is_json == True
    assert response.json.get("description") == ""

def test_create_task_without_authorization(instance, user, admin):
    response = instance.post(
        "/api/users/{}/tasks/".format(admin.get("id")),
        data={
            "title": "test task 03",
        },
        headers={"Authorization": user.get("token")}
    )
    assert response.status_code == 403
    assert response.is_json == True

def test_create_task_without_token(instance, user):
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task",
        }
    )
    assert response.status_code == 401
    assert response.is_json == True

def test_get_tasks(instance, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    response = instance.get(
        "/api/users/current/tasks/",
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 200
    assert response.is_json == True
    assert response.json[0].get("description") == "this is a test task"

def test_get_tasks_without_authorization(instance, user, admin):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": admin.get("token")}
    )

    response = instance.get(
        "/api/users/{}/tasks/".format(admin.get("id")),
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 403
    assert response.is_json == True

def test_get_tasks_of_other_user_as_admin(instance, admin, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    response = instance.get(
        "/api/users/{}/tasks/".format(user.get("id")),
        headers={"Authorization": admin.get("token")}
    )

    assert response.status_code == 200
    assert response.is_json == True
    assert response.json[0].get("description") == "this is a test task"