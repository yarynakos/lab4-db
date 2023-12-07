from flask import Blueprint, jsonify, request
from services.systems_service import find_all, find_by_id, create, delete, update

systems = Blueprint('systems', __name__)


@systems.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@systems.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@systems.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@systems.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@systems.route('/<int:id>', methods=['PUT'])
def update_entity(id):
    entity = request.get_json()
    result = update(id, entity)
    return jsonify(result)
