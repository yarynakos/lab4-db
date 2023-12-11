from app import db


class Systems(db.Model):
    __tablename__ = 'systems'
    system_id = db.Column(db.Integer, primary_key=True)
    system_name = db.Column(db.String(45), nullable=False)
