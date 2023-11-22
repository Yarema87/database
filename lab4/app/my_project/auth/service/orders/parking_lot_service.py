from typing import List

from ...dao import parking_lot_dao
from ...domain import ParkingLot
from ..general_service import GeneralService


class ParkingLotService(GeneralService):
    """
    Realisation of ParkingLot service.
    """
    _dao = parking_lot_dao

    def find_all_free(self) -> List[ParkingLot]:
        """
            Gets object from database table by boolean is_free using from Data Access layer.
            :return: search object
        """
        objects = self._dao.find_all_free()
        return objects

    def find_not_reserved(self) -> List[ParkingLot]:
        """
            Gets object from database table by boolean is_reserved using from Data Access layer.
            :return: search object
        """
        objects = self._dao.find_not_reserved()
        return objects

    def find_by_parking_id(self, parking_id: int) -> List[ParkingLot]:
        """
            Gets object from database table by integer parking_id using from Data Access layer.
            :param parking_id: integer parking_id
            :return: search object
        """
        objects = self._dao.find_by_parking_id(parking_id)
        return objects

    def find_by_car_id(self, car_id: int) -> List[ParkingLot]:
        """
            Gets object from database table by integer car_id using from Data Access layer.
            :param car_id: integer car_id
            :return: search object
        """
        objects = self._dao.find_by_car_id(car_id)
        return objects
