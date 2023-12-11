from flask import Blueprint, jsonify, request
from services.country_service import find_all, find_by_name, create, delete, add_country_proc

countries = Blueprint('country', __name__)


@countries.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@countries.route('/<string:name>', methods=['GET'])
def find_entity_by_name(name):
    entity = find_by_name(name)
    return jsonify(entity)


@countries.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@countries.route('/<string:name>', methods=['DELETE'])
def remove_entity(name):
    return delete(name)


@countries.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(name, entity)
    return jsonify(result)


@countries.route('/proc', methods=['POST'])
def add_country():
    entity = request.get_json()
    return add_country_proc(entity['name'])

