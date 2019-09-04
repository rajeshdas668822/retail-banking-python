# create Hello route
from flask import jsonify, Blueprint, request
from orm.orm_data_access.models import User
from orm.app_service.user_service import user_service
from  random import randrange

user_page = Blueprint('users', __name__, template_folder='route_config')


@user_page.route('/user', methods=['POST'])
def create_user():
    login_id = request.json['login_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']
    user_id=randrange(1, 100)
    user = User(login_id, first_name, last_name, phone,user_id)
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


@user_page.route('/user/<first_name>', methods=['DELETE'])
def delete_user_by_criteria(first_name):
    param = [('first_name', 'eq', first_name)]
    user_service.delete_by_criteria(param)
    return jsonify(" User  with first {} deleted Successfully".format(first_name))


# Get All
@user_page.route('/user', methods=['GET'])
def get_all_user():
    results = user_service.get_all()
    return jsonify(results)


# Get by login Id
@user_page.route('/user/<login_id>', methods=['GET'])
def get_user_by_login_id(login_id):
    results = user_service.get_by_login_id(login_id)
    return jsonify(results)


