from app_config import ma


from orm.orm_data_access.models import User, Account, Customer


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
