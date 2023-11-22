from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import driver_and_bonus_card_service
from ...domain import DriverAndBonusCard
from ..general_controller import GeneralController


class DriverAndBonusCardController(GeneralController):
    """
    Realisation of DriverAndBonusCard controller.
    """
    _service = driver_and_bonus_card_service

    def find_by_driver_id(self, driver_id: int) -> List[DriverAndBonusCard]:
        """
        Gets object from database table by integer driver_id using from Service layer.
        :param driver_id: integer driver_id
        :return: DTO for search object
        """
        objects = self._service.find_by_driver_id(driver_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_bonus_card_id(self, bonus_card_id: int) -> List[DriverAndBonusCard]:
        """
        Gets object from database table by integer bonus_card_id using from Service layer.
        :param bonus_card_id: integer bonus_card_id
        :return: DTO for search object
        """
        objects = self._service.find_by_bonus_card_id(bonus_card_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
