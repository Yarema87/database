from typing import List

from ...dao import driver_dao
from ...domain import Driver
from ..general_service import GeneralService


class DriverService(GeneralService):
    """
    Realisation of Driver service.
    """
    _dao = driver_dao

    def find_by_name(self, name: str) -> List[Driver]:
        """
            Gets object from database table by string name using from Data Access layer.
            :param name: string name
            :return: search object
        """
        objects = self._dao.find_by_name(name)
        return objects

    def find_by_age(self, age: int) -> List[Driver]:
        """
            Gets object from database table by integer age using from Data Access layer.
            :param age: int age
            :return: search object
        """
        objects = self._dao.find_by_age(age)
        return objects

    def find_by_phone(self, phone: str) -> List[Driver]:
        """
            Gets object from database table by string arriving using from Data Access layer.
            :param phone: string arriving
            :return: search object
        """
        objects = self._dao.find_by_phone(phone)
        return objects

    def find_by_company_id(self, company_id: int) -> List[Driver]:
        """
            Gets object from database table by integer company_id using from Data Access layer.
            :param company_id: integer company_id
            :return: search object
        """
        objects = self._dao.find_by_company_id(company_id)
        return objects
