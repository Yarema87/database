from datetime import datetime
from typing import List

from ...dao import parking_history_dao
from ...domain import ParkingHistory
from ..general_service import GeneralService


class ParkingHistoryService(GeneralService):
    """
    Realisation of ParkingHistory service.
    """
    _dao = parking_history_dao

    def find_by_arrival(self, arrival: datetime) -> List[ParkingHistory]:
        """
            Gets object from database table by datetime arrival using from Data Access layer.
            :param arrival: datetime arrival
            :return: search object
        """
        objects = self._dao.find_by_arrival(arrival)
        return objects

    def find_by_departure(self, departure: datetime) -> List[ParkingHistory]:
        """
            Gets object from database table by datetime departure using from Data Access layer.
            :param departure: datetime departure
            :return: search object
        """
        objects = self._dao.find_by_departure(departure)
        return objects

    def find_by_price(self, price: int) -> List[ParkingHistory]:
        """
            Gets object from database table by integer price using from Data Access layer.
            :param price: integer price
            :return: search object
        """
        objects = self._dao.find_by_price(price)
        return objects

    def find_by_parking_lot_id(self, parking_lot_id: int) -> List[ParkingHistory]:
        """
            Gets object from database table by integer parking_lot_id using from Data Access layer.
            :param parking_lot_id: integer parking_lot_id
            :return: search object
        """
        objects = self._dao.find_by_parking_lot_id(parking_lot_id)
        return objects

    def find_by_car_id(self, car_id: int) -> List[object]:
        """
            Gets object from database table by integer car_id using from Data Access layer.
            :param car_id: integer car_id
            :return: search object
        """
        objects = self._dao.find_by_car_id(car_id)
        return objects
