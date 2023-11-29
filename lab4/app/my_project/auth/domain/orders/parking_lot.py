from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class ParkingLot(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "parking_lot"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_free = db.Column(db.Boolean, nullable=False)
    is_reserved = db.Column(db.Boolean, nullable=False)
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)
    parking = db.relationship("Parking", backref="parking_lot_on_parking")
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    car = db.relationship("Car", backref="car_on_parking_lot")

    reservation = db.relationship("Reservation", backref='lot_which_is_reserved',
                                  primaryjoin="ParkingLot.id == Reservation.parking_lot_id",
                                  cascade="all, delete-orphan")
    parking_history = db.relationship("ParkingHistory", backref="which_was_not_free",
                                      primaryjoin="ParkingLot.id == ParkingHistory.parking_lot_id",
                                      cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Parking lot({self.id}, '{self.is_free}', '{self.is_reserved}', '{self.parking_id}', '{self.car_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "is_free": self.is_free,
            "is_reserved": self.is_reserved,
            "parking_id": self.parking_id or "",
            "parking": self.parking.street if self.parking is not None else "",
            "car_id": self.car_id or "",
            "car": self.car.model if self.car is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkingLot:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ParkingLot(
            is_free=dto_dict.get("is_free"),
            is_reserved=dto_dict.get("is_reserved"),
            parking=dto_dict.get("parking"),
            car=dto_dict.get("car"),
        )
        return obj
