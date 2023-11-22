from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class Reservation(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "reservation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arrival = db.Column(db.DateTime, nullable=False)
    departure = db.Column(db.DateTime, nullable=False)
    parking_lot_id = db.Column(db.Integer, db.ForeignKey('parking_lot.id'), nullable=False)
    parking_lot = db.relationship("ParkingLot", backref="reserved_lot", uselist=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    driver = db.relationship("Driver", backref="driver_which_reserved", uselist=False)

    def __repr__(self) -> str:
        return f"Reservation({self.id}, '{self.arrival}', '{self.departure}', '{self.parking_lot_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "arrival": self.arrival,
            "departure": self.departure,
            "parking_lot_id": self.parking_lot_id or "",
            "driver_id": self.driver_id or "",
            "driver": self.driver.name if self.driver is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reservation:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Reservation(
            arrival=dto_dict.get("arrival"),
            departure=dto_dict.get("departure"),
            parking_lot_id=dto_dict.get("parking_lot_id"),
            driver=dto_dict.get("driver"),
        )
        return obj
