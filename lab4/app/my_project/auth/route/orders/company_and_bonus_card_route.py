from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import company_and_bonus_card_controller
from ...domain import CompanyAndBonusCard

company_and_bonus_card_bp = Blueprint('companies_and_bonus_cards', __name__, url_prefix='/companies_and_bonus_cards')


@company_and_bonus_card_bp.get('')
def get_all_companies_and_bonus_cards() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(company_and_bonus_card_controller.find_all()), HTTPStatus.OK)


@company_and_bonus_card_bp.get('/company_id/<int:company_id>')
def get_by_company_id(company_id: int) -> Response:
    """
    Gets objects by company_id.
    :return: Response object
    """
    return make_response(jsonify(company_and_bonus_card_controller.find_by_company_id(company_id)), HTTPStatus.OK)


@company_and_bonus_card_bp.get('/bonus_card_id/<int:bonus_card_id>')
def get_by_bonus_card_id(bonus_card_id: int) -> Response:
    """
    Gets objects by bonus_card_id.
    :return: Response object
    """
    return make_response(jsonify(company_and_bonus_card_controller.find_by_bonus_card_id(bonus_card_id)), HTTPStatus.OK)


@company_and_bonus_card_bp.post('')
def create_object() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    comp_and_bc = CompanyAndBonusCard.create_from_dto(content)
    company_and_bonus_card_controller.create(comp_and_bc)
    return make_response(jsonify(comp_and_bc.put_into_dto()), HTTPStatus.CREATED)


@company_and_bonus_card_bp.get('/id/<int:company_and_bonus_card_id>')
def get_object(company_and_bonus_card_id: int) -> Response:
    """
    Gets object by ID.
    :return: Response object
    """
    return make_response(jsonify(company_and_bonus_card_controller.find_by_id(company_and_bonus_card_id))
                         , HTTPStatus.OK)


@company_and_bonus_card_bp.put('/<int:company_and_bonus_card_id>')
def update_object(company_and_bonus_card_id: int) -> Response:
    """
    Updates object by ID.
    :return: Response object
    """
    content = request.get_json()
    comp_and_bc = CompanyAndBonusCard.create_from_dto(content)
    company_and_bonus_card_controller.update(company_and_bonus_card_id, comp_and_bc)
    return make_response("Object updated", HTTPStatus.OK)


@company_and_bonus_card_bp.patch('/<int:company_and_bonus_card_id>')
def patch_object(company_and_bonus_card_id: int) -> Response:
    """
    Patches object by ID.
    :return: Response object
    """
    content = request.get_json()
    company_and_bonus_card_controller.patch(company_and_bonus_card_id, content)
    return make_response("Object updated", HTTPStatus.OK)


@company_and_bonus_card_bp.delete('/<int:company_and_bonus_card_id>')
def delete_object(company_and_bonus_card_id: int) -> Response:
    """
    Deletes object by ID.
    :return: Response object
    """
    company_and_bonus_card_controller.delete(company_and_bonus_card_id)
    return make_response("Object deleted", HTTPStatus.OK)


@company_and_bonus_card_bp.post('/insert/<string:p_name>/<int:p_number_of_drivers>/'
                                '<string:p_type>/<float:p_value>/<path:p_validity>/<int:p_parking_id>')
def insert_company(p_name: str, p_number_of_drivers: int,
                   p_type: str, p_value: Decimal, p_validity: datetime, p_parking_id: int) -> Response:
    """
    Inserts a company into the database.
    :param p_name: name
    :param p_number_of_drivers: number value
    :param p_type: type value
    :param p_validity: validity value
    :param p_value: value value
    :param p_parking_id: parking_id value
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(p_validity, '%Y-%m-%dT%H:%M:%S')
        return make_response(jsonify(company_and_bonus_card_controller.insert_company_and_bonus_card(p_name,
                                                                                                     p_number_of_drivers,
                                                                                                     p_type, p_value,
                                                                                                     parsed_date,
                                                                                                     p_parking_id)),
                             HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"
