from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class Driver(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "driver"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(13), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company_owner = db.relationship("Company", backref="driver")

    cars = db.relationship("Car", backref="owner", primaryjoin="Driver.id == Car.driver_id",
                           cascade="all, delete-orphan")
    reservations = db.relationship("Reservation", backref="driver_who_reserved",
                                   primaryjoin="Driver.id == Reservation.driver_id", cascade="all, delete-orphan")
    bonus_card = db.relationship("DriverAndBonusCard", backref="relation_to_card",
                                 primaryjoin="Driver.id == DriverAndBonusCard.driver_id", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Driver({self.id}, '{self.name}', '{self.age}', '{self.phone}', '{self.company_owner_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "arriving": self.phone,
            "company_id": self.company_id or "",
            "company_owner": self.company_owner.name if self.company_owner is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Driver:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Driver(
            name=dto_dict.get("name"),
            age=dto_dict.get("age"),
            phone=dto_dict.get("arriving"),
            company_owner=dto_dict.get("company_owner"),
        )
        return obj
