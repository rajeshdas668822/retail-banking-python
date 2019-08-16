from data_access.data_setup import dal
from sqlalchemy import select, update, delete
from app_service.base_service import BaseService
from util.result_helper import ResultHelper
from data_access.data_service import DefaultDao


class UserService(BaseService):

    def init_service(self, conn_string):
        print("Connection string used : {}".format(conn_string))
        # self.defaultDao = DefaultDao(conn_string)
        dal.db_init(conn_string)

    def save(self, data):
        users = [data.__dict__]
        ins = dal.users.insert()
        DefaultDao.save_data(ins, users)
        select_query = select([dal.users]).where(dal.users.columns.login_id == data.login_id)
        result_proxy = DefaultDao.find_by_query(select_query)
        return ResultHelper.resultproxy_to_dict_list(result_proxy)

    def get_all(self):
        select_all_users = select([dal.users])
        results = DefaultDao.find_by_query(select_all_users);
        return ResultHelper.resultproxy_to_dict_list(results)

    def update(self, data):
        users = [data.__dict__]
        print("user_id ======{}".format(data.user_id))
        updated_user = update(dal.users).where(dal.users.columns.user_id == data.user_id)
        DefaultDao.update_data(updated_user, users)
        select_query = select([dal.users]).where(dal.users.columns.user_id == data.user_id)
        results = DefaultDao.find_by_query(select_query)
        return ResultHelper.resultproxy_to_dict_list(results)

    def delete_by_id(self, id):
        delete_user = delete(dal.users).where(dal.users.columns.user_id == id)
        result = DefaultDao.delete_data(delete_user)
        print("result.rowcount---> {}".format(result.rowcount))


user_service = UserService()