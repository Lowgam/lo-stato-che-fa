from sqlalchemy.orm import sessionmaker

from backend_admin.database.db_connection.engine import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)