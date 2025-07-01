from app.models.base import Base, engine, SessionLocal
from app.models.user import User

def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        user = User(username="testuser", email="test@example.com", password_hash="hashed")
        db.add(user)
        db.commit()
        print("User added: ", user.username)

        db_entry = db.query(User).filter_by(username="testuser").first()
        print("Queried user: ", db_entry.username)
    finally:
        db.close()

if __name__ == "__main__":
    test_db()
