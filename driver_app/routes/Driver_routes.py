from flask import Blueprint
from driver_app.controllers.driver_controller import DriverController,DriverScheduleController

driver_bp = Blueprint('driver_bp', __name__)

@driver_bp.route('/api/drivers', methods=['GET'])
def get_all_drivers():
    return DriverController.get_all_drivers()

@driver_bp.route('/api/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    return DriverController.get_driver(driver_id)

@driver_bp.route('/api/drivers', methods=['POST'])
def create_driver():
    return DriverController.create_driver()

@driver_bp.route('/api/drivers/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    return DriverController.update_driver(driver_id)

@driver_bp.route('/api/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    return DriverController.delete_driver(driver_id)


@driver_bp.route('/api/driver/schedules', methods=['GET'])
def get_all_driver_schedules():
    return DriverScheduleController.get_all_driver_schedules()

@driver_bp.route('/api/driver/schedule/<int:driver_schedule_id>', methods=['GET'])
def get_driver_schedule(driver_schedule_id):
    return DriverScheduleController.get_driver_schedule(driver_schedule_id)

@driver_bp.route('/api/driver/schdedule', methods=['POST'])
def create_driver_schedule():
    return DriverScheduleController.create_driver_schedule()

@driver_bp.route('/api/driver/schedule/<int:driver_schedule_id>', methods=['PUT'])
def update_driver_schedule(driver_schedule_id):
    return DriverScheduleController.update_driver_schedule(driver_schedule_id)

@driver_bp.route('/api/driver/schedule/<int:driver_schedule_id>', methods=['DELETE'])
def delete_driver_schedule(driver_schedule_id):
    return DriverScheduleController.delete_driver_schedule(driver_schedule_id)

@driver_bp.route('/driver/schedules/metro/<int:metro_id>', methods=['GET'])
def get_schedules_by_metro(metro_id):
    return DriverScheduleController.get_schedules_by_metro(metro_id)

