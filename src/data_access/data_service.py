from data_access.data_setup import dal
from util.CustomException import EmptyData


# dal.db_init('sqlite:///test.db')
class DefaultDao:

    @classmethod
    def save_data(cls, inst, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = dal.get_engine().execute(inst, data)
        return results

    @classmethod
    def update_data(cls, update, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = dal.get_engine().execute(update, data)
        return results

    @classmethod
    def find_by_query(cls, select_query):
        conn = dal.get_engine().connect();
        return conn.execute(select_query)

    @classmethod
    def delete_data(cls, delete_query):
        return dal.get_engine().execute(delete_query)

    @classmethod
    def get_connection(cls):
        return dal.get_engine().connect()




