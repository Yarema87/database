from ...service import from_5th_lab_service
from ...domain import From5thLab
from ..general_controller import GeneralController


class From5thLabController(GeneralController):
    """
    Realisation of BonusCard controller.
    """
    _service = from_5th_lab_service

    def insert_noname(self, reservation_id):
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number
        using Service layer as DTO objects.
        """
        return self._service.insert_noname(reservation_id)
