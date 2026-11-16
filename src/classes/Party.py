from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text

from src.classes.Base import Base

class Party(Base):
    __tablename__ = "party"

    party_id = Column(Integer, primary_key=True)
    party_name = Column(String(30), nullable=False, unique=True)
    party_website = Column(Text, nullable=False)
    party_pic_path = Column(String(20), nullable=False)

    party_program_rel = relationship('PartyProgram', back_populates='party_rel')
    government_rel = relationship('Government', secondary='parties_in_government', back_populates='party_rel')


