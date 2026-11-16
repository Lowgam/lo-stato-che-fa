from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.classes.Base import Base

class PartyProgram(Base):
    __tablename__ = 'party-program'

    program_id = Column(Integer, primary_key=True)
    party_id = Column(ForeignKey('party.party_id'), nullable=False)

    year = Column(Integer)
    program_website = Column(Text)
    is_current = Column(Boolean, default=True)

    party_rel = relationship('Party', back_populates='party_program_rel')