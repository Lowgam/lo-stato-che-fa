from admin.src.classes.Party import Party
from admin.src.database.context_manager import get_session

# I leave this part open for future implementations. At the moment the logic of the software doesn't need a
# delete feature. Old govs, acts and parties should be archived.

def delete_party(p : Party):
    with get_session() as session:
        session.delete(p)

