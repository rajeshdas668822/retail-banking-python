from data_access.data_service import DefaultDao
from data_access.data_setup import dal
from sqlalchemy import select
from  app_service.base_service import BaseService
from util.result_helper import ResultHelper


class UserService(BaseService):
    defaultDao = None

    def init_service(self, conn_string):
        print("Connection string used : {}".format(conn_string))
        self.defaultDao = DefaultDao(conn_string)

    def save(self, data):
        users = [data.__dict__]
        ins = dal.users.insert()
        results = self.defaultDao.data_save(ins,users)
        select_query = select([dal.users]).where(dal.users.columns.login_id == data.login_id)
        return ResultHelper.resultproxy_to_dict_list(self.defaultDao.find_by_query(select_query))

    def get_all(self):
        select_all_users = select([dal.users])
        return ResultHelper.resultproxy_to_dict_list(self.defaultDao.find_by_query(select_all_users))


user_service = UserService()
