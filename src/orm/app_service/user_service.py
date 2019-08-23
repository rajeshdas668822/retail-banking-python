from orm.orm_data_access.orm_setup import User
from orm.model.model_schema import UserSchema


class OrmUserService:

    def __init__(self, orm_service=None):
        self.orm_service = orm_service
        self.user_schema = UserSchema(strict=True)

    def save(self, data):
        self.orm_service.save(data)
        return self.get_by_login_id(data, data.login_id)

    def get_all(self):
        results = self.orm_service.get_all_by_query(User)
        return results

    def get_by_login_id(self, login_id):
        param = [('login_id', 'eq', login_id)]
        return self.orm_service.get_by_criteria(param)
