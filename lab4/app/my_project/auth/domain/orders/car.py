from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class Car(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(45))
    number = db.Column(db.String(8), nullable=False)
    arriving = db.Column(db.DateTime, nullable=False)
    departure = db.Column(db.DateTime, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    driver = db.relationship("Driver", backref="car's_driver")

    history = db.relationship("ParkingHistory", backref="which_car_was", primaryjoin="Car.id == ParkingHistory.car_id"
                              , cascade="all, delete-orphan")
    lot = db.relationship("ParkingLot", backref="which_car_is", primaryjoin="Car.id == ParkingLot.car_id",
                          cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Car({self.id}, '{self.model}', '{self.number}', '{self.arriving}', '{self.deparure}', '{self.driver_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "model": self.model,
            "number": self.number,
            "arriving": self.arriving,
            "departure": self.departure,
            "driver_id": self.driver_id or "",
            "driver": self.driver.name if self.driver is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Car:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Car(
            model=dto_dict.get("model"),
            number=dto_dict.get("number"),
            arriving=dto_dict.get("arriving"),
            departure=dto_dict.get("departure"),
            driver=dto_dict.get("driver")
        )
        return obj
