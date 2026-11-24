<<<<<<< HEAD
from sqlalchemy import select

from backend_admin.classes.Party import Party
from backend_admin.database.db_connection.context_manager import get_session

def select_parties_list():
    with get_session() as session:
        stmt = select(Party).where(Party.is_archived == False)
        result = session.execute(stmt).scalars().all()
        return result

def select_party_details(p_id : int):
    with get_session() as session:
        stmt = select(Party).where(Party.party_id == p_id)
        result = session.execute(stmt).scalar()
        return result
=======

>>>>>>> c19744c14254a88a7fa751eca240214068fcc740
