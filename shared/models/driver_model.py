from datetime import datetime
from shared.utils.db_utils import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

class Driver(db.Model):
    __tablename__ = 'drivers'

    driver_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(100), nullable=False)
    hired_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    driver_schedule = relationship('DriverSchedule', back_populates='driver', cascade="all, delete-orphan")


class DriverSchedule(db.Model):
    __tablename__ = 'driver_schedules'

    schedule_id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'), nullable=False)
    metro_id = db.Column(db.Integer, db.ForeignKey('metros.metro_id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    driver = relationship('Driver', back_populates='driver_schedule')
    metro = relationship('Metro', back_populates='driver_schedule')