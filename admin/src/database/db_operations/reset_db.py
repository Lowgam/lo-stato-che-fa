from admin.src.database.engine import engine
from admin.src.classes.Base import Base

print("Tabelle registrate:", list(Base.metadata.tables))
print("Destinazione:", engine.url.host, engine.url.port, engine.url.database)

def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)