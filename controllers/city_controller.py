from flask import Blueprint, jsonify, request
from services.city_service import find_all, find_by_id, create, delete, update, add_ten

city = Blueprint('city', __name__)


@city.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@city.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@city.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@city.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@city.route('/<int:id>', methods=['PUT'])
def update_entity(id):
    entity = request.get_json()
    result = update(id, entity)
    return jsonify(result)

@city.route('/proc', methods=['POST'])
def add_ten_random():
    entity = request.get_json()
    return jsonify(add_ten(entity['cityName']))
