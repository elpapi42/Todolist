import pytest

from ... import create_app

@pytest.fixture
def instance():
    app = create_app(testing=True)
    return app.test_client()

def test_github_login_redirect(instance):
    response = instance.get("/auth/github/")
    assert response.status_code == 302

