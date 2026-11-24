from sqlalchemy import select

from backend_admin.classes.Government import Government
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

def select_current_government():
    with get_session() as session:
        stmt = select(Government).where(Government.is_current == True)
        result = session.execute(stmt).scalar()
        return result

def select_all_governments():
    with get_session() as session:
        stmt = select(Government)
        result = session.execute(stmt).scalars().all()
        return result

def select_government_details(gt_id : int):
    with get_session() as session:
        stmt = select(Government).where(Government.government_id == gt_id)
        result = session.execute(stmt).scalar()
        return result

def select_all_government_acts(g_id : int):
    with get_session() as session:
        stmt = select(Government)

