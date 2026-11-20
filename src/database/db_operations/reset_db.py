from src.database.engine import engine
from src.classes.Base import Base
from src.classes.Party import Party
from src.classes.Government import Government
from src.classes.Act import Act
from src.classes.PartyProgram import PartyProgram
from src.classes.Party_In_Government import PartyInGovernment

print("Tabelle registrate:", list(Base.metadata.tables))
print("Destinazione:", engine.url.host, engine.url.port, engine.url.database)

def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)