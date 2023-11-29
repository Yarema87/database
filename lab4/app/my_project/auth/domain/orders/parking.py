from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class Parking(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "parking"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(75), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    lots_number = db.Column(db.Integer, nullable=False)
    free_lots = db.Column(db.Integer, nullable=False)
    parking_headmaster = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    company_owner_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company_owner = db.relationship("Company", backref="company_owner_of_parking")

    lots = db.relationship("ParkingLot", backref="lots_on_parking", primaryjoin="Parking.id == ParkingLot.parking_id",
                           cascade="all, delete-orphan")
    bonus_card = db.relationship("BonusCard", backref="from_which_parking",
                                 primaryjoin="Parking.id == BonusCard.parking_id", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Parking({self.id}, '{self.street}', '{self.city}', '{self.lots_number}', '{self.free_lots}'" \
               f", '{self.parking_headmaster}', '{self.phone}', '{self.company_owner_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "street": self.street,
            "city": self.city,
            "lots_number": self.lots_number,
            "free_lots": self.free_lots,
            "parking_headmaster": self.parking_headmaster,
            "phone": self.phone,
            "company_owner_id": self.company_owner_id or "",
            "company_owner": self.company_owner.name if self.company_owner is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Parking:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Parking(
            street=dto_dict.get("street"),
            city=dto_dict.get("city"),
            lots_number=dto_dict.get("lots_number"),
            free_lots=dto_dict.get("free_lots"),
            parking_headmaster=dto_dict.get("parking_headmaster"),
            phone=dto_dict.get("phone"),
            company_owner=dto_dict.get("company_owner"),
        )
        return obj
