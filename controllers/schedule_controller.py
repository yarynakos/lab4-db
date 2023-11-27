from flask import Blueprint, jsonify, request
from services.schedule_service import find_all, find_by_id, create, delete, update

schedule = Blueprint('schedule', __name__)


@schedule.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@schedule.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@schedule.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@schedule.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@schedule.route('/<int:id>', methods=['PUT'])
def update_entity(id):
    entity = request.get_json()
    result = update(id, entity)
    return jsonify(result)
