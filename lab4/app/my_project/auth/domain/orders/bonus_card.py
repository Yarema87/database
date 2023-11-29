from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class BonusCard(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "bonus_card"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(45), nullable=False)
    value = db.Column(db.Numeric(scale=2))
    validity = db.Column(db.DateTime, nullable=False)
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)
    parking = db.relationship("Parking", backref="on_which")

    company = db.relationship("CompanyAndBonusCard", backref="relation_to_company",
                              primaryjoin="BonusCard.id == CompanyAndBonusCard.bonus_card_id"
                              , cascade="all, delete-orphan")
    driver = db.relationship("DriverAndBonusCard", backref="relation_to_driver",
                             primaryjoin="BonusCard.id == DriverAndBonusCard.bonus_card_id",
                             cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Bonus_card({self.id}, '{self.type}', '{self.value}', '{self.validity}', '{self.parking_id}'"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
            "value": self.value,
            "validity": self.validity,
            "parking_id": self.parking_id or "",
            "parking": self.parking.street if self.parking is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BonusCard:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = BonusCard(
            type=dto_dict.get("type"),
            value=dto_dict.get("value"),
            validity=dto_dict.get("validity"),
            parking=dto_dict.get("parking"),
        )
        return obj
