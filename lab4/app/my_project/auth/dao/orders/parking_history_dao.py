from typing import List

from ..general_dao import GeneralDAO
from ...domain import ParkingHistory
from datetime import datetime


class ParkingHistoryDAO(GeneralDAO):
    """
    Realisation of ParkingHistory data access layer.
    """
    _domain_type = ParkingHistory

    def find_by_arrival(self, arrival: datetime) -> List[object]:
        """
        Gets ParkingHistory objects from database table by field arrival.
        :param arrival: arrival value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingHistory.arrival == arrival).all()

    def find_by_departure(self, departure: datetime) -> List[object]:
        """
        Gets ParkingHistory objects from database table by field departure.
        :param departure: departure value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingHistory.departure == departure).all()

    def find_by_price(self, price: int) -> List[object]:
        """
        Gets ParkingHistory objects from database table by field price.
        :param price: price value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingHistory.price == price).all()

    def find_by_parking_lot_id(self, parking_lot_id: int) -> List[object]:
        """
        Gets ParkingHistory objects from database table by field parking_lot_id.
        :param parking_lot_id: parking_lot_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingHistory.parking_lot_id == parking_lot_id).all()

    def find_by_car_id(self, car_id: int) -> List[object]:
        """
        Gets ParkingHistory objects from database table by field car_id.
        :param car_id: car_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingHistory.car_id == car_id).all()

