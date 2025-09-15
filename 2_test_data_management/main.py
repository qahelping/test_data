import pytest

@pytest.fixture
def user_data():
    return {"login": "test_user", "password": "12345"}

def test_login(user_data):
    assert user_data["login"] == "test_user"


@pytest.mark.parametrize("data,expected", [
    ("1", True),
    ("", False),
])
def test_auth(data, expected):
    assert data is expected


PROD = 'prod'
TEST = 'test'
@pytest.mark.parametrize("data,expected", [
    ("1", True),
    ("", False),
])
def test_auth(data, expected):
    assert data is expected