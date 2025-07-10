#!/usr/bin/env python3
"""
Simple script to count clubs and footballers in the database
"""

import requests
import json

# API base URL
BASE_URL = "http://13.57.179.177:8000"

# JWT token (you can replace this with your actual token)
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc1MjEyOTk5Nn0.YmuT88iPGp1iB_SL2gf8SVbRYnTm_TF4C5--TmLeSbk"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def count_clubs():
    """Count total number of clubs"""
    try:
        response = requests.get(f"{BASE_URL}/clubs/", headers=headers)
        response.raise_for_status()
        clubs = response.json()
        return len(clubs)
    except Exception as e:
        print(f"Error counting clubs: {e}")
        return 0

def count_footballers():
    """Count total number of footballers"""
    try:
        response = requests.get(f"{BASE_URL}/footballers/", headers=headers)
        response.raise_for_status()
        footballers = response.json()
        return len(footballers)
    except Exception as e:
        print(f"Error counting footballers: {e}")
        return 0

def main():
    print("=== Fantasy Soccer Database Counts ===")
    print()
    
    # Count clubs
    club_count = count_clubs()
    print(f"📊 Total Clubs: {club_count}")
    
    # Count footballers
    footballer_count = count_footballers()
    print(f"⚽ Total Footballers: {footballer_count}")
    
    print()
    print("=== Summary ===")
    print(f"🏟️  Clubs: {club_count}")
    print(f"👥 Footballers: {footballer_count}")
    print(f"📈 Total Records: {club_count + footballer_count}")

if __name__ == "__main__":
    main() 