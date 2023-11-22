from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import car_controller
from ...domain import Car

car_bp = Blueprint('cars', __name__, url_prefix='/cars')


@car_bp.get('')
def get_all_cars() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_all()), HTTPStatus.OK)


@car_bp.post('')
def create_car() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.create(car)
    return make_response(jsonify(car.put_into_dto()), HTTPStatus.CREATED)


@car_bp.get('/id/<int:car_id>')
def get_car(car_id: int) -> Response:
    """
    Gets car by ID.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_by_id(car_id)), HTTPStatus.OK)


@car_bp.get('/model/<string:car_model>')
def get_car_by_model(car_model: str) -> Response:
    """
    Gets car by model.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_by_model(car_model)), HTTPStatus.OK)


@car_bp.get('/number/<string:car_model>')
def get_car_by_number(car_number: str) -> Response:
    """
    Gets car by number.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_by_number(car_number)), HTTPStatus.OK)


@car_bp.get('/arriving/<path:car_arriving>')
def get_car_by_arriving(car_arriving: datetime) -> Response:
    """
    Gets car by arriving.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(car_arriving, '%Y-%m-%dT%H:%M:%S')
        return parsed_date, make_response(jsonify(car_controller.find_by_arriving(car_arriving)), HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@car_bp.get('/departure/<path:car_departure>')
def get_car_by_departure(car_departure: datetime) -> Response:
    """
    Gets car by model.
    :return: Response object
    """
    try:
        parsed_date = datetime.strptime(car_departure, '%Y-%m-%dT%H:%M:%S')
        return parsed_date, make_response(jsonify(car_controller.find_by_departure(car_departure)), HTTPStatus.OK)
    except ValueError:
        return "Invalid datetime format"


@car_bp.get('/driver_id/<int:driver_id>')
def get_car_by_driver_id(driver_id: int) -> Response:
    """
    Gets car by driver_id.
    :return: Response object
    """
    return make_response(jsonify(car_controller.find_by_driver_id(driver_id)), HTTPStatus.OK)


@car_bp.put('/<int:car_id>')
def update_car(car_id: int) -> Response:
    """
    Updates car by ID.
    :return: Response object
    """
    content = request.get_json()
    car = Car.create_from_dto(content)
    car_controller.update(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)


@car_bp.patch('/<int:car_id>')
def patch_car(car_id: int) -> Response:
    """
    Patches car by ID.
    :return: Response object
    """
    content = request.get_json()
    car_controller.patch(car_id, content)
    return make_response("Car updated", HTTPStatus.OK)


@car_bp.delete('/<int:car_id>')
def delete_car(car_id: int) -> Response:
    """
    Deletes car by ID.
    :return: Response object
    """
    car_controller.delete(car_id)
    return make_response("Car deleted", HTTPStatus.OK)
