from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import car_service
from ...domain import Car
from ..general_controller import GeneralController


class CarController(GeneralController):
    """
    Realisation of Car controller.
    """
    _service = car_service

    def find_by_model(self, model: str) -> List[Car]:
        """
        Gets object from database table by string model using from Service layer.
        :param model: string model
        :return: DTO for search object
        """
        objects = self._service.find_by_model(model)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_number(self, number: str) -> List[Car]:
        """
        Gets object from database table by string number using from Service layer.
        :param number: string number
        :return: DTO for search object
        """
        objects = self._service.find_by_number(number)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_arriving(self, arriving: datetime) -> List[Car]:
        """
        Gets object from database table by datetime arriving using from Service layer.
        :param arriving: datetime arriving
        :return: DTO for search object
        """
        objects = self._service.find_by_arriving(arriving)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_departure(self, departure: datetime) -> List[Car]:
        """
        Gets object from database table by datetime departure using from Service layer.
        :param departure: datetime departure
        :return: DTO for search object
        """
        objects = self._service.find_by_departure(departure)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_driver_id(self, driver_id: int) -> List[Car]:
        """
        Gets object from database table by integer driver_id using from Service layer.
        :param driver_id: integer driver_id
        :return: DTO for search object
        """
        objects = self._service.find_by_driver_id(driver_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
