from sqlalchemy import text

from app import db
from dto.city_dto import CityDTO
from models.city import City


def find_all():
    entities = City.query.all()
    return [CityDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = City.query.get_or_404(id)
    return CityDTO.to_dict(entity)


def create(entity):
    new_entity = City(city_name=entity['city_name'], country_name=entity['country_name'])
    db.session.add(new_entity)
    db.session.commit()
    return CityDTO.to_dict(new_entity)


def delete(id):
    entity = City.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'City deleted successfully'}


def update(id, entity):
    update_entity = City.query.get_or_404(id)
    update_entity.city_name = entity['city_name']
    update_entity.country_name = entity['country_name']
    db.session.add(update_entity)
    db.session.commit()
    return CityDTO.to_dict(update_entity)


def add_ten(cityName):
    print(cityName)
    querry = text(f'CALL add_ten_cities("{cityName}")')
    db.session.execute(querry)
    db.session.commit()
    entities = City.query.all()
    return [CityDTO.to_dict(entity) for entity in entities]
