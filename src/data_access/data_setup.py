from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, DateTime, PrimaryKeyConstraint, ForeignKey, \
    UniqueConstraint, create_engine
from datetime import datetime


# import sqlite3
# conn = sqlite3.connect('test.db')
# print ("Opened database successfully");

class InitializeDataLayer:
    engine = None
    conn_string = None
    metadata = MetaData()

    users = Table("users", metadata,
                  Column("user_id", Integer(), autoincrement=True, nullable=False),
                  Column("login_id", String(50), index=True),
                  Column("first_name", String(50)),
                  Column("last_name", String(50)),
                  Column("phone", String(50)),
                  Column("created_on", DateTime(), default=datetime.now()),
                  Column("updated_on", DateTime(), default=datetime.now(), onupdate=datetime.now()),
                  PrimaryKeyConstraint('user_id', name='user_pk'),
                  UniqueConstraint('login_id', name='uix_username')
                  )

    customers = Table("customers", metadata,
                      Column("customer_id", Integer(), primary_key=True, autoincrement=True),
                      Column("id_type", String(10)),
                      Column("customer_ref", String(50)),
                      Column("personal_id", String(50)),
                      Column("email", String(50)),
                      Column("created_on", DateTime(), default=datetime.now()),
                      Column("updated_on", DateTime(), default=datetime.now(), onupdate=datetime.now()),
                      Column("created_by", ForeignKey('users.user_id')),
                      Column("updated_by", ForeignKey('users.user_id'))
                      )
    accounts = Table("account", metadata,
                     Column("account_id", Integer(), primary_key=True, autoincrement=True),
                     Column("account_number", String(50), index=True),
                     Column("name", String(50)),
                     Column("account_type", String(50)),
                     Column("balance", Numeric(10, 2)),
                     Column("customer_ref", ForeignKey('customers.customer_ref')),
                     Column("created_on", DateTime(), default=datetime.now()),
                     Column("updated_on", DateTime(), default=datetime.now(), onupdate=datetime.now()),
                     Column("created_by", ForeignKey('users.user_id')),
                     Column("updated_by", ForeignKey('users.user_id')))

    def db_init(self, conn_string):
        self.conn_string = conn_string
        self.engine = create_engine(self.conn_string, echo=True)
        self.metadata.create_all(self.engine)

    def get_engine(self):
        return self.engine


dal = InitializeDataLayer()
