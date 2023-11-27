from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(75), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    access_level_name = db.Column(db.String(45), db.ForeignKey('access_level.name'), nullable=False)
    access_level = db.relationship('AccessLevel', backref='user')