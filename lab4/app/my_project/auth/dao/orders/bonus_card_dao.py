from typing import List
from decimal import Decimal
from datetime import datetime

from ..general_dao import GeneralDAO
from ...domain import BonusCard


class BonusCardDAO(GeneralDAO):
    """
    Realisation of BonusCard data access layer.
    """
    _domain_type = BonusCard

    def find_by_type(self, type: str) -> List[object]:
        """
        Gets BonusCard objects from database table by field type.
        :param type: type value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(BonusCard.type == type).all()

    def find_by_value(self, value: Decimal) -> List[object]:
        """
        Gets BonusCard objects from database table by field value.
        :param value: value value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(BonusCard.value == value).all()

    def find_by_validity(self, validity: datetime) -> List[object]:
        """
        Gets BonusCard objects from database table by field validity.
        :param validity: validity value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(BonusCard.validity == validity).all()

    def find_by_parking_id(self, parking_id: int) -> List[object]:
        """
        Gets BonusCard objects from database table by field parking_id.
        :param parking_id: parking_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(BonusCard.parking_id == parking_id).all()
