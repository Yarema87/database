from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import bonus_card_service
from ...domain import BonusCard
from ..general_controller import GeneralController


class BonusCardController(GeneralController):
    """
    Realisation of BonusCard controller.
    """
    _service = bonus_card_service

    def find_by_type(self, type: str) -> List[BonusCard]:
        """
        Gets object from database table by string type using from Service layer.
        :param type: string type
        :return: DTO for search object
        """
        objects = self._service.find_by_type(type)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_value(self, value: Decimal) -> List[BonusCard]:
        """
        Gets object from database table by decimal value using from Service layer.
        :param value: decimal value
        :return: DTO for search object
        """
        objects = self._service.find_by_value(value)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_validity(self, validity: datetime) -> List[BonusCard]:
        """
        Gets object from database table by datetime validity using from Service layer.
        :param validity: datetime validity
        :return: DTO for search object
        """
        objects = self._service.find_by_validity(validity)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_parking_id(self, parking_id: int) -> List[BonusCard]:
        """
        Gets object from database table by integer parking_id using from Service layer.
        :param parking_id: integer parking_id
        :return: DTO for search object
        """
        objects = self._service.find_by_parking_id(parking_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
