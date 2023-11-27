from app import db


class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    type_of_notification = db.Column(db.String(45), nullable=False)
    time_of_notification = db.Column(db.Time)
    text_of_notification = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='notification')
    object_id = db.Column(db.Integer, db.ForeignKey('object.id'), nullable=False)
    object = db.relationship('Object', backref='notification')
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    sensor = db.relationship('Sensor', backref='notification')
