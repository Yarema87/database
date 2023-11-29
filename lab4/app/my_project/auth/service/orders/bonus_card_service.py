from typing import List
from decimal import Decimal
from datetime import datetime

from ...dao import bonus_card_dao
from ...domain import BonusCard
from ..general_service import GeneralService


class BonusCardService(GeneralService):
    """
    Realisation of BonusCard service.
    """
    _dao = bonus_card_dao

    def find_by_value(self, value: Decimal) -> List[BonusCard]:
        """
            Gets object from database table by decimal value using from Data Access layer.
            :param value: decimal value
            :return: search object
        """
        objects = self._dao.find_by_value(value)
        return objects

    def find_by_type(self, type: str) -> List[BonusCard]:
        """
            Gets object from database table by string type using from Data Access layer.
            :param type: string type
            :return: search object
        """
        objects = self._dao.find_by_type(type)
        return objects

    def find_by_validity(self, validity: datetime) -> List[BonusCard]:
        """
            Gets object from database table by datetime validity using from Data Access layer.
            :param validity: datetime validity
            :return: search object
        """
        objects = self._dao.find_by_validity(validity)
        return objects

    def find_by_parking_id(self, parking_id: int) -> List[BonusCard]:
        """
            Gets object from database table by integer parking_id using from Data Access layer.
            :param parking_id: integer parking_id
            :return: search object
        """
        objects = self._dao.find_by_parking_id(parking_id)
        return objects
