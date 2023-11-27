from flask import Blueprint, jsonify, request
from services.object_service import find_all, find_by_id, create, delete

object = Blueprint('object', __name__)


@object.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@object.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@object.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@object.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@object.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(id, entity)
    return jsonify(result)
