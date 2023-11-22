from typing import List

from ...dao import driver_and_bonus_card_dao
from ...domain import DriverAndBonusCard
from ..general_service import GeneralService


class DriverAndBonusCardService(GeneralService):
    """
    Realisation of DriverAndBonusCard service.
    """
    _dao = driver_and_bonus_card_dao

    def find_by_driver_id(self, driver_id: int) -> List[DriverAndBonusCard]:
        """
            Gets object from database table by integer driver_id using from Data Access layer.
            :param driver_id: integer driver_id
            :return: search object
        """
        objects = self._dao.find_by_driver_id(driver_id)
        return objects

    def find_by_bonus_card_id(self, bonus_card_id: int) -> List[DriverAndBonusCard]:
        """
            Gets object from database table by integer bonus_card_id using from Data Access layer.
            :param bonus_card_id: integer bonus_card_id
            :return: search object
        """
        objects = self._dao.find_by_bonus_card_id(bonus_card_id)
        return objects
