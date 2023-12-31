from app import db


class Zone(db.Model):
    __tablename__ = 'zone'
    zone_id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(45), nullable=False)
    access_level_name = db.Column(db.String(45), db.ForeignKey('access_level.access_level_name'), nullable=False)
    access_level = db.relationship('AccessLevel', backref='zone')
    object_id = db.Column(db.Integer, db.ForeignKey('object.object_id'), nullable=False)
    object = db.relationship('Object', backref='zone')
