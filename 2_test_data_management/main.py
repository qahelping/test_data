import os

import pytest
from dotenv import load_dotenv


@pytest.fixture
def user_data():
    load_dotenv()
    return {"login": "test_user", "password": "12345", "env": os.getenv('ENV')}

def test_login(user_data):
    assert user_data["login"] == "test_user"
    assert user_data["password"] == "12345"
    assert user_data["env"] == "test"


@pytest.mark.parametrize("data,expected", [
    ("1", True),
    ("", False),
])
def test_auth(data, expected):
    assert data is expected