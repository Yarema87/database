from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class DriverAndBonusCard(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "driver_and_bonus_card"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    driver = db.relationship("Driver", backref="which_driver_has_card")
    bonus_card_id = db.Column(db.Integer, db.ForeignKey('bonus_card.id'), nullable=False)
    bonus_card = db.relationship("BonusCard", backref="which_card_has_driver")

    def __repr__(self) -> str:
        return f"Parking({self.id}, '{self.driver_id}', '{self.bonus_card_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "driver_id": self.driver_id or "",
            "driver": self.driver.name if self.driver is not None else "",
            "bonus_card_id": self.bonus_card_id or "",
            "bonus_card": self.bonus_card.type if self.bonus_card is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DriverAndBonusCard:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = DriverAndBonusCard(
            bonus_card_id=dto_dict.get("bonus_card_id"),
            driver_id=dto_dict.get("driver_id")
        )
        return obj
