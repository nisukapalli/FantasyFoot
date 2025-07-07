from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.models import create_tables
from app.api import (
    auth_router, users_router, leagues_router, 
    teams_router, footballers_router, clubs_router
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_tables()
    yield
    # Shutdown
    pass

app = FastAPI(
    title="Fantasy Soccer API",
    description="A comprehensive fantasy soccer application backend",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(leagues_router)
app.include_router(teams_router)
app.include_router(footballers_router)
app.include_router(clubs_router)

@app.get("/")
def read_root():
    return {
        "message": "Fantasy Soccer API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
