from orm.orm_data_access.orm_filter_util import DynamicFilter
from orm.orm_data_access.models import User
from orm.filter import filters,sorting


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

    def get_by_filter_spec_criteria(self, entity, filter_spec):
        query = self.session.query(User)
        query = filters.apply_filters(query,filter_spec.get_filters(),True)
        query = sorting.apply_sort(query,filter_spec.get_order_by())
        return query.all()
