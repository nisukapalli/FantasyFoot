# from typing import List, Optional
# from fastapi import APIRouter, Depends, HTTPException, status, Query
# from sqlalchemy.orm import Session

# from app.models.base import SessionLocal
# from app.models.user import User
# from app.models.footballer import Footballer
# from app.models.club import Club
# from app.schemas.footballer import FootballerResponse
# from app.auth.jwt import get_current_active_user

# router = APIRouter(prefix="/footballers", tags=["footballers"])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/", response_model=List[FootballerResponse])
# def read_footballers(
#     skip: int = 0,
#     limit: int = 100,
#     league_name: Optional[str] = Query(None, description="Filter by league name"),
#     position: Optional[str] = Query(None, description="Filter by position (GK, DEF, MID, FWD)"),
#     club_id: Optional[int] = Query(None, description="Filter by club ID"),
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_active_user)
# ):
#     """Get list of footballers with optional filters"""
#     query = db.query(Footballer)
    
#     if league_name:
#         query = query.filter(Footballer.league_name == league_name)
    
#     if position:
#         query = query.filter(Footballer.position == position)
    
#     if club_id:
#         query = query.filter(Footballer.club_id == club_id)
    
#     footballers = query.offset(skip).limit(limit).all()
#     return footballers

# @router.get("/{footballer_id}", response_model=FootballerResponse)
# def read_footballer(
#     footballer_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_active_user)
# ):
#     """Get footballer by ID"""
#     footballer = db.query(Footballer).filter(Footballer.id == footballer_id).first()
#     if footballer is None:
#         raise HTTPException(status_code=404, detail="Footballer not found")
#     return footballer

# @router.get("/league/{league_name}", response_model=List[FootballerResponse])
# def read_league_footballers(
#     league_name: str,
#     skip: int = 0,
#     limit: int = 100,
#     position: Optional[str] = Query(None, description="Filter by position"),
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_active_user)
# ):
#     """Get all footballers in a specific league"""
#     query = db.query(Footballer).filter(Footballer.league_name == league_name)
    
#     if position:
#         query = query.filter(Footballer.position == position)
    
#     footballers = query.offset(skip).limit(limit).all()
#     return footballers

# @router.get("/club/{club_id}", response_model=List[FootballerResponse])
# def read_club_footballers(
#     club_id: int,
#     skip: int = 0,
#     limit: int = 100,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_active_user)
# ):
#     """Get all footballers in a specific club"""
#     footballers = db.query(Footballer).filter(
#         Footballer.club_id == club_id
#     ).offset(skip).limit(limit).all()
#     return footballers