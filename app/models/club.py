from sqlalchemy import Column, Integer, String
from .base import Base

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    abbreviation = Column(String(3), nullable=False)
    league_name = Column(String(50), nullable=False)
    city = Column(String(50), nullable=True)
    country = Column(String(50), nullable=True)
    stadium = Column(String(100), nullable=True)
    crest_url = Column(String(255), nullable=True)