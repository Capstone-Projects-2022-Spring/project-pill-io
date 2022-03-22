from flask_login import UserMixin
from __init__ import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    dob = db.Column(db.String(100))
    image = db.Column(db.String(200))


class Medication(db.Model):
    medication_id = db.Column(db.Integer, primary_key=True)
    medication_type = db.Column(db.String(100))
    medication_name = db.Column(db.String(100))
    medication_dose = db.Column(db.Integer)
    medication_time = db.Column(db.String(100))


class Prescription(db.Model):
    prescription_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    medication_id = db.Column(db.Integer)
