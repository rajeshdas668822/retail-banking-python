from flask import Flask

from app_config import config
from route_config.user_route import user_page

# init app
app = Flask(__name__)
# init config

app.config.from_object(config)

# Init DB
#db = SQLAlchemy(app)

# init MA
#ma = Marshmallow(app)


app.register_blueprint(user_page)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
