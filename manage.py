import os
import unittest

from app import blueprint

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db

from app.main.model import user
from app.main.model import blacklist
from app.main.model import cart
from app.main.model import item
from app.main.model import cart_item
# from app.main.model import closet
# from app.main.model import order

from flask_cors import CORS

app = create_app(os.getenv('FLASK_ENV'))
CORS(app)
# app.config.from_object('app.main.config.TestingConfig')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
