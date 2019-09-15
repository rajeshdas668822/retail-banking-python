from util.custom_exception import InsufficientBalance


class Account:
    def __init__(self, account_number, name, account_type,balance, customer_ref, user_id):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.customer_ref = customer_ref
        self.created_by = user_id
        self.updated_by = user_id

    def get_name(self):
        return self.name

    def get_account_number(self):
        return self.account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance("Balance is not enough")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance
