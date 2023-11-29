

# orders DB
from .orders.company_dao import CompanyDAO
from .orders.parking_dao import ParkingDAO
from .orders.driver_dao import DriverDAO
from .orders.car_dao import CarDAO
from .orders.parking_lot_dao import ParkingLotDAO
from .orders.parking_history_dao import ParkingHistoryDAO
from .orders.reservation_dao import ReservationDAO
from .orders.bonus_card_dao import BonusCardDAO
from .orders.company_and_bonus_card_dao import CompanyAndBonusCardDAO
from .orders.driver_and_bonus_card_dao import DriverAndBonusCardDAO


company_dao = CompanyDAO()
parking_dao = ParkingDAO()
driver_dao = DriverDAO()
car_dao = CarDAO()
parking_lot_dao = ParkingLotDAO()
parking_history_dao = ParkingHistoryDAO()
reservation_dao = ReservationDAO()
bonus_card_dao = BonusCardDAO()
company_and_bonus_card_dao = CompanyAndBonusCardDAO()
driver_and_bonus_card_dao = DriverAndBonusCardDAO()




