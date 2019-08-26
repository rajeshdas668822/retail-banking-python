import pytest
from native_sql.data_access.data_setup import dal
from native_sql.data_access.data_service import DefaultDao
from app_config.config import db_dir
import json
from sqlalchemy import select
from tests.data import native_sql_mock_data
import os


@pytest.fixture()
def default_dao():
    conn_string = "sqlite:///{}".format(db_dir)
    return dal.db_init(conn_string)


def test_os_test():
    basedir = os.path.abspath(os.path.realpath("data/test.db"))
    print(os.path.join(basedir, os.pardir))
    print(os.path.normpath(os.path.join(basedir, os.pardir)))



def test_users_insert(default_dao):
    ins = dal.users.insert();
    users = native_sql_mock_data.mock_user()
    results = DefaultDao.save_data(ins, users)
    assert 2 == results.rowcount


def test_customer_insert(default_dao):
    ins = dal.customers.insert()
    cust = native_sql_mock_data.mock_customer()
    results = DefaultDao.save_data(ins, cust)
    assert 2 == results.rowcount
    # print(json.dumps(cust))


def test_account_insert(default_dao):
    ins = dal.accounts.insert()
    accts = native_sql_mock_data.mock_account()
    results = DefaultDao.save_data(ins, accts)
    assert 6 == results.rowcount
    print(json.dumps(accts))


def test_user_select(default_dao):
    sel = dal.users.select()
    results = DefaultDao.find_by_query(sel)
    results = results.fetchall()
    for rp in results:
        print(rp.login_id, rp.first_name, rp.last_name)


def test_user_first(default_dao):
    sel = select([dal.users])
    results = DefaultDao.find_by_query(sel)
    results = results.first()
    print(results.login_id, results.first_name, results.last_name)


def test_user_all(default_dao):
    sel = select([dal.users.columns.login_id, dal.users.columns.first_name])
    results = DefaultDao.find_by_query(sel)
    results = results.fetchall()
    print(results)
# print(results.login_id, results.first_name, results.last_name)
