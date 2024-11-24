from flask import request
from user_app.services.user_service import RouteService,FareService
from user_app.views.user_view import RouteView,FareView

class RouteController:
    
    @staticmethod
    def get_fastest_route():
            # Get the start and end station IDs from the request
            data = request.get_json()
            start_station_id = data.get('start_station_id')
            end_station_id = data.get('end_station_id')

            # Call the service layer to compute the fastest route with details
            result = RouteService.get_fastest_route_with_details(start_station_id, end_station_id)
            
            if "message" in result and result["message"] == "Stations not found":
                return RouteView.render_error("Stations not found"), 404
            elif "message" in result and result["message"] == "No available routes for this trip":
                return RouteView.render_error("No available routes for this trip"), 404

            # Return the response with the fastest route details
            return RouteView.render_route_details(result["data"]), 200



class FareController:
    @staticmethod
    def get_fare():
        # Get the data from the request
        data = request.get_json()
        start_station_id = data.get('start_station_id')
        end_station_id = data.get('end_station_id')

        # Call the service to calculate the fare
        fare = FareService.calculate_fare(start_station_id, end_station_id)

        if fare is None:
            return FareView.render_error('Route not found or invalid stations'), 404
        
        return FareView.render_fare(fare), 200
