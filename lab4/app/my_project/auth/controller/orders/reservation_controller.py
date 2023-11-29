from http import HTTPStatus
from typing import List

from flask_restx import abort
from datetime import datetime

from ...service import reservation_service
from ...domain import Reservation
from ..general_controller import GeneralController


class ReservationController(GeneralController):
    """
    Realisation of Reservation controller.
    """
    _service = reservation_service

    def find_by_arrival(self, arrival: datetime) -> List[Reservation]:
        """
        Gets object from database table by datetime arrival using from Service layer.
        :param arrival: datetime arrival
        :return: DTO for search object
        """
        objects = self._service.find_by_arrival(arrival)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_departure(self, departure: datetime) -> List[Reservation]:
        """
        Gets object from database table by datetime departure using from Service layer.
        :param departure: datetime departure
        :return: DTO for search object
        """
        objects = self._service.find_by_departure(departure)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_parking_lot_id(self, parking_lot_id: int) -> List[Reservation]:
        """
        Gets object from database table by integer parking_lot_id using from Service layer.
        :param parking_lot_id: integer parking_lot_id
        :return: DTO for search object
        """
        objects = self._service.find_by_parking_lot_id(parking_lot_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_driver_id(self, driver_id: int) -> List[Reservation]:
        """
        Gets object from database table by integer driver_id using from Service layer.
        :param driver_id: integer driver_id
        :return: DTO for search object
        """
        objects = self._service.find_by_driver_id(driver_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
