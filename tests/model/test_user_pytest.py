import pytest
from native_sql.model import User


@pytest.fixture()
def user():
    u = User("rdas", "Rajesh", "Das", "+65-94592685")
    return u


def test_first_name(user):
    assert "Rajesh" == user.get_first_name()
