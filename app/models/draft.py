from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Draft(Base):
    __tablename__ = "drafts"

    id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    status = Column(String(20), default="pending")  # pending, active, completed, cancelled
    draft_type = Column(String(20), default="snake")  # snake, linear
    current_pick = Column(Integer, default=1)
    current_round = Column(Integer, default=1)
    max_rounds = Column(Integer, default=15)
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    league = relationship("League")
    picks = relationship("DraftPick", back_populates="draft", cascade="all, delete-orphan")

class DraftPick(Base):
    __tablename__ = "draft_picks"

    id = Column(Integer, primary_key=True, index=True)
    draft_id = Column(Integer, ForeignKey("drafts.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    footballer_id = Column(Integer, ForeignKey("footballers.id"), nullable=True)  # null if not picked yet
    pick_number = Column(Integer, nullable=False)
    round_number = Column(Integer, nullable=False)
    position = Column(String(3), nullable=True)
    picked_at = Column(DateTime(timezone=True), nullable=True)
    auto_pick = Column(Boolean, default=False)

    draft = relationship("Draft", back_populates="picks")
    team = relationship("Team")
    footballer = relationship("Footballer")