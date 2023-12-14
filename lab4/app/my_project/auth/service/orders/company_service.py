from typing import List

from ...dao import company_dao
from ...domain import Company
from ..general_service import GeneralService


class CompanyService(GeneralService):
    """
    Realisation of Company service.
    """
    _dao = company_dao

    def find_all(self) -> List[object]:
        """
        Gets all objects from table using Data Access layer.
        :return: list of all objects
        """
        return self._dao.find_all()

    def find_by_name(self, name: str) -> object:
        """
            Gets object from database table by string name using from Data Access layer.
            :param name: string name
            :return: search object
        """
        return self._dao.find_by_name(name)

    def find_by_number_of_drivers(self, number_of_drivers: int) -> List[Company]:
        """
        Gets objects from the database table by integer number_of_drivers using the Data Access layer.
        :param number_of_drivers: integer number_of_drivers
        :return: list of search objects
        """
        objects = self._dao.find_by_number(number_of_drivers)
        return objects

    def insert_company(self, p_name: str, p_number_of_drivers: int):
        """
        Inserts a company into the database.
        :param p_name: name value
        :param p_number_of_drivers: number_of_drivers value
        :return: None (no need to return anything for an INSERT)
        """
        self._dao.insert_company(p_name, p_number_of_drivers)

