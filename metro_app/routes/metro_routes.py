from flask import Blueprint
from metro_app.controllers.metro_controller import MetroController,StationController

# Create a blueprint for Metro routes
metro_bp = Blueprint('metro', __name__)

# Metro Routes

# Get all metros (GET)
@metro_bp.route('/metros', methods=['GET'])
def get_all_metros():
    return MetroController.get_all_metros()

# Get a specific metro by ID (GET)
@metro_bp.route('/metro/<int:metro_id>', methods=['GET'])
def get_metro(metro_id):
    return MetroController.get_metro_by_id(metro_id)

# Create a metro (POST)
@metro_bp.route('/metro', methods=['POST'])
def create_metro():
    return MetroController.create_metro()

# Delete a metro by ID (DELETE)
@metro_bp.route('/metro/<int:metro_id>', methods=['DELETE'])
def delete_metro(metro_id):
    return MetroController.delete_metro(metro_id)


# Station Routes

# Get all stations (GET)
@metro_bp.route('/stations', methods=['GET'])
def get_all_stations():
    return StationController.get_all_stations()

# Get a specific station by ID (GET)
@metro_bp.route('/station/<int:station_id>', methods=['GET'])
def get_station(station_id):
    return StationController.get_station(station_id)

# Create a station (POST)
@metro_bp.route('/station', methods=['POST'])
def create_station():
    return StationController.create_station()

# Delete a station by ID (DELETE)
@metro_bp.route('/station/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    return StationController.delete_station(station_id)

# Get stations by metro ID (GET)
@metro_bp.route('/stations/metro/<int:metro_id>', methods=['GET'])
def get_stations_by_metro(metro_id):
    return StationController.get_stations_by_metro(metro_id)

# Get interchange stations (GET)
@metro_bp.route('/stations/interchanges', methods=['GET'])
def get_interchange_stations():
    return StationController.get_interchange_stations()

@metro_bp.route('/stations/link', methods=['POST'])
def link_station():
    return StationController.link_stations()



