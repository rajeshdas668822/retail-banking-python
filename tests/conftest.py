import pytest
from app_config.config import conn_string
from orm.orm_data_access.orm_setup import OrmHelper
from sqlalchemy_utils import create_database, drop_database, database_exists
from orm.orm_data_access.models import Base

SQLITE_TEST_DB_URI = 'SQLITE_TEST_DB_URI'
MYSQL_TEST_DB_URI = 'MYSQL_TEST_DB_URI'
POSTGRESQL_TEST_DB_URI = 'POSTGRESQL_TEST_DB_URI'


def pytest_addoption(parser):
    parser.addoption(
        '--sqlite-test-db-uri',
        action='store',
        dest=SQLITE_TEST_DB_URI,
        default='sqlite:///test_sqlalchemy_filters.db',
        help=(
            'DB uri for testing (e.g. '
            '"sqlite:///test_sqlalchemy_filters.db")'
        )
    )


@pytest.fixture(scope='session')
def config(request):
    # return {
    #     SQLITE_TEST_DB_URI: request.config.getoption(SQLITE_TEST_DB_URI),
    #     MYSQL_TEST_DB_URI: request.config.getoption(MYSQL_TEST_DB_URI),
    #     POSTGRESQL_TEST_DB_URI: request.config.getoption(POSTGRESQL_TEST_DB_URI),
    # }
    return {SQLITE_TEST_DB_URI: "sqlite:///C:/Python-BuildArea/testdb/test_sqlalchemy_filters.db"
            }


def test_db_keys():
    """Decide what DB backends to use to run the tests."""
    test_db_uris = []
    test_db_uris.append(SQLITE_TEST_DB_URI)

    try:
        import mysql  # noqa: F401
    except ImportError:
        pass
    else:
        test_db_uris.append(MYSQL_TEST_DB_URI)

    try:
        import psycopg2  # noqa: F401
    except ImportError:
        pass
    else:
        test_db_uris.append(POSTGRESQL_TEST_DB_URI)

    return test_db_uris


@pytest.fixture(scope='session', params=test_db_keys())
def db_uri(request, config):
    return config[request.param]


@pytest.fixture(scope='session')
def is_postgresql(db_uri):
    if 'postgresql' in db_uri:
        return True
    return False


@pytest.fixture(scope='session')
def is_sqlite(db_uri):
    if 'sqlite' in db_uri:
        return True
    return False


@pytest.fixture(scope='session')
def db_engine_options(db_uri, is_postgresql):
    if is_postgresql:
        return dict(
            client_encoding='utf8',
            connect_args={'client_encoding': 'utf8'}
        )
    return {}


@pytest.fixture()
def session(db_uri, db_engine_options):
    orm_helper = OrmHelper()
    orm_helper.db_init(conn_string)
    db_session = orm_helper.get_session()
    print("Session Called ..............")
    yield db_session

    for table in reversed(Base.metadata.sorted_tables):
        db_session.execute(table.delete())

    db_session.commit()
    db_session.close()




def create_db(uri):
    """Drop the database at ``uri`` and create a brand new one. """
    destroy_database(uri)
    create_database(uri)


def destroy_database(uri):
    """Destroy the database at ``uri``, if it exists. """
    if database_exists(uri):
        drop_database(uri)
