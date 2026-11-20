from sqlalchemy import Column, Integer, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from admin.src.classes.Base import Base

class Act(Base):
    __tablename__ = 'act'
    __table_args__ = (CheckConstraint("act_title <> ''", name='party_name_not_space'),)

    act_id = Column(Integer, primary_key=True)
    government_id = Column(ForeignKey('government.government_id', ondelete='CASCADE'), nullable=False)

    act_title = Column(Text)
    act_description = Column(Text)
    act_link = Column(Text)

    government_rel = relationship("Government", back_populates="act_rel")