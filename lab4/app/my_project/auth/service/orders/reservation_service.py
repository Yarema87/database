from typing import List
from datetime import datetime

from ...dao import reservation_dao
from ...domain import Reservation
from ..general_service import GeneralService


class ReservationService(GeneralService):
    """
    Realisation of Reservation service.
    """
    _dao = reservation_dao

    def find_by_arrival(self, arrival: datetime) -> List[Reservation]:
        """
            Gets object from database table by datetime arrival using from Data Access layer.
            :param arrival: datetime arrival
            :return: search object
        """
        objects = self._dao.find_by_arrival(arrival)
        return objects

    def find_by_departure(self, departure: datetime) -> List[Reservation]:
        """
            Gets object from database table by datetime departure using from Data Access layer.
            :param departure: datetime departure
            :return: search object
        """
        objects = self._dao.find_by_departure(departure)
        return objects

    def find_by_parking_lot_id(self, parking_lot_id: int) -> List[Reservation]:
        """
            Gets object from database table by integer parking_lot_id using from Data Access layer.
            :param parking_lot_id: integer parking_lot_id
            :return: search object
        """
        objects = self._dao.find_by_parking_lot_id(parking_lot_id)
        return objects

    def find_by_driver_id(self, driver_id: int) -> List[Reservation]:
        """
            Gets object from database table by integer driver_id using from Data Access layer.
            :param driver_id: integer driver_id
            :return: search object
        """
        objects = self._dao.find_by_driver_id(driver_id)
        return objects
