#!/usr/bin/env python3
"""
Database initialization script for Fantasy Soccer App
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import create_tables
from app.models.base import SessionLocal
from app.models.user import User
from app.auth.jwt import get_password_hash

def create_admin_user():
    """Create a default admin user"""
    db = SessionLocal()
    try:
        # Check if admin user already exists
        admin = db.query(User).filter(User.username == "admin").first()
        if admin:
            print("Admin user already exists")
            return
        
        # Create admin user
        admin_user = User(
            username="admin",
            email="admin@fantasysoccer.com",
            password_hash=get_password_hash("admin123"),
            is_admin=True,
            is_active=True
        )
        db.add(admin_user)
        db.commit()
        print("Admin user created successfully")
        print("Username: admin")
        print("Password: admin123")
        
    except Exception as e:
        print(f"Error creating admin user: {e}")
        db.rollback()
    finally:
        db.close()

def init_database():
    """Initialize the database"""
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully")
    
    print("Creating admin user...")
    create_admin_user()

if __name__ == "__main__":
    init_database() 