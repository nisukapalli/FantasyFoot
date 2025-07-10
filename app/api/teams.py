from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.base import SessionLocal
from app.models.user import User
from app.models.team import Team
from app.models.league import League
from app.schemas.team import TeamCreate, TeamUpdate, TeamResponse
from app.auth.jwt import get_current_active_user

router = APIRouter(prefix="/teams", tags=["teams"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def handle_league_admin_reassignment(db: Session, league: League, user_id: int):
#     """Handle admin reassignment when a user is removed from a league"""
#     other_team = db.query(Team).filter(
#         Team.league_id == league.id,
#         Team.user_id != user_id
#     ).first()
    
#     if other_team:
#         league.admin_id = other_team.user_id
#         db.commit()
#         return True
#     else:
#         db.delete(league)
#         db.commit()
#         return False

@router.get("/", response_model=List[TeamResponse])
def read_teams(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get list of user's teams"""
    teams = db.query(Team).filter(Team.user_id == current_user.id).offset(skip).limit(limit).all()
    return teams

@router.get("/{team_id}", response_model=TeamResponse)
def read_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get team by ID"""
    team = db.query(Team).filter(Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    
    # Check if user owns this team or is admin of the league
    league = db.query(League).filter(League.id == team.league_id).first()
    if team.user_id != current_user.id and league.admin_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    return team

@router.put("/{team_id}", response_model=TeamResponse)
def update_team(
    team_id: int,
    team_update: TeamUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update team (owner only)"""
    team = db.query(Team).filter(Team.id == team_id).first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    
    if team.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Update fields
    update_data = team_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(team, field, value)
    
    db.commit()
    db.refresh(team)
    return team

# @router.delete("/{team_id}")
# def delete_team(
#     team_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_active_user)
# ):
#     """Delete team (owner only)"""
#     team = db.query(Team).filter(Team.id == team_id).first()
#     if team is None:
#         raise HTTPException(status_code=404, detail="Team not found")
    
#     if team.user_id != current_user.id:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="You can only delete your own teams"
#         )
    
#     # Check if user is admin of this league and handle admin reassignment
#     league = db.query(League).filter(League.id == team.league_id).first()
#     if league.admin_id == current_user.id:
#         admin_reassigned = handle_league_admin_reassignment(db, league, current_user.id)
#         if not admin_reassigned:
#             return {"message": "Team and league deleted successfully (no other users in league)"}
    
#     db.delete(team)
#     db.commit()
    
#     return {"message": "Team deleted successfully"}

@router.get("/league/{league_id}", response_model=List[TeamResponse])
def read_league_teams(
    league_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all teams in a league"""
    # Check if user has access to this league
    user_team = db.query(Team).filter(
        Team.league_id == league_id,
        Team.user_id == current_user.id
    ).first()
    
    league = db.query(League).filter(League.id == league_id).first()
    if league is None:
        raise HTTPException(status_code=404, detail="League not found")
    
    if league.admin_id != current_user.id and not user_team:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    teams = db.query(Team).filter(Team.league_id == league_id).all()
    return teams