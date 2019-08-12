from data_access.data_service import DefaultDao
from data_access.data_setup import dal
from sqlalchemy import select


class UserService:

    def __init__(self, conn_string):
        self.defaultDao = DefaultDao(conn_string)

    def save(self, data):
        users = [data.__dict__]
        results = self.defaultDao.data_save(users)
        select_query = select([dal.users]).where(dal.users.columns.user_id == results.inserted_primary_key)
        return self.defaultDao.find_by_query(select_query)

    def get_all(self):
        select_all_users = select([dal.users])
        return self.defaultDao.find_by_query(select_all_users)
