from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .... import db
from ..i_dto import IDto


class CompanyAndBonusCard(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "company_and_bonus_card"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship("Company", backref="which_company_has_card")
    bonus_card_id = db.Column(db.Integer, db.ForeignKey('bonus_card.id'), nullable=False)
    bonus_card = db.relationship("BonusCard", backref="which_card_has_company")

    def __repr__(self) -> str:
        return f"Parking({self.id}, '{self.company_id}', '{self.bonus_card_id}'"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "bonus_card_id": self.bonus_card_id or "",
            "bonus_card_type": self.bonus_card.type if self.bonus_card is not None else "",
            "bonus_card_value": self.bonus_card.value if self.bonus_card is not None else "",
            "bonus_card_validity": self.bonus_card.validity if self.bonus_card is not None else "",
            "bonus_card_parking_id": self.bonus_card.parking_id if self.bonus_card is not None else "",
            "company_id": self.company_id or "",
            "company_name": self.company.name if self.company is not None else "",
            "company_number_of_drivers": self.company.number_of_drivers if self.company is not None else ""
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CompanyAndBonusCard:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CompanyAndBonusCard(
            bonus_card=dto_dict.get("bonus_card"),
            company=dto_dict.get("company"),
        )
        return obj
