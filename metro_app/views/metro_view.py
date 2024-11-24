class MetroView:
    @staticmethod
    def render_metro(metro):
        return {
            "metro_id": metro.metro_id,
            "line_name": metro.line_name,
            "start_station": metro.start_station,
            "end_station": metro.end_station
        }




    @staticmethod
    def render_metros(metros):
        return [ MetroView.render_metro(metro) for metro in metros]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, metro_id=None):
        response = {"message": message}
        if metro_id:
            response["user_id"] = metro_id
        return response
    
class StationView:
    @staticmethod
    def render_station(station):
        return {
            "station_id": station.station_id,
            "station_name": station.station_name,
            "line_id": station.line_id,
            "interchange": station.interchange,
            "prev_station_id":station.prev_station_id,
            "next_station_id":station.next_station_id,
            "created_at":station.created_at,
            "updated_at":station.updated_at
        }
    
    @staticmethod
    def render_stations(stations):
        return [ StationView.render_station(station) for station in stations]
    
    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, metro_id=None):
        response = {"message": message}
        if metro_id:
            response["user_id"] = metro_id
        return response

