from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import driver_service
from ...domain import Driver
from ..general_controller import GeneralController


class DriverController(GeneralController):
    """
    Realisation of Driver controller.
    """
    _service = driver_service

    def find_by_name(self, name: str) -> List[Driver]:
        """
        Gets object from database table by string name using from Service layer.
        :param name: string name
        :return: DTO for search object
        """
        objects = self._service.find_by_name(name)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_age(self, age: int) -> List[Driver]:
        """
        Gets object from database table by integer age using from Service layer.
        :param age: integer age
        :return: DTO for search object
        """
        objects = self._service.find_by_age(age)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_phone(self, phone: str) -> List[Driver]:
        """
        Gets object from database table by string arriving using from Service layer.
        :param phone: string arriving
        :return: DTO for search object
        """
        objects = self._service.find_by_phone(phone)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_company_id(self, company_id: int) -> List[Driver]:
        """
        Gets object from database table by integer company_id using from Service layer.
        :param company_id: integer company_id
        :return: DTO for search object
        """
        objects = self._service.find_by_company_id(company_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
