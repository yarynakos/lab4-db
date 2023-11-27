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


def update(name, entity):
    update_entity = AccessLevel.query.get_or_404(name)
    update_entity.country_name = entity['access_level_name']
    db.session.add(update_entity)
    db.session.commit()
    return CountryDTO.to_dict(update_entity)

