from .auth import router as auth_router
from .users import router as users_router
from .leagues import router as leagues_router
from .teams import router as teams_router
from .footballers import router as footballers_router
from .clubs import router as clubs_router

__all__ = [
    "auth_router", "users_router", "leagues_router", 
    "teams_router", "footballers_router", "clubs_router"
]