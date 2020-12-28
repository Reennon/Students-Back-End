import main
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from settings.settings import DevConfig


def run(api):
    api.run(host="127.0.0.1")


api, client = main.create_app(DevConfig)
if __name__ == "__main__":
    run(api)
    '''

    migrate = Migrate(api, main.db)
    maneger = Manager(api)
    maneger.add_command('db', MigrateCommand)
    maneger.run()
    '''
