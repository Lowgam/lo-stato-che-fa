from sqlalchemy import Column, Integer, Boolean, CheckConstraint
from sqlalchemy.orm import relationship

from src.classes.Base import Base

class Government(Base):
    __tablename__ = 'government'

    government_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    year = Column(Integer)
    is_current = Column(Boolean, default=True, nullable=False)

    act_rel = relationship("Act", back_populates="government_rel", passive_deletes=True, cascade="all, delete")

    party_rel = relationship('Party', secondary='party_in_government', back_populates='government_rel', passive_deletes=True)