from dto.zona_dto import ZoneDTO
from models.zone import Zone
from app import db


def find_all():
    entities = Zone.query.all()
    return [ZoneDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Zone.query.get_or_404(id)
    return ZoneDTO.to_dict(entity)


def create(entity):
    new_entity = Zone(zone_name=entity['zone_name'],
                      access_level_name=entity['access_level_name'], object_id=entity['object_id'])
    db.session.add(new_entity)
    db.session.commit()
    return ZoneDTO.to_dict(new_entity)


def delete(id):
    entity = Zone.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Zone deleted successfully'}


def update(id, entity):
    update_entity = Zone.query.get_or_404(id)
    update_entity.zone_name = entity['zone_name']
    update_entity.object_id = entity['object_id']
    update_entity.access_level_name = entity['access_level_name']
    db.session.add(update_entity)
    db.session.commit()
    return ZoneDTO.to_dict(update_entity)
