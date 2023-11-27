from dto.notification_dto import NotificationDTO
from models.notification import Notification
from app import db


def find_all():
    entities = Notification.query.all()
    return [NotificationDTO.to_dict(entity) for entity in entities]


def find_by_id(id):
    entity = Notification.query.get_or_404(id)
    return NotificationDTO.to_dict(entity)


def create(entity):
    new_entity = Notification(notification_id=entity['notification_id'],
                              type_of_notification=entity['type_of_notification'],
                              time_of_notification=entity['time_of_notification'],
                              text_of_notification=entity['text_of_notification'],
                              user_id=entity['user_id'],
                              object_id=entity['object_id'],
                              sensor_id=entity['sensor_id'])
    db.session.add(new_entity)
    db.session.commit()
    return NotificationDTO.to_dict(new_entity)


def delete(id):
    entity = Notification.query.get_or_404(id)
    db.session.delete(entity)
    db.session.commit()
    return {'message': 'Notification deleted successfully'}


def update(name, entity):
    update_entity = Notification.query.get_or_404(name)
    update_entity.country_name = entity['notification_id']
    db.session.add(update_entity)
    db.session.commit()
    return NotificationDTO.to_dict(update_entity)
