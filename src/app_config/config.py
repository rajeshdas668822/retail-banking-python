import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))

db_dir = "C:/Python-BuildArea/db/test.db"

# Data Base
conn_string = "sqlite:///{}".format(db_dir)


class Config:
    SECRET_KEY = 'development key'
    ADMINS = frozenset(['test@test.com'])


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SECRET_KEY = 'Prod key'
    SQLALCHEMY_DATABASE_URI = conn_string


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
