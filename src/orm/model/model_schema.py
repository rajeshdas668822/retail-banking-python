from marshmallow_sqlalchemy import ModelSchema


from orm.orm_data_access.orm_setup import User, Account, Customer


class UserSchema(ModelSchema):
    class Meta:
        model = User


class AccountSchema(ModelSchema):
    class Meta:
        model = Account


class CustomerSchema(ModelSchema):
    class Meta:
        model = Customer
