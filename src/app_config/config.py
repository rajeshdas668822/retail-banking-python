from native_sql.data_access.data_setup import dal
from native_sql.data_access.data_service import DefaultDao
from native_sql.app_service.user_service import UserService
from orm.orm_data_access.orm_setup import OrmHelper
from orm.orm_data_access.data_service import ORMService
from orm.app_service.user_service import OrmUserService

# from flask_marshmallow import Marshmallow

db_dir = "C:/Python-BuildArea/retail-banking-python/data/test.db"

# Data Base
conn_string = "sqlite:///{}".format(db_dir)
SQLALCHEMY_DATABASE_URI = conn_string
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
orm_enabled = True

if not orm_enabled:
    dal.db_init(conn_string)
    default_dao = DefaultDao(dal)
    # service init
    user_service = UserService(default_dao)
else:
    orm_layer = OrmHelper()
    orm_layer.db_init(conn_string)
    orm_data_service = ORMService(orm_layer.get_session())
    user_service = OrmUserService(orm_data_service)

# user_service.init_marshmallow(ma)


# init MA
# ma = Marshmallow(app)
