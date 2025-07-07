from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    team_from_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team_to_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    
    status = Column(String(20), default="pending")  # pending, accepted, rejected, cancelled
    proposed_at = Column(DateTime(timezone=True), server_default=func.now())
    responded_at = Column(DateTime(timezone=True), nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    
    players_from = Column(Text, nullable=True)  # JSON array of player IDs from team_from
    players_to = Column(Text, nullable=True)    # JSON array of player IDs from team_to
    
    message = Column(Text, nullable=True)
    
    league = relationship("League")
    team_from = relationship("Team", foreign_keys=[team_from_id])
    team_to = relationship("Team", foreign_keys=[team_to_id])