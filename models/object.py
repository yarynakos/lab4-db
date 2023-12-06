from app import db


class Object(db.Model):
    __tablename__ = 'object'
    object_id = db.Column(db.Integer, primary_key=True)
    type_of_object = db.Column(db.String(45), nullable=False)
    number_of_flors = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False)
    city = db.relationship('City', backref='object')
