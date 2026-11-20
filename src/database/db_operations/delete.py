from src.classes.Party import Party
from src.classes.PartyProgram import PartyProgram
from src.classes.Government import Government
from src.classes.Party_In_Government import PartyInGovernment
from src.classes.Act import Act
from src.database.context_manager import get_session

# I leave this part open for future implementations. At the moment the logic of the software doesn't need a
# delete feature. Old govs, acts and parties should be archived.

def delete_party(p : Party):
    with get_session() as session:
        session.delete(p)

