from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from src.classes.Base import Base

class PartiesInGovernment(Base):
    __tablename__ = 'parties_in_government'
    __table_args__ = (UniqueConstraint('party_id', 'government_id', name='Unique_party_gov'),)

    parties_in_government_id = Column(Integer, primary_key=True, nullable=False)
    party_id = Column(Integer, ForeignKey('party.party_id', ondelete='RESTRICT'), nullable=False)
    government_id = Column(Integer, ForeignKey('government.government_id', ondelete='RESTRICT'), nullable=False)

