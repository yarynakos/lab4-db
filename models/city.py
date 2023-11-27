from app import db


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    country_name = db.Column(db.String(100), db.ForeignKey('country.name'), nullable=False)
    country = db.relationship('Country', backref='city')