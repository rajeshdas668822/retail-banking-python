from orm.orm_data_access.models import User
from orm.model.model_schema import UserSchema
from orm.orm_data_access.orm_filter_util import FilterSpecification
from orm.orm_data_access.data_service import dao_service


class OrmUserService:

    def __init__(self):
        self.user_schema = UserSchema()
        self.users_schema = UserSchema(many=True)

    def save_collection(self, data):
        users = self.users_schema.load(data)
        return dao_service.bulk_save(users.data)

    def save(self, data):
        results = dao_service.save(data)
        # return self.get_by_login_id(data.login_id)
        dump_data = self.user_schema.dump(results).data
        return dump_data

    def get_all(self):
        results = dao_service.get_all_by_query(User)
        dump_data = self.users_schema.dump(results).data
        return dump_data

    # def get_by_login_id(self, login_id):
    #     param = [('login_id', 'eq', login_id)]
    #     results = self.orm_service.get_by_criteria(User, param)
    #     dump_data = self.users_schema.dump(results).data
    #     return dump_data

    def get_by_login_id(self, login_id):
        filters = [{'field': 'login_id', 'op': '==', 'value': login_id}]
        filter_spec = FilterSpecification(filters, [])
        results = dao_service.get_by_filter_spec_criteria(User, filter_spec)
        dump_data = self.users_schema.dump(results).data
        return dump_data

    def get_by_user_id(self, user_id):
        param = [('user_id', 'eq', user_id)]
        users = dao_service.get_by_criteria(User, param)
        dump_data = self.users_schema.dump(users).data

    def delete_by_criteria(self, param):
        dao_service.delete_by_criteria(param)


user_service = OrmUserService()
