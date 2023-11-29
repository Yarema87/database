

from .orders.company_service import CompanyService
from .orders.parking_service import ParkingService
from .orders.driver_service import DriverService
from .orders.car_service import CarService
from .orders.parking_lot_service import ParkingLotService
from .orders.parking_history_service import ParkingHistoryService
from .orders.reservation_service import ReservationService
from .orders.bonus_card_service import BonusCardService
from .orders.company_and_bonus_card_service import CompanyAndBonusCardService
from .orders.driver_and_bonus_card_service import DriverAndBonusCardService


company_service = CompanyService()
parking_service = ParkingService()
driver_service = DriverService()
car_service = CarService()
parking_lot_service = ParkingLotService()
parking_history_service = ParkingHistoryService()
reservation_service = ReservationService()
bonus_card_service = BonusCardService()
company_and_bonus_card_service = CompanyAndBonusCardService()
driver_and_bonus_card_service = DriverAndBonusCardService()
