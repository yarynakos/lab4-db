from dto.room_dto import RoomDTO
from models.room import Room
from app import db


def find_all():
    entities = Room.query.all()
    return [RoomDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Room.query.get_or_404(id)
    return RoomDTO.to_dict(entity)


def create(entity):
    new_entity = Room(room_id=entity['room_id'], room_name=entity['room_name'],
                      type_of_room=entity['type_of_room'], zone_id=entity['zone_id'], object_id=entity['object_id'])
    db.session.add(new_entity)
    db.session.commit()
    return RoomDTO.to_dict(new_entity)


def delete(id):
    entity = Room.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Room deleted successfully'}


def update(name, entity):
    update_entity = Room.query.get_or_404(name)
    update_entity.country_name = entity['room_id']
    db.session.add(update_entity)
    db.session.commit()
    return RoomDTO.to_dict(update_entity)
