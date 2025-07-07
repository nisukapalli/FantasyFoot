from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    away_team_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    league_name = Column(String(25), nullable=False)
    match_date = Column(DateTime(timezone=True), nullable=False)
    home_score = Column(Integer, nullable=True)
    away_score = Column(Integer, nullable=True)
    is_finished = Column(Boolean, default=False)
    is_postponed = Column(Boolean, default=False)
    external_match_id = Column(String(50), nullable=True)  # For syncing with external APIs
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    home_team = relationship("Club", foreign_keys=[home_team_id])
    away_team = relationship("Club", foreign_keys=[away_team_id])
    player_performances = relationship("PlayerPerformance", back_populates="match")