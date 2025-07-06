from sqlalchemy import Column, Integer, String
from .base import Base

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(25), nullable=False)
    abbreviation = Column(String(3), nullable=False)
    league_name = Column(String(50), nullable=False)
    city = Column(String(50))
    country = Column(String(50))
    stadium = Column(String(100))
    crest_url = Column(String(255))