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
