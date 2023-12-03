from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import parking_history_service
from ...domain import ParkingHistory
from ..general_controller import GeneralController


class ParkingHistoryController(GeneralController):
    """
    Realisation of Parking controller.
    """
    _service = parking_history_service

    def find_by_arrival(self, arrival: datetime) -> List[ParkingHistory]:
        """
        Gets object from database table by datetime arrival using from Service layer.
        :param arrival: datetime arrival
        :return: DTO for search object
        """
        objects = self._service.find_by_arrival(arrival)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_departure(self, departure: datetime) -> List[ParkingHistory]:
        """
        Gets object from database table by datetime departure using from Service layer.
        :param departure: datetime departure
        :return: DTO for search object
        """
        objects = self._service.find_by_departure(departure)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_price(self, price: int) -> List[ParkingHistory]:
        """
        Gets object from database table by integer price using from Service layer.
        :param price: integer price
        :return: DTO for search object
        """
        objects = self._service.find_by_price(price)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_parking_lot_id(self, parking_lot_id: int) -> List[ParkingHistory]:
        """
        Gets object from database table by integer parking_lot_id using from Service layer.
        :param parking_lot_id: integer parking_lot_id
        :return: DTO for search object
        """
        objects = self._service.find_by_parking_lot_id(parking_lot_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_car_id(self, car_id: int) -> List[ParkingHistory]:
        """
        Gets object from database table by integer car_id using from Service layer.
        :param car_id: integer car_id
        :return: DTO for search object
        """
        objects = self._service.find_by_car_id(car_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]


