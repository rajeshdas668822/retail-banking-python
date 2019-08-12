import os
#from flask_marshmallow import Marshmallow

basedir = ''


# Data Base
conn_string = "sqlite:///" + os.path.join(basedir, "data/test.db")
SQLALCHEMY_DATABASE_URI = conn_string
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True

# init MA
#ma = Marshmallow(app)
