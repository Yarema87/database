from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import parking_controller
from ...domain import Parking

parking_bp = Blueprint('parkings', __name__, url_prefix='/parkings')


@parking_bp.get('')
def get_all_parkings() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_all()), HTTPStatus.OK)


@parking_bp.post('')
def create_parking() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    parking = Parking.create_from_dto(content)
    parking_controller.create(parking)
    return make_response(jsonify(parking.put_into_dto()), HTTPStatus.CREATED)


@parking_bp.get('/id/<int:parking_id>')
def get_parking(parking_id: int) -> Response:
    """
    Gets parking by ID.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_id(parking_id)), HTTPStatus.OK)


@parking_bp.get('/street/<string:parking_street>')
def get_parking_by_street(parking_street: str) -> Response:
    """
    Gets parking by street.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_street(parking_street)),
                         HTTPStatus.OK)


@parking_bp.get('/city/<string:parking_city>')
def get_parking_by_city(parking_city: str) -> Response:
    """
    Gets parking by city.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_city(parking_city)),
                         HTTPStatus.OK)


@parking_bp.get('/lots_number/<int:parking_lots_number>')
def get_parking_by_lots_number(parking_lots_number: int) -> Response:
    """
    Gets parking by lots number.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_lots_number(parking_lots_number)),
                         HTTPStatus.OK)


@parking_bp.get('/free_lots/<int:parking_free_lots>')
def get_parking_by_free_lots(parking_free_lots: int) -> Response:
    """
    Gets parking by free lots.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_free_lots(parking_free_lots)),
                         HTTPStatus.OK)


@parking_bp.get('/parking_headmaster/<string:parking_headmaster>')
def get_parking_by_parking_headmaster(parking_headmaster: str) -> Response:
    """
    Gets parking by headmaster.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_parking_headmaster(parking_headmaster)),
                         HTTPStatus.OK)


@parking_bp.get('/phone/<string:parking_phone>')
def get_parking_by_phone(parking_phone: str) -> Response:
    """
    Gets parking by phone.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_phone(parking_phone)),
                         HTTPStatus.OK)


@parking_bp.get('/company_owner_id/<int:company_owner_id>')
def get_parking_by_company_owner_id(company_owner_id: int) -> Response:
    """
    Gets parking by company owner id.
    :return: Response object
    """
    return make_response(jsonify(parking_controller.find_by_company_owner_id(company_owner_id)),
                         HTTPStatus.OK)


@parking_bp.put('/<int:parking_id>')
def update_parking(parking_id: int) -> Response:
    """
    Updates parking by ID.
    :return: Response object
    """
    content = request.get_json()
    parking = Parking.create_from_dto(content)
    parking_controller.update(parking_id, parking)
    return make_response("Parking updated", HTTPStatus.OK)


@parking_bp.patch('/<int:parking_id>')
def patch_parking(parking_id: int) -> Response:
    """
    Patches parking by ID.
    :return: Response object
    """
    content = request.get_json()
    parking_controller.patch(parking_id, content)
    return make_response("Parking updated", HTTPStatus.OK)


@parking_bp.delete('/<int:parking_id>')
def delete_parking(parking_id: int) -> Response:
    """
    Deletes parking by ID.
    :return: Response object
    """
    parking_controller.delete(parking_id)
    return make_response("Parking deleted", HTTPStatus.OK)
