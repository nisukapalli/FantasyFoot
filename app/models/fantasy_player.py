from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class FantasyPlayer(Base):
    __tablename__ = "fantasy_players"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    footballer_id = Column(Integer, ForeignKey("footballers.id"), nullable=False)
    is_captain = Column(Boolean, default=False)
    is_vice_captain = Column(Boolean, default=False)
    is_bench = Column(Boolean, default=False)
    bench_position = Column(Integer, nullable=True)
    added_at = Column(DateTime(timezone=True), server_default=func.now())
    removed_at = Column(DateTime(timezone=True), nullable=True)
    
    team = relationship("Team", back_populates="fantasy_players")
    footballer = relationship("Footballer") 