from dto.schedule_dto import ScheduleDTO
from models.schedule import Schedule
from app import db


def find_all():
    entities = Schedule.query.all()
    return [ScheduleDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Schedule.query.get_or_404(id)
    return ScheduleDTO.to_dict(entity)


def create(entity):
    new_entity = Schedule(schedule_id=entity['schedule_id'],
                          start_time=entity['start_time'],
                          finish_time=entity['finish_time'],
                          break_time=entity['break_time'],
                          sensor_id=entity['sensor_id'])
    db.session.add(new_entity)
    db.session.commit()
    return ScheduleDTO.to_dict(new_entity)


def delete(id):
    entity = Schedule.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Schedule deleted successfully'}


def update(name, entity):
    update_entity = Schedule.query.get_or_404(name)
    update_entity.country_name = entity['schedule_id']
    db.session.add(update_entity)
    db.session.commit()
    return ScheduleDTO.to_dict(update_entity)
