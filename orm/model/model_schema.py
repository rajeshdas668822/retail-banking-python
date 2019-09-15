from app_config.app_init import ma
from orm.orm_data_access.models import User, Account, Customer
from marshmallow import post_load, fields


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    #     Id = fields.Integer()
    #     login = fields.String()
    #     first_name = fields.String()
    #     last_name = fields.String()
    #     phone = fields.String()
    #     created_on = fields.DateTime()
    #     updated_on = fields.DateTime()
    #
    # post_load(pass_many=True)
    # def value_tuple(self, data):
    #     return (data["login_id"], data["first_name"], data["last_name"], data['phone'])


class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
