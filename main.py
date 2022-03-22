import flask_login
from flask import Flask, render_template, url_for,redirect,request
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db



# our main blueprint
main = Blueprint('main', __name__, static_url_path='/static')

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    #flask_login.current_user
    return render_template('profile.html', header_name = current_user)

@main.route('/help') # profile page that return 'profile'
@login_required
def help():
    return render_template('help.html')


app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app = create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode
    # user image upload directory and allowed image extensions and dimensions
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    app.config['UPLOAD_PATH'] = 'userimages'