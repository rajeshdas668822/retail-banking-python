from orm.model.model_schema import User, Account, Customer
from util.random_generator_util import get_generated_number


def mock_user():
    users = []
    user = User("rdas", "Rajesh", "Das", "+65-94592685", 1)
    user1 = User('pMallick', "Pabitra", 'Mallick', "+65-81384196", 2)
    users.append(user)
    users.append(user1)
    return users


def mock_customer():
    customers = []
    customer = Customer(1, "NRIC", "CUST-OBW-505431", "G5874880W", "rdas@numerix.com", 1)
    customers.append(customer)
    customer = Customer(2, "Passport", "CUST-BQB-403753", "M303216", "pabitra.4u@gmail.com", 2)
    customers.append(customer)
    return customers


def mock_account():
    accounts = []
    account = Account(1,get_generated_number("acct", 3, 100000, 999999), "Rajesh Das", "Saving Account", "9000",
                      "CUST-OBW-505431", 1)
    accounts.append(account)
    account = Account(2,get_generated_number("acct", 3, 100000, 999999), "Rajesh Das", "Current Account", "10000",
                      "CUST-OBW-505431", 1)
    accounts.append(account)
    account = Account(3,get_generated_number("acct", 3, 100000, 999999), "Rajesh Das", "Deposit Account", "12000",
                      "CUST-OBW-505431", 1)
    accounts.append(account)

    account = Account(4,get_generated_number("acct", 3, 100000, 999999), "Pabitra Mallick", "Saving Account", "90000",
                      "CUST-BQB-403753", 2)
    accounts.append(account)
    account = Account(5,get_generated_number("acct", 3, 100000, 999999), "Pabitra Mallick", "Current Account", "100000",
                      "CUST-BQB-403753", 2)
    accounts.append(account)
    account = Account(6,get_generated_number("acct", 3, 100000, 999999), "Pabitra Mallick", "Deposit Account", "120000",
                      "CUST-BQB-403753", 2)
    accounts.append(account)

    return accounts
