from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response


from ...controller import from_5th_lab_controller
from ...domain import From5thLab

from_5th_lab_bp = Blueprint('from_5th_labs', __name__, url_prefix='/from_5th_labs')


@from_5th_lab_bp.get('')
def get_all_from_5th_labs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(from_5th_lab_controller.find_all()), HTTPStatus.OK)


@from_5th_lab_bp.post('')
def create_from_5th_lab() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    from_5th_lab = From5thLab.create_from_dto(content)
    from_5th_lab_controller.create(from_5th_lab)
    return make_response(jsonify(from_5th_lab.put_into_dto()), HTTPStatus.CREATED)


@from_5th_lab_bp.put('/<int:from_5th_lab_id>')
def update_from_5th_lab(from_5th_lab_id: int) -> Response:
    """
    Updates bonus card by ID.
    :return: Response object
    """
    content = request.get_json()
    from_5th_lab = From5thLab.create_from_dto(content)
    from_5th_lab_controller.update(from_5th_lab_id, from_5th_lab)
    return make_response("Bonus card updated", HTTPStatus.OK)


@from_5th_lab_bp.patch('/<int:from_5th_lab_id>')
def patch_from_5th_lab(from_5th_lab_id: int) -> Response:
    """
    Patches bonus card by ID.
    :return: Response object
    """
    content = request.get_json()
    from_5th_lab_controller.patch(from_5th_lab_id, content)
    return make_response("Noname updated", HTTPStatus.OK)


@from_5th_lab_bp.delete('/<int:from_5th_lab_id>')
def delete_from_5th_lab(from_5th_lab_id: int) -> Response:
    """
    Deletes bonus card by ID.
    :return: Response object
    """
    from_5th_lab_controller.delete(from_5th_lab_id)
    return make_response("Bonus card deleted", HTTPStatus.OK)


@from_5th_lab_bp.post('/insert/<int:reservation_id>')
def insert_noname(reservation_id) -> Response:
    """
    Inserts a company into the database.
    :return: Response object
    """
    return make_response(jsonify(from_5th_lab_controller.insert_noname(reservation_id)),
                         HTTPStatus.OK)