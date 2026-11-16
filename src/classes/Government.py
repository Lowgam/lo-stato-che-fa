from sqlalchemy import Column, Integer, Boolean, CheckConstraint
from sqlalchemy.orm import relationship

from src.classes.Act import Act
from src.classes.Party import Party
from src.classes.Base import Base

from typing import List

class Government(Base):
    __tablename__ = 'government'
    __table_args__ = (CheckConstraint("government_name <> ''", name='party_name_not_space'),)

    government_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    year = Column(Integer)
    is_current = Column(Boolean, default=True, nullable=False)

    act_rel = relationship("Act", back_populates="government_rel")
    party_rel = relationship('Party', secondary='parties_in_government', back_populates='government_rel')