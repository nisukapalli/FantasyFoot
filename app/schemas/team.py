# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime

# class TeamBase(BaseModel):
#     name: str

# class TeamCreate(TeamBase):
#     league_id: int

# class TeamUpdate(BaseModel):
#     name: Optional[str] = None
#     status: Optional[str] = None

# class TeamResponse(TeamBase):
#     id: int
#     league_id: int
#     user_id: int
#     total_points: int
#     draft_position: Optional[int] = None
#     status: str
#     created_at: datetime

#     class Config:
#         from_attributes = True