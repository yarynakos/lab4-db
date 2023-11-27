from flask import Blueprint, jsonify, request
from services.access_service import find_all, find_by_name, create, delete

access_level = Blueprint('access_level', __name__)


@access_level.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@access_level.route('/<string:name>', methods=['GET'])
def find_entity_by_name(name):
    entity = find_by_name(name)
    return jsonify(entity)


@access_level.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@access_level.route('/<string:name>', methods=['DELETE'])
def remove_entity(name):
    return delete(name)


@access_level.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(name, entity)
    return jsonify(result)
