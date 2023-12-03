from _decimal import Decimal
from datetime import datetime
from typing import List

import sqlalchemy

from ..general_dao import GeneralDAO
from ...domain import CompanyAndBonusCard


class CompanyAndBonusCardDAO(GeneralDAO):
    """
    Realisation of CompanyAndBonusCard data access layer.
    """
    _domain_type = CompanyAndBonusCard

    def find_by_company_id(self, company_id: int) -> List[object]:
        """
        Gets CompanyAndBonusCard objects from database table by field company_id.
        :param company_id: company_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(CompanyAndBonusCard.company_id == company_id).all()

    def find_by_bonus_card_id(self, bonus_card_id: int) -> List[object]:
        """
        Gets CompanyAndBonusCard objects from database table by field bonus_card_id.
        :param bonus_card_id: bonus_card_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(CompanyAndBonusCard.bonus_card_id == bonus_card_id).all()

    def insert_company_and_bonus_card(self, p_name: str, p_number_of_drivers: int,
                                      p_type: str, p_value: Decimal, p_validity: datetime, p_parking_id: int):
        """
        Inserts a company_and_bonus_card into the database.
        :param p_name: name value
        :param p_number_of_drivers: number_of_drivers value
        :param p_type: type value
        :param p_validity: validity value
        :param p_value: value value
        :param p_parking_id: parking_id value
        :return: None (no need to return anything for an INSERT)
        """
        self._session.execute(sqlalchemy.text("CALL InsertIntoJunction(:p1, :p2, :p3, :p4, :p5, :p6)"),
                              {"p1": p_name, "p2": p_number_of_drivers,
                               "p3": p_type, "p4": p_value, "p5": p_validity, "p6": p_parking_id})
        self._session.commit()

