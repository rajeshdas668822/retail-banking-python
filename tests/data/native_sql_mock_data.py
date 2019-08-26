from native_sql.model import User
from native_sql.model import Customer
from native_sql.model.Account import Account
from util.random_generator_util import get_generated_number

import json

data = []


def mock_account():
    accounts = []
    account = Account(get_generated_number("acct", 3, 100000, 999999), "Rajesh Das", "Saving Account", "9000",
                      "CUST-OBW-505431", 1)
    accounts.append(account.__dict__)
    account = Account(get_generated_number("acct", 3, 100000, 999999), "Rajesh Das", "Current Account", "10000",
                      "CUST-OBW-505431", 1)
    accounts.append(account.__dict__)
    account = Account(get_generated_number("acct", 3, 100000, 999999), "Rajesh Das", "Deposit Account", "12000",
                      "CUST-OBW-505431", 1)
    accounts.append(account.__dict__)

    account = Account(get_generated_number("acct", 3, 100000, 999999), "Pabitra Mallick", "Saving Account", "90000",
                      "CUST-BQB-403753", 2)
    accounts.append(account.__dict__)
    account = Account(get_generated_number("acct", 3, 100000, 999999), "Pabitra Mallick", "Current Account", "100000",
                      "CUST-BQB-403753", 2)
    accounts.append(account.__dict__)
    account = Account(get_generated_number("acct", 3, 100000, 999999), "Pabitra Mallick", "Deposit Account", "120000",
                      "CUST-BQB-403753", 2)
    accounts.append(account.__dict__)

    return accounts


def mock_customer():
    customers = []
    customer = Customer(get_generated_number("cust", 3, 100000, 999999), "NRIC", "G5874880W", "rdas@numerix.com", 1)
    customers.append(customer.__dict__)
    customer = Customer(get_generated_number("cust", 3, 100000, 999999), "Passport", "M303216", "pabitra.4u@gmail.com",
                        2)
    customers.append(customer.__dict__)
    return customers


def mock_user():
    users = []
    user = User("rdas", "Rajesh", "Das", "+65-94592685")
    user1 = User('pMallick', "Pabitra", 'Mallick', "+65-81384196")
    users.append(user.__dict__)
    users.append(user1.__dict__)
    return users


__name__ = '__main__'
us = mock_account()
print(json.dumps(us))
