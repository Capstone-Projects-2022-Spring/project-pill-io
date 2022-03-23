import os

from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app, abort, logging, globals
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import jsonify
import sys

from models import User, Medication, Prescription
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db

MAX_CONTENT_LENGTH = 1024 * 1024
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
UPLOAD_PATH = 'static/userimages'

auth = Blueprint('auth', __name__) # create a Blueprint object that we name 'auth'

@auth.route('/login', methods=['GET', 'POST']) # define login page path
def login(): # define login page fucntion
    if request.method=='GET': # if the request is a GET we return the login page
        return render_template('login.html')
    else: # if the request is POST the we check if the user exist and with te right password
        email = request.form.get('email')

        password = request.form.get('password')

        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        print(user)
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flash('Please sign up before!')

            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials


        login_user(user, remember=remember)
        return redirect(url_for('main.medform'))

@auth.route('/signup', methods=['GET', 'POST'])# we define the sign up path
def signup(): # define the sign up function
    if request.method=='GET': # If the request is GET we return the sign up page and forms
        return render_template('signup.html')
    else: # if the request is POST, then we check if the email doesn't already exist and then we save data
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        dob = request.form.get('dob')
        #image file
        uploaded_file = request.files['image']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in UPLOAD_EXTENSIONS: # disallowed extensions to be fixed!
                abort(400)
            uploaded_file.save(os.path.join(UPLOAD_PATH, filename)) # saves image to folder
            image = UPLOAD_PATH + '/' + filename # sets path for the user's profile image

        print(first_name + last_name+ dob)
        print(password)

        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
        if user: # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        # use the recently uploaded file as the user's profile picture/face recognition picture
        new_user = User(email=email, first_name= first_name, last_name = last_name,
                        password=generate_password_hash(password, method='sha256'), dob = dob, image = image)

        # add the new user to the database
        flash('Account created! You can login now!! ')
        db.session.add(new_user)
        db.session.commit()

        result = User.query.filter_by(first_name = first_name).first()

        if not result:
            print
            'No result found'
        else:
            print (result)

        return redirect(url_for('auth.login'))

#medform page

@auth.route('/submitmeds', methods=['GET', 'POST'])
@login_required
def submitmeds():
    if request.method=='GET': # if the request is a GET we return the login page
        return render_template('profile.html')
    else:
        print ('Test')
        medication_name = request.form.get('medication_name')
        medication_type = request.form.get('medication_type')
        medication_dose = request.form.get('medication_dose')
        medication_time = request.form.get('medication_time')

        # new_user = User(medication_name =email, first_name=first_name, last_name=last_name,
        #                 password=generate_password_hash(password, method='sha256'), dob=dob, image=image)

        new_medication = Medication(medication_name=medication_name, medication_type=medication_type,
                                    medication_dose=medication_dose, medication_time=medication_time)

        flash('Medication created!')
        db.session.add(new_medication)
        db.session.commit()

        result = Medication.query.filter_by(medication_name=medication_name).first()

        new_prescription = Prescription(user_id=current_user.id, medication_id=new_medication.medication_id)
        db.session.add(new_prescription)
        db.session.commit()

        if not result:
            print
            'No result found'
        else:
            print(result)
        return render_template('medform.html')
        # return redirect(url_for('main.profile'))

#settings page
@auth.route('/account') # define logout path
@login_required
def account():

    return render_template('Settings.html')

#userDash page
@auth.route('/userDash') # define logout path
@login_required
def userDash():

    return render_template('userDash.html')



@auth.route('/logout') # define logout path
@login_required
def logout(): #define the logout function
    logout_user()
    return redirect(url_for('main.index'))
