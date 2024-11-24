class RouteView:
    
    @staticmethod
    def render_route_details(route_details):
        # Format the route details into a presentable format
        # You can format it as needed for the API response
        return {
            "start_station": route_details["start_station"],
            "end_station": route_details["end_station"],
            "stations_on_route": route_details["stations_on_route"]
        }

    @staticmethod
    def render_error(message):
        return {"message": message}, 404

    @staticmethod
    def render_success(message, data=None):
        response = {"message": message}
        if data:
            response["data"] = data
        return response, 200
    
class FareView:
    @staticmethod
    def render_fare(fare):
        return {
            'fare': fare
        }

    @staticmethod
    def render_error(message):
        return {
            'error': message
        }
    @staticmethod
    def render_success(message, data=None):
        response = {"message": message}
        if data:
            response["data"] = data
        return response, 200
