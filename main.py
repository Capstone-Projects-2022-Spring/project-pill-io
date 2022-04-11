import flask_login
import pyttsx3
from flask import Flask, render_template, url_for,redirect,request
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db , text_to_speech_1
from flask import jsonify
# import jyserver.Flask as jsf


# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def medform():
    #flask_login.current_user
    TEMPLATES_AUTO_RELOAD = False
    return render_template('medform.html', header_name = current_user)


@main.route('/help') # profile page that return 'profile'
@login_required
def help():
    return render_template('help.html')


@main.route('/userdash') # profile page that return 'profile'
@login_required
def userDash():
    return render_template('userDash.html')


app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    #text_to_speech("hello what is up people")
    db.create_all(app = create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode

    #text_to_speech_1("hello what is up")
    # user image upload directory and allowed image extensions and dimensions
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    app.config['UPLOAD_PATH'] = 'static/userimages'