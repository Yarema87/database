from datetime import datetime
from typing import List

from ...dao import car_dao
from ...domain import Car
from ..general_service import GeneralService


class CarService(GeneralService):
    """
    Realisation of Car service.
    """
    _dao = car_dao

    def find_by_model(self, model: str) -> List[Car]:
        """
            Gets object from database table by string model using from Data Access layer.
            :param model: string model
            :return: search object
        """
        objects = self._dao.find_by_model(model)
        return objects

    def find_by_number(self, number: str) -> List[Car]:
        """
            Gets object from database table by string number using from Data Access layer.
            :param number: string number
            :return: search object
        """
        objects = self._dao.find_by_number(number)
        return objects

    def find_by_arriving(self, arriving: datetime) -> List[Car]:
        """
            Gets object from database table by datetime arriving using from Data Access layer.
            :param arriving: datetime arriving
            :return: search object
        """
        objects = self._dao.find_by_arriving(arriving)
        return objects

    def find_by_departure(self, departure: datetime) -> List[Car]:
        """
            Gets object from database table by datetime departure using from Data Access layer.
            :param departure: datetime departure
            :return: search object
        """
        objects = self._dao.find_by_departure(departure)
        return objects

    def find_by_driver_id(self, driver_id: int) -> List[Car]:
        """
            Gets object from database table by integer driver_id using from Data Access layer.
            :param driver_id: integer driver_id
            :return: search object
        """
        objects = self._dao.find_by_driver_id(driver_id)
        return objects
