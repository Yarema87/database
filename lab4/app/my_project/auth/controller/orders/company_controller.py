from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import company_service
from ...domain import Company
from ..general_controller import GeneralController


class CompanyController(GeneralController):
    """
    Realisation of Company controller.
    """
    _service = company_service

    def find_all(self) -> List[Company]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: x.put_into_dto(), self._service.find_all()))

    def find_by_name(self, name: str) -> object:
        """
        Gets object from database table by string name using from Service layer.
        :param name: string name
        :return: DTO for search object
        """
        obj = self._service.find_by_name(name)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto()

    def find_by_number_of_drivers(self, number_of_drivers: int) -> List[Company]:
        """
        Gets object from database table by integer number_of_drivers using from Service layer.
        :param number_of_drivers: integer number_of_drivers
        :return: list of DTOs for search objects
        """
        objects = self._service.find_by_number_of_drivers(number_of_drivers)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]
