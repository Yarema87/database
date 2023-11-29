from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import driver_controller
from ...domain import Driver

driver_bp = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_bp.get('')
def get_all_drivers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_all()), HTTPStatus.OK)


@driver_bp.post('')
def create_driver() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.create(driver)
    return make_response(jsonify(driver.put_into_dto()), HTTPStatus.CREATED)


@driver_bp.get('/id/<int:driver_id>')
def get_driver(driver_id: int) -> Response:
    """
    Gets driver by ID.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_id(driver_id)), HTTPStatus.OK)


@driver_bp.get('/name/<string:driver_name>')
def get_driver_by_name(driver_name: str) -> Response:
    """
    Gets driver by name.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_name(driver_name)), HTTPStatus.OK)


@driver_bp.get('/age/<int:driver_age>')
def get_driver_by_age(driver_age: int) -> Response:
    """
    Gets driver by age.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_age(driver_age)), HTTPStatus.OK)


@driver_bp.get('/phone/<string:driver_phone>')
def get_driver_by_phone(driver_phone: str) -> Response:
    """
    Gets driver by phone.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_phone(driver_phone)), HTTPStatus.OK)


@driver_bp.get('/company_id/<int:company_id>')
def get_driver_by_company_id(company_id: int) -> Response:
    """
    Gets driver by company_id.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_company_id(company_id)), HTTPStatus.OK)


@driver_bp.put('/<int:driver_id>')
def update_driver(driver_id: int) -> Response:
    """
    Updates driver by ID.
    :return: Response object
    """
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.update(driver_id, driver)
    return make_response("driver updated", HTTPStatus.OK)


@driver_bp.patch('/<int:driver_id>')
def patch_driver(driver_id: int) -> Response:
    """
    Patches driver by ID.
    :return: Response object
    """
    content = request.get_json()
    driver_controller.patch(driver_id, content)
    return make_response("driver updated", HTTPStatus.OK)


@driver_bp.delete('/<int:driver_id>')
def delete_driver(driver_id: int) -> Response:
    """
    Deletes driver by ID.
    :return: Response object
    """
    driver_controller.delete(driver_id)
    return make_response("driver deleted", HTTPStatus.OK)
