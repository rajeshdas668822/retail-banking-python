from util.CustomException import InsufficientBalance


class Account:
    def __init__(self, first_name, last_name, account_number, balance, account_type):
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._balance = balance
        self._account_type = account_type

    def get_name(self):
        return "{} {}".format(self._first_name, self._last_name)

    def get_account_number(self):
        return self._account_number

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientBalance("Balance is not enough")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance
