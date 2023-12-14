from __future__ import annotations
from typing import Dict, Any

from .... import db
from ..i_dto import IDto


class From5thLab(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "from_5th_lab"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    noname = db.Column(db.String(45))
    reservation_id = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"From5thLab({self.id}, '{self.noname}', '{self.reservation_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "noname": self.noname,
            "reservation_id": self.reservation_id or "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> From5thLab:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = From5thLab(
            noname=dto_dict.get("noname"),
            reservation_id=dto_dict.get("reservation_id"),
        )
        return obj
