from flask import Blueprint, jsonify, request
from services.user_service import find_all, find_by_id, create, delete

user = Blueprint('user', __name__)


@user.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@user.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@user.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@user.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@user.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(id, entity)
    return jsonify(result)
