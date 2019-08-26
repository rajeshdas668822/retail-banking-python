import datetime

import pytest
from six import string_types
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from orm.filter.filters import apply_filters
from util.custom_exception import (
    BadFilterFormat, BadSpec, FieldNotFound
)
from orm.model.model_schema import User, Account, Customer
from tests.data.orm_mock_data import mock_account,mock_customer,mock_user


@pytest.fixture
def multiple_users_inserted(session):
    users = mock_user()
    session.add_all(users)
    session.commit()


@pytest.fixture
def multiple_customer_inserted(session, multiple_users_inserted):
    customers = mock_customer()
    session.add_all(customers)
    session.commit()



@pytest.fixture
def multiple_account_inserted(session, multiple_users_inserted,multiple_customer_inserted):
    accounts = mock_account()
    session.add_all(accounts)
    session.commit()



class TestFilterNotApplied:

    def test_no_filters_provided(self,session):
        query = session.query(User)
        filters = []
        filtered_query = apply_filters(query, filters)
        assert query == filtered_query

    @pytest.mark.parametrize('filter_', ['some text', 1, ''])
    def test_wrong_filters_format(self, session, filter_):
        query = session.query(User)
        filters = [filter_]

        with pytest.raises(BadFilterFormat) as err:
            apply_filters(query, filters)

        expected_error = 'Filter spec `{}` should be a dictionary.'.format(
            filter_
        )
        assert expected_error == err.value.args[0]


    @pytest.mark.usefixtures('multiple_users_inserted')
    def test_no_operator_provided(self, session):
        query = session.query(User)
        filters = [{'field': 'login_id', 'value': 'rdas'}]

        filtered_query = apply_filters(query, filters)
        result = filtered_query.all()

        assert len(result) == 1
        #assert result[0].id == 1
        #assert result[1].id == 3

    def test_no_field_provided(self, session):
        query = session.query(User)
        filters = [{'op': '==', 'value': 'rdas'}]

        with pytest.raises(BadFilterFormat) as err:
            apply_filters(query, filters)

        expected_error = '`field` is a mandatory filter attribute.'
        assert expected_error == err.value.args[0]

    # TODO: replace this test once we add the option to compare against
    # another field

    def test_no_value_provided(self, session):
        query = session.query(User)
        filters = [{'field': 'name', 'op': '==', }]

        with pytest.raises(BadFilterFormat) as err:
            apply_filters(query, filters)

        assert '`value` must be provided.' == err.value.args[0]

    def test_invalid_field(self, session):
        query = session.query(User)
        filters = [{'field': 'invalid_field', 'op': '==', 'value': 'rdas1'}]

        with pytest.raises(FieldNotFound) as err:
            apply_filters(query, filters)

        expected_error = (
            "Model <class 'test.models.Bar'> has no column `invalid_field`."
        )
        assert expected_error == err.value.args[0]

    @pytest.mark.parametrize('attr_name', [
        'metadata',  # model attribute
        'foos',  # model relationship
    ])
    def test_invalid_field_but_valid_model_attribute(self, session, attr_name):
        query = session.query(User)
        filters = [{'field': attr_name, 'op': '==', 'value': 'rdas'}]

        with pytest.raises(FieldNotFound) as err:
            apply_filters(query, filters)

        expected_error = (
            "Model <class 'test.models.Bar'> has no column `{}`.".format(
                attr_name
            )
        )
        assert expected_error == err.value.args[0]