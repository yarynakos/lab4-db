class NotificationDTO:
    def __init__(self, notification_id, type_of_notification, time_of_notification, text_of_notification, user_id,
                 object_id, sensor_id):
        self.notification_id = notification_id
        self.type_of_notification = type_of_notification
        self.time_of_notification = time_of_notification
        self.text_of_notification = text_of_notification
        self.user_id = user_id
        self.object_id = object_id
        self.sensor_id = sensor_id

    @classmethod
    def from_dict(cls, data):
        return cls(notification_id=data.get('notification_id'), type_of_notification=data.get('type_of_notification'),
                   time_of_notification=str(data.get('time_of_notification')),
                   text_of_notification=data.get('text_of_notification'), user_id=data.get('user_id'),
                   sensor_id=data.get('sensor_id'), object_id=data.get('object_id'))

    def to_dict(self):
        return {
            'notification_id': self.notification_id,
            'type_of_notification': self.type_of_notification,
            'time_of_notification': str(self.time_of_notification),
            'text_of_notification': self.text_of_notification,
            'user_id': self.user_id,
            'sensor_id': self.sensor_id,
            'object_id': self.object_id
        }
