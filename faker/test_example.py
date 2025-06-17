import pytest
from faker import Faker

status = ["Deployed",
          "Rejected",
          "Duplicate",
          "Won't Fix",
          "Cannot Reproduce"]


@pytest.fixture
def fake_seed():
    fake = Faker()
    fake.seed_instance(42)
    a = fake.bothify('TMSG-####')
    b = fake.bothify('TMSG-####')
    return a, b


@pytest.fixture
def fake_unique():
    fake = Faker()
    return {
        'task_id': fake.unique.bothify('TMSG-####'),
        'status': fake.random_element(status)
    }


def test_fake_unique(fake_unique):
    print(fake_unique)
    assert 'TMSG' in fake_unique['task_id']
    assert fake_unique['status'] in status


def test_fake_seed(fake_seed):
    print(fake_seed)
    a, b = fake_seed
    assert 'TMSG' in a
    assert 'TMSG' in b
    assert a == b
