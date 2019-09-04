from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app_config.config import config
from route_config import user_route

db = SQLAlchemy()
# init MA
ma = Marshmallow()


# def create_app(config_name):
app = Flask(__name__)
app.config.from_object(config['development'])
db.init_app(app)
ma.init_app(app)
app.register_blueprint(user_route)
    # return app


