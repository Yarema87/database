from _decimal import Decimal
from datetime import datetime
from typing import List

from ...dao import company_and_bonus_card_dao
from ...domain import CompanyAndBonusCard
from ..general_service import GeneralService


class CompanyAndBonusCardService(GeneralService):
    """
    Realisation of CompanyAndBonusCard service.
    """
    _dao = company_and_bonus_card_dao

    def find_by_company_id(self, company_id: int) -> List[CompanyAndBonusCard]:
        """
            Gets object from database table by integer company_id using from Data Access layer.
            :param company_id: string company_id
            :return: search object
        """
        objects = self._dao.find_by_company_id(company_id)
        return objects

    def find_by_bonus_card_id(self, bonus_card_id: int) -> List[CompanyAndBonusCard]:
        """
            Gets object from database table by integer bonus_card_id using from Data Access layer.
            :param bonus_card_id: integer bonus_card_id
            :return: search object
        """
        objects = self._dao.find_by_bonus_card_id(bonus_card_id)
        return objects

    def insert_company_and_bonus_card(self, p_name: str, p_number_of_drivers: int,
                                      p_type: str, p_value: Decimal, p_validity: datetime, p_parking_id: int):
        """
        Inserts a company into the database.
        :param p_name: name value
        :param p_number_of_drivers: number_of_drivers value
        :param p_type: type value
        :param p_validity: validity value
        :param p_value: value value
        :param p_parking_id: parking_id value
        :return: None (no need to return anything for an INSERT)
        """
        self._dao.insert_company_and_bonus_card(p_name, p_number_of_drivers, p_type, p_value, p_validity, p_parking_id)
