from app import db


class AccessLevel(db.Model):
    __tablename__ = 'access_level'
    access_level_name = db.Column(db.String(45), primary_key=True)