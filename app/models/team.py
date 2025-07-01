from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from .base import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    user = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    total_points = Column(Integer, default=0)
    draft_position = Column(Integer, nullable=True)
    status = Column(String(20), nullable=False, default="active")
