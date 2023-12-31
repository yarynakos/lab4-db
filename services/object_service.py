from dto.object_dto import ObjectDTO
from models.object import Object
from app import db


def find_all():
    entities = Object.query.all()
    return [ObjectDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Object.query.get_or_404(id)
    return ObjectDTO.to_dict(entity)


def create(entity):
    new_entity = Object(type_of_object=entity['type_of_object'],
                        number_of_flors=entity['number_of_flors'], city_id=entity['city_id'])
    db.session.add(new_entity)
    db.session.commit()
    return ObjectDTO.to_dict(new_entity)


def delete(id):
    entity = Object.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Object deleted successfully'}


def update(id, entity):
    update_entity = Object.query.get_or_404(id)
    update_entity.type_of_notification = entity['type_of_object']
    update_entity.time_of_notification = entity['number_of_flors']
    update_entity.city_id = entity['city_id']
    db.session.add(update_entity)
    db.session.commit()
    return ObjectDTO.to_dict(update_entity)

