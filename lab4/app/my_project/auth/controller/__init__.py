

from .orders.company_controller import CompanyController
from .orders.parking_controller import ParkingController
from .orders.driver_controller import DriverController
from .orders.car_controller import CarController
from .orders.parking_lot_controller import ParkingLotController
from .orders.parking_history_controller import ParkingHistoryController
from .orders.reservation_controller import ReservationController
from .orders.bonus_card_controller import BonusCardController
from .orders.company_and_bonus_card_controller import CompanyAndBonusCardController
from .orders.driver_and_bonus_card_controller import DriverAndBonusCardController
from .orders.from_5th_lab_controller import From5thLabController


company_controller = CompanyController()
parking_controller = ParkingController()
driver_controller = DriverController()
car_controller = CarController()
parking_lot_controller = ParkingLotController()
parking_history_controller = ParkingHistoryController()
reservation_controller = ReservationController()
bonus_card_controller = BonusCardController()
company_and_bonus_card_controller = CompanyAndBonusCardController()
driver_and_bonus_card_controller = DriverAndBonusCardController()
from_5th_lab_controller = From5thLabController()
