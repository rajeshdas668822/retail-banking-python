import pytest
from app_config.config import conn_string
from orm.orm_data_access.orm_setup import OrmHelper


@pytest.fixture()
def session():
    orm_helper = OrmHelper()
    orm_helper.db_init(conn_string)
    db_session = orm_helper.get_session()

    yield db_session
    db_session.commit()
    db_session.close()


