from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class ParkingHistory(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "parking_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    arrival = db.Column(db.DateTime, nullable=False)
    departure = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    parking_lot_id = db.Column(db.Integer, db.ForeignKey('parking_lot.id'), nullable=False)
    parking_lot = db.relationship("ParkingLot", backref="which_was_set")
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    car = db.relationship("Car", backref="which_car_arrived")

    def __repr__(self) -> str:
        return f"Parking history({self.id}, '{self.arrival}', '{self.departure}', '{self.price}'," \
               f" '{self.parking_lot_id}', '{self.car_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "arrival": self.arrival,
            "departure": self.departure,
            "price": self.price,
            "parking_lot_id": self.parking_lot_id or "",
            "car_id": self.car_id or "",
            "car": self.car.model if self.car is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkingHistory:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ParkingHistory(
            arrival=dto_dict.get("arrival"),
            departure=dto_dict.get("departure"),
            price=dto_dict.get("price"),
            parking_lot=dto_dict.get("parking_lot_id"),
            car=dto_dict.get("car"),
        )
        return obj
