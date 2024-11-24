import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from driver_app.routes.Driver_routes import driver_bp
from shared.utils.db_utils import db

from shared.models.user_model import Fare,Route  
from shared.models.metro_model import Metro,Station
from shared.models.driver_model import Driver,DriverSchedule
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9811@localhost/DMRC'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(driver_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)