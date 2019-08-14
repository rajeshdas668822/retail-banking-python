import os

# from flask_marshmallow import Marshmallow

basedir = "C:/Python-BuildArea/retail-banking-python/data"



# Data Base
#conn_string = "sqlite:///" + os.path.join(basedir,"/data/test.db")
conn_string = "sqlite:///{}".format("C:/Python-BuildArea/retail-banking-python/data/test.db")
SQLALCHEMY_DATABASE_URI = conn_string
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True

# init MA
# ma = Marshmallow(app)
