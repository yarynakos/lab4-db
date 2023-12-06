from app import db


class Room(db.Model):
    __tablename__ = 'room'
    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(45), nullable=False)
    type_of_room = db.Column(db.String(45), nullable=False)
    object_id = db.Column(db.Integer, db.ForeignKey('object.object_id'), nullable=False)
    object = db.relationship('Object', backref='room')
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.zone_id'), nullable=False)
    zone = db.relationship('Zone', backref='room')
