from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from route_config.user_route import user_page
from app_config import config
from app_service.user_service import user_service
import os

# init app
app = Flask(__name__)
# init config
config.basedir = os.path.realpath("data/test.db")
app.config.from_object(config)

# Init DB
db = SQLAlchemy(app)

# init MA
ma = Marshmallow(app)


app.register_blueprint(user_page)

#service init
user_service.init_service(config.conn_string)
#user_service.init_marshmallow(ma)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
