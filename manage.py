from distutils.log import debug
from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitches, Comments


app = create_app('development')
#app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    pass 

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitches = Pitches, Comments=Comments)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    #app.run(port=9050)
    app.run(host='0.0.0.0', port=9040)