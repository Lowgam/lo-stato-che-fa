from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text

class Base(DeclarativeBase):
    pass

class Party(Base):
    __tablename__ = "parties"

    party_id = Column(Integer, primary_key=True)
    party_name = Column(String(30))
    program_website = Column(Text)
    party_website = Column(Text)
    party_pic_path = Column(String(20))

