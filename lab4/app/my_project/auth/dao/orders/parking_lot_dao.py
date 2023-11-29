from typing import List

from ..general_dao import GeneralDAO
from ...domain import ParkingLot


class ParkingLotDAO(GeneralDAO):
    """
    Realisation of ParkingLot data access layer.
    """
    _domain_type = ParkingLot

    def find_all_free(self) -> List[object]:
        """
        Gets ParkingLot objects from database table by field is_free.
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingLot.is_free == True).all()

    def find_not_reserved(self) -> List[object]:
        """
        Gets ParkingLot objects from database table by field is_reserved.
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingLot.is_reserved == False).all()

    def find_by_parking_id(self, parking_id: int) -> List[object]:
        """
        Gets ParkingLot objects from database table by field parking_id.
        :param parking_id: parking_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingLot.parking_id == parking_id).all()

    def find_by_car_id(self, car_id: int) -> List[object]:
        """
        Gets ParkingLot objects from database table by field car_id.
        :param car_id: car_id value
        :return: search objects
        """
        return self._session.query(self._domain_type).filter(ParkingLot.car_id == car_id).all()
