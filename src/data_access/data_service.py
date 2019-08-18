from util.CustomException import EmptyData


class DefaultDao:

    def __init__(self, data_init=None):
        self.data_init = data_init

    def save_data(self, inst, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = self.data_init.get_engine().execute(inst, data)
        return results

    def update_data(self, update, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = self.data_init.get_engine().execute(update, data)
        return results

    def find_by_query(self, select_query):
        conn = self.data_init.get_engine().connect()
        return conn.execute(select_query)

    def delete_data(self, delete_query):
        return self.data_init.get_engine().execute(delete_query)

    def get_connection(self):
        return self.data_init.get_engine().connect()


class ORMDefaultDao:

    def __init__(self, session=None):
        self.session = session

    def save_data(self, inst, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = self.session.bulk_save_objects(data)
        self.session.commit()
        return self.session.q

    def update_data(self, update, data=[]):
        if data is None:
            raise EmptyData(" Data can't be empty")
        results = self.data_init.get_engine().execute(update, data)
        return results

    def find_by_query(self, select_query):
        conn = self.data_init.get_engine().connect()
        return conn.execute(select_query)

    def delete_data(self, delete_query):
        return self.data_init.get_engine().execute(delete_query)

    def get_connection(self):
        return self.data_init.get_engine().connect()
