from typing import List

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

