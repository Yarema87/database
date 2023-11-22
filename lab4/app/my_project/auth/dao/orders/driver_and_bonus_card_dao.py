from typing import List

from ..general_dao import GeneralDAO
from ...domain import DriverAndBonusCard


class DriverAndBonusCardDAO(GeneralDAO):
    """
    Realisation of DriverAndBonusCard data access layer.
    """
    _domain_type = DriverAndBonusCard

    def find_by_driver_id(self, driver_id: int) -> List[object]:
        """
        Gets DriverAndBonusCard objects from database table by field driver_id.
        :param driver_id: driver_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(DriverAndBonusCard.driver_id == driver_id).all()

    def find_by_bonus_card_id(self, bonus_card_id: str) -> List[object]:
        """
        Gets DriverAndBonusCard objects from database table by field bonus_card_id.
        :param bonus_card_id: bonus_card_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(DriverAndBonusCard.bonus_card_id == bonus_card_id).all()

