from .base import Base, engine, SessionLocal
from .user import User
from .league import League
from .team import Team
from .club import Club
from .footballer import Footballer
from .fantasy_player import FantasyPlayer
from .match import Match
from .player_performance import PlayerPerformance
from .trade import Trade
from .draft import Draft, DraftPick

def create_tables():
    Base.metadata.create_all(bind=engine)

__all__ = [
    "Base", "engine", "SessionLocal",
    "User", "League", "Team", "Club", "Footballer",
    "FantasyPlayer", "Match", "PlayerPerformance", "Trade", "Draft", "DraftPick",
    "create_tables"
]
