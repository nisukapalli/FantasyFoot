import secrets
import string
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.base import SessionLocal
from app.models.user import User
from app.models.league import League
from app.models.team import Team
from app.schemas.league import LeagueCreate, LeagueUpdate, LeagueResponse, LeagueJoin
from app.auth.jwt import get_current_active_user

router = APIRouter(prefix="/leagues", tags=["leagues"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_invite_code():
    """Generate a random invite code"""
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8))

@router.post("/", response_model=LeagueResponse)
def create_league(
    league: LeagueCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new league"""
    invite_code = None
    if league.is_private:
        invite_code = generate_invite_code()
    
    db_league = League(
        **league.dict(),
        admin_id=current_user.id,
        invite_code=invite_code
    )
    db.add(db_league)
    db.commit()
    db.refresh(db_league)
    return db_league

@router.get("/", response_model=List[LeagueResponse])
def read_leagues(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get list of leagues"""
    leagues = db.query(League).filter(
        (League.admin_id == current_user.id) |
        (League.id.in_(
            db.query(Team.league_id).filter(Team.user_id == current_user.id)
        ))
    ).offset(skip).limit(limit).all()
    return leagues

@router.get("/{league_id}", response_model=LeagueResponse)
def read_league(
    league_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get league by ID"""
    league = db.query(League).filter(League.id == league_id).first()
    if league is None:
        raise HTTPException(status_code=404, detail="League not found")
    
    # Check if user has access to this league
    user_team = db.query(Team).filter(
        Team.league_id == league_id,
        Team.user_id == current_user.id
    ).first()
    
    if league.admin_id != current_user.id and not user_team:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Add team count
    team_count = db.query(Team).filter(Team.league_id == league_id).count()
    league.team_count = team_count
    
    return league

@router.post("/{league_id}/join")
def join_league(
    league_id: int,
    join_data: LeagueJoin,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Join a league using invite code"""
    league = db.query(League).filter(League.id == league_id).first()
    if league is None:
        raise HTTPException(status_code=404, detail="League not found")
    
    if not league.is_private or league.invite_code != join_data.invite_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid invite code"
        )
    
    # Check if user already has a team in this league
    existing_team = db.query(Team).filter(
        Team.league_id == league_id,
        Team.user_id == current_user.id
    ).first()
    
    if existing_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already have a team in this league"
        )
    
    # Check if league is full
    team_count = db.query(Team).filter(Team.league_id == league_id).count()
    if team_count >= league.max_teams:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="League is full"
        )
    
    # Create team for user
    team = Team(
        name=f"{current_user.username}'s Team",
        league_id=league_id,
        user_id=current_user.id
    )
    db.add(team)
    db.commit()
    
    return {"message": "Successfully joined league"}

@router.put("/{league_id}", response_model=LeagueResponse)
def update_league(
    league_id: int,
    league_update: LeagueUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update league (admin only)"""
    league = db.query(League).filter(League.id == league_id).first()
    if league is None:
        raise HTTPException(status_code=404, detail="League not found")
    
    if league.admin_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Update fields
    update_data = league_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(league, field, value)
    
    db.commit()
    db.refresh(league)
    return league