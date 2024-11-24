from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate
from shared.models.driver_model import Driver,DriverSchedule
from shared.models.metro_model import Metro,Station
from shared.models.user_model import Fare,Route


# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9811@localhost/DMRC'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

