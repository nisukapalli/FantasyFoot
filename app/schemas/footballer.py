from pydantic import BaseModel
from typing import Optional
from datetime import date

class FootballerResponse(BaseModel):
    id: int
    name: str
    full_name: str
    position: str
    club_id: int
    league_name: str
    selected_by: Optional[int] = None
    birth_date: Optional[date] = None
    region: Optional[int] = None
    nationality: Optional[str] = None
    shirt_number: Optional[int] = None
    photo_url: Optional[str] = None
    external_api_id: Optional[str] = None

    class Config:
        from_attributes = True