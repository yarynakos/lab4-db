from dto.user_dto import UserDTO
from models.user import User
from app import db


def find_all():
    entities = User.query.all()
    return [UserDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = User.query.get_or_404(id)
    return UserDTO.to_dict(entity)


def create(entity):
    new_entity = User(surname=entity['surname'],
                      phone=entity['phone'], email=entity['email'], access_level_name=entity['access_level_name'])
    db.session.add(new_entity)
    db.session.commit()
    return UserDTO.to_dict(new_entity)


def delete(id):
    entity = User.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'User deleted successfully'}


def update(id, entity):
    update_entity = User.query.get_or_404(id)
    update_entity.surname = entity['surname']
    update_entity.name = entity['name']
    update_entity.text_of_notification = entity['text_of_notification']
    update_entity.phone = entity['phone']
    update_entity.email = entity['email']
    update_entity.access_level_name = entity['access_level_name']
    db.session.add(update_entity)
    db.session.commit()
    return UserDTO.to_dict(update_entity)
