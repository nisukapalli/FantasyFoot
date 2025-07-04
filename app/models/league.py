from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from .base import Base

class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    description = Column(String(100))
    league_name = Column(String(25), nullable=False)
    admin = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    draft_type = Column(String(20), nullable=False, default="snake")
    max_teams = Column(Integer, nullable=True)
    is_private = Column(Boolean, default=True)
    invite_code = Column(String(20), nullable=True, unique=True)
    status = Column(String(20), nullable=False, default="active")