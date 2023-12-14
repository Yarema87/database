from typing import List

import sqlalchemy

from ..general_dao import GeneralDAO
from ...domain import Parking


class ParkingDAO(GeneralDAO):
    """
    Realisation of Parking data access layer.
    """
    _domain_type = Parking

    def find_by_street(self, street: str) -> List[object]:
        """
        Gets Parking objects from database table by field street.
        :param street: street value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.street == street).all()

    def find_by_city(self, city: str) -> List[object]:
        """
        Gets Parking objects from database table by field city.
        :param city: city value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.city == city).all()

    def find_by_lots_number(self, lots_number: int) -> List[object]:
        """
        Gets Parking objects from database table by field lots_number.
        :param lots_number: lots_number value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.lots_number == lots_number).all()

    def find_by_free_lots(self, free_lots: int) -> List[object]:
        """
        Gets Parking objects from database table by field free_lots.
        :param free_lots: free_lots value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.free_lots == free_lots).all()

    def find_by_parking_headmaster(self, parking_headmaster: str) -> List[object]:
        """
        Gets Parking objects from database table by field parking_headmaster.
        :param parking_headmaster: parking_headmaster value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.parking_headmaster == parking_headmaster).all()

    def find_by_phone(self, phone: str) -> List[object]:
        """
        Gets Parking objects from database table by field phone.
        :param phone: phone value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.phone == phone).all()

    def find_by_company_owner_id(self, company_owner_id: int) -> List[object]:
        """
        Gets Parking objects from database table by field company_owner_id.
        :param company_owner_id: company_owner_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Parking.company_owner_id == company_owner_id).all()

    def timestamp(self):
        """
        Inserts a company into the database.
        :return: None (no need to return anything for an INSERT)
        """
        self._session.execute(sqlalchemy.text("CALL GenerateTablesAndCopyData()"))
        self._session.commit()
