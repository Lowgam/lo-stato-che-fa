from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, CheckConstraint

from src.classes.Base import Base

class Party(Base):
    __tablename__ = "party"
    __table_args__ = (CheckConstraint("party_name <> ''", name='party_name_not_space'),)

    party_id = Column(Integer, primary_key=True)
    party_name = Column(String(30), nullable=False, unique=True)
    party_website = Column(Text, nullable=False)
    party_pic_path = Column(String(20), nullable=False)

    party_program_rel = relationship('PartyProgram', back_populates='party_rel', passive_deletes=True)

    government_rel = relationship('Government', secondary='party_in_government', back_populates='party_rel')