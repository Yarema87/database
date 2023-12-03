from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import parking_service
from ...domain import Parking
from ..general_controller import GeneralController


class ParkingController(GeneralController):
    """
    Realisation of Parking controller.
    """
    _service = parking_service

    def find_by_street(self, street: str) -> List[Parking]:
        """
        Gets object from database table by string street using from Service layer.
        :param street: string street
        :return: DTO for search object
        """
        objects = self._service.find_by_street(street)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_city(self, city: str) -> List[Parking]:
        """
        Gets object from database table by string city using from Service layer.
        :param city: string city
        :return: DTO for search object
        """
        objects = self._service.find_by_city(city)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_lots_number(self, lots_number: int) -> List[Parking]:
        """
        Gets object from database table by integer lots_number using from Service layer.
        :param lots_number: integer lots_number
        :return: DTO for search object
        """
        objects = self._service.find_by_lots_number(lots_number)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_free_lots(self, free_lots: int) -> List[Parking]:
        """
        Gets object from database table by integer free_lots using from Service layer.
        :param free_lots: integer free_lots
        :return: DTO for search object
        """
        objects = self._service.find_by_free_lots(free_lots)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_parking_headmaster(self, parking_headmaster: str) -> List[Parking]:
        """
        Gets object from database table by string parking_headmaster using from Service layer.
        :param parking_headmaster: string parking_headmaster
        :return: DTO for search object
        """
        objects = self._service.find_by_parking_headmaster(parking_headmaster)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_phone(self, phone: str) -> List[Parking]:
        """
        Gets object from database table by string arriving using from Service layer.
        :param phone: string arriving
        :return: DTO for search object
        """
        objects = self._service.find_by_phone(phone)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_company_owner_id(self, company_owner_id: int) -> List[Parking]:
        """
        Gets object from database table by integer company_owner_id using from Service layer.
        :param company_owner_id: integer company_owner_id
        :return: DTO for search object
        """
        objects = self._service.find_by_company_owner_id(company_owner_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def timestamp(self):
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number
        using Service layer as DTO objects.
        """
        return self._service.timestamp()
