from datetime import datetime
from shared.utils.db_utils import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

class Fare(db.Model):
    __tablename__ = 'fares'

    fare_id = db.Column(db.Integer, primary_key=True)
    start_station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'), nullable=False)
    end_station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'), nullable=False)
    fare_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    start_station = relationship('Station', foreign_keys=[start_station_id])
    end_station = relationship('Station', foreign_keys=[end_station_id])


class Route(db.Model):
    __tablename__ = 'routes'

    route_id = db.Column(db.Integer, primary_key=True)
    start_station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'), nullable=False)
    end_station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    start_station = relationship('Station', foreign_keys=[start_station_id])
    end_station = relationship('Station', foreign_keys=[end_station_id])