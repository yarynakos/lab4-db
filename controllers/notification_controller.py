from flask import Blueprint, jsonify, request
from services.notification_service import find_all, find_by_id, create, delete

notification = Blueprint('notification', __name__)


@notification.route('/', methods=['GET'])
def find_all_entities():
    entities = find_all()
    return jsonify(entities)


@notification.route('/<int:id>', methods=['GET'])
def find_entity_by_id(id):
    entity = find_by_id(id)
    return jsonify(entity)


@notification.route('/', methods=['POST'])
def create_entity():
    entity = create(request.get_json())
    return jsonify(entity)


@notification.route('/<int:id>', methods=['DELETE'])
def remove_entity(id):
    return delete(id)


@notification.route('/<string:name>', methods=['PUT'])
def update_entity(name):
    entity = request.get_json()
    result = entity(id, entity)
    return jsonify(result)
