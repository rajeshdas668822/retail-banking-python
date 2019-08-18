# create Hello route
from flask import jsonify, Blueprint, request
from model.User import User
from app_config.config import user_service

user_page = Blueprint('users', __name__, template_folder='route_config')


@user_page.route('/', methods=['GET'])
def say_hello():
    return jsonify({"msg": "Hello World"})


@user_page.route('/user', methods=['POST'])
def create_user():
    print(request.json())
    login_id = request.json['login_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']
    user = User(login_id, first_name, last_name, phone)
    user = user_service.save(user)
    return jsonify(user)


@user_page.route('/user', methods=['PUT'])
def update_user():
    login_id = request.json['login_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']
    user_id = request.json['user_id']
    user = User(login_id, first_name, last_name, phone, user_id)
    user = user_service.update(user)
    return jsonify(user)


@user_page.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_by_id(user_id)
    return jsonify(" User  with Id {} deleted Successfully".format(user_id))


# Get All
@user_page.route('/user', methods=['GET'])
def get_all_user():
    results = user_service.get_all()
    return jsonify(results)
