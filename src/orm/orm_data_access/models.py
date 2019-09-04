from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base(object):
    created_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


Base = declarative_base(cls=Base)


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login_id = Column(String(50), index=True, unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(50))

    def __init__(self, login_id, first_name, last_name, phone, user_id=None):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        if user_id is not None:
            self.user_id = user_id

    def __repr__(self):
        return "<User(name={self.first_name!r})>".format(self=self)


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, autoincrement=True, nullable=False)
    id_type = Column(String(10))
    customer_ref = Column(String(50), primary_key=True)
    personal_id = Column(String(50))
    email = Column(String(50))
    created_by = Column(Integer, ForeignKey('users.user_id'))
    updated_by = Column(Integer, ForeignKey('users.user_id'))

    created_user = relationship("User", foreign_keys=created_by)
    updated_user = relationship("User", foreign_keys=updated_by)

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


class Account(Base):
    __tablename__ = "account"
    account_id = Column(Integer, autoincrement=True, nullable=False)
    account_number = Column(String(50), index=True, primary_key=True)
    name = Column(String(50))
    account_type = Column(String(50))
    balance = Column(Numeric(10, 2))
    customer_ref = Column(String(50), ForeignKey('customers.customer_ref'))
    created_by = Column(Integer, ForeignKey('users.user_id'))
    updated_by = Column(Integer, ForeignKey('users.user_id'))
    customer = relationship("Customer", foreign_keys=customer_ref)
    created_user = relationship("User", foreign_keys=created_by)
    updated_user = relationship("User", foreign_keys=updated_by)

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
