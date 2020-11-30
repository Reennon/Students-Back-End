
import main
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

def run(api):


    api.run(host="127.0.0.2")




if __name__ == "__main__":

    api = main.create_app()
    #run(api)

    migrate = Migrate(api, main.db)
    maneger = Manager(api)
    maneger.add_command('db', MigrateCommand)
    maneger.run()



