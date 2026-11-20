from backend_admin.database.db_connection.engine import engine
from backend_admin.classes.Base import Base
from backend_admin.classes.Government import Government
from backend_admin.classes.PartyProgram import PartyProgram
from backend_admin.classes.Party_In_Government import PartyInGovernment
from backend_admin.classes.Party import Party
from backend_admin.classes.Act import Act

print("Tabelle registrate:", list(Base.metadata.tables))
print("Destinazione:", engine.url.host, engine.url.port, engine.url.database)

def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)