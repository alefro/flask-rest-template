import os
import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from gunicorn.app.base import Application

from app import app
from app.models import db
from config import BASE_DIR, HOST, PORT, GUNICORN_WORKERS, LOG_LEVEL


file_log = logging.FileHandler(os.path.join(BASE_DIR, 'logs/application.log'))
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s]  * %(message)s',
                    level=LOG_LEVEL, handlers=[file_log])

migrate = Migrate(app, db)
manager = Manager(app)


@manager.command
def gunicorn():
    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': '{}:{}'.format(HOST, PORT),
                'workers': GUNICORN_WORKERS
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    logging.debug("Start Flask server.")
    manager.run()
