from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Footballer(Base):
    __tablename__ = "footballers"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(25), nullable=False)
    full_name = Column(String(100), nullable=False)
    position = Column(String(3), nullable=False)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    league_name = Column(String(25), nullable=False)
    selected_by = Column(Integer, ForeignKey("users.id"))
    birth_date = Column(Date)
    region = Column(Integer)
    nationality = Column(String(50))
    shirt_number = Column(Integer)
    photo_url = Column(String(255))
    external_api_id = Column(String(50))  # For syncing with external APIs
    
    club = relationship("Club")
    fantasy_players = relationship("FantasyPlayer")
    player_performances = relationship("PlayerPerformance")
    draft_picks = relationship("DraftPick")
    selected_by_user = relationship("User", foreign_keys=[selected_by])
