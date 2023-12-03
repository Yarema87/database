from typing import List

import sqlalchemy

from ..general_dao import GeneralDAO
from ...domain import Driver


class DriverDAO(GeneralDAO):
    """
    Realisation of Driver data access layer.
    """
    _domain_type = Driver

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Driver objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Driver.name == name).all()

    def find_by_age(self, age: int) -> List[object]:
        """
        Gets Driver objects from database table by field age.
        :param age: age value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Driver.age == age).all()

    def find_by_phone(self, phone: str) -> List[object]:
        """
        Gets Driver objects from database table by field arriving.
        :param phone: arriving value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Driver.phone == phone).all()

    def find_by_company_id(self, company_id: int) -> List[object]:
        """
        Gets Driver objects from database table by field company_id.
        :param company_id: company_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Driver.company_id == company_id).all()

