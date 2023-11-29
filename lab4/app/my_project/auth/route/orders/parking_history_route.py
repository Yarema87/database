from _decimal import Decimal
from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import parking_history_controller
from ...domain import ParkingHistory

parking_history_bp = Blueprint('parking_history', __name__, url_prefix='/parking_history')


@parking_history_bp.get('')
def get_all_parking_history() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(parking_history_controller.find_all()), HTTPStatus.OK)


@parking_history_bp.post('')
def create_parking_history() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    parking_history = ParkingHistory.create_from_dto(content)
    parking_history_controller.create(parking_history)
    return make_response(jsonify(parking_history.put_into_dto()), HTTPStatus.CREATED)


@parking_history_bp.get('/id/<int:parking_history_id>')
def get_parking_history(parking_history_id: int) -> Response:
    """
    Gets parking_history by ID.
    :return: Response object
    """
    return make_response(jsonify(parking_history_controller.find_by_id(parking_history_id)), HTTPStatus.OK)


@parking_history_bp.get('/arrival/<path:parking_history_arrival>')
def get_parking_history_by_arrival(parking_history_arrival: int) -> Response:
    """
    Gets parking_history by arrival.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(parking_history_arrival, '%Y-%m-%dT%H:%M:%S')
        return parsed_date, make_response(jsonify(parking_history_controller.find_by_arrival(parking_history_arrival)),
                                          HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@parking_history_bp.get('/departure/<path:parking_history_departure>')
def get_parking_history_by_departure(parking_history_departure: int) -> Response:
    """
    Gets parking_history by departure.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(parking_history_departure, '%Y-%m-%dT%H:%M:%S')
        return parsed_date, make_response(jsonify(parking_history_controller.find_by_departure(parking_history_departure)),
                                          HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@parking_history_bp.get('/price/<float:parking_history_price>')
def get_parking_history_by_price(parking_history_price: Decimal) -> Response:
    """
    Gets parking_history by price.
    :return: Response object
    """
    return make_response(jsonify(parking_history_controller.find_by_price(parking_history_price)), HTTPStatus.OK)


@parking_history_bp.get('/parking_lot_id/<int:parking_lot_id>')
def get_parking_history_by_parking_lot_id(parking_lot_id: int) -> Response:
    """
    Gets parking_history by parking_lot_id.
    :return: Response object
    """
    return make_response(jsonify(parking_history_controller.find_by_parking_lot_id(parking_lot_id)), HTTPStatus.OK)


@parking_history_bp.get('/car_id/<int:car_id>')
def get_parking_history_by_car_id(car_id: int) -> Response:
    """
    Gets parking_history by ID.
    :return: Response object
    """
    return make_response(jsonify(parking_history_controller.find_by_car_id(car_id)), HTTPStatus.OK)


@parking_history_bp.put('/<int:parking_history_id>')
def update_parking_history(parking_history_id: int) -> Response:
    """
    Updates parking_history by ID.
    :return: Response object
    """
    content = request.get_json()
    parking_history = ParkingHistory.create_from_dto(content)
    parking_history_controller.update(parking_history_id, parking_history)
    return make_response("Parking History updated", HTTPStatus.OK)


@parking_history_bp.patch('/<int:parking_history_id>')
def patch_parking_history(parking_history_id: int) -> Response:
    """
    Patches parking_history by ID.
    :return: Response object
    """
    content = request.get_json()
    parking_history_controller.patch(parking_history_id, content)
    return make_response("Parking History updated", HTTPStatus.OK)


@parking_history_bp.delete('/<int:parking_history_id>')
def delete_parking_history(parking_history_id: int) -> Response:
    """
    Deletes parking_history by ID.
    :return: Response object
    """
    parking_history_controller.delete(parking_history_id)
    return make_response("Parking History deleted", HTTPStatus.OK)
