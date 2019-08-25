from orm.model.model_schema import UserSchema
from orm.orm_data_access.orm_setup import User
from orm.orm_data_access.orm_filter_util import DynamicFilter


class ORMService:

    def __init__(self, session):
        self.session = session

    def save(self, data):
        self.session.add(data)
        self.session.commit()
        return data

    def bulk_save(self, data):
        return self.session.bulk_save_objects(data)

    def get_all_by_query(self, query_string):
        # users =
        # users_schema = UserSchema(many=True, strict=True)
        # dump_data = users_schema.dump(users).data
        # print(dump_data)
        return self.session.query(query_string).all()

    def get_by_criteria(self, entity, _filter_condition=[]):
        dynamic_filtered_query_class = DynamicFilter(self.session, query=None, model_class=entity,
                                                     filter_condition=_filter_condition)
        dynamic_filtered_query = dynamic_filtered_query_class.return_query()
        return dynamic_filtered_query.all()

    def delete_by_criteria(self, param):
        users = self.get_by_criteria(User, param)
        for user in users:
            self.session.delete(user)
        self.session.commit()
