import pandas as pd
from sqlalchemy.orm import Session
from app.models.base import SessionLocal
from app.models.footballer import Footballer
from app.models.club import Club

POSITION_MAP = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}

def import_data():
    """Import EPL clubs and players data"""
    epl_players_df = pd.read_csv("~/FantasyFoot/data/epl_players_raw.csv")
    epl_clubs_df = pd.read_csv("~/FantasyFoot/data/epl_clubs.csv")
    club_count = 0
    footballer_count = 0

    db: Session = SessionLocal()
    
    try:
        # Import clubs
        for _, row in epl_clubs_df.iterrows():
            club = Club(
                id=row["id"],
                name=row["name"],
                abbreviation=row["short_name"],
                league_name="Premier League",
                country="England",
            )
            db.merge(club)
            club_count += 1

        db.commit()
        print(f"Imported {club_count} clubs")

        # Import players
        for _, row in epl_players_df.iterrows():
            # Skip coaches (element_type == 5)
            if row["element_type"] == 5:
                continue
                
            # Skip players without valid data
            if pd.isna(row["web_name"]) or pd.isna(row["element_type"]):
                continue
                
            footballer = Footballer(
                id=row["id"],
                name=row["web_name"],
                full_name=f"{row['first_name']} {row['second_name']}",
                position=POSITION_MAP.get(row["element_type"], "UNK"),
                club_id=row["team"],
                league_name="Premier League",
                birth_date=pd.to_datetime(row["birth_date"]).date() if pd.notna(row["birth_date"]) else None,
                region=row["region"] if pd.notna(row["region"]) else None,
                external_api_id=str(row["id"]),
            )
            db.merge(footballer)
            footballer_count += 1

        db.commit()
        print(f"Imported {footballer_count} footballers")
        
    except Exception as e:
        print(f"Error during import: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    import_data()
