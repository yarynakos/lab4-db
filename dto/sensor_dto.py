class SensorDTO:
    def __init__(self, sensor_id, type_of_sensor, measurement_radius, room_id):
        self.sensor_id = sensor_id
        self.type_of_sensor = type_of_sensor
        self.measurement_radius = measurement_radius
        self.room_id = room_id

    @classmethod
    def from_dict(cls, data):
        return cls(sensor_id=data.get('sensor_id'), type_of_sensor=data.get('type_of_sensor'),
                   measurement_radius=data.get('measurement_radius'), room_id=data.get('room_id'))

    def to_dict(self):
        return {
            'sensor_id': self.sensor_id,
            'type_of_sensor': self.type_of_sensor,
            'measurement_radius': self.measurement_radius,
            'room_id': self.room_id
        }
