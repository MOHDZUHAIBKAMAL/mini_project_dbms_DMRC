from flask import Blueprint
from user_app.controllers.user_controller import RouteController,FareController

route_bp = Blueprint('route_bp', __name__)

@route_bp.route('/fastest_route', methods=['GET'])
def get_fastest_route():
    return RouteController.get_fastest_route()

@route_bp.route('/api/fare',methods=['GET'])
def get_fare():
    return FareController.get_fare()