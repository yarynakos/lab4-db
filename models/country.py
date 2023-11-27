from app import db


class Country(db.Model):
    __tablename__ = 'country'
    country_name = db.Column(db.String(100), primary_key=True)
























