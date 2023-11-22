from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import reservation_controller
from ...domain import Reservation

reservation_bp = Blueprint('reservations', __name__, url_prefix='/reservations')


@reservation_bp.get('')
def get_all_reservations() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(reservation_controller.find_all()), HTTPStatus.OK)


@reservation_bp.post('')
def create_reservation() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.create(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)


@reservation_bp.get('/id/<int:reservation_id>')
def get_reservation_by_id(reservation_id: int) -> Response:
    """
    Gets reservation by ID.
    :return: Response object
    """
    return make_response(jsonify(reservation_controller.find_by_id(reservation_id)), HTTPStatus.OK)


@reservation_bp.get('/arrival/<path:reservation_arrival>')
def get_reservation_by_arrival(reservation_arrival: datetime) -> Response:
    """
    Gets reservation by arrival.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(reservation_arrival, '%Y-%m-%dT%H:%M:%S')
        return parsed_date, make_response(jsonify(reservation_controller.find_by_arrival(reservation_arrival)), HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@reservation_bp.get('/departure/<path:reservation_departure>')
def get_reservation_by_departure(reservation_departure: datetime) -> Response:
    """
    Gets reservation by departure.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(reservation_departure, '%Y-%m-%dT%H:%M:%S')
        return parsed_date, make_response(jsonify(reservation_controller.find_by_departure(reservation_departure)), HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@reservation_bp.get('/parking_lot_id/<int:parking_lot_id>')
def get_reservation_by_parking_lot_id(parking_lot_id: int) -> Response:
    """
    Gets reservation by parking_lot_id.
    :return: Response object
    """
    return make_response(jsonify(reservation_controller.find_by_parking_lot_id(parking_lot_id)), HTTPStatus.OK)


@reservation_bp.get('/driver_id/<int:driver_id>')
def get_reservation_by_driver_id(driver_id: int) -> Response:
    """
    Gets reservation by driver_id.
    :return: Response object
    """
    return make_response(jsonify(reservation_controller.find_by_driver_id(driver_id)), HTTPStatus.OK)


@reservation_bp.put('/<int:reservation_id>')
def update_reservation(reservation_id: int) -> Response:
    """
    Updates parking by ID.
    :return: Response object
    """
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.update(reservation_id, reservation)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservation_bp.patch('/<int:reservation_id>')
def patch_reservation(reservation_id: int) -> Response:
    """
    Patches reservation by ID.
    :return: Response object
    """
    content = request.get_json()
    reservation_controller.patch(reservation_id, content)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservation_bp.delete('/<int:reservation_id>')
def delete_reservation(reservation_id: int) -> Response:
    """
    Deletes reservation by ID.
    :return: Response object
    """
    reservation_controller.delete(reservation_id)
    return make_response("Reservation deleted", HTTPStatus.OK)
