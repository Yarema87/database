from typing import List

from ..general_dao import GeneralDAO
from ...domain import Car
from datetime import datetime


class CarDAO(GeneralDAO):
    """
    Realisation of Car data access layer.
    """
    _domain_type = Car

    def find_by_model(self, model: str) -> List[object]:
        """
        Gets Car objects from database table by field model.
        :param model: model value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Car.model == model).all()

    def find_by_number(self, number: str) -> List[object]:
        """
        Gets Car objects from database table by field number.
        :param number: number value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Car.number == number).all()

    def find_by_arriving(self, arriving: datetime) -> List[object]:
        """
        Gets Car objects from database table by field arriving.
        :param arriving: arriving value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Car.arriving == arriving).all()

    def find_by_departure(self, departure: datetime) -> List[object]:
        """
        Gets Car objects from database table by field departure.
        :param departure: departure value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Car.departure == departure).all()

    def find_by_driver_id(self, driver_id: int) -> List[object]:
        """
        Gets Car objects from database table by field driver_id.
        :param driver_id: driver_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Car.driver_id == driver_id).all()
