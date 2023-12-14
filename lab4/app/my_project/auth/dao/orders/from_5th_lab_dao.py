import sqlalchemy

from ..general_dao import GeneralDAO
from ...domain import From5thLab


class From5thLabDao(GeneralDAO):
    """
    Realisation of BonusCard data access layer.
    """
    _domain_type = From5thLab

    def insert_noname(self, reservation_id):
        """
        Inserts a company into the database.
        :return: None (no need to return anything for an INSERT)
        """
        self._session.execute(sqlalchemy.text("CALL InsertRows(:p1)"),
                              {"p1": reservation_id})
        self._session.commit()
