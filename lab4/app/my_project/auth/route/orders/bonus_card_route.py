from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response
from decimal import Decimal
from datetime import datetime

from ...controller import bonus_card_controller
from ...domain import BonusCard

bonus_card_bp = Blueprint('bonus_cards', __name__, url_prefix='/bonus_cards')


@bonus_card_bp.get('')
def get_all_bonus_cards() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(bonus_card_controller.find_all()), HTTPStatus.OK)


@bonus_card_bp.post('')
def create_bonus_card() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    bonus_card = BonusCard.create_from_dto(content)
    bonus_card_controller.create(bonus_card)
    return make_response(jsonify(bonus_card.put_into_dto()), HTTPStatus.CREATED)


@bonus_card_bp.get('/id/<int:bonus_card_id>')
def get_bonus_card(bonus_card_id: int) -> Response:
    """
    Gets bonus card by ID.
    :return: Response object
    """
    return make_response(jsonify(bonus_card_controller.find_by_id(bonus_card_id), HTTPStatus.OK))


@bonus_card_bp.get('/type/<string:bonus_card_type>')
def get_bonus_card_by_type(bonus_card_type: str) -> Response:
    """
    Gets bonus card by type.
    :return: Response object
    """
    return make_response(jsonify(bonus_card_controller.find_by_type(bonus_card_type), HTTPStatus.OK))


@bonus_card_bp.get('/value/<float:bonus_card_value>')
def get_bonus_card_by_value(bonus_card_value: Decimal) -> Response:
    """
    Gets bonus card by value.
    :return: Response object
    """
    return make_response(jsonify(bonus_card_controller.find_by_value(bonus_card_value), HTTPStatus.OK))


@bonus_card_bp.get('/validity/<path:bonus_card_validity>')
def get_bonus_card_by_validity(bonus_card_validity: datetime) -> Response:
    """
    Gets bonus card by validity.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(bonus_card_validity, '%Y-%m-%dT%H:%M:%S')
        return parsed_date,\
            make_response(jsonify(bonus_card_controller.find_by_validity(bonus_card_validity), HTTPStatus.OK))
    except ValueError:
        return "Invalid datetime format"


@bonus_card_bp.get('/parking_id/<int:parking_id>')
def get_bonus_card_by_parking_id(parking_id: int) -> Response:
    """
    Gets bonus card by parking_id.
    :return: Response object
    """
    return make_response(jsonify(bonus_card_controller.find_by_parking_id(parking_id), HTTPStatus.OK))


@bonus_card_bp.put('/<int:bonus_card_id>')
def update_bonus_card(bonus_card_id: int) -> Response:
    """
    Updates bonus card by ID.
    :return: Response object
    """
    content = request.get_json()
    bonus_card = BonusCard.create_from_dto(content)
    bonus_card_controller.update(bonus_card_id, bonus_card)
    return make_response("Bonus card updated", HTTPStatus.OK)


@bonus_card_bp.patch('/<int:bonus_card_id>')
def patch_bonus_card(bonus_card_id: int) -> Response:
    """
    Patches bonus card by ID.
    :return: Response object
    """
    content = request.get_json()
    bonus_card_controller.patch(bonus_card_id, content)
    return make_response("Bonus card updated", HTTPStatus.OK)


@bonus_card_bp.delete('/<int:bonus_card_id>')
def delete_bonus_card(bonus_card_id: int) -> Response:
    """
    Deletes bonus card by ID.
    :return: Response object
    """
    bonus_card_controller.delete(bonus_card_id)
    return make_response("Bonus card deleted", HTTPStatus.OK)

@bonus_card_bp.get('/test')
def test_route():
    return "Test route works!"
