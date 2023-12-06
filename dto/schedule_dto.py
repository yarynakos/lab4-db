class ScheduleDTO:
    def __init__(self, schedule_id, start_time, finish_time, break_time, sensor_id):
        self.schedule_id = schedule_id
        self.start_time = start_time
        self.finish_time = finish_time
        self.break_time = break_time
        self.sensor_id = sensor_id

    @classmethod
    def from_dict(cls, data):
        return cls(schedule_id=data.get('schedule_id'),
                   start_time=str(data.get('start_time')),
                   finish_time=str(data.get('finish_time')),
                   break_time=str(data.get('break_time')),
                   sensor_id=data.get('sensor_id'))

    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'start_time': str(self.start_time),
            'finish_time': str(self.finish_time),
            'break_time': str(self.break_time),
            'sensor_id': self.sensor_id
        }
