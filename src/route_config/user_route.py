# create Hello route
from flask import jsonify, Blueprint, request
from model import User

user_page = Blueprint('users', __name__, template_folder='route_config')


@user_page.route('/', methods=['GET'])
def say_hello():
    return jsonify({"msg": "Hello World"})


@user_page.route('/user', methods=['POST'])
def create_user():
    login_id = request.json['login_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']

    user = User(login_id, first_name, last_name, phone)
    # user = users_service.save(user)
    # return user_schema.jsonify(user)


# Get All
# @user_page.route('/user', methods=['GET'])
# def get_all_user():
#     return users_schema.jsonify(users_service.get_all())
