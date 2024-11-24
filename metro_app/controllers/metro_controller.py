from flask import request
from metro_app.services.metro_service import MetroService,StationService
from metro_app.views.metro_view import MetroView,StationView
from shared.models.metro_model import Metro

class MetroController:
    # Create a new metro
    @staticmethod
    def create_metro():
        data = request.get_json()
        line_name = data.get('line_name')
        start_station = data.get('start_station')
        end_station = data.get('end_station')

        # Call service to create a metro
        metro = MetroService.create_metro(line_name, start_station, end_station)

        return MetroView.render_metro(metro), 201

    # Get metro details by metro ID
    @staticmethod
    def get_metro_by_id(metro_id):
        metro = MetroService.get_metro_by_metro_id(metro_id)
        if metro:
            return MetroView.render_metro(metro), 200
        else:
            return MetroView.render_error("Metro not found"), 404

    # Get all metros
    @staticmethod
    def get_all_metros():
        metros = MetroService.get_all_metros()
        return MetroView.render_metros(metros), 200

    # Delete metro by metro ID
    @staticmethod
    def delete_metro(metro_id):
        metro = MetroService.delete_metro(metro_id)
        if metro:
            return MetroView.render_metro(metro), 200
        else:
            return MetroView.render_error("Metro not found"), 404

class StationController:
    # Create a new station
    @staticmethod
    def create_station():
        data = request.get_json()
        station_name = data.get('station_name')
        line_name = data.get('line_name')  # The metro line to associate with the station
        interchange = data.get('interchange', False)  # If the station is an interchange station

        # Fetch the metro line by name
        metro = Metro.query.filter_by(line_name=line_name).first()

        if not metro:
            return StationView.render_error("Metro line not found"), 404

        # Call service to create a station
        station = StationService.create_station(station_name, metro.metro_id, interchange)

        return StationView.render_station(station), 201

    # Get station details by station ID
    @staticmethod
    def get_station_by_id(station_id):
        station = StationService.get_station_by_station_id(station_id)
        if station:
            return StationView.render_station(station), 200
        else:
            return StationView.render_error("Station not found"), 404

    # Get all stations
    @staticmethod
    def get_all_stations():
        stations = StationService.get_all_stations()
        return StationView.render_stations(stations), 200

    # Delete station by station ID
    @staticmethod
    def delete_station(station_id):
        station = StationService.delete_station(station_id)
        if station:
            return StationView.render_station(station), 200
        else:
            return StationView.render_error("Station not found"), 404

    # Get stations by metro ID
    @staticmethod
    def get_stations_by_metro(metro_id):
        stations = StationService.get_stations_by_metro(metro_id)
        return StationView.render_stations(stations), 200

    # Get all interchange stations
    @staticmethod
    def get_interchange_stations():
        stations = StationService.get_interchange_stations()
        return StationView.render_stations(stations), 200
    
    @staticmethod
    def link_stations():
        data=request.get_json()
        station_id = data['station_id']
        previous_station_id = data.get('previous_station_id')
        next_station_id = data.get('next_station_id')

        link=StationService.link_stations(station_id,previous_station_id,next_station_id)
        if link:
            return StationView.render_station(link), 200
        else:
            return StationView.render_error("Station not found"), 404
