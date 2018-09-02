import os
import infosystem

from flask_cors import CORS


class System(infosystem.System):

    def __init__(self):
        super().__init__(
            # TODO Add here your resources            
            )

    def configure(self):
        origins_urls = os.environ.get('ORIGINS_URLS', '*')
        CORS(self, resources={r'/*': {'origins': origins_urls}})

        self.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))
        self.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        app_database_uri = os.getenv('APP_DATABASE_URI', None)
        if app_database_uri is None:
            # if enviroment variable is not defined use SQLite
            self.config['DBDIR'] = self.config['BASEDIR'] + '/db'
            if not os.path.exists(self.config['DBDIR']):
                os.makedirs(self.config['DBDIR'])

            self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                self.config['DBDIR'] + '/infosystem.db'
        else:
            # URL os enviroment example for MySQL
            # export APP_DATABASE_URI=
            # mysql+pymysql://root:mysql@localhost:3306/orlocal
            self.config['SQLALCHEMY_DATABASE_URI'] = app_database_uri
