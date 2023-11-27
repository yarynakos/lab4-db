from flask import Blueprint, jsonify, request
from services.room_service import find_all, find_by_id, create, delete

room = Blueprint('room', __name__)


@room.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@room.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@room.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@room.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@room.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(id, entity)
    return jsonify(result)
