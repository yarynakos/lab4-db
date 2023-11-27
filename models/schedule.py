from app import db


class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time)
    finish_time = db.Column(db.Time)
    break_time = db.Column(db.Time)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    sensor = db.relationship('Sensor', backref='schedule')