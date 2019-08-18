import os
from data_access.data_setup import dal
from data_access.data_service import DefaultDao
from app_service.user_service import UserService

# from flask_marshmallow import Marshmallow

db_dir = "C:/Users/User/PycharmProjects/market-ms/data/test.db"



# Data Base
conn_string = "sqlite:///{}".format(db_dir)
SQLALCHEMY_DATABASE_URI = conn_string
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
is_orm_enabled = False

if is_orm_enabled == False :
    dal.db_init(conn_string)
    default_dao = DefaultDao(dal)
    # service init
    user_service = UserService(default_dao)
else :






#user_service.init_marshmallow(ma)


# init MA
# ma = Marshmallow(app)
