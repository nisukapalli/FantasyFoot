from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.models.base import SessionLocal
from app.models.user import User
from app.models.club import Club
from app.schemas.club import ClubResponse
from app.auth.jwt import get_current_active_user

router = APIRouter(prefix="/clubs", tags=["clubs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ClubResponse])
def read_clubs(
    skip: int = 0,
    limit: int = 100,
    league_name: Optional[str] = Query(None, description="Filter by league name"),
    country: Optional[str] = Query(None, description="Filter by country"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get list of clubs with optional filters"""
    query = db.query(Club)
    
    if league_name:
        query = query.filter(Club.league_name == league_name)
    
    if country:
        query = query.filter(Club.country == country)
    
    clubs = query.offset(skip).limit(limit).all()
    return clubs

@router.get("/{club_id}", response_model=ClubResponse)
def read_club(
    club_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get club by ID"""
    club = db.query(Club).filter(Club.id == club_id).first()
    if club is None:
        raise HTTPException(status_code=404, detail="Club not found")
    return club

@router.get("/league/{league_name}", response_model=List[ClubResponse])
def read_league_clubs(
    league_name: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all clubs in a specific league"""
    clubs = db.query(Club).filter(
        Club.league_name == league_name
    ).offset(skip).limit(limit).all()
    return clubs