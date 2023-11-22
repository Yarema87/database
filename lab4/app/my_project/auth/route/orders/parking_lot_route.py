from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import parking_lot_controller
from ...domain import ParkingLot

parking_lot_bp = Blueprint('parking_lots', __name__, url_prefix='/parking_lots')


@parking_lot_bp.get('')
def get_all_parking_lots() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(parking_lot_controller.find_all()), HTTPStatus.OK)


@parking_lot_bp.post('')
def create_parking_lot() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    parking_lot = ParkingLot.create_from_dto(content)
    parking_lot_controller.create(parking_lot)
    return make_response(jsonify(parking_lot.put_into_dto()), HTTPStatus.CREATED)


@parking_lot_bp.get('/id/<int:parking_lot_id>')
def get_parking_lot_by_id(parking_lot_id: int) -> Response:
    """
    Gets parking_lot by ID.
    :return: Response object
    """
    return make_response(jsonify(parking_lot_controller.find_by_id(parking_lot_id)), HTTPStatus.OK)


@parking_lot_bp.get('/parking_id/<int:parking_id>')
def get_parking_lot_by_parking_id(parking_id: int) -> Response:
    """
    Gets parking_lot by parking_id.
    :return: Response object
    """
    return make_response(jsonify(parking_lot_controller.find_by_parking_id(parking_id)), HTTPStatus.OK)


@parking_lot_bp.get('/car_id/<int:car_id>')
def get_parking_lot_by_car_id(car_id: int) -> Response:
    """
    Gets parking_lot by car_id.
    :return: Response object
    """
    return make_response(jsonify(parking_lot_controller.find_by_car_id(car_id)), HTTPStatus.OK)


@parking_lot_bp.get('/free')
def get_free_parking_lots() -> Response:
    """
    Gets free parking_lots.
    :return: Response object
    """
    return make_response(jsonify(parking_lot_controller.find_all_free()), HTTPStatus.OK)


@parking_lot_bp.get('/not_reserved')
def get_not_reserved_parking_lots() -> Response:
    """
    Gets not reserved parking_lots.
    :return: Response object
    """
    return make_response(jsonify(parking_lot_controller.find_not_reserved()), HTTPStatus.OK)


@parking_lot_bp.put('/<int:parking_lot_id>')
def update_parking_lot(parking_lot_id: int) -> Response:
    """
    Updates parking_lot by ID.
    :return: Response object
    """
    content = request.get_json()
    parking_lot = ParkingLot.create_from_dto(content)
    parking_lot_controller.update(parking_lot_id, parking_lot)
    return make_response("Parking Lot updated", HTTPStatus.OK)


@parking_lot_bp.patch('/<int:parking_lot_id>')
def patch_parking_lot(parking_lot_id: int) -> Response:
    """
    Patches parking_lot by ID.
    :return: Response object
    """
    content = request.get_json()
    parking_lot_controller.patch(parking_lot_id, content)
    return make_response("Parking Lot updated", HTTPStatus.OK)


@parking_lot_bp.delete('/<int:parking_lot_id>')
def delete_parking_lot(parking_lot_id: int) -> Response:
    """
    Deletes parking_lot by ID.
    :return: Response object
    """
    parking_lot_controller.delete(parking_lot_id)
    return make_response("Parking Lot deleted", HTTPStatus.OK)
