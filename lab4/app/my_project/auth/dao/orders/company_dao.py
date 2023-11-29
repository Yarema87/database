from typing import List

from ..general_dao import GeneralDAO
from ...domain import Company


class CompanyDAO(GeneralDAO):
    """
    Realisation of Company data access layer.
    """
    _domain_type = Company

    def find_all(self) -> List[object]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._session.query(self._domain_type).all()

    def find_by_name(self, name: str) -> object:
        """
        Gets Company objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Company.name == name).first()

    def find_by_number(self, number_of_drivers: int) -> List[object]:
        """
        Gets Company objects from the database table by the 'number_of_drivers' field.
        :param number_of_drivers: number_of_drivers value
        :return: list of Company objects
        """
        return self._session.query(self._domain_type).filter(Company.number_of_drivers == number_of_drivers).all()

