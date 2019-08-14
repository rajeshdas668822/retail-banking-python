from data_access.data_setup import dal
from util.CustomException import EmptyData


# dal.db_init('sqlite:///test.db')
class DefaultDao:

    def __init__(self, conn_string):
        self.conn_string = conn_string
        dal.db_init(conn_string)

    def data_save(self, inst, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = dal.get_engine().execute(inst, data)
        return results

    def find_by_query(self, select_query):
        conn = dal.get_engine().connect();
        return conn.execute(select_query)

    def get_connection(self):
        return dal.get_engine().connect()

