from dto.sensor_dto import SensorDTO
from models.sensor import Sensor
from app import db


def find_all():
    entities = Sensor.query.all()
    return [SensorDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Sensor.query.get_or_404(id)
    return SensorDTO.to_dict(entity)


def create(entity):
    new_entity = Sensor(sensor_id=entity['sensor_id'], type_of_sensor=entity['type_of_sensor'],
                        measurement_radius=entity['measurement_radius'], room_id=entity['room_id'])
    db.session.add(new_entity)
    db.session.commit()
    return SensorDTO.to_dict(new_entity)


def delete(id):
    entity = Sensor.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Sensor deleted successfully'}


def update(name, entity):
    update_entity = Sensor.query.get_or_404(name)
    update_entity.country_name = entity['sensor_id']
    db.session.add(update_entity)
    db.session.commit()
    return SensorDTO.to_dict(update_entity)
