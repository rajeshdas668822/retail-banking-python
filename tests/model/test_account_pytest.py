import pytest
from native_sql.model.Account import Account
from util.CustomException import InsufficientBalance


@pytest.fixture()
def account():
    account = Account("Rajesh", "Das", "192-715-2191", 7000, "Saving")
    return account


def test_name(account):
    assert "Rajesh Das" == account.get_name()


def test_withdraw(account):
    account.withdraw(6000)
    assert 1000 == account.get_balance()


def test_with_insufficient_balance(account):
    with pytest.raises(InsufficientBalance):
        account.withdraw(9000)


@pytest.mark.parametrize("earned,spent,expected", [
    (7000, 6000, 1000),
    (9000, 7000, 2000)
])
def test_withdraw_with_param(account, earned, spent, expected):
    account.set_balance(earned)
    account.withdraw(spent)
    assert account.get_balance() == expected
