from sqlalchemy import Column, create_engine, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

Base = declarative_base()


class OrmHelper:
    engine = None
    conn_string = None
    session = None

    def db_init(self, conn_string):
        self.conn_string = conn_string
        self.engine = create_engine(self.conn_string, echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session


orm_helper = OrmHelper()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, autoincrement=True, nullable=False)
    login_id = Column(String(50), index=True, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(50))
    created_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, login_id, first_name, last_name, phone):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        if self.user_id is not None:
            self.user_id = self.user_id

    def __repr__(self):
        return "<User(name={self.first_name!r})>".format(self=self)


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, autoincrement=True, nullable=False)
    id_type = Column(String(10))
    customer_ref = Column(String(50), primary_key=True)
    personal_id = Column(String(50))
    email = Column(String(50))
    created_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    created_by = Column(Integer, ForeignKey('users.user_id'))
    updated_by = Column(Integer, ForeignKey('users.user_id'))

    created_user = relationship("User", foreign_keys=created_by)
    updated_user = relationship("User", foreign_keys=updated_by)

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
    created_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    created_by = Column(Integer, ForeignKey('users.user_id'))
    updated_by = Column(Integer, ForeignKey('users.user_id'))

    customer = relationship("Customer", foreign_keys=customer_ref)
    created_user = relationship("User", foreign_keys=created_by)
    updated_user = relationship("User", foreign_keys=updated_by)

    def __repr__(self):
        return "<Account(name={self.account_number!r})>".format(self=self)
