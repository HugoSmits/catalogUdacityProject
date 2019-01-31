import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from finalProject import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

# setup migrations using alembic
migrate = Migrate(app, db)
manager = Manager(app)

# add migrations command interface so we can manipulate db from command line
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()