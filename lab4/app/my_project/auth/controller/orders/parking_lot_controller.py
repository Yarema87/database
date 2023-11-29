from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import parking_lot_service
from ...domain import ParkingLot
from ..general_controller import GeneralController


class ParkingLotController(GeneralController):
    """
    Realisation of ParkingLot controller.
    """
    _service = parking_lot_service

    def find_all_free(self) -> List[ParkingLot]:
        """
        Gets object from database table by boolean is_free using from Service layer.
        :return: DTO for search object
        """
        objects = self._service.find_all_free()
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_not_reserved(self) -> List[ParkingLot]:
        """
        Gets object from database table by boolean is_reserved using from Service layer.
        :return: DTO for search object
        """
        objects = self._service.find_not_reserved()
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_car_id(self, car_id: int) -> List[ParkingLot]:
        """
        Gets object from database table by integer car_id using from Service layer.
        :param car_id: integer car_id
        :return: DTO for search object
        """
        objects = self._service.find_by_car_id(car_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_parking_id(self, parking_id: int) -> List[ParkingLot]:
        """
        Gets object from database table by integer parking_id using from Service layer.
        :param parking_id: integer parking_id
        :return: DTO for search object
        """
        objects = self._service.find_by_parking_id(parking_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
