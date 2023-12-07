from flask import Blueprint, jsonify, request
from services.country_service import find_all, find_by_name, create, delete, add_country_proc

country = Blueprint('country', __name__)


@country.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@country.route('/<string:name>', methods=['GET'])
def find_entity_by_name(name):
    entity = find_by_name(name)
    return jsonify(entity)


@country.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@country.route('/<string:name>', methods=['DELETE'])
def remove_entity(name):
    return delete(name)


@country.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(name, entity)
    return jsonify(result)


@country.route('/proc', methods=["POST"])
def add_country():
    entity = add_country_proc(request.get_json()['country_name'])
    return jsonify(entity)

