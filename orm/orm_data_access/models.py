from datetime import datetime
from app_config.app_init import db


# class Base(db.Model):
#     created_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
#     updated_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class User(db.Model):
    __tablename__ = "users"

    # user_id_seq = CreateSequence('user_id_seq')

    # user_id = Column(Integer, primary_key=True,default=lambda: uuid4().hex)
    user_id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(50), index=True, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, login_id, first_name, last_name, phone, user_id=None):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        if user_id is not None:
            self.user_id = user_id

    def __repr__(self):
        return "<User(name={self.first_name!r})>".format(self=self)


class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    id_type = db.Column(db.String(10))
    customer_ref = db.Column(db.String(50), primary_key=True)
    personal_id = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    updated_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    created_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    created_user = db.relationship("User", foreign_keys=created_by)
    updated_user = db.relationship("User", foreign_keys=updated_by)

    def __init__(self, customer_id, id_type, customer_ref, personal_id, email, user_id):
        if customer_id is not None:
            self.customer_id = customer_id
        self.id_type = id_type
        self.customer_ref = customer_ref
        self.personal_id = personal_id
        self.email = email
        self.created_by = user_id
        self.updated_by = user_id

    def __repr__(self):
        return "<Customer(name={self.customer_ref!r})>".format(self=self)


class Account(db.Model):
    __tablename__ = "account"
    account_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    account_number = db.Column(db.String(50), index=True, primary_key=True)
    name = db.Column(db.String(50))
    account_type = db.Column(db.String(50))
    balance = db.Column(db.Numeric(10, 2))
    customer_ref = db.Column(db.String(50), db.ForeignKey('customers.customer_ref'))
    created_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    updated_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    created_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    customer = db.relationship("Customer", foreign_keys=customer_ref)
    created_user = db.relationship("User", foreign_keys=created_by)
    updated_user = db.relationship("User", foreign_keys=updated_by)

    def __init__(self, account_id, account_number, name, account_type, balance, customer_ref, user_id):
        if account_id is not None:
            self.account_id = account_id
        self.customer_ref = customer_ref
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.created_by = user_id
        self.updated_by = user_id

    def __repr__(self):
        return "<Account(name={self.account_number!r})>".format(self=self)
