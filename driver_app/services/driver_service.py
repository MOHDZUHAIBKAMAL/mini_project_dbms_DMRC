from shared.models.driver_model import Driver
from shared.utils.db_utils import db
from shared.models.driver_model import DriverSchedule
from views.driver_view import DriverView,DriverScheduleView
from datetime import datetime

class DriverService:
    @staticmethod
    def create_driver(name, license_number):
        # Step 1: Check if a driver with the same name and license number already exists
        existing_driver = Driver.query.filter_by(name=name, license_number=license_number).first()
        if existing_driver:
            raise ValueError(f"A driver with the name '{name}' and license number '{license_number}' already exists.")

        # Step 2: Create a new driver if no existing driver is found
        new_driver = Driver(name=name, license_number=license_number)
        db.session.add(new_driver)
        db.session.commit()

        return new_driver



    @staticmethod
    def get_driver_by_id(driver_id):
        return Driver.query.filter_by(driver_id=driver_id).first()

    @staticmethod
    def get_drivers_by_user(user_id):
        return Driver.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_drivers():
        return Driver.query.order_by(Driver.hired_date.desc()).all()

    @staticmethod
    def delete_driver(driver_id):
        driver = Driver.query.filter_by(driver_id=driver_id).first()
        if driver:
            db.session.delete(driver)
            db.session.commit()
        return driver

class DriverScheduleService:
    @staticmethod
    def create_driver_schedule(driver_id, metro_id, start_time, end_time):
        # Convert string time to datetime if necessary
        if isinstance(start_time, str):
            start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
        if isinstance(end_time, str):
            end_time = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S")

        # Step 1: Fetch existing schedules for the given metro_id
        existing_schedules = DriverSchedule.query.filter_by(metro_id=metro_id).order_by(DriverSchedule.end_time).all()

        # Step 2: Validate new schedule
        for schedule in existing_schedules:
            if not (end_time < schedule.start_time or start_time > schedule.end_time):
                # If the new schedule overlaps with an existing schedule
                raise ValueError(f"Shift overlaps with existing schedule: {schedule.start_time} to {schedule.end_time}")

        # Step 3: If no conflicts, create the new schedule
        new_schedule = DriverSchedule(
            driver_id=driver_id,
            metro_id=metro_id,
            start_time=start_time,
            end_time=end_time
        )

        db.session.add(new_schedule)
        db.session.commit()

        return new_schedule
    
    @staticmethod
    def get_driver_schedule_by_id(schedule_id):
        return DriverSchedule.query.filter_by(schedule_id=schedule_id).first()
    
    @staticmethod
    def get_driver_schedule_by_driver_id(driver_id):
        return DriverSchedule.query.filter_by(driver_id=driver_id).first()
    
    @staticmethod
    def get_all_driver_schedules():
        return DriverSchedule.query.order_by(DriverSchedule.start_time.desc()).all()
    
    @staticmethod
    def update_driver_schedule(schedule_id, new_start_time,new_end_time):
        driver_schedule = DriverSchedule.query.filter_by(schedule_id=schedule_id).first()
        if driver_schedule:
            driver_schedule.start_time=new_start_time
            driver_schedule.endt_time=new_end_time
            db.session.commit()
        return driver_schedule
    
    @staticmethod
    def delete_driver_schedule(schedule_id):
        driver_schedule = DriverSchedule.query.filter_by(schedule_id=schedule_id).first()
        if driver_schedule:
            db.session.delete(driver_schedule)
            db.session.commit()
        return driver_schedule

    @staticmethod
    def get_schedules_by_metro(metro_id):
        return DriverSchedule.query.filter_by(metro_id=metro_id).all()