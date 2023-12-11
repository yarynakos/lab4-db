from sqlalchemy import text

from models.access import AccessLevel
from dto.access_dto import AccessLevelDTO
from app import db


def find_all():
    entities = AccessLevel.query.all()
    return [AccessLevelDTO.to_dict(entity) for entity in entities]


def find_by_name(name):
    entity = AccessLevel.query.get_or_404(name)
    return AccessLevelDTO.to_dict(entity)


def create(entity):
    new_entity = AccessLevel(access_level_name=entity['access_level_name'])
    db.session.add(new_entity)
    db.session.commit()
    return AccessLevelDTO.to_dict(new_entity)


def delete(name):
    entity = AccessLevel.query.get_or_404(name)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'AccessLevel deleted successfully'}


def add_new_db():
    db.session.execute(text(f'CALL add_new_db'))
    return 'ok'
