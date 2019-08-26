from orm.orm_data_access.models import User
from orm.model.model_schema import UserSchema


class OrmUserService:

    def __init__(self, orm_service=None):
        self.orm_service = orm_service
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True, strict=True)

    def save(self, data):
        results = self.orm_service.save(data)
        # return self.get_by_login_id(data.login_id)
        dump_data = self.user_schema.dump(results).data
        return dump_data

    def get_all(self):
        results = self.orm_service.get_all_by_query(User)
        dump_data = self.users_schema.dump(results).data
        return dump_data

    def get_by_login_id(self, login_id):
        param = [('login_id', 'eq', login_id)]
        results = self.orm_service.get_by_criteria(User, param)
        dump_data = self.users_schema.dump(results).data
        return dump_data

    def get_by_user_id(self, user_id):
        param = [('user_id', 'eq', user_id)]
        users = self.orm_service.get_by_criteria(User, param)
        dump_data = self.users_schema.dump(users).data

    def delete_by_criteria(self, param):
        self.orm_service.delete_by_criteria(param)
