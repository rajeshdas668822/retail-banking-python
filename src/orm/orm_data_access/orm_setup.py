import sqlalchemy as sa
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
        self.engine = sa.create_engine(self.conn_string, echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session


class User(Base):
    __tablename__ = "users"

    user_id = sa.Column(sa.Integer, autoincrement=True, nullable=False)
    login_id = sa.Column(sa.String(50), index=True, primary_key=True)
    first_name = sa.Column(sa.String(50))
    last_name = sa.Column(sa.String(50))
    phone = sa.Column(sa.String(50))
    created_on = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, login_id, first_name, last_name, phone):
        self.login_id = login_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        # if user_id is not None:
        #     self.user_id = user_id

    def __repr__(self):
        return "<User(name={self.first_name!r})>".format(self=self)


class Customer(Base):
    __tablename__ = "customers"
    customer_id = sa.Column(sa.Integer, autoincrement=True, nullable=False)
    id_type = sa.Column(sa.String(10))
    customer_ref = sa.Column(sa.String(50), primary_key=True)
    personal_id = sa.Column(sa.String(50))
    email = sa.Column(sa.String(50))
    created_on = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now())
    created_by = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'))
    updated_by = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'))

    def __repr__(self):
        return "<Customer(name={self.customer_ref!r})>".format(self=self)


class Account(Base):
    __tablename__ = "account"
    account_id = sa.Column(sa.Integer, autoincrement=True, nullable=False)
    account_number = sa.Column(sa.String(50), index=True, primary_key=True)
    name = sa.Column(sa.String(50))
    account_type = sa.Column(sa.String(50))
    balance = sa.Column(sa.Numeric(10, 2))
    customer_ref = sa.Column(sa.String(50), sa.ForeignKey('customers.customer_ref'))
    created_on = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now())
    updated_on = sa.Column(sa.DateTime, default=datetime.now(), onupdate=datetime.now())
    created_by = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'))
    updated_by = sa.Column(sa.Integer, sa.ForeignKey('users.user_id'))

    # customer = relationship("customers", backref=backref("account"),order_by=customer_ref)

    def __repr__(self):
        return "<Account(name={self.account_number!r})>".format(self=self)
