from flask_testing import TestCase
from app.main import db
from manage import app


class BaseTestCase(TestCase):
    """
    Base Test
    sets up our test environment ready 
    before and after every test case that extends it
    """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()