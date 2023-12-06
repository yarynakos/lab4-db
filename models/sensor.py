from app import db


class Sensor(db.Model):
    __tablename__ = 'sensor'
    sensor_id = db.Column(db.Integer, primary_key=True)
    type_of_sensor = db.Column(db.String(45), nullable=False)
    measurement_radius = db.Column(db.Double)
    room_id = db.Column(db.Integer, db.ForeignKey('room.room_id'), nullable=False)
    room = db.relationship('Room', backref='sensor')
