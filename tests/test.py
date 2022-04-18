import unittest

import os
from io import BytesIO
from queue import Empty
import time

from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app, abort, logging, globals
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import sys

from models import User, UserForm, Medication, Prescription
from flask_login import login_user, logout_user, login_required, current_user

from __init__ import db, text_to_speech_1, create_app
from datetime import datetime
import calendar
from datetime import date

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['WTF_CSRF_ENABLED'] = False  # no CSRF during tests
        self.appctx = self.app.app_context()
        self.appctx.push()
        #db.create_all()
        self.client = self.app.test_client()


    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_home_page_redirect(self):
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/login'

    def test_registration_form(self):
        response = self.client.get('/signup')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # make sure all the fields are included
        assert 'name="first_name"' in html
        assert 'name="last_name"' in html
        assert 'name="email"' in html
        assert 'name="password"' in html
        #assert 'type = "submit"' in html

    def test_register_user(self):

        with open('../static/userimages/test_image.png', 'rb') as img1:
            imgStringIO1 = BytesIO(img1.read())

        response = self.client.post('/signup', content_type='multipart/form-data', data={
            'first_name': 'alice',
            'last_name': 'wonderland',
            'email': 'alice@example.com',
            'dob': '01/02/1997',
            'password': 'foo123',
            'image': (imgStringIO1, 'img1.png')
        }, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/signup'  # redirected to login

    def test_login(self):
        # login with new user
        response = self.client.post('/login', data={
            'username': 'abin@gmail.com',
            'password': '123456',
        }, follow_redirects=True)
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        #assert 'Hi, alice!' in html

    def test_register_user_mismatched_passwords(self):
        response = self.client.post('/login', data={
            'username': 'abin@gmail.com',
            'password': 'foo'
        })
        assert response.status_code == 302
        html = response.get_data(as_text=True)
        assert response.request.path == '/login'