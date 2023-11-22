from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import driver_and_bonus_card_controller
from ...domain import DriverAndBonusCard

driver_and_bonus_card_bp = Blueprint('drivers_and_bonus_cards', __name__, url_prefix='/drivers_and_bonus_cards')


@driver_and_bonus_card_bp.get('')
def get_all_drivers_and_bonus_cards() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(driver_and_bonus_card_controller.find_all()), HTTPStatus.OK)


@driver_and_bonus_card_bp.get('/bonus_card_id/<int:bonus_card_id>')
def get_by_bonus_card_id(bonus_card_id: int) -> Response:
    """
    Gets objects by bonus_card_id.
    :return: Response object
    """
    return make_response(jsonify(driver_and_bonus_card_controller.find_by_bonus_card_id(bonus_card_id)), HTTPStatus.OK)


@driver_and_bonus_card_bp.get('/driver_id/<int:driver_id>')
def get_by_driver_id(driver_id: int) -> Response:
    """
    Gets objects by driver_id.
    :return: Response object
    """
    return make_response(jsonify(driver_and_bonus_card_controller.find_by_driver_id(driver_id)), HTTPStatus.OK)


@driver_and_bonus_card_bp.post('')
def create_object() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    drive_and_bc = DriverAndBonusCard.create_from_dto(content)
    driver_and_bonus_card_controller.create(drive_and_bc)
    return make_response(jsonify(drive_and_bc.put_into_dto()), HTTPStatus.CREATED)


@driver_and_bonus_card_bp.get('/id/<int:driver_and_bonus_card_id>')
def get_object(driver_and_bonus_card_id: int) -> Response:
    """
    Gets object by ID.
    :return: Response object
    """
    return make_response(jsonify(driver_and_bonus_card_controller.find_by_id(driver_and_bonus_card_id)), HTTPStatus.OK)


@driver_and_bonus_card_bp.put('/<int:driver_and_bonus_card_id>')
def update_object(driver_and_bonus_card_id: int) -> Response:
    """
    Updates object by ID.
    :return: Response object
    """
    content = request.get_json()
    drive_and_bc = DriverAndBonusCard.create_from_dto(content)
    driver_and_bonus_card_controller.update(driver_and_bonus_card_id, drive_and_bc)
    return make_response("Object updated", HTTPStatus.OK)


@driver_and_bonus_card_bp.patch('/<int:driver_and_bonus_card_id>')
def patch_object(driver_and_bonus_card_id: int) -> Response:
    """
    Patches object by ID.
    :return: Response object
    """
    content = request.get_json()
    driver_and_bonus_card_controller.patch(driver_and_bonus_card_id, content)
    return make_response("Object updated", HTTPStatus.OK)


@driver_and_bonus_card_bp.delete('/<int:driver_and_bonus_card_id>')
def delete_object(driver_and_bonus_card_id: int) -> Response:
    """
    Deletes object by ID.
    :return: Response object
    """
    driver_and_bonus_card_controller.delete(driver_and_bonus_card_id)
    return make_response("Object deleted", HTTPStatus.OK)
