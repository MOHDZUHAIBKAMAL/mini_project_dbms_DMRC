from datetime import datetime
from shared.utils.db_utils import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

class Metro(db.Model):
    __tablename__ = 'metros'

    metro_id = db.Column(db.Integer, primary_key=True)
    line_name = db.Column(db.String(100), nullable=False)
    start_station = db.Column(db.String(100), nullable=False)
    end_station = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    routes = relationship('Route', back_populates='metro', cascade="all, delete-orphan")
    driver_schedule = relationship('DriverSchedule', back_populates='metro', cascade="all, delete-orphan")
    stations = relationship('Station', back_populates='metro', cascade="all, delete-orphan")

class Station(db.Model):
    __tablename__ = 'stations'

    station_id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(100), nullable=False)
    line_id = db.Column(db.Integer, db.ForeignKey('metros.metro_id'), nullable=False)
    interchange = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # New fields to determine travel direction
    previous_station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'),nullable=True)
    next_station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'),nullable=True)

    metro = relationship('Metro', back_populates='stations')
    previous_station = relationship('Station', remote_side=[station_id], backref='next_station')




