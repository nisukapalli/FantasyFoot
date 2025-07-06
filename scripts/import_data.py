import pandas as pd
from sqlalchemy.orm import Session
from app.models.base import SessionLocal
from app.models.footballer import Footballer
from app.models.club import Club

POSITION_MAP = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}

epl_players_df = pd.read_csv("../data/epl_players_raw.csv")
epl_clubs_df = pd.read_csv("../data/epl_clubs.csv")
club_count = 0
footballer_count = 0

db: Session = SessionLocal()
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

for _, row in epl_players_df.iterrows():
    if row["element_type"] == 5:
        continue
    footballer = Footballer(
        id=row["id"],
        name=row["web_name"],
        full_name=row["first_name"]+" "+row["second_name"],
        position=POSITION_MAP[row["element_type"]],
        club=row["team"],
        league_name="Premier League",
        birth_date=row["birth_date"],
        region=row["region"],
    )
    db.merge(footballer)
    footballer_count += 1

print(f"Imported {club_count} clubs and {footballer_count} footballers")
db.commit()
db.close()
