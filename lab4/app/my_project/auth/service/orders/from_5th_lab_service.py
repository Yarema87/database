from ...dao import from_5th_lab_dao
from ...domain import From5thLab
from ..general_service import GeneralService


class From5thLabService(GeneralService):
    """
    Realisation of BonusCard service.
    """
    _dao = from_5th_lab_dao

    def insert_noname(self, reservation_id):
        """
        Inserts a company into the database.
        :return: None (no need to return anything for an INSERT)
        """
        self._dao.insert_noname(reservation_id)
