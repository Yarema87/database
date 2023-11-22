from __future__ import annotations
from typing import Dict, Any

from .... import db
from ..i_dto import IDto


class Company(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    number_of_drivers = db.Column(db.Integer, nullable=False)

    bonus_card = db.relationship("CompanyAndBonusCard", backref="relation_to_bonus_card",
                                 primaryjoin="Company.id == CompanyAndBonusCard.company_id",
                                 cascade="all, delete-orphan")
    parking = db.relationship("Parking", backref="parking_which_owns_company",
                              primaryjoin="Company.id == Parking.company_owner_id", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Company({self.id}, '{self.name}', '{self.number_of_drivers}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "number_of_drivers": self.number_of_drivers
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Company:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Company(
            name=dto_dict.get("name"),
            number_of_drivers=dto_dict.get("number_of_drivers"),
        )
        return obj
