from flask_login import UserMixin
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, InputRequired

from __init__ import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100),nullable=False)
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    dob = db.Column(db.String(100))
    image = db.Column(db.String(200),nullable=False)

    def init(self, email, first_name, last_name, dob, image):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.image = image
        def repr(self):
            return f"Username {self.first_name}"

class UserForm(FlaskForm):
            first_name = StringField('First Name')
            last_name = StringField("Last Name")
            email = StringField("Email")
            dob = StringField("dob")
            profile_pic = FileField("Profile Pic")
            submit = SubmitField("submit")



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
