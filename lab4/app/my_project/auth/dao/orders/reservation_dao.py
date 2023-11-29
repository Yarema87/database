from typing import List
from datetime import datetime

from ..general_dao import GeneralDAO
from ...domain import Reservation


class ReservationDAO(GeneralDAO):
    """
    Realisation of Reservation data access layer.
    """
    _domain_type = Reservation

    def find_by_arrival(self, arrival: datetime) -> List[object]:
        """
        Gets Reservation objects from database table by field arrival.
        :param arrival: arrival value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Reservation.arrival == arrival).all()

    def find_by_departure(self, departure: datetime) -> List[object]:
        """
        Gets Reservation objects from database table by field departure.
        :param departure: departure value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Reservation.departure == departure).all()

    def find_by_parking_lot_id(self, parking_lot_id: int) -> List[object]:
        """
        Gets Reservation objects from database table by field parking_lot_id.
        :param parking_lot_id: parking_lot_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Reservation.parking_lot_id == parking_lot_id).all()

    def find_by_driver_id(self, driver_id: int) -> List[object]:
        """
        Gets Reservation objects from database table by field driver_id.
        :param driver_id: driver_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(Reservation.driver_id == driver_id).all()


