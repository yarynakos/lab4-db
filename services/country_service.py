from sqlalchemy import text

from models.country import Country
from dto.country_dto import CountryDTO
from app import db


def find_all():
    entities = Country.query.all()
    return [CountryDTO.to_dict(entity) for entity in entities]


def find_by_name(name):
    entity = Country.query.get_or_404(name)
    return CountryDTO.to_dict(entity)


def create(entity):
    new_entity = Country(country_name=entity['country_name'])
    db.session.add(new_entity)
    db.session.commit()
    return CountryDTO.to_dict(new_entity)


def delete(name):
    entity = Country.query.get_or_404(name)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Country deleted successfully'}


def add_country_proc(name):
    return db.session.execute(text(f'CALL add_country({name})'))
