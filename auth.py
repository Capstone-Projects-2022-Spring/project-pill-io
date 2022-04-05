import os
from queue import Empty
import time

from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app, abort, logging, globals
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import sys

from models import User, UserForm, Medication, Prescription
from flask_login import login_user, logout_user, login_required, current_user

from __init__ import db, text_to_speech_1
from datetime import datetime
import calendar
from datetime import date


MAX_CONTENT_LENGTH = 1024 * 1024
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.PNG', '.JPG', '.JPEG']
UPLOAD_PATH = 'static/userimages'

# create a Blueprint object that we name 'auth'
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])  # define login page path
def login():  # define login page fucntion
    if request.method == 'GET':  # if the request is a GET we return the login page
        return render_template('login.html')
    else:  # if the request is POST the we check if the user exist and with te right password
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
            # if the user doesn't exist or password is wrong, reload the page
            return redirect(url_for('auth.login'))
        # if the above check passes, then we know the user has the right credentials

        login_user(user, remember=remember)
        to_say = ("hello" + current_user.first_name)
        text_to_speech_1(to_say)
        return userDash()



@auth.route('/signup', methods=['GET', 'POST'])  # we define the sign up path
def signup():  # define the sign up function
    if request.method == 'GET':  # If the request is GET we return the sign up page and forms
        return render_template('signup.html')
    else:  # if the request is POST, then we check if the email doesn't already exist and then we save data
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        dob = request.form.get('dob')
        # image file
        uploaded_file = request.files['image']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in UPLOAD_EXTENSIONS:  # disallowed extensions to be fixed!
                abort(400)
            # saves image to folder
            uploaded_file.save(os.path.join(UPLOAD_PATH, filename))
            image = UPLOAD_PATH + '/' + filename  # sets path for the user's profile image

        print(first_name + last_name + dob)
        print(password)

        # if this returns a user, then the email already exists in database
        user = User.query.filter_by(email=email).first()
        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        # use the recently uploaded file as the user's profile picture/face recognition picture
        new_user = User(email=email, first_name=first_name, last_name=last_name,
                        password=generate_password_hash(password, method='sha256'), dob=dob, image=image)

        # add the new user to the database
        flash('Account created! You can login now!! ')
        db.session.add(new_user)
        db.session.commit()

        result = User.query.filter_by(first_name=first_name).first()

        if not result:
            print
            'No result found'
        else:
            print(result)

        return redirect(url_for('auth.login'))

# medform page


@auth.route('/submitmeds', methods=['GET', 'POST'])
@login_required
def submitmeds():
    if request.method == 'GET':  # if the request is a GET we return the login page
        return render_template('medform.html')
    else:
        print('Test')
        medication_name = request.form.get('medication_name')
        medication_type = request.form.get('medication_type')
        medication_dose = request.form.get('medication_dose')
        medication_time = request.form.get('medication_time')
        if(medication_name == ''):
            notifError = "No Medication Name"
            return render_template('medform.html', notifError=notifError)
        elif(medication_type == ''):
            notifError = "No Medication Type"
            return render_template('medform.html', notifError=notifError)
        elif(medication_dose == ''):
            notifError = "No Medication Dose"
            return render_template('medform.html', notifError=notifError)
        elif(medication_time is None):
            notifError = "No Medication Time"
            return render_template('medform.html', notifError=notifError)
        # new_user = User(medication_name =email, first_name=first_name, last_name=last_name,
        #                 password=generate_password_hash(password, method='sha256'), dob=dob, image=image)

        new_medication = Medication(medication_name=medication_name, medication_type=medication_type,
                                    medication_dose=medication_dose, medication_time=medication_time)


        db.session.add(new_medication)
        db.session.commit()

        # result = Medication.query.filter_by(medication_name=medication_name).first()

        new_prescription = Prescription(
            user_id=current_user.id, medication_id=new_medication.medication_id)
        db.session.add(new_prescription)
        db.session.commit()

        if (request.form.get('medication_name2')):
            medication_name2 = request.form.get('medication_name2')
            medication_type2 = request.form.get('medication_type2')
            medication_dose2 = request.form.get('medication_dose2')
            medication_time2 = request.form.get('medication_time2')
            if(medication_name2 == ''):
                notifError = "No Medication Name 2"
                return render_template('medform.html', notifError=notifError)
            elif(medication_type2 == ''):
                notifError = "No Medication Type 2"
                return render_template('medform.html', notifError=notifError)
            elif(medication_dose2 == ''):
                notifError = "No Medication Dose 2"
                return render_template('medform.html', notifError=notifError)
            elif(medication_time2 is None):
                notifError = "No Medication Time 2"
                return render_template('medform.html', notifError=notifError)
            new_medication2 = Medication(medication_name=medication_name2, medication_type=medication_type2,
                                         medication_dose=medication_dose2, medication_time=medication_time2)


            db.session.add(new_medication2)
            db.session.commit()

            new_prescription2 = Prescription(
                user_id=current_user.id, medication_id=new_medication2.medication_id)
            db.session.add(new_prescription2)
            db.session.commit()
        else:
            print("Not Exist")
        if (request.form.get('medication_name3')):
            medication_name3 = request.form.get('medication_name3')
            medication_type3 = request.form.get('medication_type3')
            medication_dose3 = request.form.get('medication_dose3')
            medication_time3 = request.form.get('medication_time3')
            if(medication_name3 == ''):
                notifError = "No Medication Name 3"
                return render_template('medform.html', notifError=notifError)
            elif(medication_type3 == ''):
                notifError = "No Medication Type 3"
                return render_template('medform.html', notifError=notifError)
            elif(medication_dose3 == ''):
                notifError = "No Medication Dose 3"
                return render_template('medform.html', notifError=notifError)
            elif(medication_time3 is None):
                notifError = "No Medication Time 3"
                return render_template('medform.html', notifError=notifError)
            new_medication3 = Medication(medication_name=medication_name3, medication_type=medication_type3,
                                         medication_dose=medication_dose3, medication_time=medication_time3)
            db.session.add(new_medication3)
            db.session.commit()
            new_prescription3 = Prescription(
                user_id=current_user.id, medication_id=new_medication3.medication_id)
            db.session.add(new_prescription3)
            db.session.commit()
        else:
            print("Not Exist")
        #
        # if not result:
        #     print
        #     'No result found'
        # else:
        #     print(result)
        notif = "Success"
        return render_template('medform.html', notif = notif)
        # return redirect(url_for('main.profile'))


# settings page
@auth.route('/account', methods=['GET', 'POST'])  # define settings path
@login_required
def account():

    form = UserForm()

    if request.method == "POST":
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        current_user.email = request.form.get('email')
        current_user.dob = request.form.get('dob')
        #current_user.image = request.form.get('image')
        uploaded_file = request.files['image']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in UPLOAD_EXTENSIONS:  # disallowed extensions to be fixed!
                abort(400)
            # saves image to folder
            uploaded_file.save(os.path.join(UPLOAD_PATH, filename))
            image = UPLOAD_PATH + '/' + filename  #
            current_user.image = image

        print("mehh" + current_user.first_name + current_user.last_name)
        try:
            db.session.commit()
            return redirect(url_for('user.account'))
        except:
            flash("Error!  Looks like there was a problem...try again!")
    elif request.method == 'GET':
        print(current_user.id)
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.dob.data = current_user.dob
        db.session.commit()
        print("hello " + current_user.first_name + current_user.last_name)

    return render_template('Settings.html', form=form)


# userDash page
@auth.route('/userDash')  # define userdash
@login_required
def userDash():
    querySchedule = db.session.query(Medication)

    querySchedule = querySchedule.outerjoin(
        Prescription, Medication.medication_id == Prescription.medication_id)

    querySchedule = querySchedule.filter(
        Prescription.user_id == current_user.id)

    queryScheduleMorning = querySchedule.filter(
        Medication.medication_time == "Morning")
    
    queryScheduleNoon = querySchedule.filter(
        Medication.medication_time == "Noon")
    
    queryScheduleNight = querySchedule.filter(
        Medication.medication_time == "Night")

    results = queryScheduleMorning.all()
    results2 = queryScheduleNoon.all()
    results3 = queryScheduleNight.all()
    
    queryList = db.session.query(Medication)

    queryList = queryList.outerjoin(
        Prescription, Medication.medication_id == Prescription.medication_id)

    queryList = queryList.filter(Prescription.user_id == current_user.id)

    resultList = queryList.all()
    
    now = datetime.now().hour
    print(now);
    morning = datetime.now().hour
    morning = 6
    noon = datetime.now().hour
    noon = 12
    night = datetime.now().hour
    night = 18
    print(results)
    print("NEXT")
    print(queryScheduleMorning)
    alert =''
    if now > morning and now < noon:
        alert = "MORNING PILLS:"
        for x in results:
            alert += ' | ' + x.medication_name
    elif now > noon and now < night:
        alert= "NOON PILLS:"
        for x in results2:
            alert += ' | ' + x.medication_name
    else:
        alert = "NIGHT PILLS:"
        for x in results3:
            alert += ' | ' + x.medication_name
    alert += ' |'

    return render_template("userDash.html", queryScheduleMorning=results, queryScheduleNoon=results2, queryScheduleNight=results3, queryList=resultList, alert=alert)



@auth.route('/logout')  # define logout path
@login_required
def logout():  # define the logout function
    to_say = ("Good Bye" + current_user.first_name)
    text_to_speech_1(to_say)
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/webcam')  # define webcam path
@login_required
def webcam():
    return render_template('webcam.html')

@auth.route('/getmeds', methods=["GET", "POST"])
@login_required
def getmeds():
    if request.method == 'GET':
        query = db.session.query(Medication)

        query = query.outerjoin(
            Prescription, Medication.medication_id == Prescription.medication_id)

        query = query.filter(Prescription.user_id == current_user.id)

        results = query.all()

        print(results)

        return render_template("userDash.html", query=results)

    else:
        return render_template("userDash.html")
