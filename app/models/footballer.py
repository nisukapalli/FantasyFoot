from sqlalchemy import Column, Integer, String, ForeignKey, Date
from .base import Base

class Footballer(Base):
    __tablename__ = "footballers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    full_name = Column(String(100), nullable=False)
    position = Column(String(3), nullable=False)
    club = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    league_name = Column(String(25), nullable=False)
    selected_by = Column(Integer, ForeignKey("users.id"))
    nationality = Column(String(50), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    shirt_number = Column(Integer, nullable=True)
    photo_url = Column(String(255), nullable=True)
    external_api_id = Column(String(50), nullable=True)  # For syncing with external APIs