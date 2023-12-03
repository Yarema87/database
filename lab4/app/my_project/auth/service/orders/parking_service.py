from typing import List

from ...dao import parking_dao
from ...domain import Parking
from ..general_service import GeneralService


class ParkingService(GeneralService):
    """
    Realisation of Parking service.
    """
    _dao = parking_dao

    def find_by_street(self, street: str) -> List[Parking]:
        """
            Gets object from database table by string street using from Data Access layer.
            :param street: string street
            :return: search object
        """
        objects = self._dao.find_by_street(street)
        return objects

    def find_by_city(self, city: str) -> List[Parking]:
        """
            Gets object from database table by string city using from Data Access layer.
            :param city: string city
            :return: search object
        """
        objects = self._dao.find_by_city(city)
        return objects

    def find_by_lots_number(self, lots_number: int) -> List[Parking]:
        """
            Gets object from database table by integer lots_number using from Data Access layer.
            :param lots_number: integer lots_number
            :return: search object
        """
        objects = self._dao.find_by_lots_number(lots_number)
        return objects

    def find_by_free_lots(self, free_lots: int) -> List[Parking]:
        """
            Gets object from database table by integer free_lots using from Data Access layer.
            :param free_lots: integer free_lots
            :return: search object
        """
        objects = self._dao.find_by_free_lots(free_lots)
        return objects

    def find_by_parking_headmaster(self, parking_headmaster: str) -> List[Parking]:
        """
            Gets object from database table by string parking_headmaster using from Data Access layer.
            :param parking_headmaster: string parking_headmaster
            :return: search object
        """
        objects = self._dao.find_by_parking_headmaster(parking_headmaster)
        return objects

    def find_by_phone(self, phone: str) -> List[Parking]:
        """
            Gets object from database table by string arriving using from Data Access layer.
            :param phone: string arriving
            :return: search object
        """
        objects = self._dao.find_by_phone(phone)
        return objects

    def find_by_company_owner_id(self, company_owner_id: int) -> List[Parking]:
        """
            Gets object from database table by integer company_owner_id using from Data Access layer.
            :param company_owner_id: integer company_owner_id
            :return: search object
        """
        objects = self._dao.find_by_company_owner_id(company_owner_id)
        return objects

    def timestamp(self):
        """
        Inserts a company into the database.
        :return: None (no need to return anything for an INSERT)
        """
        self._dao.timestamp()
