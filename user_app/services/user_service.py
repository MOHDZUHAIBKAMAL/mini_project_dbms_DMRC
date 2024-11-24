
from shared.models.metro_model import Station,Metro
from shared.models.user_model import Fare,Route
from shared.utils.db_utils import db
from sqlalchemy import or_

class RouteService:
    @staticmethod
    def get_fastest_route_with_details(start_station_id, end_station_id):
        start_station = Station.query.filter_by(station_id=start_station_id).first()
        end_station = Station.query.filter_by(station_id=end_station_id).first()

        if not start_station or not end_station:
            return {"message": "Stations not found"}, 404

        # Initialize variables
        route_details = []
        current_station = start_station
        current_line = None

        # If both stations are on the same line, we can directly calculate the route
        if start_station.line_id == end_station.line_id:
            # Traverse from start to end (forward direction)
            route = RouteService.get_route_in_direction(start_station, end_station)
            
            for station in route:
                # Check if line changes
                if current_line != station.line_id:
                    if current_line:
                        direction_msg = f"Switch to {station.metro.line_name} at {current_station.station_name}, going towards {station.station_name}"
                    else:
                        direction_msg = f"Start your journey on {station.metro.line_name} at {current_station.station_name}, going towards {station.station_name}"
                    route_details.append({"message": direction_msg})

                route_details.append({
                    "station_name": station.station_name,
                    "line_name": station.metro.line_name,
                    "direction": f"towards {station.station_name}"
                })

                # Update the current station and line
                current_station = station
                current_line = station.metro.line_name

            # Add final station to route details
            route_details.append({
                "station_name": current_station.station_name,
                "line_name": current_line,
                "direction": f"towards {end_station.station_name}"
            })

            return {
                "message": "Fastest route found",
                "data": {
                    "start_station": start_station.station_name,
                    "end_station": end_station.station_name,
                    "stations_on_route": route_details
                }
            }

        else:
            # If stations are on different lines, we need to find the transfer stations
            # For simplicity, we will assume a direct transfer logic exists
            # You can expand this logic to handle multiple transfers

            route_with_transfer = RouteService.get_route_with_transfer(start_station, end_station)
            
            for station in route_with_transfer:
                route_details.append({
                    "station_name": station.station_name,
                    "line_name": station.metro.line_name,
                    "direction": f"towards {station.next_station.station_name if station.next_station else 'End'}"
                })

            return {
                "message": "Route with transfer found",
                "data": {
                    "start_station": start_station.station_name,
                    "end_station": end_station.station_name,
                    "stations_on_route": route_details
                }
            }

    @staticmethod
    def get_route_in_direction(start_station, end_station):
        # Traverse stations in order and return the stations between start and end
        route = []
        current_station = start_station
        while current_station != end_station:
            route.append(current_station)
            current_station = current_station.next_station  # Follow the direction to the next station
        route.append(end_station)
        return route

    @staticmethod
    def get_route_with_transfer(start_station, end_station):
        # Simplified transfer logic - can be extended with more complex route-finding algorithms
        route = []
        current_station = start_station
        while current_station != end_station:
            route.append(current_station)
            # Find the next station considering line transfers
            current_station = current_station.next_station
        route.append(end_station)
        return route
    
class FareService:
    @staticmethod
    def calculate_fare(start_station_id, end_station_id):
        # Get the fastest route details
        route_details = RouteService.get_fastest_route_with_details(start_station_id, end_station_id)

        if not route_details:
            return {"message": "Route not found"}, 404

        # Count the number of stations in the route (including start and end stations)
        num_stations = len(route_details['data']['stations_on_route'])

        # Calculate the fare (2.5 per station, or modify as per your fare policy)
        total_fare = num_stations * 2.5  # Example fare calculation: 2.5 per station

        return {"message": "Fare calculated", "fare": total_fare}

