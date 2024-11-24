from shared.models.metro_model import Metro,Station
from shared.utils.db_utils import db
from flask import request

class MetroService:
    @staticmethod
    def create_metro(line_name,start_station,end_station):
        new_metro = Metro(line_name=line_name, start_station=start_station, end_station=end_station)
        db.session.add(new_metro)
        db.session.commit()

        return new_metro

    @staticmethod
    def get_metro_by_metro_id(station_id):
        return Metro.query.filter_by(station_id=station_id).first()

    @staticmethod
    def get_all_metros():
        return Metro.query.all()


    @staticmethod
    def delete_metro(station_id):
        station=Metro.query.filter_by(station_id=station_id).first()
        db.session.delete(station)
        db.session.commit()
        return station
    


class StationService:
    @staticmethod
    def create_station(station_name, metro_id, interchange):
        # Create and save a new station
        station = Station(station_name=station_name, line_id=metro_id, interchange=interchange)
        db.session.add(station)
        db.session.commit()
        return station

    @staticmethod
    def get_station_by_station_id(station_id):
        # Fetch the station by ID
        return Station.query.filter_by(station_id=station_id).first()

    @staticmethod
    def get_all_stations():
        # Fetch all stations
        return Station.query.all()

    @staticmethod
    def delete_station(station_id):
        # Delete a station by ID
        station = Station.query.filter_by(station_id=station_id).first()
        if station:
            db.session.delete(station)
            db.session.commit()
        return station

    @staticmethod
    def get_stations_by_metro(metro_id):
        # Fetch all stations by metro ID
        return Station.query.filter_by(line_id=metro_id).all()

    @staticmethod
    def get_interchange_stations():
        # Fetch all stations that are interchange stations
        return Station.query.filter_by(interchange=True).all()
    
    @staticmethod
    def link_stations(station_id,previous_station_id,next_station_id):
        # Fetch the current station
        station = Station.query.get(station_id)
        if not station:
            raise ValueError(f"Station with ID {station_id} not found.")

        # Update previous station link
        if previous_station_id is not None:
            previous_station = Station.query.get(previous_station_id)
            if not previous_station:
                raise ValueError(f"Previous station with ID {previous_station_id} not found.")
            station.previous_station_id = previous_station_id
            previous_station.next_station_id = station_id
        else:
            # If no previous station, set the field to NULL
            station.previous_station_id = None

        # Update next station link
        if next_station_id is not None:
            next_station = Station.query.get(next_station_id)
            if not next_station:
                raise ValueError(f"Next station with ID {next_station_id} not found.")
            station.next_station_id = next_station_id
            next_station.previous_station_id = station_id
        else:
            # If no next station, set the field to NULL
            station.next_station_id = None

        # Commit all changes
        db.session.commit()
        final_station=Station.query.get(station_id)
        return final_station
