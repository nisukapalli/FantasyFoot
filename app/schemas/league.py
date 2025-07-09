from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LeagueBase(BaseModel):
    name: str
    description: Optional[str] = None
    league_name: str
    draft_type: str = "snake"
    max_teams: int = 15
    is_private: bool = True

class LeagueCreate(LeagueBase):
    pass

class LeagueUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    draft_type: Optional[str] = None
    max_teams: Optional[int] = None
    is_private: Optional[bool] = None
    status: Optional[str] = None

class LeagueJoin(BaseModel):
    invite_code: str

class LeagueResponse(LeagueBase):
    id: int
    admin_id: int
    invite_code: Optional[str] = None
    status: str
    created_at: datetime
    team_count: Optional[int] = None

    class Config:
        from_attributes = True