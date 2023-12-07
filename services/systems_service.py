from dto.systems_dto import SystemsDTO
from models.systems import Systems
from app import db


def find_all():
    entities = Systems.query.all()
    return [SystemsDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Systems.query.get_or_404(id)
    return SystemsDTO.to_dict(entity)


def create(entity):
    new_entity = Systems(system_name=entity['system_name'])
    db.session.add(new_entity)
    db.session.commit()
    return SystemsDTO.to_dict(new_entity)


def delete(id):
    entity = Systems.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Systems deleted successfully'}


def update(id, entity):
    update_entity = Systems.query.get_or_404(id)
    update_entity.system_name = entity['system_name']
    db.session.add(update_entity)
    db.session.commit()
    return SystemsDTO.to_dict(update_entity)

