from contextlib import contextmanager

from admin.src.database.session import SessionLocal

@contextmanager
def get_session():
    session = SessionLocal()
    try :
        yield session # the code runs and the session can be used
        session.commit() # commit the changes of this session
    except Exception as e :
        session.rollback() # in case of error, rollback
        print(f"Error: {e}")
    finally:
        session.close() # close the session