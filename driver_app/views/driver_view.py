class DriverView:
    @staticmethod
    def render_driver(driver):
        return {
            "post_id": driver.driver_id,
            "user_id": driver.name,
            "content": driver.license_number,
            "created_at": driver.hired_date
        }

    @staticmethod
    def render_drivers(drivers):
        return [DriverView.render_driver(driver) for driver in drivers]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, driver_id=None):
        response = {"message": message}
        if driver_id:
            response["driver_id"] = driver_id
        return response
    
class DriverScheduleView:
    @staticmethod
    def render_driver_schedule(driver_schedule):
        return{
            "schedule_id":driver_schedule.schedule_id,
            "driver_id":driver_schedule.driver_id,
            "metro_id":driver_schedule.metro_id,
            "start_time":driver_schedule.start_time,
            "end_time":driver_schedule.end_time
        }

    @staticmethod
    def render_driver_schedules(deriver_schedules):
         return [DriverScheduleView.render_driver_schedule(driver_schedule) for driver_schedule in deriver_schedules]


    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, driver_id=None):
        response = {"message": message}
        if driver_id:
            response["Schedule_id"] = driver_id
        return response
