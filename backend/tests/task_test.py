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
    assert response.json[0].get("description") == "this is a test task"

def test_get_task_by_id(instance, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    task_id = response.json.get("id")

    response = instance.get(
        "/api/users/current/tasks/{}/".format(task_id),
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 200
    assert response.json.get("description") == "this is a test task"

def test_get_task_by_unregistered_id(instance, user):
    # Generate Dummy id
    task_id = uuid.uuid4()

    response = instance.get(
        "/api/users/current/tasks/{}/".format(task_id),
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 404
    assert response.is_json == True

def test_get_task_by_invalid_id(instance, user):
    response = instance.get(
        "/api/users/current/tasks/nonuuid/",
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 422
    assert response.is_json == True

def test_update_task_by_id(instance, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    task_id = response.json.get("id")

    response = instance.put(
        "/api/users/current/tasks/{}/".format(task_id),
        data={
            "title": "test task 99",
            "description": "this is not a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 200
    assert response.json.get("description") == "this is not a test task"
    assert response.json.get("title") == "test task 99"

def test_update_task_by_id_as_complete(instance, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    task_id = response.json.get("id")

    response = instance.put(
        "/api/users/current/tasks/{}/".format(task_id),
        data={
            "is_done": True
        },
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 200
    assert response.json.get("is_done") == True

def test_update_task_by_id_with_bad_authorization(instance, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    task_id = response.json.get("id")

    response = instance.put(
        "/api/users/current/tasks/{}/".format(task_id),
        data={
            "title": "test task 99",
            "description": "this is not a test task",
        },
        headers={"Authorization": user.get("token")[:-1]}
    )

    assert response.status_code == 401
    assert response.is_json == True

def test_delete_task(instance, user):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": user.get("token")}
    )

    task_id = response.json.get("id")

    response = instance.delete(
        "/api/users/current/tasks/{}/".format(task_id),
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 204

def test_delete__other_user_task(instance, user, admin):
    # Create Task
    response = instance.post(
        "/api/users/current/tasks/",
        data={
            "title": "test task 01",
            "description": "this is a test task",
        },
        headers={"Authorization": admin.get("token")}
    )

    task_id = response.json.get("id")

    response = instance.delete(
        "/api/users/{}/tasks/{}/".format(admin.get("id"), task_id),
        headers={"Authorization": user.get("token")}
    )

    assert response.status_code == 403




