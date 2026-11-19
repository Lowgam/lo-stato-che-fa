from src.classes.Party import Party
from src.classes.PartyProgram import PartyProgram
from src.classes.Government import Government
from src.classes.Party_In_Government import PartyInGovernment
from src.classes.Act import Act
from src.database.context_manager import get_session

def delete_party(p : Party):
    with get_session() as session:
        session.delete(p)

