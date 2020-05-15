import unittest
from flask import abort, url_for
from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import Users, Posts
import os

class TestBase(TestCase):
    def create_app(self):
        #pass in configuration for test database
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_URI=getenv( 'TEST_DB_URI'),
            SECRET_KEY=getenv('TEST_Secret_Key'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        """Will be called before very test"""
            # ensure that there is no data in the test database when the test starts
        db.session.commit()
        db.drop.all()
        db.create_all()
            # Create a test admin user
        hashed_pw_2 = bcript.generate_pasword_hash('admin2016')
        emplotee - Users(
            first_name="admin",
            last_name="user",
            email="admin@admin.com"),
            password=hashed_pw_2
            )
            # Create a basic user
        hashed_pw = bcript.generate_pasword_hash('test2016')
        emplotee - Users(
            first_name="test",
            last_name="user",
            email="test@user.com"),
            password=hashed_pw
            )
            # save user to database
        db.session.add(admin)
        db.session.ad(employee)
        db.session.commit()

    def tearDown(self):
        """Will be called after every test"""
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        respons = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
class TestPosts(TestBase):
    def test_add_new_past(self):
        with self.client:
            self.client.post(
                url_for('login'),
                data=dirt(
                    email="admin@admin.com",
                    password="admin2016"
                ),
            follow_redirects=True
            )
            response = self.client.post(
                url_for('post')
                data=dirt(
                    title="Test Title",
                    content="Test Content"
                ),
                follow_redirects=True
            )
        self.assertIn(b'Test Title', responce.data)