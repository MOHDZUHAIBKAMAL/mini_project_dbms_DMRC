from flask import request
from driver_app.services.driver_service import DriverService
from driver_app.services.driver_service import DriverScheduleService
from views.driver_view import DriverView,DriverScheduleView

class DriverController:
    @staticmethod
    def get_all_drivers():
        drivers = DriverService.get_all_drivers()
        return DriverView.render_drivers(drivers), 200

    @staticmethod
    def get_driver(driver_id):
        driver = DriverService.get_driver_by_id(driver_id)
        if not driver:
            return DriverView.render_error('driver not found'), 404
        return DriverView.render_driver(driver), 200

    @staticmethod
    def create_driver():
        try:
            data = request.get_json()
            name = data.get('name')
            license_number = data.get('license_number')

            driver = DriverService.create_driver(name, license_number)
            return DriverView.render_success('Driver created successfully', driver.driver_id), 201

        except ValueError as e:
            return DriverView.render_error(str(e)), 400


    @staticmethod
    def delete_driver(driver_id):
        driver = DriverService.delete_driver(driver_id)
        if driver:
            return DriverView.render_success('driver deleted successfully', driver.driver_id), 200
        return DriverView.render_error('driver not found'), 404

    
class DriverScheduleController:
    @staticmethod
    def get_all_driver_schedules():
        driver_schedules = DriverScheduleService.get_all_driver_schedules()
        return DriverScheduleView.render_driver_schedules(driver_schedules), 200

    @staticmethod
    def get_driver_schedule(driver_schedule_id):
        driver_schedule = DriverScheduleService.get_driver_schedule_by_id(driver_schedule_id)
        if not driver_schedule:
            return DriverView.render_error('driver_schedule not found'), 404
        return DriverScheduleView.render_driver_schedule(driver_schedule), 200

    @staticmethod
    def create_driver_schedule():
        data = request.get_json()
        driver_id= data.get('driver_id')
        metro_id=data.get('metro_id')
        start_time=data.get('start_time')
        end_time=data.get('end_time')

        driver_schedule = DriverScheduleService.create_driver_schedule(driver_id,metro_id,start_time,end_time)
        return DriverScheduleView.render_success('driver_schedule created successfully', driver_schedule.schedule_id), 201

    @staticmethod
    def update_driver_schedule(driver_schedule_id):
        data = request.get_json()
        new_start_time = data.get('new_start_time')
        new_end_time=data.get('new_end_time')

        driver_schedule = DriverScheduleService.update_driver_schedule(driver_schedule_id, new_end_time,new_start_time)
        if driver_schedule:
            return DriverView.render_success('driver_schedule updated successfully', driver_schedule.schedule_id), 200
        return DriverView.render_error('driver_schedule not found'), 404

    @staticmethod
    def delete_driver_schedule(driver_schedule_id):
        driver_schedule = DriverScheduleService.delete_driver_schedule(driver_schedule_id)
        if driver_schedule:
            return DriverView.render_success('driver_schedule deleted successfully', driver_schedule.schedule_id), 200
        return DriverView.render_error('driver_schedule not found'), 404

    @staticmethod
    def get_driver_schedule_with_driver_id(driver_id):
        driver_schedule=DriverScheduleService.get_driver_schedule_by_driver_id(driver_id)
        if not driver_schedule:
            return DriverView.render_error('driver_schedule not found'), 404
        return DriverScheduleView.render_driver_schedule(driver_schedule), 200
    
    @staticmethod
    def get_schedules_by_metro(metro_id):
        driver_schedules = DriverScheduleService.get_schedules_by_metro(metro_id)
        if not driver_schedules:
            return DriverView.render_error('No driver schedules found for the specified metro line'), 404
        return DriverScheduleView.render_driver_schedules(driver_schedules), 200