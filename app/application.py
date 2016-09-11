import os
import uuid

from infosystem.common import authorization
from infosystem import database
from flask import Flask
from infosystem import system as system_module


app = Flask(__name__)
app.config['BASEDIR'] = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['BASEDIR'] + '/infosystem.db'

system = system_module.System([
    # TODO List here your modules
    ]
)

database.db.init_app(app)
with app.app_context():
    database.db.create_all()

for subsystem in system.subsystems.values():
    app.register_blueprint(subsystem)

def protect():
    return authorization.protect(system)

app.before_request(protect)

def load_app():
    return app
