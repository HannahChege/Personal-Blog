from app import create_app,db
from flask_script import Manager,Server
from app.models import Admin,Blog
from  flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = create_app('development')
app = create_app('test')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Admin = Admin, Blog= Blog )

if __name__ == '__main__':
    manager.run()