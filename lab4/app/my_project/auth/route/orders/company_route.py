from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from ...controller import company_controller
from ...domain import Company

company_bp = Blueprint('companies', __name__, url_prefix='/companies')


@company_bp.get('')
def get_all_companies() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(company_controller.find_all()), HTTPStatus.OK)


@company_bp.post('')
def create_company() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)


@company_bp.get('/id/<int:company_id>')
def get_company_by_id(company_id: int) -> Response:
    """
    Gets company by ID.
    :return: Response object
    """
    return make_response(jsonify(company_controller.find_by_id(company_id)), HTTPStatus.OK)


@company_bp.get('/drivers/<int:company_number_of_drivers>')
def get_company_by_number_of_drivers(company_number_of_drivers: int) -> Response:
    """
    Gets company by number of drivers.
    :return: Response object
    """
    return make_response(jsonify(company_controller.find_by_number_of_drivers(company_number_of_drivers)), HTTPStatus.OK)


@company_bp.get('/name/<string:company_name>')
def get_company_by_name(company_name: str) -> Response:
    """
    Gets company by name.
    :return: Response object
    """
    return make_response(jsonify(company_controller.find_by_name(company_name)), HTTPStatus.OK)


@company_bp.put('/<int:company_id>')
def update_company(company_id: int) -> Response:
    """
    Updates company by ID.
    :return: Response object
    """
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.update(company_id, company)
    return make_response("Company updated", HTTPStatus.OK)


@company_bp.patch('/<int:company_id>')
def patch_company(company_id: int) -> Response:
    """
    Patches company by ID.
    :return: Response object
    """
    content = request.get_json()
    company_controller.patch(company_id, content)
    return make_response("Company updated", HTTPStatus.OK)


@company_bp.delete('/<int:company_id>')
def delete_company(company_id: int) -> Response:
    """
    Deletes company by ID.
    :return: Response object
    """
    company_controller.delete(company_id)
    return make_response("Company deleted", HTTPStatus.OK)


@company_bp.post('/insert/<string:p_name>/<int:p_number_of_drivers>')
def insert_company(p_name: str, p_number_of_drivers: int) -> Response:
    """
    Inserts a company into the database.
    :param p_name: name
    :param p_number_of_drivers: number value
    :return: Response object
    """
    return make_response(jsonify(company_controller.insert_company(p_name, p_number_of_drivers)),
                         HTTPStatus.OK)

