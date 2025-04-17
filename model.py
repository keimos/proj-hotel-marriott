from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Reservation {self.guest_name} ->{self.room_type}'