import pytest
from data_access.data_setup import dal
from data_access.data_service import DefaultDao
import json
from sqlalchemy import select
from tests.data import mock_data
import os


@pytest.fixture()
def default_dao():
    # conn_string = "sqlite:///C:/Users/User/PycharmProjects/market-ms/data/test.db"
    basedir = os.path.realpath("data/test.db")
    conn_string = "sqlite:///{}".format(basedir)
    return DefaultDao(conn_string)


def test_users_insert(default_dao):
    ins = dal.users.insert();
    users = mock_data.mock_user()
    results = default_dao.data_save(ins, users)
    assert 2 == results.rowcount


def test_customer_insert(default_dao):
    ins = dal.customers.insert()
    cust = mock_data.mock_customer()
    results = default_dao.data_save(ins, cust)
    assert 2 == results.rowcount
    # print(json.dumps(cust))


def test_account_insert(default_dao):
    ins = dal.accounts.insert()
    accts = mock_data.mock_account()
    results = default_dao.data_save(ins, accts)
    assert 6 == results.rowcount
    print(json.dumps(accts))


def test_user_select(default_dao):
    sel = dal.users.select()
    results = default_dao.find_by_query(sel)
    results = results.fetchall()
    for rp in results:
        print(rp.login_id, rp.first_name, rp.last_name)


def test_user_first(default_dao):
    sel = select([dal.users])
    results = default_dao.find_by_query(sel)
    results = results.first()
    print(results.login_id, results.first_name, results.last_name)


def test_user_all(default_dao):
    sel = select([dal.users.columns.login_id, dal.users.columns.first_name])
    results = default_dao.find_by_query(sel)
    results = results.fetchall()
    print(results)
# print(results.login_id, results.first_name, results.last_name)
