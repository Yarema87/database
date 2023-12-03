from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus
from typing import List

from flask_restx import abort

from ...service import company_and_bonus_card_service
from ...domain import CompanyAndBonusCard
from ..general_controller import GeneralController


class CompanyAndBonusCardController(GeneralController):
    """
    Realisation of Company_and_bonus_card controller.
    """
    _service = company_and_bonus_card_service

    def find_by_bonus_card_id(self, bonus_card_id: int) -> List[CompanyAndBonusCard]:
        """
        Gets object from database table by integer bonus_card_id using from Service layer.
        :param bonus_card_id: integer bonus_card_id
        :return: DTO for search object
        """
        objects = self._service.find_by_bonus_card_id(bonus_card_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def find_by_company_id(self, company_id: int) -> List[CompanyAndBonusCard]:
        """
        Gets object from database table by integer company_id using from Service layer.
        :param company_id: integer company_id
        :return: DTO for search object
        """
        objects = self._service.find_by_company_id(company_id)
        if not objects:
            abort(HTTPStatus.NOT_FOUND)
        return [obj.put_into_dto() for obj in objects]

    def insert_company_and_bonus_card(self, p_name: str, p_number_of_drivers: int,
                                      p_type: str, p_value: Decimal, p_validity: datetime, p_parking_id: int):
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number
        using Service layer as DTO objects.
        :param p_name: name
        :param p_number_of_drivers: number value
        :param p_type: type value
        :param p_validity: validity value
        :param p_value: value value
        :param p_parking_id: parking_id value
        """
        return self._service.insert_company_and_bonus_card(p_name, p_number_of_drivers, p_type, p_value,
                                                           p_validity, p_parking_id)
